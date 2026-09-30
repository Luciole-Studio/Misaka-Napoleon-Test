#!/usr/bin/env python3
"""Explicit counterfactual subsistence transport sensitivity, not historical observations."""
import csv
from pathlib import Path
out = Path(__file__).with_name('E1_scenario_stress.csv')
fields = ['scenario','scope','people','horses','food_kg_per_person_day','fodder_kg_per_horse_day','human_food_t_per_day','horse_feed_t_per_day','gross_t_per_day','gross_t_per_year_if_365d','local_supply_share_assumed','handling_loss_share_assumed','imported_t_per_day_if_local_share','status','interpretation']
# Personnel and horse stocks are hypothetical continental force-network snapshots,
# NOT F2 army estimates, actual 1803 inventories, or point-to-point transported loads.
ASSUMPTIONS = [
 ('S2 low','continental forward force',180000,40000,.85,.05),
 ('S2 central','continental forward force',200000,45000,.65,.10),
 ('S2 high','continental forward force',220000,50000,.50,.15),
 ('S3 continued war','continental forward force',300000,60000,.65,.10),
 ('S6-lite','continental forward force',350000,70000,.65,.10),
 ('S6-max','continental forward force',500000,100000,.65,.10),
 ('S6-full','continental forward force',650000,130000,.65,.10),
 ('S6-full extreme','continental forward force',800000,160000,.50,.15),
]
with out.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fields);w.writeheader()
 for name,scope,p,h,share,loss in ASSUMPTIONS:
  human=p*1.5/1000; horse=h*10/1000; gross=human+horse
  imported=gross*(1-share)/(1-loss)
  w.writerow(dict(zip(fields,[name,scope,p,h,1.5,10,round(human,2),round(horse,2),round(gross,2),
                                round(gross*365,2),share,loss,round(imported,2),'MODEL_NOT_OBSERVATION',
                                'Gross is all-theatre annualized consumption if force is present 365d; local supply fraction and loss assumptions are illustrative; feed is NOT all grain; not necessarily hauled from France'])) )
print(f'{out}: {len(ASSUMPTIONS)} model sensitivity rows')
