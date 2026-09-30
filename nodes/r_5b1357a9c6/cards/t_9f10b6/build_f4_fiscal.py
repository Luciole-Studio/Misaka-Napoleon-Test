"""Build F4_fiscal.csv. All observations are manual source transcriptions.
No interpolation of missing historical cells. Models are separately tagged.
Run from project root: python3 nodes/r_5b1357a9c6/cards/t_9f10b6/build_f4_fiscal.py
"""
import csv
from pathlib import Path
P = Path(__file__).resolve().parent
rows=[]
cols=['id','record_type','scenario','period','territory','series','value','low','high','unit','basis','source_id','locator','formula','notes']
def add(kind,period,series,value=None,low=None,high=None,basis='',src='M',loc='',note='',scenario='S0',territory='法国当时疆域；逐年变化',unit='百万法郎',formula=''):
    rows.append(dict(zip(cols,[f'F4-{len(rows)+1:03d}',kind,scenario,str(period),territory,series,value,low,high,unit,basis,src,loc,formula,note])))
def hist(period,series,v,basis,loc,note=''):
    add('文献转录',period,series,v,basis=basis,loc=loc,note=note)
# Tax series: French republican financial years are NOT calendar years.
periods=['An XI','An XII','An XIII','An XIV-1806','1807','1808','1809','1810','1811','1812','1813','1814']
seriesdata={
 'droits_reunis_net':{'An XIII':26.640,'1807':85,'1808':90,'1809':111.844,'1810':116,'1811':128.241,'1812':144},
 'customs_net':{'An XI':36.924,'An XII':41.485,'An XIII':52.725,'An XIV-1806':60.800,'1807':60.400,'1808':18.559,'1809':11.552,'1810':35.881,'1811':79.3},
 'tobacco_manufacturing_retail_duties':{'An XII':3.740713,'An XIII':8.362903,'1807':13.353495,'1809':18.177424,'1810':21.126745},
 'registration_stamp_forests_gross':{'An XIII':202.703,'An XIV-1806':244.761,'1807':225,'1808':230.882,'1809':260.161,'1810':245.900,'1811':238.100,'1812':253.040},
 'direct_tax_principal_and_centimes_collected':{'An XII':371,'1807':372.480170,'1809':386.881472,'1810':386},
}
locs={'droits_reunis_net':'p305/PDF325','customs_net':'p306/PDF326','tobacco_manufacturing_retail_duties':'p302/PDF322','registration_stamp_forests_gross':'pp304-305/PDF324-325','direct_tax_principal_and_centimes_collected':'p309/PDF329'}
for s,d in seriesdata.items():
    for per in periods:
        note='An XIV-1806为15个月；税制和疆域变化；禁止将各组自动相加。'
        basis={'droits_reunis_net':'作者所列净产品；税种范围历次变化','customs_net':'作者所列关税净产品','tobacco_manufacturing_retail_duties':'烟草制造/零售税；不含进口关税及阿尔卑斯外烟草','registration_stamp_forests_gross':'登记/印花/森林毛产品','direct_tax_principal_and_centimes_collected':'作者称实收；含本金和附加税；非中央直接税预算同口径'}[s]
        if s=='customs_net':
            if per=='1810': note+='此格仅普通关税；另列非常关税61.046。'
            if per=='1811': note+='原文未拆普通与非常，不纳固定疆域经常税校准。'
        if s=='tobacco_manufacturing_retail_duties' and per in ['1811','1812','1813','1814']: note+='1811起专卖制，不能机械续接此税项。'
        add('文献转录' if per in d else '缺测',per,s,d.get(per),basis=basis,loc=locs[s],note=note)
for per,v in [('An XIII',53.490825),('An XIV-1806',74),('1807',107.5),('1808',117),('1809',144),('1810',145),('1811',168)]:
    hist(per,'droits_reunis_gross',v,'毛产品', 'p305/PDF325','An XIII作者脚注疑53m应为33m，保留原值且不用作模型；1811为概数。')
for per,v in [('An XIV-1806',34.233296),('1807',71.083080),('1808',75.598420),('1809',97.4563),('1811',105.5),('1812',116.331)]:
    hist(per,'drink_duties',v,'酒类税产出；属于droits reunis子项','pp300-301;305/PDF320-321;325','不得与droits_reunis再加总')
for per,v in [('An XIV-1806',24.258),('1807',21.579),('1808',19.365),('1809',20.489),('1810',25.454)]:
    hist(per,'tobacco_duties_including_customs',v,'烟草两类税合计；不含阿尔卑斯外','p302 n1/PDF322','与制造零售系列为交叉范围，不加总；叙述与脚注进口税差额并非各年均4-5m。')
hist('1809','tobacco_transalpine',6.305375,'阿尔卑斯外烟草另项','p302 n1/PDF322')
hist('1812','tobacco_monopoly_total',43,'专卖总收益；作者另列费用26','p304 n1/PDF324','不是净上缴43；口径已变')
hist('1812','tobacco_monopoly_costs',26,'费用','p304 n1/PDF324')
add('算术','1812','tobacco_monopoly_net_arithmetic',17,basis='43-26；由作者数计算，不是原表独立格',loc='p304 n1/PDF324',formula='43-26')
hist('1810','customs_extraordinary',61.046,'非常关税产品；包括库存重税/许可证/没收','p306/PDF326','影像校核为61.046而非OCR61.040')
hist('1810-08至1812-01-01','customs_extraordinary_cumulative',105.927667,'累计；不是1811年度经常收入','p306/PDF326')
hist('1810年7月法令后4个月','customs_extraordinary_first_four_months',53.622620,'荷兰40%/50%库存税、许可证、没收货物拍卖等合计','p306/PDF326','一次性库存性质；不可逐年重征同一批货')
add('算术','1811','customs_extraordinary_implied',105.927667-61.046,basis='累计减1810年度非常关税；假设非常制度1810-07/08才起步，故日历年1810非常额约等于8–12月部分',loc='p306/PDF326',formula='105.927667-61.046',note='推算值，原文未列此格；累计期至1812-01-01含1811全年')
add('算术','1811','customs_ordinary_implied',79.3-(105.927667-61.046),basis='1811总79.3减推算非常额',loc='p306/PDF326',formula='79.3-(105.927667-61.046)',note='结果约34.4，与1810普通关税35.881同量级，可作一致性交叉检验；仍是推算不是原表')
for per,v in [('An XIII',172.763591),('1808',180.869),('1810',192.635)]:
    hist(per,'registration_stamp_domains_net_rights',v,'净权利/账期（exercice）应收，不等于当年现金','p305 n1/PDF325','图像核读：脚注区分par année与par exercice，两数同属An XIII，非年份混写')
hist('1810账期截至1811-04-01','registration_stamp_domains_cash',179.634,'截至日期现金到账','p305 n1/PDF325')
hist('An XIII当年12个月','registration_stamp_domains_cash',149.627795,'年度现金；不是账期应收','p305 n1/PDF325','原文：pour l’an XIII c’était 172.763.591 pour l’exercice, mais seulement 149.627.795 encaissés pendant les 12 mois')
add('算术','An XIII','registration_cash_to_exercise_ratio',149.627795/172.763591*100,basis='十二个月现金÷账期权利；账期长于十二个月，因此不等于欠缴率',loc='p305 n1/PDF325',unit='%',formula='149.627795/172.763591*100',note='只证“账面收入≠当年可用现金”，不得移植到其他税种或年份')
# Two benchmark budgets; source explicitly says previsons.
bench=[('direct_taxes',301.5,340.696),('registration_domains_forests',185,206),('customs_and_salt',46,150),('droits_reunis_and_tobacco',25,220),('lottery',14,15),('post',10,12),('eastern_saltworks',3,3),('external_receipts',30,30),('communal_asset_sales_levy',0,149),('total_including_misc',684,1150)]
for s,a,b in bench:
    for per,v in [('An XIII',a),('1813',b)]:
        add('预算',per,'budget_'+s,v,basis='预期预算；非实收',loc='p322/PDF342 image checked',note='An XIII直接税301.5m为原扫描；不用网页311m。0只指本预算行未列，不指无任何资产售卖。')
for s,v in [('customs',100),('salt',50),('droits_reunis',150),('tobacco',70)]:
    add('预算','1813','budget_detail_'+s,v,basis='1813-03-20预算',loc='p362 n3/PDF382',note='是上述合并项目拆分；不再次相加')
hist('1810','land_tax_principal_total',208.561472,'应分摊本金','p307/PDF327')
hist('1810','land_tax_principal_new_france',35.648,'新并合地区分摊本金','p307/PDF327')
add('算术','1810','land_tax_principal_old_france',208.561472-35.648,basis='总额减新地区；非实际收款',loc='p307/PDF327',formula='208.561472-35.648')
# Official budgets and their known incomparabilities.
for per,v in [('An XIII',684),('An XIV-1806',986),('1807',720),('1808',772),('1809',786),('1810',795),('1811',954),('1812',1030),('1813',1150)]:
    add('预算或作者引述总额',per,'published_revenue_total_mixed',v,basis='Gaudin总额引述/1811以后预期；不等于固定疆域经常实收',loc='pp320-322/PDF340-342',note='An XIV-1806=15个月；不用于年度贡赋依赖比；页321影像修正OCR980→986、780→786')
for per in ['1804','1805','1806','1807','1808','1809','1810','1811','1812','1813','1814']:
    add('缺测',per,'comparable_annual_extraordinary_share_all_resources',basis='严格相同边界的年度全资源贡赋比未形成',src='BR;M',loc='BR p14附表;M pp315-324',unit='%',note='缺失不等于0；共和历与15个月会计期不能强配公历年。')
for per,v in [('An XIV-1806',390.563257),('1807',321.4),('1808',335.529),('1809',340.149),('1810',350),('1811',460),('1812',520),('1813',585)]:
    add('拨款',per,'army_credits_legal',v,basis='军务和军政两部法定拨款；不含盟军等全经济成本',loc='p324/PDF344 image checked')
for per,v in [('An XIV-1806',434.072),('1807',343.549),('1808',378.328),('1809',398.286),('1810',379.064),('1811',506.096),('1812',558),('1813',673)]:
    add('回溯性转引',per,'army_credits_Mollien',v,basis='Mollien回忆录所列拨款，与法律列不同',loc='p324/PDF344 image checked',note='不能平均两列制造唯一值')
for per,v in [('An XII',180),('An XIII',140),('1811',155),('1812',159),('1813',167)]:
    add('预算量级',per,'navy_budget',v,basis='Marion紧接拨款段所列量级；不是船舶单价',loc='p325/PDF345')
add('预算量级','1806-1810','navy_budget_range',low=105,high=110,basis='作者概括各年范围',loc='p325/PDF345')
add('预算','1810-07-26','army_sovereignty_baseline',350,basis='皇帝罗马分摊计算的全帝国基准',src='C-JUL',loc='1810-07-26财务会议')
add('预算','1810-07-26','navy_sovereignty_baseline',100,basis='同上',src='C-JUL',loc='1810-07-26财务会议')
add('计划','1810-06-06','ordinary_revenue_projection',low=710,high=720,basis='普通收入概算；Tuscany含入、Rome/Illyria另列',src='C-JUN',loc='1810-06-06 notes §§7,11')
# Branda: mutually exhaustive appendix rows, NOT annual budget.
components=[('french_indirect_contributions',1272),('property_sales_deductions',224),('special_customs',137),('additional_centimes',62),('deposits',69),('civil_list_loans',95),('ordinary_foreign_contributions',809),('extraordinary_domain_loans',154),('treaty_external_revenue',453),('allied_savings',383),('unpaid_expenditure',503),('private_institution_loans',123)]
for s,v in components:
    add('作者重建','1803-1814','extra_war_finance_'+s,v,basis='额外战争融资分类；名义累计',src='BR',loc='p14附表：Details of extraordinary financing',note='计入节省不是收到现金；内部贷款不是新财富；原文不同段有舍入或排印差异，依能配平附表。')
assert sum(v for s,v in components)==4284
for s,v in [('grand_total',4284),('french_treasury_subtotal',1859),('war_subtotal',1799)]:
    add('作者重建','1803-1814','extra_war_finance_'+s,v,basis='附表分类总数；非全部军费',src='BR',loc='p14附表')
add('算术','1803-1814','extra_war_finance_war_share',1799/4284*100,basis='附表1799/4284',src='BR',loc='p14附表',unit='%',formula='1799/4284*100')
for per,v in [(1805,8.8242),(1806,23.259980),(1807,18.827825),(1808,10.668783),(1809,56.768065),(1810,24.748825),(1811,14.890360),(1812,60.072365),(1813,35.687777)]:
    add('作者模型',per,'allied_contingent_avoided_cost',v,basis='战役兵日×1.91法郎；法国避免的开支非实收',src='BR',loc='p13盟军兵日表',note='Mollien700/年经二手转引；1812按作者战役日设定，不认作全年度维持成本')
# Assessments, receipts including kind, and remittances are separate series.
for per,s,v,b in [
    ('1805','austria_collected_including_material',75.473655,'收得含缴获物资，不是全现金'),
    ('1805','austria_remitted_to_france',48.428,'带回法国额，非全部索赔'),
    ('1809','austria_assessed',250,'索取额'),
    ('1809','austria_collected',164.488675,'作者收得额'),
    ('1809','austria_spent_locally',76,'原文圆整数，不强制配平'),
    ('1809','austria_remitted_to_france',88,'原文圆整数，不强制配平'),
    ('1807','portugal_assessed',100,'索取额'),
    ('1807','portugal_collected',6,'收得额')]:
    add('文献转录',per,s,v,basis=b,src='M',loc='pp317-319/PDF337-339',territory='外国贡赋；现金和实物按各行区分',note='经Marion转La Bouillerie账；不得再加到Branda累计表')
# Debt/pensions/endowments and regional anchors.
for per,s,v,basis,loc in [('1807','debt_and_pensions',105.9,'年度预算负担','p325/PDF345'),('1811','debt_and_pensions',148,'年度预算负担含荷兰','p325/PDF345'),('1811','dutch_rentes_service',26,'三分之一化后年度息额，不是本金','p325/PDF345'),('1813-01-01','pensions_total',46.518996,'年度养老金，非赠产年租','p325/PDF345'),('1809-12-21','rentes_annual_inscribed',56.730583,'年度票息，不是债务本金','p343/PDF363'),('1809-12-21','rentes_private_french',32.927267,'年度票息份额','p343/PDF363'),('1809-12-21','rentes_foreign_holders',5,'年度票息概数','p343/PDF363')]:
    hist(per,s,v,basis,loc)
add('文献转录','1814-07','endowment_top_group_income',18,basis='1814表中约600名年收益>4000法郎者合计；与1810年初全体者18m是不同群体的同数值',src='SG',loc='p683',note='不得将两个18视作同一序列或相加')
add('文献转录','1809-08','endowment_annual_income',15.165,basis='1809年8月全体赠产年收益',src='SG',loc='p683')
add('文献转录','1810-01','endowment_annual_income',18,basis='原文超过18m；不是总养老金',src='SG',loc='p683',note='下限；4035受益人')
add('算术','1814-07','endowment_reconstructed_annual_income',3500*.0005+950*.002+770*.004+18,basis='分层数重建约24.73m；非精确审计总额',src='SG',loc='p683',formula='3500*0.0005+950*0.002+770*0.004+18')
add('计划','1812','annexed_receipts_gross',342.260044,basis='所有1792以来并合地预期毛额',loc='p321/PDF341 image checked')
add('计划','1812','annexed_receipts_net',226.389345,basis='原文nets；扣项未全部分解，非财政利润',loc='p321/PDF341 image checked')
# Regional components of the 1812 expected annexed receipts (Marion p321, citing AF IV 1072).
_reg=[('比利时',83),('荷兰',66.5),('汉萨各部',38.791),('莱茵各部',37.5),('皮埃蒙特',33),('托斯卡纳',22.5),('利古里亚',16),('罗马国家',16.5)]
for terr,v in _reg:
    add('计划','1812','annexed_receipts_component',v,basis='1812预计1030m总收入中该地区份额；原文未逐项声明毛或净',loc='p321/PDF341 image checked',territory=terr,note='八项加总313.791，小于毛342.260044且原文尚有etc.，故更可能属毛口径；不得当作净上缴巴黎或实收。')
add('算术','1812','annexed_receipts_components_sum',sum(v for _,v in _reg),basis='八个列名地区相加；原文另有etc.未列项',loc='p321/PDF341',formula='83+66.5+38.791+37.5+33+22.5+16+16.5',note='用于判断分项属毛口径，不是原表合计格')
# Gaudin 30 April 1811: extra revenue expected from the most recent annexations.
for terr,v in [('荷兰',55),('Bouches-du-Rhin/Escaut/Bréda',7),('三个汉萨部',20),('伊利里亚',10),('Rome/Trasimène',12.5)]:
    add('计划','1811-04-30','gaudin_recent_annexation_extra_revenue',v,basis='Gaudin报告最近并合地可预见增收，全部合计“105万万至多”',loc='p321/PDF341 image checked',territory=terr,note='预见增收非已实收；五项加总104.5，与“至多105”一致。同页巴卡Simplon税收连行政费用都不够。')
add('计划','1810-07-25','Dutch_debt_service_anticipated',28,basis='皇帝问Mollien概算；与Marion列出的年度债息26不同',src='C-JUL',loc='致Mollien',territory='荷兰')
add('计划','1810-07-25','Dutch_army_navy_anticipated',32,basis='10m荷兰盾陆军+6m海军，原信近似×2',src='C-JUL',loc='致Mollien',territory='荷兰')
for s,v in [('Roman_gross_claim_rejected',15.9),('Roman_municipal_cost_to_deduct',3),('Roman_population_in_imperial_calculation',.8),('Roman_sovereignty_target',8)]:
    add('计划','1810-07',s,v,basis='帝国目标/批评，不是当地实绩',src='C-JUL',loc='7-22/7-26财政会议',territory='Rome/Trasimene',unit='百万人' if s.endswith('calculation') else '百万法郎')
add('算术','1810-07-26','sovereignty_per_million_population',496.5/37,basis='原文舍入为14；这里精确除法',src='C-JUL',loc='罗马财政会议',unit='百万法郎/百万人',formula='496.5/37')
for s,v in [('population',1.5),('budget',13.5),('army_navy_cost',9.9)]:
    add('文献转录','1809-1813地区概况' if s=='population' else '1812','Illyria_'+s,v,basis='Grab地区人口量级非1812普查；预算不是收入',src='GR',loc='pp188,191',territory='伊利里亚',unit='百万人' if s=='population' else '百万法郎')
# S6 threshold table: imperial allocation TARGETS vs whatever can be checked. Targets are not receipts.
for terr,s,v,src,loc,b in [
    ('Rome/Trasimène','s6_target_sovereignty_share_gross',11,'C-JUL','1810-07-26会议','80万人×每百万约14m的目标分摊'),
    ('Rome/Trasimène','s6_target_net_after_local_charges',8,'C-JUL','1810-07-26会议','扣民用表1.5与教目支出1.2后的目标净额'),
    ('Rome/Trasimène','s6_gaudin_expected_increment',12.5,'M','p321/PDF341','Gaudin 1811-04-30可预见增收'),
    ('Rome/Trasimène','s6_marion_1812_component',16.5,'M','p321/PDF341','1812并合地预计份额，推断为毛'),
    ('荷兰','s6_target_threshold_total',60,'C-JUL','1810-07-25致Mollien','债息28+陆海约32的粗列门槛'),
    ('荷兰','s6_target_debt_service',28,'C-JUL','1810-07-25致Mollien','三分之一化(tiercement)后的年息测算目标'),
    ('荷兰','s6_marion_debt_annuity_after_tiercement',26,'M','p325/PDF345','削至三分之一后的年金额，原为78；非本金'),
    ('荷兰','s6_gaudin_expected_increment',55,'M','p321/PDF341','Gaudin可预见增收'),
    ('荷兰','s6_marion_1812_component',66.5,'M','p321/PDF341','1812份额，推断为毛'),
    ('汉萨各部','s6_gaudin_expected_increment',20,'M','p321/PDF341','Gaudin可预见增收'),
    ('汉萨各部','s6_marion_1812_component',38.791,'M','p321/PDF341','1812份额，推断为毛'),
    ('伊利里亚','s6_gaudin_expected_increment',10,'M','p321/PDF341','Gaudin可预见增收'),
    ('伊利里亚','s6_checked_expenditure_1812',13.5,'GR','pp188,191','Grab报告预算支出，其中军海9.9；收入长期不敷'),
    ('托斯卡纳','s6_marion_1812_component',22.5,'M','p321/PDF341','已1810年6月计入普通贡献'),
    ('Simplon','s6_checked_shortfall_flag',None,'M','p321/PDF341','原文：税收连行政费用都不够；并入理由为对意交通'),
    ('加泰罗尼亚','s6_checked_any',None,'MODEL','待D2','本卡未取得任何可核数；缺测不是零')]:
    add('计划' if v is not None else '缺测','1810-1812',s,v,basis=b,src=src,loc=loc,territory=terr,scenario='S6',note='帝国分摊目标/预计，**目标非实收**；可核实收待D2以当地账簍填入')
add('算术','1810-07-26','s6_target_per_million_exact',496.5/37,basis='主权费496.5÷3700万人；文书自取整为14',src='C-JUL',loc='罗马财政会议',unit='百万法郎/百万人',scenario='S6',formula='496.5/37',note='D2/P2应以各地人口乘此得目标，再减当地民政/驻军/旧债得净得')
# F5 interface: displayed price of elite compensation, and the notable income distribution.
for per,s,v,u,src,loc,b in [
    ('1803-1814','senator_annual_salary',25000,'法郎/人年','LZ','Lentz网页正文','帝国元老年俸，另有sénatoreries及勋章'),
    ('an IX-1810','senatorerie_count',36,'处','LZ','附录2','初31处，经1806/1808/1810数波至36；每处年入2–2.5万法郎'),
    ('1814-04/05','bourbon_pension_per_senator',36000,'法郎/人年','LZ','Lentz网页正文','复辟实付的继承价；另84名元老入贵族院'),
    ('1814-04/05','bourbon_peers_from_senate',84,'人','LZ','Lentz网页正文','同上'),
    ('1803-1814','notable_income_share_500_5000',75,'%','BCN','Perseé书评','显贵电子名册分析：75%收入在19500–5000法郎区间'.replace('19500','500'))]:
    add('文献转录',per,s,v,unit=u,basis=b,src=src,loc=loc,note='经二手网页/书评转述，原档未阅；用于补偿池量级对照，不作预算实支')
# Restoration comparison: NOT directly appended to Napoleonic net budgets.
rest=[(1816,729,-19,9.10),(1817,879,81,10.44),(1818,900,-20,13.54),(1819,938,41,18.66),(1820,895,33,18.44),(1821,933,26,18.64),(1822,928,1,18.86),(1823,933,-75,19.59),(1824,919,3,20.52),(1825,960,-3,20.12),(1826,979,6,19.84),(1827,983,-38,20.84),(1828,948,5,20.45),(1829,978,7,20.36),(1830,992,-124,21.01),(1831,971,-270,21.71),(1832,949,-189,21.62),(1833,985,-144,22.02),(1834,990,-56,18.25),(1835,1008,-26,18.12)]
for yr,rev,bal,interest in rest:
    for s,v,u in [('fiscal_revenue',rev,'百万法郎'),('balance',bal,'百万法郎'),('debt_interest_share_expenditure',interest,'%')]:
        add('二手数据转录',yr,'restoration_'+s,v,basis='EHES表1转Mitchell/Vaslin；1818会计毛净变更不得机械接帝国',src='OUV',loc='Table1 print41/PDF42',territory='复辟/七月王朝法国',unit=u)
for per,s,v in [('1836','army_navy',267),('1846','army_navy',495),('1836','public_works',65),('1846','public_works',217)]:
    add('后出统计转录',per,'Juglar_'+s,v,basis='普通+特别支出；各项范围见原文',src='J',loc='p308/PDF4',territory='当年法国')
add('后出叙述','1823','rente_5pct_issue_price',89.55,basis='发行价；不是票息5%即市场利率',src='LB',loc='section I',unit='每100面值法郎',territory='复辟法国')
add('算术','1823','rente_5pct_current_yield',5/89.55*100,basis='简化当期收益率；不含佣金/支付时间/转换权',src='LB',loc='section I',unit='%',formula='5/89.55*100',territory='复辟法国')
# Bank/debt observations: instrument definitions retained.
for per,s,v,u,basis,src,loc in [
    ('1806','bank_discount_rate',5,'%','法兰西银行贴现率；不是政府公债收益率','PL','Empire节'),
    ('1807','bank_discount_rate',4,'%','同上','PL','Empire节'),
    ('1808','bank_treasury_loan',40,'百万法郎','该次贷款流量，不是银行资本','PL','Empire节'),
    ('1814帝国末','bank_treasury_claim',50,'百万法郎','文献约数；债权存量非新增贷款','PL','Empire节'),
    ('1799-11','perpetual_rentes_service',46.3,'百万法郎/年','年票息非债务本金；与其他来源40m有日期范围差异','BW','print30/PDF32'),
    ('1814-04','perpetual_rentes_service',63.3,'百万法郎/年','年票息非债务本金','BW','print30/PDF32'),
    ('1806-1812','sinking_fund_bonds_issued',224,'百万法郎','累计票据发行，不是年末存量','BW','print30/PDF32')]:
    add('文献转录',per,s,v,unit=u,basis=basis,src=src,loc=loc)
add('文献转录','1806-1812','sinking_fund_bonds_coupon',low=6,high=7,unit='%',basis='名义票息；市场实际发行成本不明',src='BW',loc='print30/PDF32')
for n in [400000,450000,500000,550000]:
    for c in [600,700,900,1000]:
        add('模型','S5初期','army_cost_person_sensitivity',n*c/1e6,basis='建制人数×年度单位成本；中心700转Mollien，600缺装备为低界，900为主高界，1000为dIvernois争议数的额外压力项',src='MODEL;M',loc='pp322-323/PDF342-343',scenario='S5',territory='固定核心法国建制；独立盟军另列',formula=f'{n}*{c}/1000000',note='600/700转Mollien回溯估计，900为1806Naples报告、1000为dIvernois争议估计；非可用战斗人员单价，独立盟軍不并入法国现金' )
# Cross-card joint manpower audit, separately tagged as conditional model.
french_gross = 300_000_000/700
available = (french_gross+200_000)*.85
for s,v,u,formula in [
    ('French_gross_supported_L300_c700',french_gross,'人','300000000/700'),
    ('total_present_allies200k_q085',available,'人','(300000000/700+200000)*0.85'),
    ('S2_margin_present',available-540_000,'人','(300000000/700+200000)*0.85-540000'),
    ('S5_margin_present',available-490_000,'人','(300000000/700+200000)*0.85-490000'),
    ('S6_lite_margin_present',available-566_250,'人','(300000000/700+200000)*0.85-566250'),
    ('S2_allies_required',540_000/.85-french_gross,'人','540000/0.85-300000000/700'),
    ('S6_lite_allies_required',566_250/.85-french_gross,'人','566250/0.85-300000000/700')]:
    add('模型','1815-1820','joint_'+s,round(v,3),unit=u,basis='F2最终任务量与F4陆军300m闭合案；不是实测兵力',src='MODEL;F2;M',loc='F2_joint_budget_manpower.csv;M pp322-323',scenario='S6' if 'S6_' in s else ('S2' if 'S2_' in s else 'S5'),territory='法国建制+独立盟军；匹配F2任务范围',formula=formula,note='85%在场为F2参数；盟军自养及额外现金40m能否同兑现待区域核查')
# Model: all amounts in approximate 1810 purchasing-power planning units.
for yr in [1815,1820,1830,1840,1848]:
    n=yr-1815
    lo,hi=700*1.005**n,800*1.0125**n
    add('模型',yr,'S5_net_recurring_capacity',low=round(lo,3),high=round(hi,3),basis='1815净经常700-800；年增长0.5%-1.25%；不是实测平减数据',src='MODEL;C-JUN;M;OUV',loc='报告§S5',scenario='S5',territory='固定1810年6月税收核心；不含后续外圈及藩属',formula=f'700*1.005^{n};800*1.0125^{n}',note='无新征服赔款；不自动含盟国转移；低高为规划边界而非概率区间')
    centre=750*1.01**n; nonmil=300*1.0075**n
    add('模型',yr,'S5_central_joint_army_navy_ceiling',round(centre-nonmil-25,3),basis='中心T750年增1%;非军300年增0.75%;新补偿25;无永久新借款',src='MODEL;M;SG',loc='报告§S5',scenario='S5',territory='固定1810年6月税收核心；不含后续外圈及藩属',formula=f'750*1.01^{n}-300*1.0075^{n}-25',note='尚须减储备积累/过渡借款服务；非军含原债息养老金。')
configs=[('S5_maintenance',750,0,280,20,300,140,10),('S5_naval_compromise',800,40,300,25,300,195,20),('S5_land_heavy',800,40,300,25,350,170,20),('S3_high_mobilisation',750,40,330,30,390,220,20)]
for name,T,A,N,K,L,V,Q in configs:
    for s,v in [('net_recurring_T',T),('allied_cash_A',A),('nonmilitary_existing_debt_N',N),('new_compensation_K',K),('army_test_L',L),('navy_test_V',V),('reserve_accumulation_Q',Q),('annual_balance',T+A-N-K-L-V-Q)]:
        add('模型','1815-1820',name+'_'+s,v,basis='联立测试；不是历史数；军费以F2人力包络和Mollien单位费用作条件校验，非实际军费',src='MODEL;M;C-JUL;T;SG',loc='报告§S5',scenario='S3' if name.startswith('S3') else 'S5',territory='固定核心+明确盟约转移',formula='T+A-N-K-L-V-Q' if s=='annual_balance' else '',note='A不包括已替法国付军费的实物；不得重复减L。')
regional=[('low_friction',24,6,1,4,2,0),('intermediate',20,7,2,5,3,1),('hostile_frontier',12,6,2,9,3,3)]
for name,T,C,D,G,I,R in regional:
    for s,v in [('net_tax_T',T),('local_civil_C',C),('inherited_debt_D',D),('military_security_G',G),('integration_investment_I',I),('resistance_loss_R',R),('net_central_N',T-C-D-G-I-R)]:
        add('模型','并合后年度',name+'_'+s,v,basis='每100万人阈值测试；不是该地区实测估计',src='MODEL;C-JUL;M;GR',loc='报告§S6',scenario='S6',territory='抽象边际单元；由D1/D2置换',unit='百万法郎/百万人',formula='T-C-D-G-I-R' if s=='net_central_N' else '')
for L in [0,50,100,150,200]:
    add('模型','每新增100万人','S6_inherited_debt_interest',L*.06,basis='本金L×6%规划利率；把旧债转入的边际代价',src='MODEL;M',loc='报告§S6',scenario='S6',territory='抽象新增百万人地区；非历史法国总债',unit='百万法郎/年',formula=f'{L}*0.06',note='非历史借款报价')
# --- 第二代次补订：Branda 附录逐格开采（依据 notes_branda_appendix.md；上一代次只用了p14汇总四行） ---
for c,v in [('Italy',22.7),('Hanover',22.0),('Naples',36.1),('Westphalia',48.3)]:
    add('文献转录','1803-1814','allied_quartering_paid_'+c,v,basis='盟国为其境内法军驻屯支付的金额；对法国是避免成本，不是汇入巴黎的现金',src='BR',loc='p13附表 Sums paid by the allied countries for the quartering of French troops',territory=c,note='国别合计经本卡复算与总计129.1一致；逐年分配因缓存OCR丢格致列对齐破坏，不可恢复，禁止构造补差数')
add('文献转录','1803-1814','allied_quartering_paid_total',129.1,basis='四国合计',src='BR',loc='p13附表',formula='22.7+22.0+36.1+48.3',note='注16称取自国库总账，惟那不勒斯用Ilari(USSME 2004)研究；故该行非单一来源')
add('算术','1803-1814','savings_line_383_reconstruction',253.748180+129.1,basis='附表A盟军兵日节省总额(253,748,180法郎)＋附表B驻屯总计129.1m，用以复核附表C“Savings 383”行',src='BR',loc='p12/p13/p14三表',formula='253.74818+129.1',note='结果382.85≈383，附表自洽；而Branda正文同段写352又写“over 380”，352无法由其自身附表复现。本卡采383并记352为不可复现正文数字')
for s,v in [('treaty_extraordinary_planned',414),('treaty_extraordinary_unpaid_1814',136),('treaty_extraordinary_received',278)]:
    add('文献转录','1805-1813',s,v,basis='财务条款直接惠及Domaine Extraordinaire的条约清单；作者明言不含意大利',src='BR',loc='p11附表',formula='414-136=278' if s.endswith('received') else '',note='正文另称实收“only 276 million”，与附表278差2，保留不调和；与附表C“条约外部收入453”口径不同，不得互换')
add('文献转录','1808-1813','spain_ordinary_contributions_seized_by_army',350,basis='西班牙普通贡赋，全数由军队就地取用',src='BR',loc='p10-11附表 ordinary contributions',territory='西班牙战区',note='同表该行“付予法国国库”与“归入Domaine Extraordinaire”两列均为0；此0是原表明确格，非缺测')
add('文献转录','1808-1813','spain_ordinary_contributions_to_paris',0,basis='同行两列合计；原表明确为0',src='BR',loc='p10-11附表',territory='西班牙战区',note='观测到的零，不是缺测；证明战区榨取未必转化为中央可支配资源')
add('文献转录','An X (1802)','peacetime_breakeven_total_budget',500,basis='作者称1802年取得的收支平衡点约500m，亚眠和约破裂后失效',src='BR',loc='p7正文',territory='1802年法国疆域',note='作者未给该平衡点的军/民分项，故不得据此推算1802年军费份额；仅作和平基准量级')
for s,v in [('allied_ordinary_contributions_to_treaty',144),('treaty_lump_sum_indemnity',700),('army_of_occupation_1815_11_to_1818_10',328),('compensation_for_imperial_seizures',240),('total_paid_by_france',1412)]:
    add('文献转录','1814-1818','restoration_extraction_'+s,v,basis='战败后战胜国对法国的反向榨取',src='BR',loc='p14附表',territory='1815年后法国',formula='144+700+328+240' if s=='total_paid_by_france' else '',note='复算1412 ✓。在法国不战败的S5/S6中这是净避免额，属有史实数值支撑的反事实收益')
YRS=11.5
for s,v in [('additional_war_cost',4284),('war_financed_total',1799),('avoided_cost_component',383),('external_cash_like',1416),('external_cash_excl_spain',1066),('domestic_treasury_legs',1859),('deferred_deficit',503),('bank_loans',123)]:
    add('算术','1803-1814年均','annualised_'+s,round(v/YRS,3),basis=f'Branda附表{v}m ÷ 11.5年(An XI 1803–1814)',src='BR',loc='p14附表',formula=f'{v}/11.5',note='期间取11.5年；若取11或12年各值变动约±4%。年均掩盖战役年峰值（1809/1812），不得当作任一年实际值。1416=809+154+453；1066=1416-350(西班牙就地消耗)')
add('模型','和平转型','peace_removes_war_surcharge_per_year',round(4284/YRS,3),basis='战争附加成本年均；和平时该成本与其四条融资腿同时消失',src='BR;MODEL',loc='报告§补8',scenario='S5',formula='4284/11.5',note='恒等式：372.5＝外部156.4＋本土国库161.7＋递延赤字43.7＋银行10.7。贡赋不是净资源而是一条融资腿')
add('模型','和平转型','tribute_exit_cash_loss_share_of_ordinary_revenue',round(1416/YRS/750*100,2),basis='外部现金类年均÷S5中心经常收入750m',src='BR;MODEL',loc='报告§补8',scenario='S5',unit='%',formula='(1416/11.5)/750*100',note='剔除西班牙就地消耗350后为(1066/11.5)/750=12.4%')

with (P/'F4_fiscal.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
# Internal mechanical checks only; these do not validate historical interpretation.
assert len({r['id'] for r in rows})==len(rows)
for r in rows:
    if r['record_type']=='缺测': assert r['value'] is None
    if r['record_type']=='模型': assert r['scenario']!='S0'
print('Wrote',len(rows),'records to',P/'F4_fiscal.csv')
print('War share',1799/4284*100)
print('Endowments',3500*.0005+950*.002+770*.004+18)
for y in [1815,1820,1830,1840,1848]:
    n=y-1815
    print(y,'T range',round(700*1.005**n,1),round(800*1.0125**n,1),'centre joint mil',round(750*1.01**n-300*1.0075**n-25,1))
