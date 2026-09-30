#!/usr/bin/env python3
"""Recompute Q2 source arithmetic + transparent scenario envelopes.
Standard library, no hidden downloaded data, regression, imputation or simulation as observation.
Model corner counts ARE NOT probabilities. Run build_panel.py first.
"""
from pathlib import Path
import csv,json,itertools,math,hashlib
from collections import Counter
R=Path(__file__).resolve().parent
with (R/'Q2_panel.csv').open(encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
assert len({r['obs_id'] for r in rows})==len(rows)
assert all(r['source_id'] and r['locator'] and r['unit'] for r in rows)
assert all(r['value']=='' for r in rows if r['value_status']=='not_obtained')
def get(geo,metric,start=None):
    x=[r for r in rows if r['geo']==geo and r['metric']==metric and (start is None or r['period_start']==str(start))]
    assert len(x)==1,(geo,metric,start,len(x))
    return float(x[0]['value'])
calc=[]
def c(name,value,unit,formula,note):calc.append(dict(calculation=name,value=round(value,9),unit=unit,formula=formula,note=note))
for geo in ['Rhineland4','Alsace2','French_Empire_excl4Italy']:
    for st in [1800,1806]:
        m=get(geo,'mobilised',st)
        for met in ['draft_dodgers_pre_presentation','deserters_after_joining']:
            c(f'{geo}_{st}_{met}_percent',100*get(geo,met,st)/m,'percent',f'{geo}:{met}/{geo}:mobilised*100 in {st}','Rowe same-source ratio; not RP23 dodging definition.')
for met in ['draft_dodgers_pre_presentation','deserters_after_joining']:
    def rate(geo,st):return 100*get(geo,met,st)/get(geo,'mobilised',st)
    changes={geo:rate(geo,1806)-rate(geo,1800) for geo in ['Rhineland4','Alsace2']}
    c(f'{met}_rhine_change',changes['Rhineland4'],'percentage_points','later ratio - earlier ratio','Descriptive, not annexation effect.')
    c(f'{met}_rhine_minus_alsace_change',changes['Rhineland4']-changes['Alsace2'],'percentage_points','(Rhine later-earlier)-(Alsace later-earlier)','Two non-random regions, no parallel-trend test; not causal DID.')
c('roer_nominal_tax_change',100*(get('Roer','tax_paid_reported')/get('Roer','old_regime_tax_estimate')-1),'percent','(11138406/6250000-1)*100','Old-regime estimate not uniform-tax base or causal control.')
c('piedmont_incorporated_registered',100*get('Piedmont','incorporated_conscripts')/get('Piedmont','registered_11_cohorts'),'percent','35281/166556*100','Registration share, not quota completion.')
for st in [1800,1806]:
    c(f'piedmont_exempted_{st}',100*get('Piedmont','exempted',st)/get('Piedmont','registered',st),'percent','exempted/registered*100','Different cohort windows, disease and classification possible.')
c('piedmont_population_sum',sum(get(x,'population') for x in ['Doire','Marengo','Po','Sesia','Stura','Tanaro']),'persons','sum(six department populations)','Difference from prose retained.')
c('piedmont_population_discrepancy',sum(get(x,'population') for x in ['Doire','Marengo','Po','Sesia','Stura','Tanaro'])-get('Piedmont','population_total_prose'),'persons','1861852-1813473','Not silently reconciled.')
c('piedmont_joined_components',sum(get('Piedmont',m) for m in ['incorporated_conscripts','volunteers','velites']),'persons','35281+2682+280','Matches p219 not p214.')
c('piedmont_evaders_components',get('Piedmont','mixed_evaders',1800)+get('Piedmont','mixed_evaders',1806),'persons','6272+2929','Does not match all-period9272.')
c('belgium_cumulative_incorporated_population',100*get('Belgium9','incorporated_cumulative')/get('Belgium9','population_used'),'percent','216111/3028705*100','Not unique persons, annual flow or D1 quoted6.12%.')
c('marion_regional_sum',sum(float(r['value']) for r in rows if r['metric']=='projected_revenue_regional'),'million_francs','83+66.5+38.791+37.5+33+22.5+16+16.5','etc omitted in original; not all-annexed actual cash.')
c('marion_unitemized_projected_gross',get('Annexed_all','projected_gross_all')-sum(float(r['value']) for r in rows if r['metric']=='projected_revenue_regional'),'million_francs','342.260044-regional sum','Do not assign residual to invented province.')
c('oct1813_deadline_arrival',100*get('French_recruit_call','arrived_by_dec31')/get('French_recruit_call','october_call_quota'),'percent','72265/127433*100','One call by Dec31, not all1813 final result.')
for x in [2812,3256]:
    c(f'rp23_increment_{x}_share',100*x/10499,'percent',f'{x}/10499*100','Text/appendix discrepancy; not rerun of microdata.')
# Recalculate simple normal intervals on published coefficients, not causal/forecast intervals.
with (R/'Q2_published_estimates.csv').open(encoding='utf-8-sig') as f:ests=list(csv.DictReader(f))
for e in ests:
    b=float(e['coefficient']);se=float(e['se_conley_brackets'] or e['se_parentheses'])
    for tag,v in [('low',b-1.96*se),('high',b+1.96*se)]:
        c(f"{e['table_column']}_{e['regressor']}_normal95_{tag}",v,e['outcome'],'published coefficient +/-1.96*reported SE','Normal approximation, not predictive or causal uncertainty; no finite-cluster correction.')
with (R/'Q2_calculations.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(calc[0]));w.writeheader();w.writerows(calc)
# Transparent policy calibration. All ranges below are analyst assumptions, NOT fitted estimates.
profiles={
 'L':dict(q=(1.8,2.8),a0=(.50,.70),a1=(.80,.95),T=(3,6),g0=(6,10),g1=(2,4)),
 'M':dict(q=(1.5,2.5),a0=(.35,.60),a1=(.65,.90),T=(6,12),g0=(10,16),g1=(4,8)),
 'H':dict(q=(1.2,2.2),a0=(.10,.35),a1=(.45,.75),T=(10,20),g0=(20,35),g1=(10,20))
}
# Units q/g: per1000 total inhabitants; a: fraction of assigned draft arriving.
ass=[]
for p,vs in profiles.items():
    for k,v in vs.items():
        ass.append(dict(profile=p,parameter=k,lower=v[0],upper=v[1],status='ANALYST_ASSUMPTION_NOT_ESTIMATED',ground='See report sec6; source cases constrain direction not endpoints'))
for k,v in [('population',1000000),('service_years',5),('training_lag',1),('annual_retention',.90),('trained_deployable_fraction',.80)]:
    ass.append(dict(profile='all',parameter=k,lower=v,upper=v,status='FIXED_SCENARIO_ASSUMPTION',ground='Five-year peace term: F90p215; other values stress-test assumptions'))
with (R/'Q2_assumptions.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(ass[0]));w.writeheader();w.writerows(ass)
model=[];crossings={};summ=[]
def path(q,a0,a1,T,g0,g1,retention=.9,usable=.8,service=5):
    # At t1 first cohort enters. At t2 it becomes deployable. Total service includes
    # the one training year: service=5 yields FOUR deployable cohorts, not five.
    # No existing army is credited.
    arr={t:1000*q*(a0+(a1-a0)*min(t/T,1)) for t in range(1,21)}
    out=[]
    for t in range(1,21):
        stock=usable*sum(arr.get(t-1-k,0)*retention**k for k in range(service-1))
        g=1000*(g1+(g0-g1)*max(1-t/T,0))
        out.append((t,arr[t],stock,g,stock-g))
    return out
for p,params in profiles.items():
    crossings[p]=[]
    for idx,vals in enumerate(itertools.product(*params.values()),1):
        out=path(*vals)
        cross=next((t for t,a,s,g,n in out if n>=0),None);crossings[p].append(cross)
        for t,a,s,g,n in out:
            model.append(dict(profile=p,corner=idx,year_since_annexation=t,annual_arrivals=a,deployable_stock=s,security_frontier_requirement=g,net_stock=n,status='CONDITIONAL_MODEL_NOT_OBSERVATION'))
    for yr in [5,10,20]:
        rr=[m for m in model if m['profile']==p and m['year_since_annexation']==yr]
        sm=dict(profile=p,year_since_annexation=yr)
        for k in ['annual_arrivals','deployable_stock','security_frontier_requirement','net_stock']:
            sm[k+'_min']=round(min(x[k] for x in rr),1);sm[k+'_max']=round(max(x[k] for x in rr),1)
        summ.append(sm)
for name,data in [('Q2_model_paths.csv',model),('Q2_model_summary.csv',summ)]:
    with (R/name).open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
# All corners fiscal requirement, no fictional tax receipts.
fiscal=[]
for p,ps in profiles.items():
    fiscal.append(dict(profile=p,settled_garrison_min_per1000=ps['g1'][0],settled_garrison_max_per1000=ps['g1'][1],cost_low=700,cost_high=1000,minimum_tax_surplus_before_security_million=ps['g1'][0]*.7,maximum_tax_surplus_needed_million=ps['g1'][1]*1.,status='ACCOUNTING_THRESHOLD_NOT_REVENUE_PREDICTION'))
with (R/'Q2_fiscal_thresholds.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(fiscal[0]));w.writeheader();w.writerows(fiscal)
# Conditional mean/pivot check: no random folds or pseudo classification score produced.
loo=[
 ['Rhineland4','Two-period annexed vs old-core arithmetic','No comparable annexed group remains; convergence speed conclusion loses its key time comparison','NO_STATISTICAL_LOOCV'],
 ['Piedmont','Existing military institutions permit partial rapid induction','Rhine remains but no early2-4year administrative-response anchor; widen low-friction maturity judgment','QUALITATIVE_DEPENDENCY_CHECK'],
 ['Belgium9','Pre-enlistment and later evasion need distinct metrics','Rowe still establishes metric reversal; conclusion survives','QUALITATIVE_DEPENDENCY_CHECK'],
 ['Roer','Tax payment may coexist with fiscal reinvestment','No department-level paid-tax point remains; reject tax convergence fitting','NO_STATISTICAL_LOOCV'],
 ['RP23','Enforcement-cost-dependent draft quota selection','Woolf lighter quotas still support mechanism qualitatively; no published effect-size use','QUALITATIVE_DEPENDENCY_CHECK'],
 ['Outer_annexed','Out-of-sample class','Comparable annual outputs absent before1811 for Holland/Hansa; no train/test discrimination score exists','NOT_TESTABLE_WITH_ASSEMBLED_DATA']]
with (R/'Q2_leave_one_audit.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f);w.writerow(['leave_out','claim','effect_on_inference','status']);w.writerows(loo)
# Minimal model invariants and source-conflict checks, not source authentication.
assert all(m['annual_arrivals']>=0 and m['deployable_stock']>=0 and abs(m['net_stock']-(m['deployable_stock']-m['security_frontier_requirement']))<1e-6 for m in model)
assert all(m['deployable_stock']==0 for m in model if m['year_since_annexation']==1)
assert sum(get(x,'population') for x in ['Doire','Marengo','Po','Sesia','Stura','Tanaro'])==1861852
assert get('Piedmont','mixed_evaders',1800)+get('Piedmont','mixed_evaders',1806)==9201
assert len(model)==3*64*20
assert abs(path(1.8,.5,.8,6,10,4)[-1][2] - 1440*.8*sum(.9**k for k in range(4)))<1e-6
report={'source_and_gap_rows':len(rows),'explicit_gap_rows':sum(r['value']=='' for r in rows),'source_status_counts':dict(Counter(r['value_status'] for r in rows)),'published_estimates':len(ests),'calculation_rows':len(calc),'model_rows':len(model),'statistical_regressions_run':0,'statistical_leave_one_predictions_run':0,'microdata_downloaded':False,'checks':'PASSED: structural/arithmetic only; not causal or documentary validation','crossing_envelopes':{p:{'earliest':min([x for x in xs if x is not None],default=None),'latest_if_crosses_by20':max([x for x in xs if x is not None],default=None),'some_do_not_cross_by20':any(x is None for x in xs)} for p,xs in crossings.items()}}
(R/'Q2_validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
# Side sensitivities: demonstrate service and attrition matter, never a probability.
sens=[]
for p,ps in profiles.items():
    vals=[sum(v)/2 for v in ps.values()]
    for ret,u,L in itertools.product([.85,.9,.95],[.7,.8,.85],[5,7]):
        out=path(*vals,retention=ret,usable=u,service=L)
        for t,a,s,g,n in out:
            if t in [10,20]:sens.append(dict(profile=p,retention=ret,usable=u,service=L,year=t,net_stock=round(n,1),status='MODEL_SENSITIVITY'))
with (R/'Q2_stock_sensitivity.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sens[0]));w.writeheader();w.writerows(sens)
print(json.dumps(report,ensure_ascii=False,indent=2))
print('MODEL ENVELOPES (per million population; not confidence intervals)')
for s in summ:print(s)
