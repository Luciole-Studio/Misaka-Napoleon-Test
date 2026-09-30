"""Independent arithmetic/content audit. No historical validity inferred from passes."""
from pathlib import Path
import csv,math,json,re,hashlib,unicodedata
P=Path(__file__).resolve().parent
ROOT=P.parents[3]
def rows(name):
 with (P/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def norm(s):return ' '.join(unicodedata.normalize('NFKC',s).replace('’',"'").replace('‘',"'").split())
a=rows('F2_capacity.csv');assert len(a)==12
assert [int(x['year']) for x in a]==list(range(1803,1815))
assert all(x['national_incorporated_actual']=='' and x['national_annual_deaths']=='' for x in a)
assert all(x['male_cohort_source'] and x['retirement_source'] for x in a)
assert a[7]['force_reported_total']=='324996' and a[7]['force_present_low']=='262051'
assert a[8]['force_present_low']=='286414' and a[8]['force_present_high']=='291414'
assert a[9]['foreign_share_status'].startswith('strictly_more_than_half')
r=rows('F2_garrison_disaggregated.csv');summ=rows('F2_s6_scenarios.csv');assert len(r)==37
for x in summ:
 local=[y for y in r if y['scenario']==x['scenario']]
 for k in ['low','central','high']:
  total=sum(int(y['present_'+k]) for y in local)
  assert total==int(x['demand_'+k])
  assert int(x['present_supply'])-total==int(x['balance_'+k])
  for y in local:
   if y['population_proxy']:
    # Density CSV rounded to5 decimals so recomposition tolerates0.5 persons.
    assert abs(float(y['population_proxy'])*float(y['density_'+k+'_per1000'])/1000-int(y['present_'+k]))<.51
assert all(y['density_status']=='assumption_not_historical_estimate' for y in r)
assert int(summ[2]['demand_central'])-230000+5000==877250
traj=rows('F2_integration_annual_model.csv');assert len(traj)==26
for rel,first in [(0.6,10),(1.,5)]:
 t=[x for x in traj if float(x['reliability'])==rel];n=0
 for x in t:
  year=int(x['year_after_annexation'])
  if year:n=n*(1-1/6-.025)+(1.8 if year>=2 else 0)
  assert abs(float(x['gross_local_stock'])-n)<.000006
  assert abs(float(x['net_present'])-(n*.85*rel-4))<.000006
 assert min(int(x['year_after_annexation']) for x in t if float(x['net_present'])>0)==first
terms=rows('F2_service_regimes.csv');assert len(terms)==15
for x in terms:
 n=float(x['target_gross']);L=float(x['service_years_parameter'] or 0)
 c=n*.025/(.9*(1-math.exp(-.025*6))) if x['regime']=='fixed6' else n*((1/L if L else 0)+.025)/.9
 assert abs(float(x['calls_needed'])-c)<.51
joint=rows('F2_joint_budget_manpower.csv');assert len(joint)==27
for x in joint:
 n=float(x['army_budget_francs'])/float(x['cost_proxy_francs_per_gross_soldier'])
 ready=(n+float(x['independent_allies_gross']))*.85
 assert abs(float(x['total_present'])-ready)<.51
 assert abs(float(x['annual_army_calls_hazard6'])-n*(1/6+.025)/.9)<.51
 for key,demand in [('S2',540000),('S5',490000),('S6_lite',566250)]:assert abs(float(x[key+'_balance'])-(ready-demand))<.51
peace=rows('F2_peace_annual_model.csv');assert len(peace)==82
for s in ['S2','S5']:
 last=500000.
 for x in [y for y in peace if y['scenario']==s]:
  assert abs(last-float(x['french_opening_gross']))<=.51
  last=last+.9*int(x['calls_assumption'])-last*(1/6+.025)
  assert abs(last-float(x['french_closing_gross']))<=.51
assert len(rows('F2_replacement_sensitivity.csv'))==27
assert len(rows('F2_annexation_sensitivity.csv'))==18
assert len(rows('F2_hardware_benchmarks.csv'))==13
# Second-round inputs: separate period observations, levy subsets and model arms.
regional=rows('F2_regional_recruitment_evidence.csv');assert len(regional)==6
expected=[(9081,2763,1203),(24186,8138,725),(7921,615,1813),(13933,2386,1843),(313616,65220,87288),(530219,162831,64100)]
for x,(n,d,e) in zip(regional,expected):
 assert (int(x['mobilised_reported']),int(x['draft_dodgers_reported']),int(x['deserters_reported']))==(n,d,e)
 assert abs(float(x['draft_dodgers_per_mobilised'])-d/n)<1e-12
 assert abs(float(x['deserters_per_mobilised'])-e/n)<1e-12
 assert x['status']=='published_period_aggregate_not_independent_or_annual'
batch=rows('F2_levy_batch_evidence.csv');assert len(batch)==1
assert batch[0]['order_date']=='1813-10-09' and batch[0]['observation_deadline']=='1813-12_end'
assert abs(float(batch[0]['deadline_arrival_ratio'])-72265/127433)<1e-12
assert a[10]['partial_levy_calls']=='127433' and a[10]['partial_levy_arrived']=='72265'
assert all(not x['partial_levy_arrived'] for x in a if x['year']!='1813')
bridge=rows('F2_service_definition_bridge.csv');assert len(bridge)==5
for x in bridge:
 if x['total_contract_years']:
  term=int(x['total_contract_years']);k=int(x['deployable_cohorts']);v=float(x['post_training_retention'])
  assert k==term-1
  factor=(1-v**k)/(1-v) # geometric closed form, not generator's explicit sum
 else:factor=1/(1/6+.025)
 gross=2*.9*factor;present=gross*.85*.6
 assert abs(float(x['stock_factor'])-factor)<1e-10
 assert abs(float(x['reliable_present_per1000'])-present)<1e-10
 assert abs(float(x['net_present_per1000'])-(present-4))<1e-10
 assert abs(float(x['calls_per1000_for_zero_balance'])-4/(.9*.85*.6*factor))<1e-10
 assert abs(float(x['rho_for_zero_balance'])-4/(2*.9*.85*factor))<1e-10
assert float(bridge[0]['net_present_per1000'])>0>float(bridge[1]['net_present_per1000'])
food=rows('F2_food_scope_bridge.csv');assert len(food)==2
for x in food:
 total=(int(x['people'])*1.5+int(x['horses'])*10)/1000
 assert abs(float(x['total_metric_t_day'])-total)<1e-10
 assert abs(float(x['annualized_metric_t_if_365days'])-total*365)<1e-10
assert float(food[1]['total_metric_t_day'])-float(food[0]['total_metric_t_day'])==250
# Bounded literal excerpt checks; typography/whitespace normalized only.
quotes=[
 ('O10','downloads/f2_oman_vol3.txt','Of whom 324,996 are actually in Spain, and of these 262,051 are ‘Present under arms’ with the colours.'),
 ('P11','downloads/pages/43dacbcb242e.md','quatre-vingt mille seront mis en activité ; le reste formera la réserve.'),
 ('P10','downloads/pages/df27e5314cf3.md','Le budget de l’armée d’Italie ne doit pas dépasser 30 millions.'),
 ('P10J','downloads/pages/82a063e7e022.md','Guerre et administration de la guerre. . . . 350,000,000'),
 ('R33','downloads/pages/a21d8807b909.md','Au 1 er janvier 1833, l’armée présentait un effectif de 421,494 hommes et 82,057 chevaux.'),
 ('G03','downloads/pages/2ad693d5ac13.md','where over half of his 600,000 troops were non-French.'),
 ('SON04','downloads/pages/977ad00e38d7.md','In all, well over one-half of the Lombard and Venetian troops remained loyal to Austria'),
 ('BR25','downloads/pages/26d8892840a9.md','Au 1er avril 1812, les magasins abritaient 811 000 fusils.'),
 ('G13','downloads/pages/fc4c533d40d3.md','a decree of 9 October 1813 ordered the draft of 127.433 French recruits from the classes of 1808–1814, yet only 72.265 men reached their units'),
 ('M71_quantity','downloads/pages/94b41b5822a4.md','During the year following December 4, 1793, 6,000 private and communal saltpeter works had produced 8,170,000 kgm'),
 ('M71_scope','downloads/pages/94b41b5822a4.md','The 6,000 works mentioned were shops for the leaching of naturally-saltpeterish earths')]
verified=[]
for key,file,quote in quotes:
 text=(ROOT/file).read_text(encoding='utf-8')
 assert norm(quote) in norm(text),(key,'literal_mismatch')
 verified.append(dict(source=key,file=file,quote=quote))
checks=json.loads((P/'F2_model_checks.json').read_text(encoding='utf-8'))
assert checks['vcreveld_source_status'].startswith('author_hypothetical200k_not_observed')
assert checks['food_kg_per_person_day_model_assumption']==1.5
assert checks['vcreveld_haul_capacity_source_tons_unspecified']==18000
report=(P/'F2_french_army_capacity.md').read_text(encoding='utf-8')
assert '人力可行≠财政闭合。' in report
assert 'Q2并未提供可直接替换的实测时滞函数' in report
assert '不是1813全年实到' in report
assert '3.537‰' in report and '−0.463‰' in report
assert '最终地图' in report and '联合乐观' in report
for marker in list('①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯'):assert marker in report
section=report.split('## ⑭ ')[1].split('## ⑮ ')[0]
line_count=sum(1 for line in section.splitlines() if re.match(r'\|18\d\d',line))
assert line_count>=25
for i in range(1,9):assert '|B'+str(i)+' ' in report
source=(P/'SOURCES.md').read_text(encoding='utf-8')
assert len(source)>5000
# Every local material/file path in final sources must exist (brace groups omitted).
paths=re.findall(r'`((?:downloads|nodes)/[^`{}]+)`',source)
for path in paths:assert (ROOT/path).exists(),path
hash_names=['F2_french_army_capacity.md','F2_refinement.md','SOURCES.md','F2_capacity.csv','F2_s6_scenarios.csv','F2_joint_budget_manpower.csv','F2_regional_recruitment_evidence.csv','F2_levy_batch_evidence.csv','F2_service_definition_bridge.csv','F2_food_scope_bridge.csv','F2_round2_checks.json','F2_model.py','F2_build_capacity.py','F2_integration_model.py','F2_round2_interfaces.py','validate_f2.py','notes_round2_sources.md','F2_round2_changes.md','VALIDATION.md']
hashes={name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in hash_names}
result={'status':'all_checks_passed','checked_file_sha256':hashes,'annual_evidence_rows':len(a),'narrative_timeline_rows':line_count,'S6_region_rows':len(r),'maturation_rows':len(traj),'service_rows':len(terms),'joint_budget_rows':len(joint),'peace_model_rows':len(peace),'round2_regional_rows':len(regional),'round2_levy_batch_rows':len(batch),'round2_service_bridge_rows':len(bridge),'round2_food_bridge_rows':len(food),'literal_checks':verified,'warning':'Passes establish arithmetic/structure/literal presence only, not causal validity or archival authentication.'}
(P/'F2_validation_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='literal_checks'},ensure_ascii=False,indent=2))
