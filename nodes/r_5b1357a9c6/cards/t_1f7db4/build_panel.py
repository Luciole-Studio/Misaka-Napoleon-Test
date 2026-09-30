#!/usr/bin/env python3
"""Q2: source transcription, not an annual balanced panel or downloaded microdata.
Run from any working directory. Python standard library only. All source IDs in SOURCES.md.
The numerical literals below are transcribed published figures; no annual interpolation.
"""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parent
FIELDS = ['obs_id','geo','geo_level','integration_class','period_start','period_end','period_label','metric','value','unit','denominator','value_status','source_id','locator','comparability','notes']
rows=[]
def add(geo,level,cl,start,end,period,metric,value,unit,denom,status,source,loc,comp,notes=''):
    rows.append(dict(zip(FIELDS,[f'Q{len(rows)+1:03}',geo,level,cl,start,end,period,metric,value,unit,denom,status,source,loc,comp,notes])))
# R03, Table 3. Aggregate French Empire includes the Rhineland and Alsace.
for geo,cl,vals in [('Rhineland4','annexed_inner',[(9081,2763,6,1203),(24186,8138,8,725)]),('Alsace2','old_france',[(7921,615,13,1813),(13933,2386,17,1843)]),('French_Empire_excl4Italy','overlapping_aggregate',[(313616,65220,11,87288),(530219,162831,20,64100)])]:
    for (st,en,label),v in zip([(1800,1805,'AnIX-XIII 1800/1-1804/5'),(1806,1810,'1806-1810')],vals):
        for metric,val,unit,den in zip(['mobilised','draft_dodgers_pre_presentation','dodgers_arrested_percent','deserters_after_joining'],v,['persons','persons','percent','persons'],['','author mobilised','draft dodgers','author mobilised']):
            add(geo,'region_group',cl,st,en,label,metric,val,unit,den,'reported_count_or_rate','R03','p179 Table3; PDF193','rowe_two_period','Not RP23 definition; no annualization. Empire aggregate not independent.')
for metric,val in [('tax_paid_reported',11138406),('old_regime_tax_estimate',6250000)]:
    add('Roer','department','annexed_inner',1803,1803,'1803 memorandum; old-regime comparator date unspecified',metric,val,'francs','','reported_memorandum' if 'paid' in metric else 'historical_estimate','R03','pp201-202; PDF215-216','roer_fiscal','Same-tax/base equivalence not demonstrated; no assessed tax or net expenditure.')
for geo,n in [('French_Empire',15500),('Rhineland4',527)]:
    add(geo,'aggregate','overlapping_aggregate' if geo=='French_Empire' else 'annexed_inner',1809,1809,'1809', 'gendarmes',n,'persons','','reported_count','R03','p181; PDF195','gendarmes','Not all occupation/security forces.')
# F90 population and cumulative cohorts: preserve contradictions, do not repair.
for geo,val in [('Doire',224127),('Marengo',332554),('Po',395193),('Sesia',204445),('Stura',395074),('Tanaro',310459)]:
    add(geo,'department','annexed_inner',1805,1806,'AnXIV population table', 'population',val,'persons','','reported_count','F90','p213','piedmont_population','Tanaro later abolished; cannot assume constant 1800-1810 boundary.')
add('Piedmont','region','annexed_inner',1805,1806,'AnXIV', 'population_total_prose',1813473,'persons','','reported_count_conflict','F90','p213','piedmont_population','Six rows sum 1861852, not this number.')
for metric,val in [('registered_11_cohorts',166556),('reported_average_cohort',15354),('exempted_all',53740),('incorporated_conscripts',35281),('volunteers',2682),('velites',280),('all_joined_prose_p214',38242),('all_joined_prose_p219',38243),('mixed_evaders_all',9272),('condemned_refractaires',6938),('refractaires_returned',211),('refractaires_arrested',942)]:
    add('Piedmont','region','annexed_inner',1800,1810,'11 cohorts through1810; not exactly calendar-year flows',metric,val,'persons','','reported_count_conflict' if metric in ['registered_11_cohorts','reported_average_cohort','all_joined_prose_p214','mixed_evaders_all'] else 'reported_count','F90','pp213-214,219','piedmont_cohorts','Includes distinct registration/medical/induction categories; do not add all metrics.')
for st,en,label,reg,ex,mix in [(1800,1805,'AnIX-XIII',69319,16007,6272),(1806,1810,'1806-1810',88242,37733,2929)]:
    for met,n in [('registered',reg),('exempted',ex),('mixed_evaders',mix)]:
        add('Piedmont','region','annexed_inner',st,en,label,met,n,'persons','registered' if met=='exempted' else '','reported_count','F90','p214','piedmont_cohorts','Period mixed-evader sum differs from reported all-period total by71.')
add('Piedmont','region','annexed_inner',1802,1803,'AnXI; statement cut-off unspecified','quota',4000,'persons','','reported_plan','F90','p218 n27','piedmont_early','Author quotes Napoleon; not a full-year finalized levy.')
add('Piedmont','region','annexed_inner',1802,1803,'AnXI; statement cut-off unspecified','departed_rhetorical_ceiling',500,'persons','quota4000','rhetorical_ceiling_not_observation','F90','p218 n27','piedmont_early','je ne sache pas quil y en ait 500 de partis; not exactly500 arrivals.')
add('Piedmont','region','annexed_inner',1803,1803,'Thermidor AnXI','gendarmes',668,'persons','','derived_sum_406plus262','F90','p219 n34','gendarmes','Foot406; mounted262; not total occupation troops.')
for metric,val in [('population_used',3028705),('called_up_cumulative',225147),('incorporated_cumulative',216111),('mixed_evaders_cumulative',89267),('reincorporated',24560)]:
    add('Belgium9','region','annexed_inner',1798,1813,'AnVII to1813-11-15',metric,val,'persons','','reported_count','F90','p221 n41','belgium_cumulative','Darquenne via Stevens via Frasca; unique-person deduplication unknown.')
add('Belgium9','region','annexed_inner',1800,1810,'AnIX-1810','exemption_percent',17.9,'percent','called_up','reported_rate','F90','p221','belgium_exemption','Not same denominator as RP23 cohort exemption rate.')
# W91: pooled rates and administrative experience. These are not annual points.
for st,en,label,r,d in [(1798,1805,'through1804-05',10.7,49.3),(1805,1809,'1805-1809',42.4,14.8)]:
    for met,val in [('refractaires_percent',r),('deserters_percent',d)]:
        add('Belgium9','region','annexed_inner',st,en,label,met,val,'percent','stages not fully specified','reported_rate','W91','p160; PDF171','woolf_belgium','Cannot sum rates or concatenate with RP23.')
for st,en,label,val,status in [(1800,1805,'1800-1805',10,'approximate_rate'),(1806,1810,'1806-1810',2,'strict_upper_bound')]:
    add('Rhineland4','region','annexed_inner',st,en,label,'desertion_percent_woolf',val,'percent','author aggregate','reported_'+status,'W91','p161; PDF172','woolf_rhine','Conflicts with R03 13%/3%; definitions/sample differ or unresolved. Do not average.')
for year,val in [(1800,2.4),(1805,6.5),(1812,10)]:
    add('Prefects_all','person_pool','overlapping_aggregate',year,year,str(year),'mean_prior_admin_experience',val,'years','','reported_mean','W91','p76; PDF87','prefects','Not department staffing density.')
add('Empire92depts','department_group','mixed',1810,1812,'1810-1812','mobile_column_arrests',63000,'persons','','reported_count','W91','p162; PDF173','enforcement','Arrests are policing output, not consent or conscription success.')
# M25: all figures are projected receipts; exact observed collection not supplied.
for geo,cl,val in [('Belgium','annexed_inner',83),('Holland','annexed_outer',66.5),('Hanseatic','annexed_outer',38.791),('Rhineland','annexed_inner',37.5),('Piedmont','annexed_inner',33),('Tuscany','annexed_outer',22.5),('Liguria','annexed_inner',16),('Rome','annexed_outer',16.5)]:
    add(geo,'region',cl,1812,1812,'1812 budget expectations','projected_revenue_regional',val,'million_francs','','budget_projection','M25','p321; PDF341','marion1812','Regional line gross/net not explicit; sum closer to gross. Not realized receipts.')
for metric,val in [('projected_gross_all',342.260044),('projected_net_all',226.389345)]:
    add('Annexed_all','aggregate','mixed',1812,1812,'1812 budget expectations',metric,val,'million_francs','','budget_projection','M25','p321; PDF341','marion1812','Do not treat net as after every strategic military cost.')
add('Recent_annexed','aggregate','annexed_outer',1811,1811,'Gaudin1811-04-30','projected_revenue_ceiling',105,'million_francs','','budget_upper_projection','M25','p321; PDF341','marion1811','At most105; regional components104.5 rounded.')
for metric,val in [('soldier_cost_maintenance',600),('soldier_cost_including_arms_horses',700),('naples_soldier_cost_reported',900)]:
    year=1806 if metric=='naples_soldier_cost_reported' else ''
    period='1806-11-12 report' if year else 'Napoleonic period; exact accounting year not fixed here; Mollien retrospective memoir'
    add('French_army','aggregate','mixed',year,year,period,metric,val,'francs_per_soldier_year','','reported_cost_estimate','M25','pp322-323; PDF342-343','military_cost','600/700/900 not same accounting perimeter;1000 contested estimate also discussed; do not assign all costs to1806.')
# G13: different counting windows remain different.
for geo,cl,st,en,met,n,status,loc in [('Italy_Kingdom','satellite',1807,1810,'draft_evaders',22227,'reported_count','p108'),('Italy_Kingdom','satellite',1806,1810,'army_deserters',17750,'contemporary_estimate','p109'),('Marches3','satellite_new',1808,1808,'initial_quota',1020,'reported_plan','p108'),('French_recruit_call','mixed',1813,1813,'october_call_quota',127433,'reported_plan','p118'),('French_recruit_call','mixed',1813,1813,'arrived_by_dec31',72265,'reported_count','p118')]:
    add(geo,'region_or_event',cl,st,en,'October09-December31' if geo=='French_recruit_call' else f'{st}-{en}',met,n,'persons','',''+status,'G13',loc,'grab_events','Author transcribes archival/secondary sources; not direct archive reading.')
# RP23 appendix descriptive quantities: never treated as local observations.
for metric,n,unit,den in [('conscription_rate_mean',29.59,'percent','cohort'),('draft_dodging_mean',14.95,'percent','effectively drafted'),('draft_dodging_p25',3.556,'percent','effectively drafted'),('draft_dodging_p50',10.92,'percent','effectively drafted'),('draft_dodging_p75',21.69,'percent','effectively drafted'),('exemption_mean',54.21,'percent','cohort'),('dodging_observations',554,'records',''),('conscription_observations',555,'records','')]:
    add('RP23_sample','sample_distribution','mixed',1806,1810,'1806-1810',metric,n,unit,den,'published_summary_not_microdata','RP23A','p4 Table1','rp23_summary','No population weighting assumed; cannot multiply means for aggregate soldiers.')
for metric,n,source,loc in [('draft_dodgers_observed',10499,'RP23','p1092'),('additional_dodgers_main',3256,'RP23','p1092'),('additional_dodgers_appendix',2812,'RP23A','p61'),('additional_sent_appendix',3256,'RP23A','p61')]:
    add('French_controlled','aggregate','mixed',1810,1810,'1810',metric,n,'persons','','published_observation' if 'observed' in metric else 'published_counterfactual_conflict',source,loc,'rp23_back_envelope','Text27% corresponds to2812, not3256; S/C semantics also unresolved.')
# Explicit coverage gaps: one period record, not fourteen fake missing observations.
for geo,cl in [('OldFrance','old_france'),('Belgium','annexed_inner'),('Rhineland','annexed_inner'),('Piedmont','annexed_inner'),('Liguria','annexed_inner'),('Tuscany','annexed_outer'),('Rome','annexed_outer'),('Holland','annexed_outer'),('Hanseatic','annexed_outer'),('Illyria','special_provinces'),('Catalonia','military_annexation'),('ItalyKingdom','satellite'),('Naples','satellite')]:
    add(geo,'coverage',''+cl,1800,1813,'coverage_audit_1800-1813','comparable_annual_collected_to_assessed_tax','','ratio','','not_obtained','AUDIT','notes_method.md','missing','Absence in this assembled evidence, not proof records do not exist. Roer one tax-paid point does not close ratio.')
with (ROOT/'Q2_panel.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
# Only selected, actually-read published estimates; no new regression.
ests=[
 ['RP23','Table1col3','log_ruggedness','draft_dodging_pp',3.86229,1.06111,1.35414,534,'log unit','year+military division','annexed partly included'],
 ['RP23','Table1col5','log_ruggedness','draft_dodging_pp',6.20847,1.66293,2.20756,292,'log unit','year+military division','Belgian German Italian depts removed by controls'],
 ['RP23','Table1col3','distance_paris','draft_dodging_pp',3.31115,0.88206,1.43014,534,'100km','year+military division','association not distance threshold'],
 ['RP23','Table1col5','distance_paris','draft_dodging_pp',3.05406,1.21080,1.90045,292,'100km','year+military division','restricted sample'],
 ['RP23','Table1col3','border','draft_dodging_pp',2.66730,1.30976,1.74814,534,'binary','year+military division','spatial SE includes zero'],
 ['RP23','Table1col5','border','draft_dodging_pp',4.66339,2.52049,3.63635,292,'binary','year+military division','spatial SE includes zero'],
 ['RP23','Table4col4','group45_x1810','draft_dodging_pp',-4.99631,1.73068,'',554,'relative to1809','year+department','reported spatial SE per text; pretrend not randomized'],
 ['RP23','Table4col8','group45_x1810','population_conscript_share',-0.00024,0.00006,'',555,'share','year+department','rounded coefficient; appendix uses-0.0002387']
]
with (ROOT/'Q2_published_estimates.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f);w.writerow(['source_id','table_column','regressor','outcome','coefficient','se_parentheses','se_conley_brackets','N','regressor_unit','fixed_effects','notes']);w.writerows(ests)
print(f'Wrote {len(rows)} source/gap rows, {len(ests)} published-estimate rows. No new regression.')
