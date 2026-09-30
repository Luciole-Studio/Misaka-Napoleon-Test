"""C4 local accounting illustrations, NOT estimated historical trajectories.
No regressions, elasticity estimation, historical interpolation or FX conversion.
All parameter combinations declared below are emitted. Run from project root.
"""
import csv
from pathlib import Path
from decimal import Decimal as D
P = Path(__file__).resolve().parent

def save(name, fields, rows):
    with (P/name).open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

rows=[]
for r in (D('0'), D('.03'), D('.06')):
    d=D(0)
    for year in range(1812,1831):
        old=d; interest=r*old; d=old+interest+D(1)
        n=year-1811
        closed=D(n) if r==0 else ((1+r)**n-1)/r
        assert abs(closed-d)<D('1e-20')
        assert abs(d-old-interest-1)<D('1e-20')
        rows.append(dict(year=year,n=n,rate=str(r),annual_incremental_primary_gap=1,
                         incremental_interest=str(round(interest,6)),incremental_liability=str(round(d,6)),
                         unit='arbitrary_money_unit',status='MODEL_UNCALIBRATED',
                         locator='c4_endurance_scenarios.md section 6; build_sensitivity.py',
                         interpretation_limit='Not UK or French debt; zero initial incremental balance; all new interest borrowed; fixed rate; no valuation change'))
save('c4_unit_sensitivity.csv',list(rows[0]),rows)

rows=[]
for saved in (0,5,10,15):
    for enforcement in (0,2,5):
        for recovered in (0,5):
            loss=10; gap=loss+enforcement-saved-recovered
            rows.append(dict(external_cash_loss=loss,spending_saved=saved,enforcement_added=enforcement,
                             domestic_cash_recovery=recovered,incremental_primary_gap=gap,
                             unit='arbitrary_money_unit',status='MODEL_UNCALIBRATED',
                             locator='c4_endurance_scenarios.md section 6',
                             interpretation_limit='24 complete combinations; not empirical French values; negative gap is budget improvement not observed surplus'))
save('c4_transition_sensitivity.csv',list(rows[0]),rows)

rows=[]
for s in ('S2_maritime_coexistence','S3_strict_blockade','S3_licence_compromise','S5_conditional_peace'):
    for year in range(1812,1831):
        rows.append(dict(scenario=s,year=year,uk_tax_revenue='NA',uk_debt='NA',fr_net_transfers='NA',
                         fr_available_reserves='NA',binding_constraint_year='NA',status='NOT_IDENTIFIED',
                         locator='c4_endurance_scenarios.md sections 6-9; C2 c2_gaps.csv',
                         interpretation_limit='Historical cross-sections do not identify counterfactual annual paths; NA is not zero; S5 conditional activation date unspecified'))
save('c4_annual_status.csv',list(rows[0]),rows)
print('Created 57 unit rows, 24 transition rows, 76 annual NA rows. Recurrence and closed-form checks passed.')
for r in (D('0'),D('.03'),D('.06')):
    print('r=',r,[(year,round(D(year-1811) if r==0 else ((1+r)**(year-1811)-1)/r,4)) for year in (1812,1815,1820,1825,1830)])
