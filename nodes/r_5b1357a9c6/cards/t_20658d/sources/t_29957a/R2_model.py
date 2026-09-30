#!/usr/bin/env python3
"""R2 conditional envelope, not causal estimation. Python stdlib only.
Run from any directory: python3 /path/R2_model.py.
Sources, definitions and prior parameter choices are in model_protocol.md/SOURCES.md.
"""
from pathlib import Path
from itertools import product
import csv, json, hashlib

ROOT = Path(__file__).resolve().parent
with (ROOT/'R2_inputs.csv').open(newline='') as f:
    inputs = list(csv.DictReader(f))
fields = list(inputs[0])
rows = list(inputs)

def add(year, scenario, series, value, unit, price_basis, base_year,
        kind, quality, source_id, locator, note):
    rows.append(dict(zip(fields,[year,scenario,series,value,unit,price_basis,base_year,
                               kind,quality,source_id,locator,note])))

# Declare gaps rather than manufacture annual observations.
for series, unit in [('paper_money_stock','million_paper_rubles'),
                     ('national_exports_silver','million_silver_rubles'),
                     ('national_imports_silver','million_silver_rubles'),
                     ('funded_public_debt_silver','million_silver_rubles')]:
    observed = {int(r['year']) for r in inputs if r['series']==series}
    for y in range(1803,1816):
        if y not in observed:
            add(y,'S0',series,'',unit,'nominal','none','missing','not_observed',
                'SOURCES','gap_register','not interpolated; public debt excludes paper money')

for r in inputs:
    if r['series']=='paper_kopecks_per_silver_ruble':
        add(r['year'],'S0','silver_kopecks_per_paper_ruble',10000/float(r['value']),
            'silver_kopecks_per_paper_ruble','exchange_rate','none','derived','auxiliary',
            'S11','annual_exchange_table','10000/input; annual average inversion is an approximation not average reciprocal')

with (ROOT/'R2_parameters.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['scenario','parameter','low','high','status','grounds'])
    for sc,vals in {'S2':{'neutral_retention':(.70,.95),'continental_replacement':(.10,.30),'realized_price':(.90,1)},
                    'S3':{'neutral_retention':(.15,.40),'continental_replacement':(.10,.35),'realized_price':(.65,.85)}}.items():
        for key,(lo,hi) in vals.items():
            w.writerow([sc,key,lo,hi,'assumption','S01 p144-146 and209-213; S03 p856; not econometric estimates'])
    for key,lo,hi in [('export_estate_share',.30,.65),('inland_estate_share',.03,.15),('british_share',.5,.75),('fixed_commitments',.25,.5)]:
        w.writerow(['all',key,lo,hi,'assumption','model_protocol; b bounded by S01p37 and S02p263'])

endpoints=[]; summary={}
for sc, ns, rs, ps in [('S2',[.70,.95],[.10,.30],[.90,1]),('S3',[.15,.40],[.10,.35],[.65,.85])]:
    for estate, es in [('export',[.30,.65]),('inland',[.03,.15])]:
        vals=[]
        for e,b,n,r,p,d in product(es,[.5,.75],ns,rs,ps,[.25,.5]):
            g=p*(n+(1-n)*r)
            loss=e*b*(1-g)
            free_loss=loss/(1-d)
            assert 0<=g<=1 and 0<=loss<=e*b and 0<=free_loss<=1
            vals.append((loss,free_loss))
            endpoints.append([sc,estate,e,b,n,r,p,d,g,loss*100,free_loss*100])
        key=sc+'_'+estate
        summary[key]={'gross_min_pct':min(x[0] for x in vals)*100,'gross_max_pct':max(x[0] for x in vals)*100,
                      'free_min_pct':min(x[1] for x in vals)*100,'free_max_pct':max(x[1] for x in vals)*100,
                      'endpoint_count':len(vals)}
        for label,v in summary[key].items():
            if label!='endpoint_count':
                add('1808-1815',sc,estate+'_estate_'+label,v,'percent','scenario_constant_origin_price','no_blockade=100',
                    'scenario','conditional_not_probability','MODEL','equation_L_e_b_g','corner envelope; not sample estimate')
with (ROOT/'R2_loss_grid.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['scenario','estate','e','b','n','r','p','d','retained_british_channel', 'gross_loss_pct','free_cash_loss_pct']);w.writerows(endpoints)

# Additional transparent sensitivities.
summary['central']={}
for sc,n,r,p in [('S2',.85,.20,.95),('S3',.25,.20,.75)]:
    e,b,d=.5,.65,.4
    L=e*b*(1-p*(n+(1-n)*r))
    summary['central'][sc]={'gross_pct':100*L,'free_pct':100*L/(1-d)}
summary['falsifier_probe']={}
for g in [.70,.90,1.05]:
    losses=[e*(1-g)*100 for e in [.30,.65]]
    summary['falsifier_probe'][str(g)]={'gross_min_pct':min(losses),'gross_max_pct':max(losses)}
# If a flax estate really has b=.90, otherwise S3 parameters unchanged.
flax=[e*.9*(1-p*(n+(1-n)*r))*100 for e,n,r,p in product([.3,.65],[.15,.4],[.1,.35],[.65,.85])]
summary['S3_flax_sensitivity']={'gross_min_pct':min(flax),'gross_max_pct':max(flax)}

hemp=60000
uk=.61*hemp; fr=.024*hemp; cont=(.024+.07+.159)*hemp
summary['hemp_replacement']={'scale_tons_author':hemp,'uk_scale':uk,'france_scale':fr,'continental_scale':cont,
        'france_needed_total_multiplier':(fr+uk)/fr,'continental_needed_total_multiplier':(cont+uk)/cont,
        'continental_increment_for_10pct_uk':uk*.1/cont,'continental_increment_for_35pct_uk':uk*.35/cont,
        'warning':'circa1800 quantity times1806 shares is a scenario scale not observation; destination shares assumed to map to quantities at similar prices; value/volume basis unstated in table; intermediary flows may be British-bound'}
for k,v in summary['hemp_replacement'].items():
    if isinstance(v,(float,int)):
        add('circa1806','REPLACEMENT',k,v,'tons_author' if 'scale' in k else 'ratio','physical_or_ratio','crossyear_scale',
            'scenario','scaling_only','S01+S02','p28/p263','not observed1806 tonnage; table share value/volume basis unstated; similar-price mapping assumption')
summary['population']={str(y):[43.785*(1+g)**(y-1811) for g in [.006,.009]] for y in [1815,1830,1848]}
for y,vs in summary['population'].items():
    for tag,v in zip(['low','high'],vs):
        add(y,'S5','population_'+tag,v,'million_people','physical','1811','scenario','comparison_geography',
            'S15+MODEL','table6 and .6-.9pct annual growth','not actual imperial boundary census; excludes Poland and Finland')
# Invariant checks and no illicit aggregation.
assert abs(sum([61,2.4,7,15.9,13.7])-100)<1e-9
assert abs((fr+uk)/fr-26.416666666666668)<1e-9
assert len(endpoints)==256
keys=[(str(r['year']),r['scenario'],r['series']) for r in rows]
assert len(keys)==len(set(keys))
for r in rows:
    r.update(frequency='annual_or_explicit_interval',seasonal_adjustment='NSA/not_applicable',
             retrieved_at='2026-09-23',vintage='read_version_see_SOURCES')
with (ROOT/'R2_series.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields+['frequency','seasonal_adjustment','retrieved_at','vintage']);w.writeheader();w.writerows(rows)
summary['row_counts']={'input':len(inputs),'total':len(rows),'missing':sum(r['kind']=='missing' for r in rows),'loss_grid':len(endpoints)}
(ROOT/'R2_model_results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
metadata={'units':'per-row in R2_series.csv; unknown currency explicitly segregated',
 'frequency':'annual or declared intervals','seasonal_adjustment':'NSA / not applicable',
 'real_or_nominal':'per-row price_basis; never aggregate unknown currency',
 'base_year':'per-row;1807 terms of trade;none for nominal money;conditional no-blockade=100',
 'source':'SOURCES.md plus explicitly hypothetical MODEL rows',
 'source_url':'per-source SOURCES.md', 'retrieved_at':'2026-09-23','vintage':'frozen captured versions; read ranges in notes',
 'limits':'metadata presence check cannot certify historical truth or currency equivalence'}
(ROOT/'R2_metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
