"""B5 descriptive tables + explicit scenario arithmetic, NOT causal estimation.
Reproduce: python3 nodes/r_5b1357a9c6/cards/t_87ba37/build_B5_tables.py
BoE cached cells read from selected snapshot. Original errors retained in raw fields.
"""
from pathlib import Path
import csv,json,math
import openpyxl
P=Path(__file__).resolve().parent
w=openpyxl.load_workbook(P/'B5_boe_selected.xlsx',read_only=True,data_only=True)
def save(name,rows):
 with (P/name).open('w') as f:
  x=csv.DictWriter(f,fieldnames=list(rows[0]));x.writeheader();x.writerows(rows)
def rowsbyyear(s):
 return {int(r[0]):r for r in w[s].iter_rows(values_only=True) if r and isinstance(r[0],(int,float)) and 1700<=r[0]<=1900}
s=rowsbyyear('A40. Trade by region 1710-1822');annual=[]
for y in range(1803,1816):
 r=s.get(y)
 if not r or r[2] is None:
  annual.append(dict(year=y,north_europe='',south_europe_turkey_egypt='',asia='',latin_foreign_west_indies='',usa_raw='',usa_corrected='',canada='',british_west_indies='',africa='',total_raw='',total_corrected='',unit='GBP_m_official_fixed_old_prices_incl_reexports',source='A40!row112',note='1813_missing_no_imputation'));continue
 raw=float(r[20]);usa=float(r[14]);cor=usa-10 if y==1811 else usa
 annual.append(dict(year=y,north_europe=r[2],south_europe_turkey_egypt=r[4],asia=r[8],latin_foreign_west_indies=r[16],usa_raw=usa,usa_corrected=cor,canada=r[12],british_west_indies=r[18],africa=r[6],total_raw=raw,total_corrected=raw-10 if y==1811 else raw,unit='GBP_m_official_fixed_old_prices_incl_reexports',source=f'A40!row{y-1701}',note='1811_USA_minus10_based_on_Marshall1833_p74_pdf88' if y==1811 else 'raw_cached_value'))
save('B5_annual_exports_1803_1815.csv',annual)
a=rowsbyyear('A4. Ind Production 1270-1870');b=rowsbyyear('A47. Wages and prices');c=rowsbyyear('A1. Headline series');iv=[]
for y in range(1803,1849):
 r=a[y];v=b[y];row={'year':y}
 for k,j in [('industry',13),('coal',3),('iron',2),('textiles',4)]:row[k+'_1803_100']=100*r[j]/a[1803][j]
 row.update(weekly_earnings_GBP=v[1],cpi_raw=v[3],cpi_1803_100=100*v[3]/b[1803][3],real_full_employment_earnings_1803_100=100*(v[1]/v[3])/(b[1803][1]/b[1803][3]),population_GB_NI_thousands=c[y][24],source=f'A4!row{y-1261};A47!row{y-1202};A1!year{y}')
 iv.append(row)
save('B5_industry_wages_1803_1848.csv',iv)
s=w['A41. Trade by region 1784+'];bench=[]
for i in range(10,15):
 row={'period':s[f'A{i}'].value,'europe':s[f'T{i}'].value/1000,'near_east':s[f'C{i+11}'].value/1000,'africa':s[f'G{i+11}'].value/1000,'asia':s[f'K{i+11}'].value/1000,'australasia':s[f'O{i+11}'].value/1000,'canada':s[f'C{i+22}'].value/1000,'usa':s[f'G{i+22}'].value/1000,'west_indies':s[f'K{i+22}'].value/1000,'latin_america':s[f'O{i+22}'].value/1000,'total_excl_ireland':s[f'T{i+22}'].value/1000,'reexports_europe':s[f'U{i}'].value/1000,'reexports_total':s[f'U{i+22}'].value/1000,'unit':'GBP_m_current_computed_declared_domestic_unless_reexports','source':f'A41!rows{i},{i+11},{i+22};Davis1979_via_BoE'}
 row['domestic_sum_error']=sum(row[k] for k in ['europe','near_east','africa','asia','australasia','canada','usa','west_indies','latin_america'])-row['total_excl_ireland'];bench.append(row)
save('B5_market_benchmarks.csv',bench)
# Parameters registered here: author-selected stress envelopes, not estimated probabilities.
params={
'early_benchmark_1804_6':{
 'S2':{'europe_retained':[.35,.60],'latin_extra':[.4,1.4],'asia_extra':[0,.5],'usa_extra':[.8,2.5],'other_extra':[.3,1.0],'realization':[.75,.90]},
 'S3':{'europe_retained':[.05,.20],'latin_extra':[.2,1.0],'asia_extra':[0,.4],'usa_extra':[0,1.5],'other_extra':[.2,.8],'realization':[.55,.80]},
 'S5':{'europe_retained':[.70,1.0],'latin_extra':[.7,1.5],'asia_extra':[.2,.8],'usa_extra':[1,3],'other_extra':[.3,1],'realization':[.90,1.0]}},
'late_benchmark_1844_6':{
 'S2':{'europe_retained':[.40,.70],'latin_extra_ratio':[.1,.4],'asia_extra_ratio':[.1,.4],'usa_extra_ratio':[0,.3],'other_extra_ratio':[.03,.15],'realization':[.85,.95]},
 'S3':{'europe_retained':[.05,.20],'latin_extra_ratio':[.1,.35],'asia_extra_ratio':[.1,.5],'usa_extra_ratio':[0,.25],'other_extra_ratio':[.05,.2],'realization':[.80,.90]},
 'S5':{'europe_retained':[.75,1.0],'latin_extra_ratio':[0,.1],'asia_extra_ratio':[0,.1],'usa_extra_ratio':[0,.1],'other_extra_ratio':[0,.1],'realization':[.95,1.0]}}}
(P/'B5_scenario_parameters.json').write_text(json.dumps(params,indent=2))
mr=[]
for horizon,sp in params.items():
 base=bench[0] if horizon.startswith('early') else bench[-1]
 for scen,p in sp.items():
  for edge,j in [('low',0),('high',1)]:
   loss=base['europe']*(1-p['europe_retained'][j]);extras={}
   for market,key in [('latin','latin_america'),('asia','asia'),('usa','usa'),('other','other')]:
    if horizon.startswith('early'):extras[market]=p[market+'_extra'][j]
    else:
     amount=base[key] if key!='other' else base['total_excl_ireland']-base['europe']-base['latin_america']-base['asia']-base['usa']
     extras[market]=p[market+'_extra_ratio'][j]*amount
   gain=sum(extras.values())*p['realization'][j]
   mr.append(dict(horizon=horizon,scenario=scen,edge=edge,base_europe=base['europe'],base_total=base['total_excl_ireland'],europe_retention=p['europe_retained'][j],europe_loss=loss,latin_extra_shipments=extras['latin'],asia_extra_shipments=extras['asia'],usa_extra_shipments=extras['usa'],other_extra_shipments=extras['other'],realization=p['realization'][j],effective_extra=gain,replacement_of_loss=gain/loss if loss>0 else '',total_after=base['total_excl_ireland']-loss+gain,relative_total=(base['total_excl_ireland']-loss+gain)/base['total_excl_ireland'],status='ASSUMPTION_STRESS_NOT_OBSERVATION'))
save('B5_market_scenarios.csv',mr)
growth={'S1':([.98,1.05],[0,.003]),'S2':([.9,1.0],[-.004,0]),'S3':([.78,.9],[-.011,-.004]),'S5':([.94,1.02],[-.002,.002]),'S6_hard_durable':([.75,.88],[-.012,-.004])}
gp=[]
for scen,(initial,delta) in growth.items():
 for year in [1815,1820,1830,1835,1840,1848]:
  for j,edge in enumerate(['low','high']):
   rel=initial[j]*math.exp(delta[j]*(year-1815))
   gp.append(dict(scenario=scen,year=year,edge=edge,relative_1815=initial[j],annual_log_growth_wedge=delta[j],relative_S0=rel,industry_1803_100=(a[year][13]/a[1803][13])*100*rel,status='SUBJECTIVE_ENVELOPE_NOT_CAUSAL_ESTIMATE'))
save('B5_growth_paths.csv',gp)
hr=list(csv.DictReader((P/'B5_exports_declared_1805_1811.csv').open()));checks=[]
for r in hr:
 err=sum(float(r[k]) for k in list(r)[2:11])-float(r['printed_total'])
 assert abs(err)<.031
 checks.append({'year':r['year'],'category':r['category'],'component_sum_minus_printed':round(err,5)})
assert max(abs(r['domestic_sum_error']) for r in bench)<.005
# Diagnostics are not the narrow falsifier: official all goods and northern Europe only.
x={r['year']:r for r in annual if r['year']!=1813}
e0=sum(x[y]['north_europe'] for y in [1804,1805,1806])/3
a0=sum(x[y]['asia']+x[y]['latin_foreign_west_indies'] for y in [1804,1805,1806])/3
prox=[]
for y in range(1808,1813):
 gap=e0-x[y]['north_europe'];inc=x[y]['asia']+x[y]['latin_foreign_west_indies']-a0
 prox.append(dict(year=y,north_europe_loss=gap,latin_plus_asia_increment=inc,ratio=inc/gap if gap>0 else '',note='all_goods_old_fixed_prices_not_domestic_not_cash'))
save('B5_replacement_diagnostics.csv',prox)
dom={int(r['year']):r for r in hr if r['category']=='domestic'}
def dr(y,k):return float(dom[y][k])
hec_north_gap=sum(dr(y,'north_europe_incl_france') for y in [1805,1806,1807])/3-dr(1811,'north_europe_incl_france')
hec_alt_inc=dr(1811,'rest_america')+dr(1811,'asia')-sum(dr(y,'rest_america')+dr(y,'asia') for y in [1805,1806,1807])/3
hec_1805=(dr(1811,'rest_america')+dr(1811,'asia')-dr(1805,'rest_america')-dr(1805,'asia'))/(dr(1805,'north_europe_incl_france')-dr(1811,'north_europe_incl_france'))
late_s3_high=next(r for r in mr if r['scenario']=='S3' and r['horizon'].startswith('late') and r['edge']=='high')
needed=late_s3_high['europe_loss']/late_s3_high['realization'];planned=late_s3_high['effective_extra']/late_s3_high['realization']
extra_checks={'H1811_north_gap_baseline1805_7':hec_north_gap,'H1811_rest_America_plus_Asia_increment':hec_alt_inc,'H1811_broad_proxy_ratio_1805_7':hec_alt_inc/hec_north_gap,'H1811_broad_proxy_ratio_1805':hec_1805,'lateS3_needed_gross_extra':needed,'lateS3_needed_relative_nonEurope':needed/(bench[-1]['total_excl_ireland']-bench[-1]['europe']),'lateS3_unfilled_gross_extra':needed-planned,'growth_sensitivity_plus_0_3pp_33years':math.exp(.003*33)-1,'growth_sensitivity_minus_0_3pp_33years':math.exp(-.003*33)-1}
audit={'extra_checks':extra_checks,'heckscher_sum_checks':checks,'davis_sum_max_error':max(abs(r['domestic_sum_error']) for r in bench),'official_proxy_five_year_net_ratio':sum(r['latin_plus_asia_increment'] for r in prox)/sum(r['north_europe_loss'] for r in prox),'official_proxy_1811':prox[3],'cautions':['No formal identification of pure-Latin domestic export falsifier','Neither quantities nor GDP can be recovered from declared export levels','Scenario envelopes are selected assumptions, not probability confidence intervals','A40_1811_corrected_raw_retained','1813_missing']}
(P/'B5_checks.json').write_text(json.dumps(audit,indent=2))
md=['# B5可复算表（原始口径见正文与SOURCES）','\n## 本国产品目的地三年均：当期£m，排爱尔兰','|期间|欧洲|亚洲|拉美|美国|总额|','|---|---:|---:|---:|---:|---:|']
for r in bench:md.append('|'+str(r['period'])+'|'+'|'.join(f'{r[k]:.3f}' for k in ['europe','asia','latin_america','usa','total_excl_ireland'])+'|')
md+=['\n## 出口替代情景（假设，不是观测；不同基准期不得相减）','|基准|情景|边|欧损失|额外已实现|总额/基准|','|---|---|---|---:|---:|---:|']
for r in mr:md.append(f"|{r['horizon']}|{r['scenario']}|{r['edge']}|{r['europe_loss']:.2f}|{r['effective_extra']:.2f}|{r['relative_total']*100:.1f}%|")
md+=['\n## 工业上限（同年S0=100，不是置信区间）','|情景|年份|下沿|上沿|','|---|---:|---:|---:|']
for scen in growth:
 for year in [1815,1830,1835,1840,1848]:
  z=[r for r in gp if r['scenario']==scen and r['year']==year];md.append(f"|{scen}|{year}|{z[0]['relative_S0']*100:.1f}|{z[1]['relative_S0']*100:.1f}|")
md+=['\n## 历史工业工资（1803=100，工资不含失业/短时）','|年|工业|煤|铁|纺织|CPI|实际薪率|人口GB+NI千人|','|---|---:|---:|---:|---:|---:|---:|---:|']
for r in iv:
 if r['year'] in [1803,1808,1810,1811,1812,1815,1816,1817,1819,1830,1840,1848]:
  md.append('|'+str(r['year'])+'|'+'|'.join(f'{r[k]:.1f}' for k in ['industry_1803_100','coal_1803_100','iron_1803_100','textiles_1803_100','cpi_1803_100','real_full_employment_earnings_1803_100','population_GB_NI_thousands'])+'|')
(P/'B5_export_substitution.md').write_text('\n'.join(md)+'\n')
print('Built annual, benchmark, diagnostic and scenario tables; assertions passed.')
