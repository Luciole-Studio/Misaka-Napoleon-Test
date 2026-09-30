from pathlib import Path
import csv,json
P=Path(__file__).resolve().parent
rows=[]
for r in csv.DictReader((P/'预算.csv').open()):
 r={k:float(v) for k,v in r.items()}
 used=sum(v for k,v in r.items() if k!='revenue')
 assert used==r['revenue']
 r['balance']=r['revenue']-used
 r['army_roster_at_700']=r['army']*1000000/700
 r['army_roster_at_900']=r['army']*1000000/900
 rows.append(r)
out={'unit':'million francs; army cost francs per person-year; author scenarios, not historical revenue observations','budgets':rows,'province_example_gross':{'retained':83+37.5+33+16,'excluded':66.5+38.791+22.5+16.5,'unallocated':342.260044-(83+37.5+33+16+66.5+38.791+22.5+16.5)},'common_fund_spendable':{'base_5m_5pct':5-20*.05-1,'5m_7pct':5-20*.07-1,'3m_7pct':3-20*.07-1},'rail_1500km_cost_mfr':[1500*.25,1500*.40],'annual_rail_15years_mfr':[1500*.25/15,1500*.40/15],'navy_extra_195_vs_165':195-165,'navy_extra_share_rail_40':(195-165)/40,'rouanet_piano_source_mismatch':{'2812_over_10499':2812/10499,'3256_over_10499':3256/10499},'annualized_3144_nine_month_letters':3144*12/9}
(P/'复算结果.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
