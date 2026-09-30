"""Reproduce arithmetic only; no fitted probabilities or causal validation.
Run: python3 nodes/r_5b1357a9c6/cards/t_f4bb81/A_calculations.py
Inputs: manually transcribed A_fiscal_anchors.csv and A_scenario_bounds.csv.
"""
from pathlib import Path
import csv
import json
from decimal import Decimal

HERE = Path(__file__).resolve().parent
with (HERE / 'A_fiscal_anchors.csv').open(encoding='utf-8', newline='') as f:
    fiscal = list(csv.DictReader(f))
results = []
for row in fiscal:
    r = Decimal(row['revenue_million_flCM'])
    e = Decimal(row['expenditure_million_flCM'])
    m = Decimal(row['military_million_flCM'])
    results.append({'year': int(row['year']),
                    'deficit_million_flCM': float(e-r),
                    'military_to_revenue_pct': float((100*m/r).quantize(Decimal('.01')))})
with (HERE / 'A_scenario_bounds.csv').open(encoding='utf-8', newline='') as f:
    bounds = list(csv.DictReader(f))
assert all(Decimal(x['low']) <= Decimal(x['high']) for x in bounds)
occupancy = {'low': 25000 + 30000 + 45000,
             'high': 45000 + 55000 + 80000}
pop = [100 * (1 + x)**38 for x in (.005, .01)]
output = {'scope': 'ARITHMETIC_ONLY_NOT_MODEL_VALIDATION',
          'fiscal': results,
          'occupation_persons_assumed_sum': occupancy,
          'occupation_frictionless_half': {k: v/2 for k,v in occupancy.items()},
          'population_index_1848_given_1810_100': pop,
          'source_rows': len(fiscal), 'scenario_rows': len(bounds),
          'notes': ['flCM is silver-value conversion not constant purchasing power',
                    'Annual territorial changes persist',
                    'Deficit is not identical to new debt',
                    'Scenario endpoints are conditional bounds not probability intervals']}
(HERE / 'A_calculation_results.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(output, ensure_ascii=False, indent=2))
