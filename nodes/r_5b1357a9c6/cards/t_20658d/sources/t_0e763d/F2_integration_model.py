"""F2 disaggregation and tenure supplement. All density/reliability inputs are
scenario assumptions, NOT estimated historical coefficients. This refines, not
validates, the earlier S6_coercive aggregate stress-test. Population values are
scenario geographic proxies; see notes_new_analogies.md and SOURCES.md.
"""
from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def save(name,rows):
 with (P/name).open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# name,population_proxy,densities per1000 OR fixed troop assignments, source anchors
base=[
 ('old_France',30000000,(2,70/30,80/30),'H72_magnitude;not_exact_census'),
 ('inner_annexed_ring',7000000,(3,4,5),'P10J_37m_minus_model30m;G03_Belgium_Piedmont'),
 ('north_Italian_kingdom',6700000,(5,7.5,10),'G03_pp158_162;SON04;OOB48'),
 ('west_Germany_new_excludes_left_Rhine',4000000,(5,7.5,10),'scenario_map_proxy;G03_allied_army_mechanism'),
 ('Illyria',1500000,(8,12,16),'G03_pp188_191;P10'),
 ('coastal_special_units',None,(35000,45000,55000),'E97_III;P11;separate_from_regional_billets'),
 ('mobile_central_reserve',None,(150000,175000,200000),'E97_III;strategic_design_not_density'),
 ('remaining_Germany_allied_tasks',None,(40000,55000,70000),'G03_p26;political_contract_assumption'),
 ('Poland_eastern_deterrence',None,(50000,70000,90000),'V77;G03;not_occupation_of_Russia'),
 ('southern_Italy_allied_tasks',None,(15000,20000,30000),'G03_p26;not_Sicily_conquest'),
 ('Spain_liaison',None,(0,5000,15000),'O11_counterfactual_avoided_war')]
rows=[]
for scenario in ['S6_lite','S6_max','S6_full']:
 vals=list(base)
 if scenario!='S6_lite':
  vals=[x for x in vals if x[0] not in ['remaining_Germany_allied_tasks','southern_Italy_allied_tasks','Spain_liaison','coastal_special_units','mobile_central_reserve']]
  vals += [
   ('south_Germany_new',6000000,(8,11,15),'scenario_map_proxy;G03_allied_exit_mechanism'),
   ('remaining_north_German_tasks',None,(15000,20000,30000),'scenario_contract_not_annexation'),
   ('Naples_mainland',5000000,(10,14,18),'scenario_population_proxy;G03_Calabria;FR06_analogy'),
   ('Spain_all',10541221,(180000/10541.221,230000/10541.221,280000/10541.221),'C1797_lagged;O11_theater_present_27.17-27.65permille'),
   ('coastal_special_units',None,(60000,70000,85000),'E97_III;O11;extra_ports'),
   ('mobile_central_reserve',None,(180000,200000,220000),'E97_III;strategic_design')]
 if scenario=='S6_full':
  vals += [('Habsburg_residual_excludes_Illyria',25000000,(4.8,6,7.2),'scenario_map_proxy;must_replace_with_A_card'),
           ('Scandinavia',8000000,(2.5,3.75,5),'scenario_map_proxy;not_simultaneous_royal_navy_defeat')]
 for name,pop,dens,src in vals:
  amount=[round(pop*d/1000) for d in dens] if pop else list(dens)
  rows.append(dict(scenario=scenario,region=name,population_proxy=pop or '',population_status='scenario_proxy_not_common_year_census' if pop else 'not_population_scaled_task',density_low_per1000=round(dens[0],5) if pop else '',density_central_per1000=round(dens[1],5) if pop else '',density_high_per1000=round(dens[2],5) if pop else '',present_low=amount[0],present_central=amount[1],present_high=amount[2],source_anchors=src,density_status='assumption_not_historical_estimate',territory_note='excludes_Britain_Russia_Ottoman_hinterland;no_Sicily_or_Portugal_annexation'))
save('F2_garrison_disaggregated.csv',rows)
sums=[]
for scenario,gross,q in [('S6_lite',700000,.85),('S6_max',1000000,.8),('S6_full',1000000,.8)]:
 r=[x for x in rows if x['scenario']==scenario];lo=sum(x['present_low'] for x in r);c=sum(x['present_central'] for x in r);hi=sum(x['present_high'] for x in r)
 sums.append(dict(scenario=scenario,present_supply=round(gross*q),supply_status='lite_same700k_no_free_new_army;others_deliberately_generous1000k',demand_low=lo,demand_central=c,demand_high=hi,balance_low=round(gross*q-lo),balance_central=round(gross*q-c),balance_high=round(gross*q-hi),sustainable800k_at85_balance_central=round(680000-c),lite_30k_gross_allied_interruption_balance=round(gross*q-.85*30000-c) if scenario=='S6_lite' else '',status='conditional_sensitivity_no_probability'))
save('F2_s6_scenarios.csv',sums)
# Annual maturation path for a representative1000 residents, zero inherited army.
# Existing allied units transferred into French status are NOT new additions.
# Retention hazard follows main model, annual training delay of1 year.
traj=[]
for rho in [.6,1.0]:
 N=0
 for t in range(0,13):
  if t>0:N=N*(1-1/6-.025)+(1.8 if t>=2 else 0)
  q=.85;available=N*q*rho
  traj.append(dict(year_after_annexation=t,representative_population=1000,annual_call=2,conversion=.9,trained_inflow=1.8 if t>=2 else 0,gross_local_stock=round(N,5),reliability=rho,reliable_present=round(available,5),low_pressure_policing=3,extra_border=1,net_present=round(available-4,5),status='illustrative_unfitted;one_year_training_delay'))
save('F2_integration_annual_model.csv',traj)
# 240k/350k/500k: fixed six-year survival; indefinite law is not infinite service.
terms=[]
for n in [240000,350000,500000]:
 for regime,L in [('fixed6',6),('indefinite_effective8',8),('indefinite_effective10',10),('indefinite_effective12',12),('no_discharge_shortterm_floor',None)]:
  mu=.025;s=.9
  c=n*mu/(s*(1-math.exp(-mu*L))) if regime=='fixed6' else (n*(1/L+mu)/s if L else n*mu/s)
  terms.append(dict(target_gross=n,regime=regime,service_years_parameter=L or '',conversion=s,other_permanent_exit=mu,calls_needed=round(c),cohort_reference=300000,cohort_share=round(c/300000,5),cohort_status='H72_1790_95_oldFrance_reference_not_full_annexed_pool',source='R18;H72;E97_XVI',interpretation='model_not_observed;indefinite_length_unestimated'))
save('F2_service_regimes.csv',terms)
# Joint F4/F2 interface: price ranges have different cost scope; not observed cost law.
joint=[]
for budget in [230000000,300000000,350000000]:
 for cost in [600,700,900]:
  for allies in [150000,200000,250000]:
   french=budget/cost;present=(french+allies)*.85
   joint.append(dict(army_budget_francs=budget,cost_proxy_francs_per_gross_soldier=cost,cost_scope='pay_upkeep_only_600;arms_remounts700;Naples_high900;not_linear_empirical_cost',French_gross_supported=round(french),independent_allies_gross=allies,present_ratio=.85,total_present=round(present),S2_balance=round(present-540000),S5_balance=round(present-490000),S6_lite_balance=round(present-566250),annual_army_calls_hazard6=round(french*(1/6+.025)/.9),status='conditional_joint_budget_not_observation',source='M25_pp322_323_viaMollien;F4_fixedJune1810_taxcore;F2_scenarios'))
save('F2_joint_budget_manpower.csv',joint)
checks={'O10_reported_grand_total':360603,'O10_column_sum':9484+287650+16287+44254+2898,'O10_author_inSpain_total':324996,'O10_author_inSpain_present':262051,'O10_present_ratio':262051/324996,'O10_present_per1000_using1797':262051/10541221*1000,'joint_budget_rows':len(joint),'S6':sums,'Oman_present_density_using1797_low':286414/10541221*1000,'Oman_present_density_using1797_high':291414/10541221*1000,'Oman_present_density_using11m_low':286414/11000000*1000,'Oman_present_density_using11m_high':291414/11000000*1000,'service_regimes':terms,'maturation60_percent_first_positive_year':next(x['year_after_annexation'] for x in traj if x['reliability']==.6 and x['net_present']>0)}
assert len(rows)==37
assert all(r['present_low']<=r['present_central']<=r['present_high'] for r in rows)
assert sums[2]['demand_central']-sums[1]['demand_central']==180000
(P/'F2_integration_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False,indent=2))
