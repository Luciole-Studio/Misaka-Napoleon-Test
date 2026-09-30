"""Reproduce transparent arithmetic assumptions, NOT an estimated historical model.
Run from any directory: python3 /path/to/PR_arithmetic.py
Inputs/outputs are beside this script. Uses only Python standard library.
"""
from pathlib import Path
import csv

root = Path(__file__).resolve().parent
with (root / 'PR_parameters.csv').open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
assert len({r['id'] for r in rows}) == len(rows)
assert all(None not in r for r in rows), 'Misaligned CSV columns'
results = []
values = {}
for r in rows:
    num = lambda k: float(r[k])
    if r['kind'] == 'population':
        low = num('base_low') * (1 + num('growth_low')) ** num('years')
        high = num('base_high') * (1 + num('growth_high')) ** num('years')
        formula = 'base*(1+annual_net_growth)^years'
    elif r['kind'] == 'army':
        pl, ph = values['pop_s5']
        low = pl * num('rate_low') * num('availability_low')
        high = ph * num('rate_high') * num('availability_high')
        formula = 'S5_population*assumed_mobilisation_rate*availability'
    elif r['kind'] == 'garrison':
        low = sum(num(k+'_low') for k in ['garrison', 'nodes', 'mobile'])
        high = sum(num(k+'_high') for k in ['garrison', 'nodes', 'mobile'])
        formula = 'fortresses+nodes+mobile_reserve; excludes external field front'
    else:
        raise ValueError(r['kind'])
    assert 0 <= low <= high
    values[r['id']] = (low, high)
    results.append(dict(id=r['id'], scenario=r['scenario'], low=round(low),
                        high=round(high), unit=r['unit'], formula=formula,
                        provenance=r['source'], status='ASSUMPTION_ARITHMETIC_NOT_OBSERVATION'))
rl,rh = values['control_rump']
ml,mh = values['abolition_medium']
results.append(dict(id='increment_medium_minus_rump', scenario='S6_minus_S2',
                    low=round(ml-rh), high=round(mh-rl), unit='persons',
                    formula='low=medium_low-rump_high; high=medium_high-rump_low',
                    provenance='T08 anchor plus assumed task buckets',
                    status='ASSUMPTION_ARITHMETIC_NOT_OBSERVATION'))
with (root / 'PR_calculations.csv').open('w',encoding='utf-8',newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(results[0]))
    w.writeheader(); w.writerows(results)
for r in results:
    print(r['id'], r['low'], r['high'], r['unit'])
print('No currency conversion or probability inference performed.')
