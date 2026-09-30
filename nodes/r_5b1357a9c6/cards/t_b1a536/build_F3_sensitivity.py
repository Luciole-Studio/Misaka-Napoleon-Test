#!/usr/bin/env python3
"""One-at-a-time stress tests and implied material demand; NOT observed traffic."""
import csv, json, math
from pathlib import Path
from copy import deepcopy
from build_F3_model import PARAMS, simulate, ROOT
BASE=deepcopy(PARAMS)
rows=[]
for scenario in ['W','P']:
    for case in ['base','lower_launches_30pct','lower_recruitment_30pct','lower_skill_addition_30pct','higher_hull_exit_2pp','ready_minus_10pp','crew_900_skill_550','no_Antwerp_initial12_and_launch3','initial_personnel_minus10k','war_loss_3_per_year']:
        PARAMS.clear();PARAMS.update(deepcopy(BASE))
        if case=='lower_launches_30pct':
            for group in ['W','P_after_1815']:
                for k in PARAMS[group]:
                    if k.startswith('launches'):PARAMS[group][k]=[v*.7 for v in PARAMS[group][k]]
        if case=='lower_recruitment_30pct':
            for g in ['W','P_after_1815']:
                PARAMS[g]['personnel_inflow_thousands']=[v*.7 for v in PARAMS[g]['personnel_inflow_thousands']]
                PARAMS[g]['qualified_inflow_thousands']=[v*.7 for v in PARAMS[g]['qualified_inflow_thousands']]
        if case=='lower_skill_addition_30pct':
            for g in ['W','P_after_1815']:PARAMS[g]['qualified_inflow_thousands']=[v*.7 for v in PARAMS[g]['qualified_inflow_thousands']]
        if case=='higher_hull_exit_2pp':
            for g in ['W','P_after_1815']:PARAMS[g]['hull_retirement_rate']=[v+.02 for v in PARAMS[g]['hull_retirement_rate']]
        if case=='ready_minus_10pp':
            for g in ['W','P_after_1815']:PARAMS[g]['hull_ready_fraction']=[v-.1 for v in PARAMS[g]['hull_ready_fraction']]
        if case=='crew_900_skill_550':
            PARAMS['crew_per_battle_ship_thousands']=.9;PARAMS['qualified_crew_per_battle_ship_thousands']=.55
        if case=='no_Antwerp_initial12_and_launch3':
            PARAMS['initial']['hulls']=38
            for g in ['W','P_after_1815']:
                for k in PARAMS[g]:
                    if k.startswith('launches'):PARAMS[g][k]=[max(0,v-3) for v in PARAMS[g][k]]
        if case=='initial_personnel_minus10k':
            PARAMS['initial']['total_personnel_thousands']=[v-10 for v in PARAMS['initial']['total_personnel_thousands']]
        if case=='war_loss_3_per_year':
            PARAMS['W']['annual_war_losses_ships']=[3,3,3]
        rs,a=simulate(scenario,1)
        for r in rs:
            if r['year'] in [1815,1820,1825,1830]:
                rows.append({'scenario':scenario,'test':case,'year':r['year'],'hulls':r['hulls'],'M_thousand':r['personnel_total_1000'],'Q_thousand':r['qualified_personnel_1000'],'A12':r['mobilizable_integer'],'binding':r['binding']})
PARAMS.clear();PARAMS.update(BASE)
with (ROOT/'F3_sensitivity.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
# Stères are retained as the source's unit. No conversion to solid cubic metres.
# Demand coefficients are assumptions anchored in S02's 3737 stères / 80-gun ship.
material=[]
for s in ['W','P']:
  for j,b in enumerate(['low','base','high']):
    rs,a=simulate(s,j)
    for r in rs:
      if r['year'] not in [1815,1820,1825,1830]:continue
      wood_per_ship=[3000,3500,4200][j]
      repair_fraction=[.20,.30,.40][j];repair_period=[10,8,7][j]
      nonline=[10000,15000,20000][j]
      new=r['launches']*wood_per_ship
      repair=r['hulls']*repair_fraction/repair_period*wood_per_ship
      material.append({'scenario':s,'bound':b,'year':r['year'],'unit':'source_steres_equivalent_not_solid_m3','line_new_required':round(new,2),'line_repair_required':round(repair,2),'nonline_assumed_required':nonline,'total_required_not_actual_transport':round(new+repair+nonline,2),'wood_coefficient_assumed':wood_per_ship,'repair_interval_assumed_years':repair_period,'source_anchor':'S02 paragraph3:3737stere per80gun;other coefficients explicit assumptions'})
with (ROOT/'F3_material_requirements.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=material[0]);w.writeheader();w.writerows(material)
print('one-at-a-time stress 1830 (base parameter set):')
for r in rows:
 if r['year']==1830:print(r['scenario'],r['test'],r['A12'],r['binding'])
print('Material rows=',len(material),'Sensitivity rows=',len(rows))
