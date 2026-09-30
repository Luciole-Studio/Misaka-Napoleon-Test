"""Serialize reviewed historical observations; blanks remain unknown.
No interpolation, no division of cumulative conscription/losses into annual series.
See SOURCES.md for source keys; all year columns refer to calendar year unless stated.
"""
from pathlib import Path
import csv
P=Path(__file__).resolve().parent
annual=[120000,60000,210000,80000,80000,240000,76000,160000,120000,237000,1140000,None]
classes={1803:60000,1804:60000,1805:60000,1806:80000,1807:80000,1808:80000,1809:80000,1810:110000,1811:120000,1812:120000,1813:137000,1814:150000}
notes={
1803:'LAV legacy calendar-year call-up includes mixed measures; class is separate axis',
1804:'No national annual arrivals recovered',
1805:'Main campaign army 150000 not national total; E97 III',
1806:'Conflict E97 XVI says160000 incl60000 reserve; do not reconcile or average',
1807:'E97 III Prussia-Poland324000 incl hospitals; approx1/3 allies only this force',
1808:'P08 Jan23 report authorizes80000 of class1809; not annual total',
1809:'E97 XVI 60000 then75550; scope differs from LAV76000; no manufactured total',
1810:'O10 Jan15 author states324996 actually inSpain;262051 present;grand360603 includesFrance/onmarch and column arithmetic discrepancy30;P11 Dec13 authorization not arrivals',
1811:'P11 draft target80000 active+40000 reserve; E97 aggregate167000/90000reserve differs; O11 dateJuly15',
1812:'G03 Russian army600000 >half non-French; E97 horse losses130000-175000; no annual national deaths',
1813:'LAV1140000 is orders incl recalled classes and NationalGuard not incorporated; H72 May >1m explicitly theoretical',
1814:'LAV mentions levée en masse but no annual total; E97 hope300000 not actual'
}
rows=[]
for y,v in zip(range(1803,1815),annual):
    row=dict(year=y,record_type='historical_evidence_not_complete_series',male_cohort_reference=300000,male_cohort_source='H72_pp49_50;1790_95_average_proxy_not_annual_or_full_territory',evasion_rate_national='',evasion_source='RP23_1806_10_department_data;F89;no_national_annual_rate_recovered',annexed_province_incorporated='',annexed_source='H72_cumulative389000_only;no_annual_flow',foreign_independent_allied_flow='',foreign_flow_source='G03_cumulative720000_and_treaty_quotas_only',retirement_flow='',retirement_source='no_national_annual_observation',net_national_force_change='',net_change_source='missing_opening_closing_same_scope',legacy_order_total_reported=v or '',legacy_order_status='LAV_web_transcription_uncalibrated' if v else 'missing',class_quota_reported=classes[y],class_quota_status='LAV_class_year_not_order_year;excludes_unresolved_recall_scope',national_incorporated_actual='',national_incorporated_status='not_recovered',partial_levy_order_date='',partial_levy_deadline='',partial_levy_calls='',partial_levy_arrived='',partial_levy_status='',national_annual_deaths='',national_deaths_status='H72_cumulative_only',force_scope='',force_reported_total='',force_present_low='',force_present_high='',foreign_share_reference='',foreign_share_status='not_recovered',horse_national_stock='',horse_loss_low='',horse_loss_high='',horse_loss_scope='',arms_stock_fusils='',arms_stock_date='',saint_etienne_annual_fusils='',charleville_annual_fusils='',douai_annual_guns='',strasbourg_annual_guns='',essonnes_annual_powder_tonnes='',hardware_status='plant_annual_series_not_recovered;see_F2_hardware_benchmarks.csv',source_ids='LAV;annual_levies_evidence.md',notes=notes[y])
    if y==1805:
        row.update(force_scope='E97_III_main_GrandeArmee_not_national',force_reported_total=150000,source_ids='LAV;E97_III')
    if y==1807:
        row.update(force_scope='E97_III_Prussia_Poland_including_hospitals;not_national',force_reported_total=324000,foreign_share_reference=.333333,foreign_share_status='E97_approx_one_third_allies_not_exact_bound',source_ids='LAV;E97_III')
    if y==1808: row['source_ids']='LAV;P08;E97_XVI'
    if y==1810:
        row.update(force_scope='O10_Spain_1810-01-15_author_explicit_in_country_subtotal_not_national',force_reported_total=324996,force_present_low=262051,force_present_high=262051,source_ids='LAV;P11;P10;O10')
    if y==1811:
        row.update(force_scope='O11_Spain_six_armies_1811-07-15_excludes_Bayonne8298',force_reported_total=354461,force_present_low=286414,force_present_high=291414,source_ids='LAV;P11;O11;E97_XVI')
    if y==1812:
        row.update(force_scope='G03_p26_Russian_campaign_international_army',force_reported_total=600000,foreign_share_reference=.5,foreign_share_status='strictly_more_than_half;not_annual_French_army_share',horse_loss_low=130000,horse_loss_high=175000,horse_loss_scope='E97_XVI_Russian_campaign_all_horses_not_only_cavalry',arms_stock_fusils=811000,arms_stock_date='1812-04-01',source_ids='LAV;G03;E97_XVI;BR25')
    if y==1813:
        row.update(source_ids='LAV;H72;E97_XVI;BR25;G13',partial_levy_order_date='1813-10-09',partial_levy_deadline='1813-12_end',partial_levy_calls=127433,partial_levy_arrived=72265,partial_levy_status='G13_transfer_Leggiere_p69;subset_scope_unreconciled_not_whole_year')
        row['notes']+=';G13 dated subset127433 calls/72265 arrived byDec_end,not_annual_total;see F2_levy_batch_evidence.csv'
    rows.append(row)
with (P/'F2_capacity.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
bench=[
['G01','1812-04-01','Empire_armories','fusils_stock',811000,'','guns','author_report_not_archive_rechecked','BR25','Les usines d armement;Faute de séries','not annual production'],
['G02','1812-04-01/1813-07-01','Empire','new_fusils_15month_total',159000,'','guns','author_report','BR25','same','do not assign entire total to1813'],
['G03','1812-04-01/1813-07-01','Empire','fusils_consomme_15month_total',880000,'','guns','author_report','BR25','same','warehouse issue/use;not all irrecoverable loss'],
['G04','Empire_period_general','Empire','typical_monthly_new_fusils',8000,10000,'guns_per_month','author_estimate_not_annual_observations','BR25','same','annualized96000-120000 is arithmetic not observed'],
['G05','1813_mobilization','Empire','shoulder_arms_monthly_difficult_threshold',18000,'','weapons_per_month','author_estimate_not_hard_limit','BR25','same','broader than fusils;not plant output'],
['A01','1804-09-23/1808-01-01','Metz','cannon_made',279,'','guns','author_report','BR25','Jauger efficacité','39month total;not Douai or Strasbourg'],
['A02','1804-09-23/1808-01-01','Metz','cannon_accepted',211,'','guns','author_report','BR25','same','acceptance differs from manufacture'],
['P01','Empire_period_general','national_civilian_and_military','powder_annual_approx',3000,'','tonnes_per_year','author_estimate_general','BR25','Un élément indispensable','not Essonnes annual output or army allocation'],
['P02','1808','Le_Ripault','daily_powder_potential',800,'','kg_per_day','capacity_not_actual_production','BR25','Toutes ces usines','not Essonnes;cannot multiply365 for actual output'],
['H01','1833-01-01','reported_army_incl_gendarmerie_NAfrica','horses_stock',82057,'','horses','minister_report_via_two_newspapers','R33','Effectif','peace_era_analogy;not1812'],
['M01','1818_law','French_army','authorized_stock',240000,'','persons','legal_target_not_actual','R18','p6','not capacity maximum'],
['M02','1818_law','French_army','usual_annual_call_limit',40000,'','persons_per_year','legal_usual_limit','R18','p6','volunteers and exceptions separate'],
['M03','1833-01-01','army_incl_gendarmerie_foreign_NAfrica','reported_stock',421494,'','persons','reported_actual_not_field_effective','R33','Effectif','not longrun peace average'],
]
heads=['id','period','scope','metric','value_low','value_high','unit','status','source_id','locator','limitation']
with (P/'F2_hardware_benchmarks.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(heads); w.writerows(bench)
assert len(rows)==12 and len(bench)==13
assert all(r['national_incorporated_actual']=='' for r in rows)
print('Wrote12 annual evidence rows and13 benchmark rows; no annual arrivals invented.')
