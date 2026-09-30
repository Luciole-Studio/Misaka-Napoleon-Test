#!/usr/bin/env python3
"""B4 deterministic interface tables. Arithmetic checks are NOT historical validation.
Reads the existing 48-case land matrix, never overwrites it. All generated force,
time, food and delivery outputs are conditional models, not observations.
"""
import csv
import hashlib
import json
import math
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'B4_landing_scenario_matrix.csv'
with BASE.open(encoding='utf-8-sig', newline='') as f:
    base = list(csv.DictReader(f))
assert len(base) == 48
assert {r['landing_zone'] for r in base} == {'Kent', 'Sussex', 'Thames–Essex', 'Weymouth'}
assert {r['effective_warning_bin'] for r in base} == {'W0', 'W1', 'W2'}
assert {int(r['French_effective_ashore_D2']) for r in base} == {20000, 40000, 80000, 120000}
assert len({(r['landing_zone'], r['effective_warning_bin'], r['French_effective_ashore_D2']) for r in base}) == 48
assert all(r['evidence_status'] == 'MODEL_NOT_OBSERVATION' for r in base)


def save(name, rows):
    assert rows and all(set(r) == set(rows[0]) for r in rows)
    assert all(v is not None and str(v) != '' for r in rows for v in r.values())
    with (ROOT / name).open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def case_id(r):
    return f"{r['landing_zone']}_{r['effective_warning_bin']}_F{r['French_effective_ashore_D2']}"


def nearest_thousand_half_up(value):
    # Match the original matrix's 14,500 -> 15,000 convention, not Python bankers rounding.
    return int(math.floor(value / 1000 + .5) * 1000)


def r1(value):
    return float(Decimal(str(value)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))


profiles = {
    'T0_FULL_DELIVERED': ('UNFIXED_BY_LAND_CASE', 'ASSUMED_FOR_LAND_ONLY', 'S01;S02;S03;S04'),
    'T1_TWO_TIDE_PROPOSAL': ('2_PROPOSED_AFTER_PRESTAGING', 'UNVALIDATED_DELIVERY_GATE', 'S18 pp398-400'),
    'T2_SIX_TIDE_MODEL': ('6_GLOVER_FULL_FLOTILLA_MODEL', 'UNVALIDATED_DELIVERY_GATE', 'S14 chapter1'),
    'T3_INFANTRY_FIRST': ('UNFIXED_INCOMPLETE_GUNS_HORSES', 'COMBINED_ARMS_CONDITION_FALSE', 'S02;S03;S18'),
}
expanded = []
for r in base:
    force = int(r['French_effective_ashore_D2'])
    outcome = r['ordinal_outcome']
    for profile, (tides, status, sources) in profiles.items():
        if profile == 'T0_FULL_DELIVERED':
            integrated = f'{outcome}_CONDITIONAL_ON_DELIVERY'
        elif profile in ('T1_TWO_TIDE_PROPOSAL', 'T2_SIX_TIDE_MODEL'):
            integrated = f'NOT_ADMITTED_IF_DELIVERED_{outcome}'
        else:
            shifted = {'I': 'I', 'C': 'I', 'F': 'C', 'F西': 'C'}[outcome]
            integrated = f'{shifted}_ONE_GRADE_QUALITY_STRESS_ONLY'
        low = high = 'NOT_ESTIMATED'
        if r['landing_zone'] == 'Kent' and force == 80000:
            if profile == 'T1_TWO_TIDE_PROPOSAL':
                low, high = 12 + 12 + 10 + 12, 24 + 26 + 12 + 36
            elif profile == 'T2_SIX_TIDE_MODEL':
                low, high = 12 + 72 + 10 + 12, 24 + 72 + 12 + 36
        expanded.append({
            'parent_land_case': case_id(r),
            'baseline_year': 1805,
            'landing_zone': r['landing_zone'],
            'effective_warning_bin': r['effective_warning_bin'],
            'French_combined_arms_target_D2_not_observed': force,
            'transport_profile': profile,
            'French_headcount_for_T3_only': force if profile == 'T3_INFANTRY_FIRST' else 'NOT_APPLICABLE',
            'land_outcome_if_full_force_delivered': outcome,
            'conditional_integrated_judgment': integrated,
            'integrated_case_status': status,
            'departure_tides_basis': tides,
            'serial_safety_weather_hours_low_assumed': low,
            'serial_safety_weather_hours_high_assumed': high,
            'window_scope': '80K_KENT_ONLY_NO_EMPIRICAL_THROUGHPUT',
            'D0_definition': 'FIRST_UNLOADING_NOT_FIRST_DEPARTURE',
            'warning_delivery_independence': 'NOT_ASSUMED_INDEPENDENT_LONG_PREP_NEEDS_WARNING_REVIEW',
            'evidence_status': 'MODEL_NOT_OBSERVATION',
            'land_confidence': r['confidence'],
            'delivery_confidence': 'ASSUMED_NOT_MEASURED' if profile == 'T0_FULL_DELIVERED' else 'LOW_UNVERIFIED',
            'sources': sources,
        })
save('B4_transport_expanded_matrix.csv', expanded)

# Cary 1815 source miles; one furlong = 1/8 mile. Never treat as 1805 route returns.
# Origins are not silently merged: London Bridge, Westminster, Whitechapel and Hyde Park differ.
routes = [
    ('London Bridge', 'Hythe', 67, 'S21 pp11-12', 'direct'),
    ('Maidstone', 'Hythe', 67 - (34 + 3/8), 'S21 pp11-12', 'same_route_difference'),
    ('Ashford', 'Hythe', 67 - (54 + 4/8), 'S21 pp11-12', 'same_route_difference'),
    ('Westminster Bridge', 'East/South Bourne', 60 + 4/8, 'S21 p50', 'direct'),
    ('Whitechapel Church', 'St Osyth', 62, 'S21 pp535-536;546', 'direct'),
    ('Chelmsford', 'St Osyth via Colchester', 62 - (28 + 7/8), 'S21 pp535-536;546', 'same_route_difference'),
    ('Colchester', 'St Osyth', 62 - 51, 'S21 p546', 'same_route_difference'),
    ('Colchester', 'Harwich', 71 + 5/8 - 51, 'S21 pp535-536;546', 'same_route_difference'),
    ('Whitechapel Church', 'Harwich', 71 + 5/8, 'S21 p546', 'direct'),
    ('Hyde Park Corner', 'Weymouth', 127 + 6/8, 'S21 p84', 'direct'),
]
marches = []
for origin, destination, miles, source, method in routes:
    marches.append({
        'origin': origin, 'destination': destination,
        'road_miles_1815_source': miles, 'distance_method': method,
        'source_year': 1815, 'scenario_year': 1805,
        'foot_miles_day_low_assumed': 15, 'foot_miles_day_high_assumed': 20,
        'foot_departure_delay_days_low_assumed': .5, 'foot_departure_delay_days_high_assumed': 1,
        'reform_days_low_assumed': .25, 'reform_days_high_assumed': .5,
        'foot_days_low_model': r1(.75 + miles / 20),
        'foot_days_high_model': r1(1.5 + miles / 15),
        'fast_troop_wagon_days_low_model': r1(1.25 + miles / 40),
        'fast_troop_wagon_days_high_model': r1(1.5 + miles / 40),
        'supply_wagon_days_low_model': r1(1.25 + miles / 30),
        'supply_wagon_days_high_model': r1(1.5 + miles / 25),
        'foot_days_low_minus20pct_distance_stress': r1(.75 + .8 * miles / 20),
        'foot_days_high_plus20pct_distance_stress': r1(1.5 + 1.2 * miles / 15),
        'troop_wagon_speed_basis': 'S01_p137_plan_not_observed_40_mi_day',
        'supply_wagon_speed_basis': 'S20_p244_plan_not_observed_25_to_30_mi_day_24h_notice',
        'route_source': source,
        'evidence_status': '1815_GEOGRAPHY_PROXY_PLUS_MODEL_NOT_1805_MEASURED_PERFORMANCE',
        'confidence': 'LOW_TIME_MODEL_DISTANCE_SCAN_CHECKED',
    })
save('B4_march_time_ranges.csv', marches)

kent = {r['effective_warning_bin']: r for r in base if r['landing_zone'] == 'Kent'}
strength = []
for r in base:
    for mode in ('JUNE_STOCK_64614', 'ESSEX_SAME_ARRIVAL_AS_KENT'):
        stock = 64614 if mode == 'JUNE_STOCK_64614' else 58000
        template = kent[r['effective_warning_bin']] if mode == 'ESSEX_SAME_ARRIVAL_AS_KENT' and r['landing_zone'] == 'Thames–Essex' else r
        low_a = float(template['arrival_share_low_assumed'])
        high_a = float(template['arrival_share_high_assumed'])
        outcome = r['ordinal_outcome']
        if mode == 'ESSEX_SAME_ARRIVAL_AS_KENT' and r['landing_zone'] == 'Thames–Essex' and r['effective_warning_bin'] == 'W1' and int(r['French_effective_ashore_D2']) == 20000:
            outcome = 'I'
        strong_position = 'C' if r['effective_warning_bin'] == 'W2' and int(r['French_effective_ashore_D2']) == 80000 else outcome
        strength.append({
            'parent_land_case': case_id(r), 'sensitivity_profile': mode,
            'GB_regular_stock_scenario': stock,
            'arrival_share_low_assumed': low_a, 'arrival_share_high_assumed': high_a,
            'British_regular_D2_low_model': nearest_thousand_half_up(stock * low_a),
            'British_regular_D2_high_model': nearest_thousand_half_up(stock * high_a),
            'militia_D2_low_assumed': template['militia_D2_low_assumed'],
            'militia_D2_high_assumed': template['militia_D2_high_assumed'],
            'baseline_outcome': r['ordinal_outcome'],
            'sensitivity_judgment_not_fitted': outcome,
            'separate_strong_position_80k_W2_branch': strong_position,
            'strong_position_condition': '30_to_40k_regulars_plus25_to35k_trained_militia_guns_cavalry_prepared_position_NOT_VERIFIED',
            'sources': 'S07 stock;S20 p165 transport_not_combat_strength;B4 section6',
            'evidence_status': 'MODEL_NOT_OBSERVATION', 'confidence': 'LOW_TO_MEDIUM',
            'judgment_method': 'QUALITATIVE_ORDINAL_NOT_AUTOMATIC_STRENGTH_RATIO',
        })
save('B4_British_strength_sensitivity.csv', strength)

food = []
for F in (20000, 40000, 80000, 120000):
    g = math.ceil(F / 20232)
    food.append({
        'French_target': F,
        'Montreuil_20232_combat_seat_template_groups': g,
        'combat_craft_template_count_not_minimum': g * 216,
        'auxiliary_transport_template_count_not_minimum': g * 126,
        'total_craft_template_count_not_minimum': g * 342,
        'combat_seats_template_total': g * 20232,
        'horse_places_in_template_not_minimum': g * 1391,
        'horses_under_10pct_headcount_assumption': int(F * .10),
        'horse_place_shortfall_vs_10pct_model_not_observed': max(0, int(F * .10) - g * 1391),
        'required_average_ready_men_per_hour_over48h_not_unloading_rate': r1(F / 48),
        'human_food_metric_tonnes_day_model': F * .0015,
        'horse_ratio_low_assumed': .05, 'horse_ratio_mid_assumed': .10, 'horse_ratio_high_assumed': .15,
        'horse_fodder_kg_day_assumed': 10,
        'total_food_tonnes_day_lowhorse_model': F * .002,
        'total_food_tonnes_day_midhorse_model': F * .0025,
        'total_food_tonnes_day_highhorse_model': F * .003,
        'seven_day_food_tonnes_midhorse_model': F * .0025 * 7,
        'horse_gun_ammo_minimum': 'NOT_FROZEN',
        'food_basis': 'S19_p64_HYPOTHETICAL_NOT_MOSCOW_ACTUAL_RETURN_approx_1.5kg',
        'capacity_basis': 'S18_p445_PLANNED_ONE_CORPS_NOT_TOTAL_FLEET_NOT_TIDAL_THROUGHPUT',
        'evidence_status': 'MODEL_NOT_OBSERVATION',
    })
save('B4_capacity_food_sensitivity.csv', food)

assert len(expanded) == 192 and len(marches) == 10 and len(strength) == 96 and len(food) == 4
assert all(r['conditional_integrated_judgment'] and r['integrated_case_status'] for r in expanded)
assert sum(r['integrated_case_status'] == 'UNVALIDATED_DELIVERY_GATE' for r in expanded) == 96
assert all(r['foot_days_low_model'] <= r['foot_days_high_model'] for r in marches)
assert all(r['combat_seats_template_total'] >= r['French_target'] for r in food)
assert next(r for r in food if r['French_target'] == 80000)['horse_place_shortfall_vs_10pct_model_not_observed'] == 2436
base_by_id = {case_id(r): r for r in base}
for row in strength:
    original = base_by_id[row['parent_land_case']]
    if row['sensitivity_profile'] == 'ESSEX_SAME_ARRIVAL_AS_KENT' and original['landing_zone'] != 'Thames–Essex':
        for k in ('British_regular_D2_low_model', 'British_regular_D2_high_model'):
            assert row[k] == int(original[k]), (row['parent_land_case'], k)
outputs = ['B4_transport_expanded_matrix.csv', 'B4_march_time_ranges.csv', 'B4_British_strength_sensitivity.csv', 'B4_capacity_food_sensitivity.csv']
checks = {
    'scope': 'ARITHMETIC_AND_STRUCTURE_ONLY_NOT_HISTORICAL_VALIDATION',
    'base_sha256': hashlib.sha256(BASE.read_bytes()).hexdigest(),
    'build_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'base_cases': len(base), 'expanded_cases': len(expanded), 'routes': len(marches),
    'strength_sensitivities': len(strength), 'food_capacity_rows': len(food),
    'empty_required_cells': 0, 'delivery_gates_unvalidated': 96,
    'new_observed_invasion_outcomes': 0,
    'all_assertions_passed': True,
    'outputs_sha256': {n: hashlib.sha256((ROOT / n).read_bytes()).hexdigest() for n in outputs},
}
(ROOT / 'B4_supplement_checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in checks.items() if k != 'outputs_sha256'}, ensure_ascii=False, indent=2))
