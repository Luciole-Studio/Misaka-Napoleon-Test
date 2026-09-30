"""C3 bounded arithmetic and missing-data register; no fleet simulation.
Run from project root: python3 nodes/r_b55f2c1cf5/cards/t_7ee3b0/build_c3.py
Only C2 stock rows 2--4 enter arithmetic. No interpolation or calibrated rates.
"""
import csv, hashlib, json, math
from pathlib import Path
from fractions import Fraction
ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
SRC = ROOT/'nodes/r_b55f2c1cf5/cards/t_104134/c2_series.csv'
with SRC.open() as f:
    raw = list(csv.DictReader(f))
obs = {}
for line, row in enumerate(raw, 2):
    if row['series']=='naval_stock' and row['ship_class']=='line':
        year=int(row['year'])
        a,b,c,d,e = [int(row[k]) for k in ['sea_commission','sea_ordinary','harbour_commission','harbour_ordinary','building_ordered_low']]
        obs[year] = dict(commission=a, ordinary=b, sea=a+b, gross=a+b+c+d+e, line=line)
assert [(y,obs[y]['sea'],obs[y]['gross']) for y in sorted(obs)] == [(1803,111,172),(1804,115,172),(1805,116,181)]
def save(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
rows=[]
for s in ['a_historical','b_amiens_continues','c_S2_consolidation','d_S3_blockade_intensified']:
    for y in range(1803,1831):
        # S2/S3 are defined here to branch only after Tilsit; b after Jan 1803.
        available = y in obs and (s!='b_amiens_continues' or y==1803)
        o=obs[y] if available else {}
        rows.append(dict(scenario=s,year=y,time_basis='start_of_year',
            UK_sea_commission=o.get('commission','NA'),UK_sea_ordinary=o.get('ordinary','NA'),
            UK_sea_category_hulls=o.get('sea','NA'),France_comparable_hulls='NA',
            France_UK_hull_ratio='NA',France_UK_tonnage_ratio='NA',
            trained_stock_proxy_ratio='NA',escort_projection_index='NA',
            input_C2_physical_line=o.get('line','NA'),
            status='partial_observation_not_calibration' if available else 'not_identified',
            reason='no_French_national_stock;no_training_days;no_mission_capacity'))
save('c3_scenarios.csv',rows)
thresholds=[]
for y,o in obs.items():
    for target in [Fraction(4,5),Fraction(1,1)]:
        thresholds.append(dict(UK_reference_year=y,UK_sea_category_hulls=o['sea'],
            target_fraction=float(target),minimum_French_same_scope_hulls=math.ceil(target*o['sea']),
            C2_physical_line=o['line'],status='conditional_arithmetic_not_observed_French_strength'))
save('c3_thresholds.csv',thresholds)
quality=[]
for h in [Fraction(4,5),Fraction(1)]:
    for target in [Fraction(7,10),Fraction(1)]:
        quality.append(dict(hypothetical_hull_ratio=float(h),target_effective_ratio=float(target),
            required_other_factors_ratio=float(target/h),
            status='identity_only_not_estimated_quality;requires_multiplicative_diagnostic_assumption'))
save('c3_quality_thresholds.csv',quality)
checks=[dict(check='UK_1803_reaggregation',expected=172,computed=obs[1803]['gross'],relative_error='0',status='arithmetic_only_not_model_validation'),dict(check='UK_1804_reaggregation',expected=172,computed=obs[1804]['gross'],relative_error='0',status='arithmetic_only_not_model_validation'),dict(check='UK_1805_reaggregation',expected=181,computed=obs[1805]['gross'],relative_error='0',status='arithmetic_only_not_model_validation')]
for check in ['FR_launches_1807_1814','FR_national_stock_1814','UK_same_scope_stock_1807_1814','crew_training_proxy_1807_1814']:
    checks.append(dict(check=check,expected='NA',computed='NA',relative_error='NA',status='not_executable_missing_inputs'))
save('c3_calibration.csv',checks)
assert len(rows)==112
assert all(r['France_UK_hull_ratio']=='NA' for r in rows)
assert len([r for r in rows if r['UK_sea_category_hulls']!='NA'])==10
files=[SRC, ROOT/'nodes/r_b55f2c1cf5/cards/t_104134/c2_gaps.csv', ROOT/'nodes/r_b55f2c1cf5/cards/t_104134/manpower/late_supply_addendum.md']
manifest={'method':'exact integer sums and Fraction thresholds only; no estimated historical model','input_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'outputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.glob('c3_*.csv'))},'annual_rows':len(rows),'tests':'passed sums, row count, no fabricated ratios, branch inheritance'}
(OUT/'c3_replay_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
