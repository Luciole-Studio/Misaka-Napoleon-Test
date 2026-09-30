"""F2 transparent scenario arithmetic; NOT an estimated historical law.
Units: persons, horses, years, kilograms. All normative/model inputs below are
explicit assumptions. Empirical anchors and scope are in SOURCES.md and main report.
Run: python3 F2_model.py (writes only alongside this script).
"""
from pathlib import Path
import csv, json, math
OUT = Path(__file__).resolve().parent

def save(name, rows):
    with (OUT/name).open('w', newline='', encoding='utf-8-sig') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

# Demand = simultaneous present-duty billets; no training/hospital personnel here.
regions = {
'S2': [('core',75000,90000,100000),('coast',35000,45000,55000),('mobile_reserve',150000,160000,200000),('Germany',70000,85000,110000),('Italy',50000,65000,80000),('SE_border',15000,20000,30000),('Poland_east',50000,70000,90000),('Iberia',0,5000,15000)],
'S5': [('core',80000,90000,100000),('coast',35000,40000,50000),('mobile_reserve',150000,160000,180000),('Germany',55000,70000,85000),('Italy',40000,50000,65000),('SE_border',15000,20000,25000),('Poland_east',45000,55000,70000),('Iberia',0,5000,10000)],
'S6_coercive': [('core',90000,100000,110000),('coast',60000,70000,85000),('mobile_reserve',180000,200000,220000),('Germany',130000,155000,180000),('Italy',80000,100000,120000),('Habsburg_lands',120000,150000,180000),('Poland_east',60000,80000,100000),('Iberia',180000,230000,280000),('Scandinavia',20000,30000,40000)]}
rows=[]
for s, rs in regions.items():
    for reg,lo,c,hi in rs:
        rows.append(dict(scenario=s,region=reg,low=lo,central=c,high=hi,unit='persons_present',status=('legacy_audit_only_use_disaggregated_S6' if s=='S6_coercive' else 'model_assumption'),anchor='O11;E97_III;G03_pp26_161;P10'))
save('F2_garrison.csv',rows)
summary=[]
for s,gross,q in [('S2',700000,.85),('S5',750000,.85),('S6_coercive',1000000,.80)]:
    rs=regions[s]; lo=sum(x[1] for x in rs); c=sum(x[2] for x in rs); hi=sum(x[3] for x in rs)
    summary.append(dict(scenario=s,gross_stock_assumption=gross,present_ratio_assumption=q,present_supply=round(gross*q),demand_low=lo,demand_central=c,demand_high=hi,balance_central=round(gross*q-c),balance_if_low_demand=round(gross*q-lo),balance_if_high_demand=round(gross*q-hi),status=('legacy_audit_only_use_disaggregated_S6' if s=='S6_coercive' else 'conditional_model_not_forecast')))
save('F2_scenarios.csv',summary)

# Stock-flow approximation, not exact cohort discharge: C entrants, s conversion,
# L planned normal service/retirement parameter, not realized duration including deaths.
# Main model uses retirement hazard1/L; fixed-term variant is also calculated.
# mu OTHER permanent exits. q affects usable stock only.
stock=[]
for C in [90000,105000,115000]:
    for L in [5,6,7]:
        for mu in [.015,.025,.04]:
            N=.9*C/(1/L+mu)
            stock.append(dict(annual_call=C,conversion=.9,service_years=L,other_exit_rate=mu,steady_gross=round(N),fixed_term_variant=round(.9*C*(1-math.exp(-mu*L))/mu),status='sensitivity_assumptions',anchor='P11;H72_pp49_50;peace_analogy'))
save('F2_replacement_sensitivity.csv',stock)

# Central annual peace path. 1808 starting stock is assumed, NOT reconstructed.
# No population-growth extrapolation. S5 raises calls only 10k after 1815.
trajectory=[]
for scenario in ['S2','S5']:
    N=500000.
    for y in range(1808,1849):
        C=115000 if scenario=='S5' and y>=1815 else 105000
        demand=490000 if scenario=='S5' and y>=1815 else 540000
        beginning=N; trained=.9*C; exits=N*(1/6+.025); N=N+trained-exits
        ready=.85*(N+200000)
        trajectory.append(dict(scenario=scenario,year=y,french_opening_gross=round(beginning),calls_assumption=C,trained_inflow=round(trained),exit_flow_approx=round(exits),french_closing_gross=round(N),allied_gross_assumption=200000,present_total=round(ready),demand_present=demand,balance_present=round(ready-demand),status='model_not_observed',source='model_inputs;H72;P11;E97;G03'))
save('F2_peace_annual_model.csv',trajectory)

# Extra provinces sensitivity; population is a SCENARIO size, not a territorial census.
# Do not add this potential recruitment to core stock until the new recruiting system matures.
new=[]
for P in [10000000,20000000,30000000]:
    for rho in [.6,1.0]:
        for d in [.003,.015,.025]:
            C=.002*P; gross=.9*C/(1/6+.025); available=.85*rho*gross
            req=P*d + .001*P # extra external/security tasks, separately assumed
            new.append(dict(new_population_assumption=P,annual_call_rate_assumption=.002,reliability_assumption=rho,policing_density_assumption=d,extra_frontier_density_assumption=.001,mature_gross_potential=round(gross),mature_reliable_present=round(available),present_cost=round(req),net_present=round(available-req),steady_state_only=True,status='model_assumptions_not_empirical_coefficients'))
save('F2_annexation_sensitivity.csv',new)

checks={
'oman_gross_sum':sum([90186,25537,57949,51088,99442,30259]),
'oman_present_printed_sum':sum([68827,23139,38633,48783,88442,23590]),
'oman_aragon_detail_sum':sum([7689,7826,6380,4433,4892,1808,1876,3645,2244,2990]),
'oman_present_using_detail':sum([68827,23139,38633,43783,88442,23590]),
'oman_printed_present_ratio':291414/354461,
'oman_detail_present_ratio':286414/354461,
'census1797_population':10541221,
'oman_gross_per_1000_using1797':354461/10541221*1000,
'oman_gross_per_1000_using11m_assumption':354461/11000000*1000,
'vcreveld_source_status':'author_hypothetical200k_not_observed;tons_unspecified_in_passage;metric_food_is_model_normalization',
'food_kg_per_person_day_model_assumption':1.5,
'vcreveld_food_200k_tonnes_per_day':200000*1.5/1000,
'vcreveld_600_miles_20miles_day_roundtrip_days':2*600/20,
'vcreveld_haul_capacity_source_tons_unspecified':300*2*600/20,
'vcreveld_haul_capacity_tonnes_metric_normalization_assumption':300*2*600/20,
'peace_central_replacement_for500k':500000*(1/6+.025)/.9,
'war_replacement_for750k_mu105':750000*(1/6+.105)/.9,
'S2_allies100k_gross_loss_present':100000*.85,
'S2_central_margin_after_allies100k_loss':595000-85000-540000,
'S5_central_margin_after_allies100k_loss':637500-85000-490000,
'food500k_plus125k_horses_10kg_assumption_tonnes_day':(500000*1.5+125000*10)/1000,
'food500k_plus125k_horses_tonnes_year':(500000*1.5+125000*10)/1000*365,
'fixed_term6_mu025_calls90000':.9*90000*(1-math.exp(-.025*6))/.025,
'fixed_term6_mu025_calls115000':.9*115000*(1-math.exp(-.025*6))/.025,
'Brun_15month_arithmetic_residual_not_observed':811000+159000-880000,
'Brun_new_over_warehouse_use':159000/880000,
'Brun_300k_weapons_months_at8k':300000/8000,
'Brun_300k_weapons_months_at10k':300000/10000,
'Brun_300k_weapons_months_at18k':300000/18000,
'warning':'All non-source inputs are assumptions; no probabilities, no empirical causality estimated.'}
assert checks['oman_gross_sum']==354461
assert checks['oman_present_printed_sum']==291414
assert checks['oman_aragon_detail_sum']==43783
assert checks['oman_present_using_detail']==286414
assert len(trajectory)==82
assert all(x['low']<=x['central']<=x['high'] for x in rows)
(OUT/'F2_model_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'scenario_summaries':summary,'checks':checks,'status':'arithmetic_assertions_passed'},ensure_ascii=False,indent=2))
