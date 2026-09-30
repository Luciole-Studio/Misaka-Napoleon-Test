#!/usr/bin/env python3
"""F3: conditional capacity envelope, not a fitted historical forecast.
All annual steps end at a representative mid-year; t0 = summer 1810.
W = continental peace but continuing maritime war.
P = W until mid-1815, then maritime truce + sustained naval investment.
Only arithmetic, no fitted probabilities or hidden interpolation.
"""
from pathlib import Path
import csv, json, math, subprocess, hashlib
ROOT=Path(__file__).resolve().parent
BACKEND=Path('/Users/makiko/.misaka/shared/skill-library/repair-20260917T042736Z/skills/planning-labs/capacity-balance-lab/scripts/capacity_balance.py')
PY=Path('/Users/makiko/.misaka/shared/skill-library/repair-20260917T042736Z/runtime/python/bin/python')

PARAMS={
 'description':'Explicit assumption envelope. Not a confidence interval, historical series or probability estimate.',
 'time':'annual mid-year stock; 1810 summer baseline; first full annual step labelled 1811; P maritime truce starts after mid-1815',
 'extension':'1831-1835 holds the 1821-1830 parameters constant for a 25-year stock test, NOT a sail-only strategic forecast; 1830 training factor is capped',
 'initial': {'hulls':50,'total_personnel_thousands':[60,65,70],'qualified_personnel_thousands':[35,40,45]},
 'bounds':['low','base','high'],
 'W':{
   'launches_1811_1815':[8,10,12], 'launches_1816_1820':[7,8.5,10], 'launches_1821_1830':[6,7,8],
   'hull_retirement_rate':[.06,.05,.04], 'annual_war_losses_ships':[1.5,1,.5],
   'personnel_exit_rate':[.10,.09,.08], 'personnel_inflow_thousands':[8,10,12],
   'qualified_exit_rate':[.07,.06,.05], 'qualified_inflow_thousands':[4,4.5,5],
   'hull_ready_fraction':[.70,.775,.85], 'other_personnel_thousands':[25,30,35],
   'other_qualified_thousands':[15,17.5,20],
   'fleet_training_factor_1815':[.55,.65,.75], 'fleet_training_factor_1830':[.65,.75,.85],
   'annual_sea_training_days_assumed':[30,55,80],
   'commissioned_share_of_mobilizable':[.80,.875,.95]
 },
 'P_after_1815':{
   'launches_1816_1820':[8,9,10], 'launches_1821_1830':[6,7,8],
   'hull_retirement_rate':[.045,.04,.035], 'annual_war_losses_ships':[.2,.1,0],
   'personnel_exit_rate':[.06,.055,.05], 'personnel_inflow_thousands':[8,9,10],
   'qualified_exit_rate':[.04,.035,.03], 'qualified_inflow_thousands':[5,5.5,6],
   'hull_ready_fraction':[.80,.85,.90],
   'other_personnel_1816_1820_thousands':35, 'other_personnel_1821_1830_thousands':40,
   'other_qualified_1816_1820_thousands':20, 'other_qualified_1821_1830_thousands':23,
   'fleet_training_factor_1830':[.85,.925,1.0],
   'annual_sea_training_days_assumed':[90,120,150],
   'commissioned_share_of_mobilizable':[.45,.55,.65]
 },
 'crew_per_battle_ship_thousands':.8,
 'qualified_crew_per_battle_ship_thousands':.45,
 'mean_loaded_displacement_tonnes':[3200,3500,3800],
 'young_fleet_retirement_rate_1811_1815':[.035,.025,.015],
 'provenance':{
   'hulls':'S01 p15: 50 in summer 1810, including Netherlands; no new allied fleets added twice',
   'personnel':'S01 p16 Ganteaume estimates 30k real French mariners plus limited allied access; S05 1810-07-13 proposed 66k all personnel. Initial 60-70k is assumption, NOT observed muster.',
   'launches':'S01 p15 growth 50->72; S04 1811-03-05 Antwerp 18 slips/3 years/6 per year planned, S06 1811-10-02 8 planned; factual launches separately audited. Long-run schedule includes budget and repair competition.',
   'retirement':'S08 Annales1820 quotation: 52 afloat, 10 condemned 1814-19 plus 2, average 14 years before refit; S01 p15 Antwerp radoub after 8 not10 years. Model geometric rates are NOT estimated hazards.',
   'other_personnel':'S05 plan 66k for50 line +30 frigates +400 small craft; 50*0.8=40k implies order-of-magnitude 26k non-line personnel; reserved pool rises in P to support commerce escort/global tasks',
   'crew_and_displacement':'S11 Clouet 74:705,80:811,118:~1000-1130; loaded displacements ~3080,3704-3875,4830-5095t. 800/450 crew and 3200-3800t averages are scenario assumptions.',
   'training':'S01 pp19-23 actual practice reports, 1813 cruises mean2-3months with heavy losses; S07 institutional sea training; numerical factors/days are explicit sensitivity assumptions, not measured French/RN ratios.',
   'recruitment':'S01 p18 20k coastal conscription levy for1811 is an order, not actual arrival. Model 8-12k entrants,4-6k qualified additions require time, retention and trade; no independent calibrated rates.'
 }
}

def value(a,j): return a[j] if isinstance(a,list) else a

def simulate(s,j):
    init=PARAMS['initial']; h=init['hulls']; p=init['total_personnel_thousands'][j]; q=init['qualified_personnel_thousands'][j]
    rows=[]; commissions=[]; retirements=[]; prior=h
    for y in range(1810,1836):
        k=PARAMS['P_after_1815'] if s=='P' and y>=1816 else PARAMS['W']
        key='launches_1811_1815' if y<=1815 else 'launches_1816_1820' if y<=1820 else 'launches_1821_1830'
        launches=value(k[key],j) if y>1810 else 0
        exit_rate=PARAMS['young_fleet_retirement_rate_1811_1815'][j] if y<=1815 else value(k['hull_retirement_rate'],j)
        natural_exit=h*exit_rate if y>1810 else 0
        losses=value(k['annual_war_losses_ships'],j) if y>1810 else 0
        if y>1810:
            h=h+launches-natural_exit-losses
            p=p*(1-value(k['personnel_exit_rate'],j))+value(k['personnel_inflow_thousands'],j)
            q=q*(1-value(k['qualified_exit_rate'],j))+value(k['qualified_inflow_thousands'],j)
            commissions.append([launches]);retirements.append([natural_exit+losses])
        r=value(k['hull_ready_fraction'],j)
        if s=='P' and y>=1816:
            other=k['other_personnel_1816_1820_thousands' if y<=1820 else 'other_personnel_1821_1830_thousands']
            qother=k['other_qualified_1816_1820_thousands' if y<=1820 else 'other_qualified_1821_1830_thousands']
        else:
            other=value(k['other_personnel_thousands'],j);qother=value(k['other_qualified_thousands'],j)
        candidates=[r*h,(p-other)/PARAMS['crew_per_battle_ship_thousands'],(q-qother)/PARAMS['qualified_crew_per_battle_ship_thousands']]
        available=max(0,min(candidates));integer_available=math.floor(available+1e-9)
        # training is a sensitivity ruler, not an observation or a battle-winning probability
        a0=PARAMS['W']['fleet_training_factor_1815'][j]
        a1=(PARAMS['P_after_1815'] if s=='P' else PARAMS['W'])['fleet_training_factor_1830'][j]
        quality=a0+(a1-a0)*min(15,max(0,y-1815))/15
        days=value(k['annual_sea_training_days_assumed'],j)
        commissioned=math.floor(integer_available*value(k['commissioned_share_of_mobilizable'],j))
        assert 0<=q<=p and h>0 and 0<=available<=h and qother<=q and other<=p
        assert integer_available*PARAMS['crew_per_battle_ship_thousands']+other<=p+1e-8
        assert integer_available*PARAMS['qualified_crew_per_battle_ship_thousands']+qother<=q+1e-8
        rows.append(dict(record_type='model_not_observation',scenario=s,bound=PARAMS['bounds'][j],year=y,
          hulls=round(h,6),launches=launches,natural_retirement=round(natural_exit,6),war_loss=losses,hull_exit_rate=exit_rate,
          personnel_total_1000=round(p,6),qualified_personnel_1000=round(q,6),
          nonline_personnel_reserved_1000=other,nonline_qualified_reserved_1000=qother,
          ready_fraction=r,mobilizable_continuous=round(available,6),mobilizable_integer=integer_available,
          binding=['hull_readiness','personnel','qualified_personnel'][candidates.index(min(candidates))],
          commissioned_model_I=commissioned,
          reserve_ready_within_12m=integer_available-commissioned,
          hulls_not_mobilizable_within12m=round(h-integer_available,6),
          hull_physical_readiness_ceiling=round(r*h,6),
          displacement_hulls_t=round(h*PARAMS['mean_loaded_displacement_tonnes'][j],2),
          displacement_mobilizable_t=integer_available*PARAMS['mean_loaded_displacement_tonnes'][j],
          fleet_training_factor_assumed=round(quality,6),
          trained_ship_equivalents_diagnostic=round(integer_available*quality,4),
          sea_training_days_assumed=days,
          evidence_ids='S01;S04;S05;S06;S07;S08;S11',assumptions='F3_model_parameters.json'))
        if y>1810: assert abs(h-(prior+launches-natural_exit-losses))<1e-8
        prior=h
    # independent replay by the existing stock-flow engine
    inp={'K0':[init['hulls']],'commissioning':commissions,'retirement':retirements,'sectors':['line_hulls']}
    res=subprocess.run([str(PY),str(BACKEND),'stock-flow','--json',json.dumps(inp)],capture_output=True,text=True,check=True)
    reply=json.loads(res.stdout)
    assert reply['ok'] and reply['feasible']
    assert len(reply['trajectory'])==len(rows)
    residual=max(abs(a['hulls']-b['total']) for a,b in zip(rows,reply['trajectory']))
    assert residual<1e-5
    return rows,dict(scenario=s,bound=PARAMS['bounds'][j],input=inp,backend_output=reply,max_abs_replay_residual=residual)

if __name__=='__main__':
    rows=[];audit=[]
    for s in ['W','P']:
        for j in range(3):
            r,a=simulate(s,j);rows.extend(r);audit.append(a)
    (ROOT/'F3_model_parameters.json').write_text(json.dumps(PARAMS,ensure_ascii=False,indent=2)+'\n')
    with (ROOT/'F3_capacity.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    (ROOT/'F3_model_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    keyrows=[r for r in rows if r['year'] in [1815,1820,1825,1830,1835]]
    table=['|情景/参数|年|船体H|总人员千人|合格人员千人|可动员整舰A|船体排水量千吨|训练舰当量（诊断）|','|---|---:|---:|---:|---:|---:|---:|---:|']
    for r in keyrows:
        table.append(f"|{r['scenario']}/{r['bound']}|{r['year']}|{r['hulls']:.1f}|{r['personnel_total_1000']:.1f}|{r['qualified_personnel_1000']:.1f}|{r['mobilizable_integer']}|{r['displacement_hulls_t']/1000:.1f}|{r['trained_ship_equivalents_diagnostic']:.1f}|")
    (ROOT/'F3_model_keypoints.md').write_text('\n'.join(table)+'\n')
    print('\n'.join(table))
    print('rows=',len(rows),'all personnel/hull constraints checked; backend stock-flow replay outputs saved')
