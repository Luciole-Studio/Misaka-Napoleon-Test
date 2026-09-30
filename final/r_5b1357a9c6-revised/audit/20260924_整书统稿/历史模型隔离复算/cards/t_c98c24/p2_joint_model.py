#!/usr/bin/env python3
"""P2 conditional scenario accounting, not historical fit or a statistical forecast.
Inputs are frozen in territory_inputs.csv. Python stdlib only. Run from any cwd.
Outputs region_detail.csv, scenario_summary.csv, scenario_sensitivity.csv.
"""
from __future__ import annotations
import csv
import itertools
from pathlib import Path

ROOT=Path(__file__).resolve().parent
D={}
with (ROOT/'territory_inputs.csv').open(newline='') as f:
    for r in csv.DictReader(f):
        for k in ('pop_m','departments','baseline_B_fr_present','ally_roster_B',
                  'garrison_low_per1000','garrison_mid_per1000','garrison_high_per1000',
                  'gend_low_per1000','gend_mid_per1000','gend_high_per1000',
                  'gend_local_share','official_local_share','call_per1000','incorporation',
                  'reliable','surplus_low_Mfr','surplus_mid_Mfr','surplus_high_Mfr'):
            r[k]=float(r[k]);
        D[r['region']]=r
CORE=('old_france','D1_inner')
A=('Parma',)
SELECT=('Tuscany','Valais')
WEST=('Berg','Westphalia','west_rest')
FOUR=('north_Italy',*WEST,'Illyria','Catalonia')
OTHER=('Tuscany','Valais','Holland','Hanseatic','Rome')
C=('south_Germany','Naples_mainland','Spain_rest')
CASES={
 'A_inner_1810': CORE+A,
 'B_select_no_Berg_1825':CORE+A+SELECT,
 'B_select_Berg_1825':CORE+A+SELECT+('Berg',),
 'B_full_four_1815':CORE+A+FOUR,
 'B_full_historical_outer_1815':CORE+A+FOUR+OTHER,
 'C_province_pressure_1830':CORE+A+FOUR+OTHER+C,
 'historical_direct_1812_scale_only':CORE+A+OTHER,
}
assert all(len(set(v))==len(v) for v in CASES.values())
assert abs(sum(D[n]['pop_m'] for n in FOUR)-13.1)<1e-8
F2_S2_DEMAND=540000.0
F2_INNER_7M_PRESENT=28000.0
F2_HUMAN_FRENCH_ROSTER=500000.0
F4_ARMY_BUDGET_M=300.0
F4_ALLIED_ROSTER=200000.0
F4_FR_UNIT_COST=700.0
PRESENT=0.85
# Five-year illustrative normal term with one training year and 10% cohort decay.
# year=10 has cohorts indexed 0..3, not ten cumulative cohorts in service.
def mature_present(r:dict, years:float)->float:
    if r['status_1812']=='existing_direct' or r['region'] in CORE: return 0.0
    terms=min(4,max(0,int(years)-1))
    return (r['pop_m']*1_000_000*r['call_per1000']/1000 *
            r['incorporation']*r['reliable']*sum(0.9**i for i in range(terms)))

fields=['case','region','pop_m','departments','gross_gend_mid','locally_recruited_gend_mid',
        'france_recruited_gend_mid','senior_posts_mid','externally_recruited_senior_mid',
        'all_paid_civil_posts_mid','externally_recruited_paid_mid',
        'garrison_mid_present','B_French_garrison_already_present',
        'incremental_garrison_present','lost_independent_B_roster','annual_levy_nominal',
        'annual_arrived','mature_extra_present_y10','cash_surplus_pre_incremental_army_Mfr']
details=[]
for case,names in CASES.items():
    for n in names:
        r=D[n]; p=r['pop_m']*1_000_000
        gend=p*r['gend_mid_per1000']/1000
        civil=r['departments']*160
        senior=r['departments']*10
        billet=p*r['garrison_mid_per1000']/1000
        is_core=n in CORE
        increment=0.0 if is_core else max(0,billet-r['baseline_B_fr_present'])
        cash=0.0 if is_core or r['status_1812']=='existing_direct' else r['surplus_mid_Mfr']
        details.append(dict(case=case,region=n,pop_m=r['pop_m'],departments=r['departments'],
          gross_gend_mid=gend,locally_recruited_gend_mid=gend*r['gend_local_share'],
          france_recruited_gend_mid=gend*(1-r['gend_local_share']),
          senior_posts_mid=senior,externally_recruited_senior_mid=senior*(1-r['official_local_share']),
          all_paid_civil_posts_mid=civil,externally_recruited_paid_mid=civil*(1-r['official_local_share']),
          garrison_mid_present=billet,B_French_garrison_already_present=r['baseline_B_fr_present'] if not is_core else billet,
          incremental_garrison_present=increment,lost_independent_B_roster=r['ally_roster_B'] if not is_core else 0,
          annual_levy_nominal=p*r['call_per1000']/1000,
          annual_arrived=p*r['call_per1000']/1000*r['incorporation'],
          mature_extra_present_y10=mature_present(r,10),
          cash_surplus_pre_incremental_army_Mfr=cash))

def calc(case,level='mid',years=10,frgross=F2_HUMAN_FRENCH_ROSTER,
         allied=F4_ALLIED_ROSTER,army_budget=F4_ARMY_BUDGET_M,
         cost=F4_FR_UNIT_COST,ally_retained_fraction=0.0,baseline_task_shift=0.0,
         removed_historical_tax_net_Mfr=0.0,cash_level=None):
    names=CASES[case]; rows=[D[n] for n in names]
    inner=D['D1_inner']; inner_change=inner['pop_m']*1_000_000*inner[f'garrison_{level}_per1000']/1000-F2_INNER_7M_PRESENT
    delta=sum(max(0,r['pop_m']*1_000_000*r[f'garrison_{level}_per1000']/1000-r['baseline_B_fr_present']) for r in rows if r['region'] not in CORE)
    # Full lost A-state independent units replaced neither on the B ledger nor as free French units.
    roster_removed=sum(r['ally_roster_B'] for r in rows if r['region'] not in CORE)*(1-ally_retained_fraction)
    allies_left=allied-roster_removed
    assert allies_left>=0,(case,allies_left)
    # Retained self-financed B units keep their recruitment base: do not also
    # count the same share of local recruits as a new French cohort.
    new_conscripts=sum(mature_present(r,years)*(1-ally_retained_fraction if r['ally_roster_B'] else 1)
                       for r in rows if r['region'] not in CORE)
    demand=F2_S2_DEMAND+inner_change+delta+baseline_task_shift
    physical_supply=(frgross+allies_left)*PRESENT+new_conscripts
    # F4's high 800M central tax case already incorporates historical directly
    # annexed regions. Those cannot be counted as fresh Paris revenue again.
    # A territory returned to B may lower old tax; uncertain net, tested separately.
    cash_level=cash_level or level
    cash_delta=sum(r[f'surplus_{cash_level}_Mfr']*(1-ally_retained_fraction if r['ally_roster_B'] else 1)
                   for r in rows if r['region'] not in CORE and r['status_1812']!='existing_direct')
    withheld=army_budget-removed_historical_tax_net_Mfr
    # If a former vassal's billet still stays earmarked locally, cash_delta must EXCLUDE
    # that earmark; it cannot also be counted as a remittance to Paris.
    required_french_roster=max(0,(demand-allies_left*PRESENT)/PRESENT)
    french_roster_paid=(withheld+cash_delta)*1_000_000/cost
    budget_gap_Mfr=(required_french_roster*cost/1_000_000-withheld-cash_delta)
    gov_dept=sum(r['departments'] for r in rows)
    official_gross_low=gov_dept*100; official_gross_mid=gov_dept*160; official_gross_high=gov_dept*220
    gend_demand=sum(r['pop_m']*1_000_000*r[f'gend_{level}_per1000']/1000 for r in rows)
    external_official=sum(r['departments']*160*(1-r['official_local_share']) for r in rows)
    external_gend=sum(r['pop_m']*1_000_000*r[f'gend_{level}_per1000']/1000*(1-r['gend_local_share']) for r in rows)
    # Some B-roster units may remain only if explicit politics *and* funding is retained;
    # they appear in allies_left, not also new French recruits.
    return dict(case=case,level=level,years_since_new_annex=years,
       population_m=sum(r['pop_m'] for r in rows),departments=gov_dept,
       gross_senior_posts=gov_dept*10,gross_civil_low=official_gross_low,
       gross_civil_mid=official_gross_mid,gross_civil_high=official_gross_high,
       externally_recruited_paid_mid=external_official,
       gross_gendarmes=gend_demand,foreign_recruited_gendarmes=external_gend,
       gend_over_1809_actual=gend_demand/15474,gend_over_1811_regulation=gend_demand/26000,
       baseline_demand=F2_S2_DEMAND,inner_revision=inner_change,
       additional_garrison_present=delta,allied_roster_lost=roster_removed,
       allied_roster_remaining=allies_left,annual_nominal_levy=sum(r['pop_m']*1_000_000*r['call_per1000']/1000 for r in rows if r['region'] not in CORE),
       annual_arrived=sum(r['pop_m']*1_000_000*r['call_per1000']/1000*r['incorporation'] for r in rows if r['region'] not in CORE),
       mature_extra_present=new_conscripts,demand_present=demand,human_present_supply=physical_supply,
       human_balance_present=physical_supply-demand,
       required_french_roster=required_french_roster,
       french_paid_roster=french_roster_paid,cash_delta_Mfr=cash_delta,
       excluded_historical_direct_tax_net_penalty_Mfr=removed_historical_tax_net_Mfr,
       minimum_extra_central_army_Mfr=max(0,required_french_roster*cost/1_000_000-withheld),
       army_budget_gap_Mfr=budget_gap_Mfr,
       human_assumption='F2_500k_Fr_plus200k_B;new_A_recruits_exclude_actual1812_A_regions',
       cash_assumption='F4_300M_Fr_army_700fr_per_head;1812_existing_direct_cash_already_in_base;regional_new_cash_hypothetical',
       note='all_counts_not_same_year_census;annual_levy_not_extra_stock;no_navy_growth_paid_twice')

def save(name,rows,headers=None):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=headers or list(rows[0]));w.writeheader();w.writerows(rows)

save('region_detail.csv',details,fields)
rows=[calc(c,lev,10) for c,lev in itertools.product(CASES,('low','mid','high'))]
save('scenario_summary.csv',rows)
save('P2_budget.csv',rows)
# Independent accounting identities and scope checks, not historical validation.
for z in rows:
    assert abs(z['human_present_supply']-z['demand_present']-z['human_balance_present'])<1e-6
    assert abs((z['french_paid_roster']*PRESENT+z['allied_roster_remaining']*PRESENT-z['demand_present'])
               +z['army_budget_gap_Mfr']*1_000_000/F4_FR_UNIT_COST*PRESENT)<1e-6
    assert z['mature_extra_present']<=z['annual_arrived']*4+1e-6
assert abs(calc('C_province_pressure_1830')['population_m']-77.317)<1e-8
assert calc('B_select_Berg_1825',years=0)['mature_extra_present']==0
assert calc('B_select_Berg_1825',ally_retained_fraction=1)['mature_extra_present']==0
sens=[]
for c,ally_keep,armycost,budget,years,shift,removed_net in itertools.product(
 ('B_select_Berg_1825','B_full_historical_outer_1815','C_province_pressure_1830'),
 (0,0.5,1),(600,700,900),(250,300,350),(0,10),(-30000,0,30000),(0,30,60)):
    z=calc(c,'mid',years,500000,200000,budget,armycost,ally_keep,shift,
           removed_historical_tax_net_Mfr=removed_net if c.startswith('B_select') else 0)
    sens.append(dict(case=c,ally_retained_fraction=ally_keep,fr_cost=armycost,
      initial_army_budget_Mfr=budget,years=years,baseline_task_shift=shift,
      removed_historical_tax_net_Mfr=removed_net if c.startswith('B_select') else 0,
      human_balance_present=z['human_balance_present'],budget_gap_Mfr=z['army_budget_gap_Mfr'],
      lost_B_roster=z['allied_roster_lost'],required_fr_roster=z['required_french_roster']))
save('scenario_sensitivity.csv',sens)
# Cross all revenue and garrison settings; diagonal low/mid/high is not a bound.
corners=[]
for c,glev,tlev in itertools.product(CASES,('low','mid','high'),('low','mid','high')):
    z=calc(c,glev,cash_level=tlev)
    corners.append(dict(case=c,garrison_level=glev,revenue_level=tlev,
        demand_present=z['demand_present'],human_balance_present=z['human_balance_present'],
        cash_delta_Mfr=z['cash_delta_Mfr'],army_budget_gap_Mfr=z['army_budget_gap_Mfr']))
save('P2_corners.csv',corners)
policy=[]
for c,allies,budget,penalty,shift in itertools.product(
    ('B_select_no_Berg_1825','B_select_Berg_1825'),(200000,250000),(300,330),(0,30,60),(0,30000)):
    z=calc(c,allied=allies,army_budget=budget,removed_historical_tax_net_Mfr=penalty,
           baseline_task_shift=shift)
    paid_present=z['french_paid_roster']*PRESENT+z['allied_roster_remaining']*PRESENT
    policy.append(dict(case=c,allied_initial_roster=allies,army_before_tax_penalty_Mfr=budget,
       tax_penalty_Mfr=penalty,task_shock_present=shift,fr_paid_roster=z['french_paid_roster'],
       allied_remaining_roster=z['allied_roster_remaining'],paid_present_supply=paid_present,
       demand_present=z['demand_present'],paid_present_balance=paid_present-z['demand_present'],
       fiscal_gap_Mfr=z['army_budget_gap_Mfr']))
save('P2_policy_closure.csv',policy)
# Deliberately seek a counterexample to the baseline negative verdict.
optimistic=[]
for c in ('B_full_historical_outer_1815','C_province_pressure_1830'):
    z=calc(c,'low',ally_retained_fraction=1,army_budget=350,cost=700,
           baseline_task_shift=-30000,cash_level='high')
    optimistic.append(dict(case=c,garrison_level='low',revenue_level='high',
       ally_retained_fraction=1,army_budget_Mfr=350,unit_cost=700,task_shift=-30000,
       human_balance_present=z['human_balance_present'],budget_gap_Mfr=z['army_budget_gap_Mfr'],
       demand_present=z['demand_present'],required_fr_roster=z['required_french_roster'],
       cash_delta_Mfr=z['cash_delta_Mfr']))
save('P2_joint_optimistic.csv',optimistic)
if __name__=='__main__':
    for x in rows:
        if x['level']=='mid':
            print(x['case'], 'population_m',round(x['population_m'],3),
              'civil',x['gross_civil_mid'],'gend',round(x['gross_gendarmes']),
              'demand',round(x['demand_present']),'phys_bal',round(x['human_balance_present']),
              'budget_gap_Mfr',round(x['army_budget_gap_Mfr'],1))
