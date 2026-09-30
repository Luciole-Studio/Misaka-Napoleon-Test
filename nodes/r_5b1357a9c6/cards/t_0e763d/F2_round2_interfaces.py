"""Bounded F2 second-round evidence and arithmetic bridge.
No fitted coefficients, no new national annual data, no probabilities.
Separate Rowe's period mobilised counts, Grab's dated levy subset, and models.
"""
from pathlib import Path
import csv
import json

P = Path(__file__).resolve().parent

def save_csv(name, rows):
    with (P / name).open('w', encoding='utf-8-sig', newline='') as handle:
        w = csv.DictWriter(handle, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

# Rowe 2003 printed p179, Table 3; PDF193 image checked in this F2 turn.
# Mobilised is the author's denominator, NOT retrospectively redefined as arrivals.
raw = [
    ('Rhineland_four_departments', '1800/1-1804/5', 9081, 2763, 1203),
    ('Rhineland_four_departments', '1806-1810', 24186, 8138, 725),
    ('Alsace_two_departments', '1800/1-1804/5', 7921, 615, 1813),
    ('Alsace_two_departments', '1806-1810', 13933, 2386, 1843),
    ('Empire_excluding_named_Italian_departments', '1800/1-1804/5', 313616, 65220, 87288),
    ('Empire_excluding_named_Italian_departments', '1806-1810', 530219, 162831, 64100),
]
regional = []
for region, period, n, dodgers, deserters in raw:
    regional.append(dict(region=region, period=period, mobilised_reported=n,
        draft_dodgers_reported=dodgers, deserters_reported=deserters,
        draft_dodgers_per_mobilised=dodgers/n,
        deserters_per_mobilised=deserters/n,
        status='published_period_aggregate_not_independent_or_annual',
        source_id='ROW03', locator='printed179_Table3_PDF193_doc_efa2c87c4afb',
        definition_warning='Do not add rates or infer arrival_count;Empire_contains_the_two_regions',
        coverage_warning='Empire_excludes_Arno_Mediterranee_Ombrone_Vicariats_de_Pontrenoli'))
save_csv('F2_regional_recruitment_evidence.csv', regional)

levy = [dict(order_date='1813-10-09', observation_deadline='1813-12_end',
             reported_classes='1808-1814', reported_subset_calls=127433,
             reported_arrived_by_deadline=72265,
             deadline_arrival_ratio=72265/127433,
             status='Grab2013_transfers_Leggiere2007;subset_scope_unreconciled_with_whole_decree',
             source_id='G13', locator='printed118_note75;L07_printed69_not_read',
             warning='NOT_annual_incorporation_or_final_success_rate;do_not_merge_with_Pigeard_decree_total')]
save_csv('F2_levy_batch_evidence.csv', levy)

# Match F2's rates, vary only the service convention and explicitly one retention arm.
# s includes conversion into a trained intake; no extra training-year survival deduction.
# Finite contract: service duration includes the one training year.
r, s, q, rho, g = 2.0, .9, .85, .6, 4.0
cases = []
hazard_years, other_exit = 6, .025
factor = 1/(1/hazard_years + other_exit)
for label, total_term, retention, count, factor in [
    ('F2_legacy_hazard6', '', 1-other_exit, '', factor),
    ('fixed_total5_includes_training1', 5, .975, 4, sum(.975**k for k in range(4))),
    ('fixed_total6_includes_training1', 6, .975, 5, sum(.975**k for k in range(5))),
    ('fixed_total7_includes_training1', 7, .975, 6, sum(.975**k for k in range(6))),
    ('fixed_total5_retention90_stress', 5, .90, 4, sum(.90**k for k in range(4))),
]:
    gross = r*s*factor
    present = gross*q*rho
    cases.append(dict(case=label, population_denominator=1000,
        annual_calls_per1000=r, conversion_s=s,
        total_contract_years=total_term, training_years=1,
        deployable_cohorts=count, post_training_retention=retention,
        hazard_retirement_parameter=1/6 if not total_term else '',
        stock_factor=factor, availability_q=q, reliability_rho=rho,
        security_present_per1000=g, trained_gross_per1000=gross,
        reliable_present_per1000=present, net_present_per1000=present-g,
        calls_per1000_for_zero_balance=g/(s*q*rho*factor),
        rho_for_zero_balance=g/(r*s*q*factor),
        status='conditional_model_not_estimated;no_probability',
        warning='Finite_term_includes_training;hazard6_is_not_same_contract;new_arm_does_not_rewrite_legacy_S6'))
save_csv('F2_service_definition_bridge.csv', cases)

# E1/F2 ration interface: illustrative deployed force, not whole national army.
food = []
for name, people, horses in [('E1_S6max_example',500000,100000),
                             ('F2_large_force_example',500000,125000)]:
    human, feed = people*1.5/1000, horses*10/1000
    food.append(dict(case=name, people=people, horses=horses,
        food_kg_per_person_day=1.5, fodder_kg_per_horse_day=10,
        human_t_day=human, horse_feed_t_day=feed, total_metric_t_day=human+feed,
        annualized_metric_t_if_365days=(human+feed)*365,
        status='illustration_not_observation;horse_feed_not_all_grain',
        source='F2_V77_metric_normalized_assumption;E1_scenario_stress.csv',
        warning='Not_total_European_force;not_all_hauled_from_France'))
save_csv('F2_food_scope_bridge.csv', food)

checks = dict(
    regional_rows=len(regional), levy_batch_rows=len(levy), service_rows=len(cases),
    food_rows=len(food), levy_deadline_ratio=levy[0]['deadline_arrival_ratio'],
    hazard_net_per1000=cases[0]['net_present_per1000'],
    fixed_total5_net_per1000=cases[1]['net_present_per1000'],
    fixed_total5_calls_per1000_threshold=cases[1]['calls_per1000_for_zero_balance'],
    fixed_total5_rho_threshold=cases[1]['rho_for_zero_balance'],
    food_difference_metric_t_day=food[1]['total_metric_t_day']-food[0]['total_metric_t_day'],
    warning='Arithmetic checks are not historical calibration.')
assert len(regional)==6 and len(cases)==5
assert cases[0]['net_present_per1000']>0>cases[1]['net_present_per1000']
assert checks['food_difference_metric_t_day']==250
(P/'F2_round2_checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(checks, ensure_ascii=False, indent=2))
