#!/usr/bin/env python3
"""B6 reproducible arithmetic, not an estimated causal model.
Inputs: Heckscher 1922 p245 (GBP millions, current declared values, GB ports),
Hansard 25 Feb1823 c249 (old pounds-shillings-pence), and declared assumptions.
Output: bounds/sensitivities; no 1812-15 interpolation, no India allocation.
Run: python3 nodes/r_5b1357a9c6/cards/t_0fed70/calculate_bounds.py
"""
from pathlib import Path
from decimal import Decimal as D
import csv, json, hashlib
P=Path(__file__).resolve().parent

def load(name):
    with (P/name).open(encoding='utf-8',newline='') as f: return list(csv.DictReader(f))
def write_csv(name, rows):
    with (P/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def pack(row):
    out={'year':int(row['year'])}
    for k,v in row.items():
        if k!='year': out[k]=D(v)
    return out
rows=[pack(r) for r in load('trade_heckscher.csv')]
for r in rows:
    for tag in ('D','R'):
        r['E_narrow_'+tag]=sum(r[x+'_'+tag] for x in ('north_europe','spain','portugal'))
        r['E_mixed_'+tag]=r['E_narrow_'+tag]+r['med_levant_'+tag]
        r['nonAsia_overseas_'+tag]=sum(r[x+'_'+tag] for x in ('africa','usa','rest_america'))
base=next(r for r in rows if r['year']==1806)
res=[]; checks=[]
regions=['north_europe','spain','portugal','med_levant','ireland_guernsey','asia','africa','usa','rest_america']
for r in rows:
    o={'year':r['year']}
    for tag in ('D','R'):
        for k in ('north_europe','E_narrow','E_mixed','nonAsia_overseas','rest_america','usa'):
            o[k+'_'+tag]=r[k+'_'+tag]
            o['delta_1806_'+k+'_'+tag]=r[k+'_'+tag]-base[k+'_'+tag]
        err=sum(r[k+'_'+tag] for k in regions)-r['total_'+tag]
        checks.append({'year':r['year'],'kind':tag,'row_sum_minus_published_total_GBPm':str(err),'within_rounding_tolerance_0.05':abs(err)<=D('.05')})
    res.append(o)
write_csv('trade_bounds.csv',res)
sens=[]
for r in rows:
    if r['year']<1808: continue
    inc=r['rest_america_D']-base['rest_america_D']
    for scope in ('north_europe','E_narrow','E_mixed'):
        loss=base[scope+'_D']-r[scope+'_D']
        for alpha in map(D,('0','.25','.5','.75','1')):
            sens.append({'year':r['year'],'Europe_proxy':scope,'restAmerica_increment_GBPm':inc,'European_loss_GBPm':loss,'assumed_formalEmpire_share_of_increment':alpha,'allocated_increment_GBPm':alpha*inc,'offset_ratio_if_loss_positive':str((alpha*inc/loss).quantize(D('.0001'))) if loss>0 else 'NA_no_loss','alpha_needed_for_full_offset_if_loss_positive':str((loss/inc).quantize(D('.0001'))) if loss>0 and inc>0 else 'NA'})
write_csv('trade_sensitivity.csv',sens)
baseline_sensitivity=[]
for byear in (1805,1806,1807):
    b=next(r for r in rows if r['year']==byear)
    for r in rows:
        if r['year']<1808: continue
        inc=r['rest_america_D']-b['rest_america_D']
        for scope in ('north_europe','E_narrow','E_mixed'):
            loss=b[scope+'_D']-r[scope+'_D']
            baseline_sensitivity.append({'baseline_year':byear,'year':r['year'],'Europe_proxy':scope,'restAmerica_increment_GBPm':inc,'Europe_loss_GBPm':loss,'raw_ratio_if_loss_positive':str((inc/loss).quantize(D('.0001'))) if loss>0 else 'NA_no_loss'})
write_csv('baseline_sensitivity.csv',baseline_sensitivity)
fiscal=load('fiscal_1820.csv')
to_pence=lambda r: int(r['pounds'])*240+int(r['shillings'])*12+int(r['pence'])
row_total=sum(to_pence(r) for r in fiscal if r['station']!='published_total')
printed=to_pence(next(r for r in fiscal if r['station']=='published_total'))
psd=lambda n: {'pounds':n//240,'shillings':(n%240)//12,'pence':n%12}
fs={'computed_row_sum':psd(row_total),'published_total':psd(printed),'row_sum_minus_published_pence':row_total-printed,'note':'Do not silently repair source discrepancy. Commissary payments are not total colonial cost.'}
sc=[]
for r in load('scenario_assumptions.csv'):
    sc.append({'scenario':r['scenario'],'exports_1844GBP_equivalent_low_GBPm':D('8')*D(r['trade_multiplier_low']),'exports_1844GBP_equivalent_high_GBPm':D('8')*D(r['trade_multiplier_high']),'central_cost_1848GBP_equivalent_low_GBPm':D('4')*D(r['cost_multiplier_low']),'central_cost_1848GBP_equivalent_high_GBPm':D('4')*D(r['cost_multiplier_high']),'soldiers_low':r['soldiers_low'],'soldiers_high':r['soldiers_high'],'status':'judgment_range_not_statistical_confidence_interval'})
write_csv('scenario_ranges.csv',sc)
# Sensitivity for 10,000 white and 5,000 black soldiers between two station rates; no assumed equal allocation.
# Observed 1817-36 averages from Craton1976 n11, via Roberts/Tulloch, not 1803 causal rates.
medical={'white_10000_deaths_per_year_sensitivity':[10000*.0785,10000*.1213],'black_5000_deaths_per_year_sensitivity':[5000*.030,5000*.040],'excludes':'invaliding,combat,desertion; no claim of a causal racial effect'}
audit={'trade_checks':checks,'fiscal_1820':fs,'medical_sensitivity':medical,'source_hashes':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('trade_heckscher.csv','fiscal_1820.csv','scenario_assumptions.csv')},'limits':['Heckscher transfers Hansard; underlying custom books not checked','Geographic Europe mixed with Levant in one column','Rest of America is not British Empire','Asia excluded wholesale, not a clean non-India series','Exports are gross shipments, not receipts or fiscal surplus','1812-15 regional data not imputed','Scenario ranges are analyst-chosen multipliers, not estimated elasticities, around contested contemporary anchors']}
(P/'audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(c['within_rounding_tolerance_0.05'] for c in checks)
print(json.dumps({'trade_rounding_checks_pass':len(checks),'fiscal':fs,'medical':medical},ensure_ascii=False,indent=2))
