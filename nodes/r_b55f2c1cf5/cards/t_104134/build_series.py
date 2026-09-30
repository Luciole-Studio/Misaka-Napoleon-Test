"""Consolidate checked extracts; no interpolation or estimation. Run from project root."""
from pathlib import Path
import csv
B=Path('nodes/r_b55f2c1cf5/cards/t_104134')
fields=['series','year','time_scope','geography','ship_class','metric','value_low','value_high','unit','sea_commission','sea_ordinary','harbour_commission','harbour_ordinary','building_ordered_low','building_ordered_high','source','locator_all_numeric_fields','check_source','source_file','quality','caveat']
rows=[]
def get(p):
    return list(csv.DictReader((B/p).open()))
def add(**kw):
    assert not set(kw)-set(fields)
    rows.append(kw)
for r in get('naval/UK_1803_1805.csv'):
    add(series='naval_stock',year=r['year'],time_scope=r['snapshot'],geography=r['country'],ship_class=r['ship_class'],metric='mutually_exclusive_status_columns',unit='ships',sea_commission=r['sea_commission'],sea_ordinary=r['sea_ordinary'],harbour_commission=r['harbour_commission'],harbour_ordinary=r['harbour_ordinary'],building_ordered_low=r['building_or_ordered'],building_ordered_high=r['building_or_ordered'],source=r['source'],locator_all_numeric_fields=r['locator'],check_source='FremontBarnes2007_reproduction_only' if r['ship_class']=='line' and r['year'] in ['1803','1805'] else '',source_file='naval/UK_1803_1805.csv',quality=r['status'],caveat='commission_mixes_at_sea_and_fitting;ordinary_not_immediately_ready;all_cruisers_includes_line')
for r in get('naval/mobilisation_1803.csv'):
    add(series='mobilisation_anchor',year=r['date'][:4],time_scope='before_1803-05-01' if r['date']=='1803-05-01' else r['date'],geography=r['country'],ship_class='line',metric='sea_or_fitting_mixed_in_commission',sea_commission=r['value'],unit=r['unit'],source=r['source'],locator_all_numeric_fields=r['locator'],source_file='naval/mobilisation_1803.csv',quality='single_source_anchor_not_monthly_series',caveat=r['caveat']+';overlaps_year_start_stock_do_not_sum')
for r in get('france/observations.csv'):
    add(series='French_port_observation',year=r['year'],time_scope=r['time_scope'],geography=r['place'],ship_class='line_or_two_decker_as_metric',metric=r['metric'],value_low=r['low'],value_high=r['high'],unit=r['unit'],source=r['source'],locator_all_numeric_fields=r['locator'],source_file='france/observations.csv',quality='single_source_not_frozen',caveat=r['caveat']+(';1837_volume_number_not_independently_verified' if r['year']=='1811' else ''))
for r in get('fiscal/cotton_1808_1812.csv'):
    for m in ['cotton_manufactures','cotton_yarn']:
        add(series='cotton_export',year=r['year'],time_scope='year_end_unknown',geography=r['geography'],metric=m,value_low=r[m],value_high=r[m],unit=r['unit'],source=r['main_source'],locator_all_numeric_fields='Heckscher1922_p246;Ogawa2020_p36_table1',check_source=r['check_source'],source_file='fiscal/cotton_1808_1812.csv',quality=r['status'],caveat='not_current_price_receipts;underlying_customs_return_unread')
for r in get('fiscal/war_taxes_1804_1809.csv'):
    for m in ['customs_excise_war_taxes','property_tax','reported_total']:
        add(series='war_taxes',year=r['year_end'][:4],time_scope=r['year_end'],geography=r['geography'],metric=m,value_low=r[m],value_high=r[m],unit=r['unit'],source=r['source'],locator_all_numeric_fields=r['locator'],source_file='fiscal/war_taxes_1804_1809.csv',quality=r['status'],caveat='war_taxes_only;total_is_reported_not_recalculated;not_all_revenue')
for r in get('manpower/borne_1793.csv'):
    add(series='manpower',year=r['year'],time_scope=r['time_scope'],geography='British_navy',metric=r['metric'],value_low=r['value'],value_high=r['value'],unit=r['unit'],source=r['source'],locator_all_numeric_fields=r['locator'],source_file='manpower/borne_1793.csv',quality='retrospective_single_source_not_frozen',caveat=r['quality'])
for r in get('manpower/prisoners.csv'):
    add(series='prisoners',year=r['report_date'][:4],time_scope='reported_'+r['report_date'],geography=r['geography'],metric=r['category'],value_low=r['value'],value_high=r['value'],unit=r['unit'],source=r['source'],locator_all_numeric_fields=r['locator'],source_file='manpower/prisoners.csv',quality='single_source_scope_limited',caveat=r['scope_limit'])
with (B/'c2_series.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fields); w.writeheader(); w.writerows(rows)
assert len(rows)==53,len(rows)
for r in get('naval/UK_1803_1805.csv'):
    assert int(r['sea_commission'])+int(r['sea_ordinary'])==int(r['sea_total'])
    assert sum(int(r[k]) for k in ['sea_commission','sea_ordinary','harbour_commission','harbour_ordinary','building_or_ordered'])==int(r['grand_total'])
print('53 observations consolidated; six naval status reconciliations passed; no missing value imputed.')
