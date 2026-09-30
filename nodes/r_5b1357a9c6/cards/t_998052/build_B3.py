#!/usr/bin/env python3
"""B3: published observations + explicitly labelled scenario accounting. No fit or interpolation."""
from pathlib import Path
import csv,json,hashlib,math
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[3]
rows=[]
def add(section,year,metric,value,unit,source,locator,note='',scenario='S0',high=None):
    rows.append(dict(section=section,scenario=scenario,year=year,metric=metric,value_low=value,value_high=value if high is None else high,unit=unit,source=source,locator=locator,note=note))
old=ROOT/'nodes/r_b55f2c1cf5/cards/t_104134/naval/UK_1803_1805.csv'
for r in csv.DictReader(old.open()):
    for key in ['sea_commission','sea_ordinary','sea_total','harbour_commission','harbour_ordinary','building_or_ordered','grand_total','sea_commission_tons']:
        add('observation',r['year'],r['ship_class']+'_'+key,int(r[key]),'James_tons_burthen' if 'tons' in key else 'ships','J3',r['locator'],'Jan1; modern old-card extraction; image re-read in B3; sea ordinary may require repair')
# Jan 1 Line and Cruisers rows, directly read in Benyon modern transcription.
data={1806:[104,16,120,17,27,26,190,184976,27607,212583,551,39,590,3,0],1807:[103,20,123,20,27,36,206,180671,36459,217130,606,51,657,0,2],1808:[113,13,126,19,44,48,237,197350,25089,222439,618,55,673,2,5]}
keys=['sea_commission','sea_ordinary','sea_total','harbour_commission','harbour_ordinary','building_or_ordered','grand_total','sea_commission_tons','sea_ordinary_tons','sea_total_tons']
for y,v in data.items():
    assert v[0]+v[1]==v[2] and v[2]+v[3]+v[4]+v[5]==v[6]
    for key,x in zip(keys,v[:10]):add('observation',y,'line_'+key,x,'James_tons_burthen' if 'tons' in key else 'ships',f'J{y-1792}',f'Abstract{y-1792}:Line','Jan1; modern HTML transcription; not independently image-verified')
    for key,x in zip(['sea_commission','sea_ordinary','sea_total'],v[10:13]):add('observation',y,'all_cruisers_including_line_'+key,x,'ships',f'J{y-1792}',f'Abstract{y-1792}:Cruisers','Includes Line; do not add')
    add('observation',y-1,'line_built',v[13]+v[14],'ships',f'J{y-1792}',f'Abstract{y-1792}:Built','Built kings + merchants; previous year, not net growth')
for y,x in [(1802,1),(1803,5),(1804,3)]:add('observation',y,'line_built',x,'ships','J3',f'Abstract{y-1791}:Line Built','Image read; sum kings + merchants; previous year')
# A modern published series; grants are not outturn expenditure.
vals=[(1803,100000,10211378),(1804,100000,12350606),(1805,120000,15035630),(1806,120000,18864341),(1807,130000,17400337),(1808,130000,18087547),(1809,130000,19578467),(1810,145000,18975120),(1811,145000,19822000),(1812,145000,19305759),(1813,140000,20096709),(1814,117400,19312070),(1815,90000,19032700)]
for y,m,b in vals:
    add('observation',y,'naval_supplies_granted',b,'nominal_GBP','FB','p44:Expenditure','Total includes non-fleet transport/prisoner charges; fiscal periods not pure calendar year')
    add('observation' if y!=1814 else 'source_conflict',y,'voted_seamen_marines_reported_FB',m,'persons','FB','p44:Expenditure','Not actual borne; some years changed within 13 lunar months; 1814 conflicts with James prose')
# Detail source has temporal subdivisions; preserve without making annual averages.
parts=[(1803,2,38000,12000),(1803,4,45600,14400),(1803,7,77600,22400),(1804,13,78000,22000),(1805,13,90000,30000),(1806,13,91000,29000),(1807,1,91000,29000),(1807,12,98600,31400),(1808,13,98600,31400),(1809,13,98600,31400),(1810,13,113600,31400),(1811,13,113600,31400),(1812,13,113600,31400),(1813,13,108600,31400),(1814,7,86000,31400),(1814,6,74000,16000),(1815,3,55000,15000),(1815,10,70000,20000),(1816,13,24000,9000),(1817,13,13000,6000),(1818,13,14000,6000),(1819,13,14000,6000),(1820,13,15000,8000)]
for y,months,s,m in parts:
    note=f'{months} lunar months in the specified vote; no dates invented; not actual borne'
    typ='source_conflict' if y==1814 and months==7 else 'observation'
    if typ=='source_conflict':note+='; Appendix9 says86000+31400; James text says140000 total; do not reconcile silently'
    for metric,v in [('voted_seamen',s),('voted_marines',m),('voted_total',s+m)]:add(typ,y,metric,v,'persons','JB',f'year{y}:months{months}',note)
add('source_conflict',1814,'voted_total_James_prose_7months',140000,'persons','J1814text','volVI1902 p116; edition title and text actually read','Conflicts with Appendix9; not independent source')
# Post-1820 Budget table includes boys explicitly and borne separately.
post=[(1821,14000,8000,24937,6391902),(1822,13000,8000,23806,6480325),(1823,16000,8700,26314,5442540),(1824,20000,9000,30502,5762893),(1825,20000,9000,31456,5983126),(1826,21000,9000,32519,None),(1827,21000,9000,33106,6125850),(1828,21000,9000,31818,6395965),(1829,21000,9000,32458,5878794),(1830,20000,9000,31160,5594955)]
for y,s,m,a,b in post:
    for metric,v,u in [('voted_seamen_boys',s,'persons'),('voted_marines',m,'persons'),('voted_total',s+m,'persons'),('actually_borne',a,'persons'),('naval_supplies_granted_Benyon',b,'nominal_GBP')]:add('source_corrupt' if v is None else 'observation',y,metric,'' if v is None else v,u,'JB',f'year{y}:post1820_table','1826 supplies raw string=6,7.35,004; not silently repaired' if v is None else 'Modern Benyon compilation; upstream official tables not fully established; not all attributable to James; no independent muster check')
# Read Hansard numbers retained separately from compiled website series.
for y,m,mar,loc in [(1817,19000,6000,'1817-02-17 vol35 cc408-409; six lunar months only'),(1820,23000,8000,'1820-05-17 vol1 cc459-460;13 lunar months'),(1826,30000,9000,'1826-02-21 vol14 cc678-689'),(1830,29000,9000,'1830-03-01 vol22 cc1121-1143; planned annual average')]:
    add('observation',y,'Hansard_voted_total',m,'persons','HPOST',loc,'Includes marines; not borne')
    add('observation',y,'Hansard_voted_marines',mar,'persons','HPOST',loc,'Included in total not additional')
for y,b,a in [(1817,5985415,6473062),(1818,6547810,6521714),(1819,6527781,6393552),(1820,6691345,6387799),(1821,6382786,None)]:
    add('observation',y,'Hume_gross_navy_estimate',b,'nominal_GBP','H21','No28;1821-06-27','Quoted Annual Estimates; not including old-store deductions')
    if a is not None:add('observation',y,'Hume_reported_actual_navy_expenditure',a,'nominal_GBP','H21','No28;1821-06-27','Quoted Annual Finance Accounts; timing not harmonized;1820 No5 differs by400')
add('observation',1826,'Hansard_aggregate_estimate',6135004,'nominal_GBP','HPOST','1826-02-21 vol14 cc678-689','Hume amendment; not outturn; network table string corrupt')
add('observation',1830,'Hansard_aggregate_estimate',5595000,'nominal_GBP','HPOST','1830-03-01 vol22 cc1121-1143','Oral rounded total; not exact grant or outturn')
for y,b in [(1815,4499193),(1816,3023270),(1817,2034952),(1818,2099990),(1819,1988430),(1820,2065533),(1821,1990880)]:add('observation',y,'Hume_voted_build_repair_wear_total',b,'nominal_GBP','H21','No32;1821-06-27','Includes wear/repairs/stores; not new construction only;1820 wear differs3 from H1820')
# Force packages (assumed allocation of a real attainable aggregate envelope).
packages={'P0':(15,25,60,7000),'A_low':(45,50,60,10000),'A_high':(70,75,90,12000),'W_low':(100,100,200,15000),'W_high':(115,115,230,15000),'E':(125,125,260,16000)}
calc=[]
for p,(L,R,C,O) in packages.items():
    M=650*L+280*R+110*C+O
    low=4_000_000+85*M; high=6_000_000+105*M
    calc.append(dict(package=p,line=L,frigates=R,small_cruisers=C,other_personnel=O,total_personnel=M,cost_low=low,cost_high=high))
    for k,v in [('commissioned_line',L),('commissioned_frigates',R),('commissioned_small_cruisers',C),('other_personnel',O),('total_personnel',M)]:add('model', '1815-1830',k,v,'persons' if 'personnel' in k else 'ships','B3_assumption','model_assumptions.md:personnel','Not a historical establishment; correlated package; all onboard marines included',p)
    add('model','1815-1830','annual_planning_cost',low,'GBP_at_1812_cost_level','B3_assumption','K+[85,105]*M','K=[4m,6m]; one-anchor compatibility not parameter identification',p,high)
thresholds=[]
for f in [40,60,80,100]:
    low=math.ceil((1.05*f+15)/.85);high=math.ceil((1.20*f+25)/.75)
    ilow=math.ceil(1.05*f+15);ihigh=math.ceil(1.20*f+25)
    thresholds.append({'french_deployable_pressure':f,'UK_sea_hulls_low':low,'UK_sea_hulls_high':high,'UK_task_lines_low':ilow,'UK_task_lines_high':ihigh})
    add('model','1815-1830','required_UK_sea_line_hulls',low,'ships','B3_assumption','ceil((rF+g)/a)','F is hostile deployable pressure not ledger hulls; necessary not sufficient; r=[1.05,1.20],g=[15,25],a=[.75,.85]',f'F_pressure_{f}',high)
    add('model','1815-1830','required_UK_task_lines',ilow,'ships','B3_assumption','ceil(rF+g)','I must at least cover this need; peaceful French training not automatically hostile pressure',f'F_pressure_{f}',ihigh)
# Optional subagent transcription, once present; a schema bridge documented in source evidence.
annual=BASE/'sources/annual/annual_1809_1815.csv'
annual_complete_rows=0
if annual.exists():
    for r in csv.DictReader(annual.open()):
        y=int(r['year'])
        if all(r.get(k,'') not in ('','NA') for k in keys):
            annual_complete_rows+=1
            assert int(r['sea_commission'])+int(r['sea_ordinary'])==int(r['sea_total'])
            assert sum(int(r[k]) for k in ['sea_total','harbour_commission','harbour_ordinary','building_or_ordered'])==int(r['grand_total'])
        for key in keys:
            if r.get(key,'') not in ('','NA'):
                add('observation',y,'line_'+key,int(r[key]),'James_tons_burthen' if 'tons' in key else 'ships',f'J{y-1792}',f'Abstract{y-1792}:Line','Modern HTML transcription; checks and disputes in sources/annual/evidence.md')
        for key in ['sea_commission','sea_ordinary','sea_total']:
            v=r.get('cruisers_'+key,'')
            if v not in ('','NA'):add('observation',y,'all_cruisers_including_line_'+key,int(v),'ships',f'J{y-1792}',f'Abstract{y-1792}:Cruisers','Includes Line')
        built=r.get('built_total',r.get('built_previous_year',''))
        if built not in ('','NA'):add('observation',y-1,'line_built',int(built),'ships',f'J{y-1792}',f'Abstract{y-1792}:Built','Previous calendar year; gross flow not stock change')
# Paired planning endpoints, not statistically estimated fleet curves.
# Annual gross commissioning is only a feasibility accounting assumption.
ys=[1815,1820,1825,1830]
Hs={'low':[120,125,130,130],'high':[135,145,155,155]}
A12={'W':{'low':[105,110,115,115],'high':[125,135,145,145]},'P':{'low':[90,95,100,100],'high':[120,130,140,140]}}
Is={'W':{'low':[100,100,105,105],'high':[115,120,125,125]},'P':{'low':[45,45,45,45],'high':[70,70,70,70]}}
responses=[]
for scenario in ['W','P']:
    for b in ['low','high']:
        for j,y in enumerate(ys):
            h=Hs[b][j];am=A12[scenario][b][j];im=Is[scenario][b][j]
            assert im<=am<=h
            built='' if j==0 else (30 if b=='low' else 40)
            exit='' if j==0 else Hs[b][j-1]+built-h
            # 12-month peak concentration is not the all-stations package.
            mobM=650*am+280*60+110*90+15000
            if scenario=='P':
                rfrig,small,other=(50,60,10000) if b=='low' else (75,90,12000)
            else:
                rfrig,small,other=(115,230,15000) if b=='high' and j==0 else (100,200,15000)
            standingM=650*im+280*rfrig+110*small+other
            rr=dict(record_type='model_not_observation',scenario=scenario,bound=b,year=y,reference_time='1815_post_truce_choice_not_same_date_as_F3' if scenario=='P' and y==1815 else 'planning_year_point',sea_line_hulls=h,mobilizable_within_12months=am,commissioned_line=im,assumed_built_previous_5years=built,implied_exit_previous_5years=exit,mobilized_concentration_personnel=mobM,standing_frigates=rfrig,standing_small_cruisers=small,standing_other_personnel=other,standing_total_personnel=standingM,standing_cost_low=4000000+85*standingM,standing_cost_high=6000000+105*standingM,note='Paired envelope; W beyond115 line ships reduces cruiser demands versus full emergencyE; 12m mobilization shifts crews/global commitments; no measured exit/muster rate; onboard marines included')
            responses.append(rr)
            for k,v in [('sea_line_hulls',h),('mobilizable_line_within_12months',am),('commissioned_line',im),('built_previous_5years',built),('implied_exit_previous_5years',exit)]:
                if v!='':add('model',y,k,v,'ships','B3_assumption','model_assumptions.md:paired_endpoints','Scenario endpoint not observation; simultaneous global maxima forbidden',scenario+'_'+b)
with (BASE/'B3_response.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(responses[0]));w.writeheader();w.writerows(responses)
# Historical wide table generated only from observation rows; no model backfill.
byyear={y:{} for y in range(1803,1816)}
for r in rows:
    if r['section']=='observation' and str(r['year']).isdigit() and int(r['year']) in byyear:
        byyear[int(r['year'])][r['metric']]=r['value_low']
head='|年初|海勤现役I|海勤ordinary|海勤H|港勤现役|港勤ordinary|在建/订购|账籍总数|Cruisers海勤合计|上年Built|\n|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n'
for y,d in byyear.items():
    values=[d['line_'+k] for k in ['sea_commission','sea_ordinary','sea_total','harbour_commission','harbour_ordinary','building_or_ordered','grand_total']]+[d['all_cruisers_including_line_sea_total']]
    prev=[r['value_low'] for r in rows if r['section']=='observation' and str(r['year'])==str(y-1) and r['metric']=='line_built']
    values.append(prev[0] if prev else '')
    head+='|'+str(y)+'|'+'|'.join(map(str,values))+'|\n'
(BASE/'table_historical.md').write_text(head)
with (BASE/'B3_capacity.csv').open('w',newline='') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
res={'method':'deterministic accounting, no fitted parameters','rows':len(rows),'packages':calc,'thresholds':thresholds,'annual_source_loaded':annual_complete_rows==7,'annual_complete_rows':annual_complete_rows,'paired_response_rows':len(responses),'skill_audit':'econ-integrity data_provenance audit passed metadata presence; not source validation'}
(BASE/'B3_calculations.json').write_text(json.dumps(res,ensure_ascii=False,indent=2))
print(json.dumps(res,ensure_ascii=False,indent=2))
