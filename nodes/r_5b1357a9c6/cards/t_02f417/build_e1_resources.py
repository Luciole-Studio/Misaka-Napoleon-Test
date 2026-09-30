#!/usr/bin/env python3
"""Rebuild E1_resources.csv from cited, read source observations; no interpolation."""
import csv
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[4]  # exam root
OUT = Path(__file__).with_name('E1_resources.csv')
POP = ROOT / 'downloads/E1_OWID_Gapminder_population_1800_1850.csv'
FIELDS = ['record_id','dimension','territory','boundary_basis','year_start','year_end','value_low','value_high','unit','statistic','status','source_ref','locator','quality','notes']
records = []

def add(id, dimension, territory, boundary, y0, y1, lo, hi, unit, statistic, status, source, locator, quality, notes=''):
    assert not any(r['record_id'] == id for r in records), id
    assert lo == '' or (hi != '' and float(lo) <= float(hi)), id
    records.append(dict(zip(FIELDS, [id,dimension,territory,boundary,y0,y1,lo,hi,unit,statistic,status,source,locator,quality,notes])))

# Gapminder/OWID historical population: retrospective modern territory, interpolated.
# UK 1800/1815 withheld because GBR coverage changes from GB toward UK.
COUNTRIES = ['Austria','Belgium','Denmark','Finland','France','Germany','Hungary','Italy','Netherlands','Norway','Poland','Portugal','Russia','Spain','Sweden','Switzerland','Turkey','United Kingdom','United States']
YEARS = {1800,1815,1830,1848}
seen = set()
with POP.open(encoding='utf-8-sig', newline='') as f:
    for row in csv.DictReader(f):
        name, year = row['Entity'], int(row['Year'])
        if name not in COUNTRIES or year not in YEARS or (name == 'United Kingdom' and year in {1800,1815}):
            continue
        key = (name,year)
        assert key not in seen, key
        seen.add(key)
        code = name.upper().replace(' ','_')
        add(f'POP_{code}_{year}', 'population', name, 'retrospective modern statistical geography, NOT 1803 polity', year,year,
            int(row['Population']),int(row['Population']), 'people', 'modelled population estimate', 'IMPUTED_SERIES',
            'downloads/E1_OWID_Gapminder_population_1800_1850.csv', f'Entity={name};Year={year}', 'LOW',
            'Source upstream Gapminder v7/Clio Infra; raw printed precision not observational accuracy; cannot sum modern territories into empires')
assert len(seen) == len(COUNTRIES)*4-2, (len(seen),len(COUNTRIES)*4-2)
for year, count, label in [(1801,10942646,'Great Britain census'),(1811,12590803,'Great Britain census'),
                           (1821,14391631,'Great Britain census'),(1821,21282966,'UK including British Sea Islands'),
                           (1831,24410429,'UK including British Sea Islands'),(1841,27041031,'UK including British Sea Islands'),
                           (1821,6801827,'Ireland enumeration'),(1831,7767401,'Ireland enumeration'),(1841,8175124,'Ireland general return')]:
    terr = 'Ireland' if label.startswith('Ireland') else ('United Kingdom' if label.startswith('UK') else 'Great Britain')
    add(f'PORTER_POP_{terr.replace(" ","_").upper()}_{year}','population',terr,label,year,year,count,count,'people','enumerated persons','HISTORICAL_SOURCE',
        'downloads/E1_Porter_ProgressOfNation_1847.txt','doc 68daef23399c indexed pp.24–28; printed pp.8–11','MEDIUM',
        '1821 UK total includes British Sea Islands; 1841 Ireland general return may differ from separately added army count; Title page confirms 1851 new edition; local download filename misleading')

# Oak, timber, naval material: census, target, receipt and launch are distinct variables.
for vals in [
('OAK_FR_1805','France imperial/communal forests in 1805 census',1805,7337832,'trees >=5 French feet girth','CENSUS','doc 0fd6bd047f2a printed p.7'),
('OAK_FR_PROGRAM_120','Napoleonic program incl other port requirements',1811,543937,'trees required in planning calculation','MODEL_CONTEMPORARY','doc 0fd6bd047f2a printed pp.9–10'),
('OAK_FR_ORDER_1812','France/empire port allocation',1812,225000,'steres ordered, NOT received','ORDER','doc 0fd6bd047f2a printed pp.9–10'),
('OAK_ANTWERP_1812','Antwerp and Holland planned allocation',1812,132000,'steres ordered, NOT received','ORDER','doc 0fd6bd047f2a printed pp.9–10'),
]:
    id, territory, year, v, statistic, status, loc = vals
    add(id,'shipbuilding_timber',territory,'historical political geography',year,year,v,v,'count' if 'trees' in statistic else 'stere',statistic,status,
        'downloads/F3_Todorov_redressement_1810_1813.pdf',loc,'MEDIUM','Todorov cites French archival documents, not independently consulted; stere not solid m3')
for year,v in [(1807,4442),(1808,16729)]:
    add(f'MAST_NA_{year}','shipbuilding_mast','North America to British market','trade flow',year,year,v,v,'masts','masts >12 inches, import/source series','HISTORICAL_SOURCE',
        'downloads/pages/f9c908249692.md',f'Albion 1926 printed p.356, {year} row','MEDIUM','Trade arrivals, not navy dockyard receipt or suitable subset')
add('HEMP_RU_UK_1801','hemp','Russia to Britain','all British imports, not navy',1801,1801,37000,37000,'tons unspecified','Russian hemp imported by Britain','SECONDARY_QUOTED_PRIMARY',
    'nodes/r_b55f2c1cf5/cards/t_104134/manpower/late_supply_addendum.md','Davey 2009 excerpt line 501','MEDIUM','Total UK imports, not navy acquisition; original historical ton definition not checked')
add('HEMP_RUSSIAN_UK_1762_82','hemp','Russia to Britain','share of British imports of hemp, not all raw fibre',1762,1782,95.9,95.9,'percent','18,392/19,172 tons in Davey historical comparison','SECONDARY_QUOTED_PRIMARY',
    'downloads/R2_Davey2009.pdf','doc 9cdc057c893a PDF p.23 / thesis printed p.12','MEDIUM_LOW',
    'Pre-1803 comparison only; author sentence incongruously begins in 1801 then switches to between 1762 and 1782; yearly versus period-total tonnes unspecified; NOT a dated 1808–12 navy figure')
for year,v in [(1807,9),(1808,10),(1809,3),(1810,7),(1811,9),(1812,8),(1813,4)]: 
    add(f'FR_LAUNCH_7YARDS_{year}','ship_launch','seven named French/imperial yard groups','Antwerp Brest Rochefort Lorient Toulon Genoa Venice',year,year,v,v,'ships of the line','minimum identified hulls launched','SECONDARY_COMPILATION',
        'nodes/r_5b1357a9c6/cards/t_b1a536/yards_launches_1807_1813.csv',f'year={year};notes_yards.md','MEDIUM_LOW','Secondhand ship lists; not all yards, not commissioned warships')

# French saltpetre: distinct renewable/requisition stock and import access.
for id,y0,y1,v,label in [('NITRE_FR_1788',1788,1788,1800000,'domestic annual production'),
                         ('NITRE_FR_CRASH',1793,1794,8170000,'Dec 1793 to Dec 1794 6000 shops, short-term leaching output'),
                         ('NITRE_FR_1828',1828,1828,500000,'domestic annual production as reported by Thenard')]:
    add(id,'saltpetre','France','contemporaneous legal territory variable',y0,y1,v,v,'kg',label,'SECONDARY_QUOTED_PRIMARY',
        'downloads/pages/94b41b5822a4.md','Multhauf 1971 printed pp.174–178 / cached lines 80–106','MEDIUM',
        '1794 mostly natural nitrate soil and wall scrapings, NOT artificial nitre beds; 1828 is reported parliamentary estimate')

# Coal/pig iron: retrospective aggregates separate from individual polity and port flows.
# Chaptal reports 2,500,000 metric quintals in a work PUBLISHED in 1794,
# but does not give the observation year. Do not assign this to 1794 in a dated CSV.
add('COAL_FR_1812_14','coal','France','1815 current French boundaries',1812,1814,820000,820000,'metric tonnes/year','three-year mean output','SECONDARY_QUOTED_PRIMARY',
    'downloads/E1_Chaptal1819_industrie_v2.txt','doc a77b035c9087 indexed p.46 / printed pp.112–113 (Cordier)','MEDIUM','8,200,000 metric quintals /10; NOT each individual year')
for window,values in [((1820,1824),{'United Kingdom':17.7,'France':1.1,'Germany':1.2,'Austria':.1}),
                       ((1840,1844),{'United Kingdom':34.2,'France':3.5,'Germany':4.4,'Austria':.52,'Belgium':4.1})]:
    for terr,v in values.items():
        add(f'COAL_{terr.upper().replace(" ","_")}_{window[0]}_{window[1]}','coal',terr,'retrospective country aggregate',*window,v,v,'million metric tonnes/year',
            'five-year average coal and lignite output','SECONDARY_COMPILATION','downloads/pages/360e2a6cb9f5.md','Fordham Tables 3 (from Fontana vol.4 pt.2 appendices)','MEDIUM_LOW','Source compiles Fontana; original statistical appendix not personally read')
for y,v in [(1802,170000),(1806,250000),(1823,442066),(1825,581367),(1828,702584),(1830,653417),(1840,1396400),(1848,2093736)]:
    add(f'PIG_IRON_GB_{y}','pig_iron','Great Britain','reported geography, 1840 excludes Ireland',y,y,v,v,'historical tons unspecified','annual pig iron output/estimate','HISTORICAL_SOURCE',
        'downloads/E1_Porter_ProgressOfNation_1847.txt','doc 68daef23399c indexed pp.276–278 / printed pp.267–270','MEDIUM',
        '1802/1806 official-tax-related estimates; 1823 onward private ironmaster estimates; do not equate tons and metric tonnes')
for terr,v in {'United Kingdom':669,'France':212,'Germany':90,'Austria':85,'Russia':164}.items():
    add(f'PIG_IRON_{terr.upper().replace(" ","_")}_1825_29','pig_iron',terr,'retrospective country aggregate',1825,1829,v,v,'thousand metric tonnes/year','five-year average','SECONDARY_COMPILATION',
        'downloads/pages/360e2a6cb9f5.md','Fordham Table 4 (from Fontana vol.4 pt.2 appendices)','MEDIUM_LOW','Original appendix not personally read')
for y,v in [(1800,5187),(1803,5616),(1806,6863),(1809,6821),(1812,7248),(1813,8166),(1820,7364),(1830,10748),(1848,12870)]:
    add(f'COPPER_CORNWALL_{y}','copper','Cornwall','county, NOT Britain',y,y,v,v,'historical tons unspecified','annual copper mine output','HISTORICAL_SOURCE',
        'downloads/E1_Porter_ProgressOfNation_1847.txt','doc 68daef23399c indexed pp.280–281 / printed pp.271–272','MEDIUM','Copper mined, not copper naval usable or received')
for y,v in [(1820,8127),(1830,13232)]:
    add(f'COPPER_UK_{y}','copper','United Kingdom','all mines, pre-1820 not reported',y,y,v,v,'historical tons unspecified','annual copper mine output','HISTORICAL_SOURCE',
        'downloads/E1_Porter_ProgressOfNation_1847.txt','doc 68daef23399c indexed p.281 / printed p.272','MEDIUM','After 1834 smelted imported ore hard to separate; do not extrapolate to 1803')

# Livestock: national headcounts vs working agricultural livestock.
for id,y0,y1,v,unit,label in [
('HORSE_FR_130_DEPTS_1813',1813,1813,3500011,'horses','Feb 25 census total of 130 departments'),
('HORSE_FR_YOUNG_1813',1813,1813,837581,'horses','under four years, part of census'),
('HORSE_FR_FOALS_1813',1813,1813,280320,'foals/year','reported annual births'),
('HORSE_FR_REMONTS_1812_13',1812,1813,212671,'horses','Nov 1812 to Dec 1813 depot-processed acquisitions'),
('HORSE_FR_PURCHASE_1813',1813,1813,81918,'horses','state purchase subset (not additive to depot count)'),
('HORSE_FR_DRAUGHT_PURCHASE_1813',1813,1813,67704,'horses','draught subset of state purchase'),
('HORSE_FR_REMOUNT_LOSS_1814',1812,1814,182212,'horses','no longer in acquired pool by Apr 6 1814, NOT mortality count')]:
    add(id,'horse','French 130 departments' if 'DEPTS' in id or 'YOUNG' in id or 'FOALS' in id else 'French army remount system',
        'imperial census boundary' if 'DEPTS' in id or 'YOUNG' in id or 'FOALS' in id else 'army multi-region procurement',y0,y1,v,v,unit,label,
        'SECONDARY_QUOTED_PRIMARY','downloads/pages/f3c3e5561ee4.md','Dawson 2013 cached lines 20–60/604–610','MEDIUM_LOW','Dawson cites AN/SHD not personally checked; counts overlap and window differs')
for terr,horses,oxen in [('England and Wales',700000,78000),('France',1560000,1702000),('Germany at 1873 borders',1656000,1924000),('Netherlands',142000,''),('Sweden',280000,278000)]:
    key = terr.upper().replace(' ','_')
    add(f'AG_HORSE_{key}_1815','horse_agricultural',terr,'historical boundary except projected German 1873 border',1815,1815,horses,horses,'working agricultural horses',
        'agricultural draught horse estimate','RECONSTRUCTION','downloads/E1_WardeKander2009_draught_animals.pdf','doc 3cbbd254460a PDF pp.3,6,9–12; numbers in thousands converted ×1000','MEDIUM_LOW',
        'Authors use 1812/Montalivent, 1791/Lavoisier shares for France; Germany extrapolated; NOT entire horse census or military surplus')
    if oxen != '':
        add(f'AG_OX_{key}_1815','oxen_agricultural',terr,'same reconstructed boundary as horse row',1815,1815,oxen,oxen,'oxen/cows or oxen as table labeled',
            'working agricultural bovine estimate','RECONSTRUCTION','downloads/E1_WardeKander2009_draught_animals.pdf','doc 3cbbd254460a PDF pp.3,6,9–12','MEDIUM_LOW',
            'Original PDF p.9 image confirms 78k oxen; its horse-equivalent column reports 700k horses without converting oxen, an internal inconsistency; do not add unadjusted' if terr == 'England and Wales' else 'Germany combines oxen and cows; France oxen distinct')

# Black Sea port volume is neither Russian national wheat output nor France-accessible inventory.
# This workbook omits its YEAR column: human-readable companion page confirms
# 1812=worksheet row6, 1830=row24, 1848=row42. Empty cells and 0 are distinct.
ODESSA = ROOT / 'downloads/E1_BlackSea_Odessa_exports_imports.xlsx'
ws = load_workbook(ODESSA,read_only=True,data_only=True).active
assert round(float(ws['C6'].value)) == 36718 and round(float(ws['C24'].value)) == 78248 and round(float(ws['C42'].value)) == 254094
for y in range(1812,1849):
    v = ws.cell(row=y-1806,column=3).value
    if v is None or (isinstance(v,str) and not v.strip()):
        continue
    v = round(float(v))  # source unit conversion generates spurious decimals
    add(f'ODESSA_WHEAT_EXPORT_{y}','grain_wheat_export','Odessa','Russian Black Sea port; commercial output only',y,y,v,v,'metric tonnes','annual wheat export through port','COMPILED_HISTORICAL_SERIES',
        'downloads/E1_BlackSea_Odessa_exports_imports.xlsx',f'worksheet Φύλλο1 cell C{y-1806}; web page cities.blacksea.gr/en/odessa/5-7/ gives year; source docx section 1 Russia and section 2 units','MEDIUM_LOW',
        'Source conversions create false decimal precision; absent years not zeros; traders/transit/Bosporus/naval control determine France-accessible fraction; underlying Obzor not personally checked')

# Climate and epidemic: event/model estimands must not be converted into all-European totals.
add('POTATO_SWISS_SIM_1816','crop_model','Switzerland','modern 2km grid model with modern varieties',1816,1816,20,50,'percent potential yield reduction','potato potential yield loss','MODEL_NOT_OBSERVATION',
    'downloads/E1_Flueckiger2017_TamboraCrop.pdf','doc a14dba75fdb5 PDF pp.1–3','MEDIUM','CropSyst weather counterfactual not historical observed yield')
add('CHOLERA_VILNIUS_1831_CASES','cholera','Vilnius city','historical municipal reporting',1831,1831,3706,3706,'people sick','reported cholera cases','HISTORICAL_SOURCE_RECONSTRUCTION',
    'downloads/E1_Vilnius1831_cholera_hospital.pdf','doc e10cbcde9735 PDF pp.3–4 / journal pp.77–78','MEDIUM','Apr 5 to Dec 18; concealment and population uncertainty')
add('CHOLERA_VILNIUS_1831_DEATH','cholera','Vilnius city','historical municipal reporting',1831,1831,1772,1772,'deaths','reported cholera deaths','HISTORICAL_SOURCE_RECONSTRUCTION',
    'downloads/E1_Vilnius1831_cholera_hospital.pdf','doc e10cbcde9735 PDF pp.3–4 / journal pp.77–78','MEDIUM','Case fatality 47.8%; not all-population death rate')

add('EMIGRANT_WUERTT_1816_17','migration','Württemberg','historical kingdom',1816,1817,17500,17500,'people','outward emigrants during 1816/17 (peak year)','SECONDARY_COMPILATION',
    'downloads/pages/f8b5b8268f1c.md','Glaser et al. 2017 web text L164; article cites official statistics','MEDIUM_LOW',
    '1815/16–1817/18 cumulative 22630; do not transplant figures into S5 without accounting for end of Napoleonic war and routes')
with OUT.open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, FIELDS)
    writer.writeheader()
    writer.writerows(records)
print(f'{OUT}: {len(records)} rows; population {len(seen)} OWID four-point rows and 9 Porter rows')
