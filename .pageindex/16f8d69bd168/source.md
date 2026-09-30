# B5材料、出处与独立性

本卡只引用实际读过的版本。以下短码对应主报告；来源中有立场、讹误或统计口径冲突，不因其权威而豁免。每一网页本地文件保留source_url/final_url/content_kind；没有把下载成功当通读。无圣赫勒拿回溯材料。

## 实际使用的材料

### H｜Eli F. Heckscher, *The Continental System: An Economic Interpretation*，Oxford，1922英译版
- 版本：`downloads/c15_heckscher1922.pdf`；doc `1baaae7f3185`，436 PDF页。复用上一轮t_f81a6f/t_95ef51材料，本卡重读相关段、复看表页。
- 实读/使用：印pp173–177（PDF189–193，1808危机）；238–247（PDF254–263，1810–12及出口表）；324–334（PDF340–350，部门与社会影响）。印p363关于国家信用的结论由旧卡定位，主报告没有用其单句替代财政研究。
- 精确表位：印p175/PDF191、p242/PDF258、p245/PDF261（已看图，旋转图`heckscher_p245_rotated.png`）、p246/PDF262、p329/PDF345。
- 关键内容：p245本产/转口、北欧/西葡/地中海—黎凡特/亚洲/美国/其余美洲；p329两港煤海运，不是全国煤产。p330：“There was certainly no pause in the industrial revolution”；随即强调危机不是封锁单独或主要造成，是作者解释，本卡用C反论制衡。
- 限制：大量数字来自Hansard、Porter等；并非独立原始海关观测。表中“real values”不是现代不变价。民族性格解释不用。Cort之子熟铁量为请愿声称，不当测量。
- 已存笔记：`notes_heckscher_orourke.md`；人工表：`B5_exports_declared_1805_1811.csv`。

### D40/D41/I/W｜Bank of England, *A millennium of macroeconomic data*，v3.1
- 入口：https://www.bankofengland.co.uk/statistics/research-datasets；精确xlsx：https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/a-millennium-of-macroeconomic-data-for-the-uk.xlsx；复用B2在2026-09-23取得`downloads/B2_BoE_millennium_v31.xlsx`（日期据B2来源记录，非重新下载）。源SHA256：`4c23dd392a498691eac92659aec283fb43f28118bd80511dc87fc595974195eb`。
- 本卡用openpyxl只读缓存，原坐标保存在`B5_boe_selected.xlsx`；未重算源公式。`B5_boe_cells.csv`为长表，`extract_boe.py`为提取器。
- **D40** A40：Moreau（1822）经Mitchell（1988）汇编，原注“From 1784 the declared and computed values in the next sheet are to be preferred.” A40行102–114=1803–15；C北欧、E南欧含土/埃、I亚洲、Q拉美含外国西印度、O美国、M加拿大、S英属西印度、G非洲、U总。含转口、旧价；1813缺。1811校订见M。没有亲阅Moreau/Mitchell原书。
- **D41** A41：Ralph Davis（1979）转录，Computed Values of External Trade—Great Britain；三年均、£000，国内出口与转口分列。本卡使用行10–14、21–25、32–36。欧洲本产T、亚洲K、拉美O、美国G、全球本产T、全球转口U；全球排爱尔兰。爱尔兰块D列与全球转口重复的可疑字段不用。没有把经BoE转录说成已读Davis原著。
- **I** A4：Stephen Broadberry, Bruce M. S. Campbell, Alexander Klein, Mark Overton and Bas van Leeuwen, *British Economic Growth, 1270–1870*（CUP，2015）数据。行542–587对应1803–48；C铁、D煤、E纺织、N总工业。只用比值/重定1803=100，不把原指数写成吨。A1人口Y为GB+NI地理重建，不是整个英国含全爱尔兰。
- **W** A47：B复合周薪、D首选CPI，重定1803=100；原注1770–1882 CPI来自Feinstein1998；薪率链接Feinstein/Geary-Stark等。原公式1812 B610=B611×AR610/AR611，AR为充分就业货币收入。实际购买力=B/D，不能扣除未观测失业、短时及家庭结构。
- 局限：历史重建和拼接，不是现代统计局实时观察。A4的年际与出口/地方就业分歧不拿来做封锁因果回归。详`notes_boe_scope.md`和`B5_data_metadata.json`。

### M｜John Marshall, *A Statistical Display of the Finances, Navigation and Commerce of the United Kingdom of Great Britain and Ireland*，1833（作者/年份按数字馆题录）
- 原扫描：https://archive.org/download/b22297042/b22297042.pdf；转至https://ia601903.us.archive.org/15/items/b22297042/b22297042.pdf。
- `downloads/B5_Marshall_statistical_display1833.pdf`，doc `6732fd554ca2`；SHA256 `6732fd554ca206d55ce2060d31852f46686eaf853b0b621a7f802abbf027e2e7`。
- 实读标题页及印p74/PDF88文字＋页图；没有阅读全296页。页题为Official Value of Merchandize ... America and Foreign West Indies。
- 1811行：外西印度3,046,819；美国1,431,829；英属北美1,909,689；合计6,388,337。支持对BoE A40美国/北美多记约£10m的修订。
- 不是用不同估价强行对齐：这也是旧官方价值。全球27.459m是本卡对BoE同表总加总的派生校订，不假称Marshall这一页给出全球数。首次抄错环节未定；1805美国与BoE仍有约0.002m小差，未擅自全序列替换。
- `notes_marshall_correction.md`。早期OCR巨页`downloads/pages/26c8c80b061c.md`仅定位，核定依据原页图。

### P08｜“Liverpool Petition Respecting the Orders in Council Bill”
- HC Deb 3 March 1808 vol10 cc889–895。
- https://api.parliament.uk/historic-hansard/commons/1808/mar/03/liverpool-petition-respecting-the-orders
- `downloads/pages/6305bcbe013e.md`；本卡全段读。Gascoyne呈请愿；议长/财政大臣的税案程序异议；Tarleton称1461支持者未签；80对128拒受。
- 精确用途：城市政治不等于商人共同体。关于失业40万人、利物浦占美贸四分之三均是议员声称，本卡不入数量表。

### P11｜“Commercial Credit”
- HC Deb 11 March 1811 vol19 cc327–350。
- https://api.parliament.uk/historic-hansard/commons/1811/mar/11/commercial-credit
- `downloads/pages/3b8b8e348c6d.md`；本卡重读cc327–348，后两栏未声称重读完。摘录`notes_hansard_1811.md`。
- cc328–331商人—制造商—工人链、南美货积压；cc332–333六百万Exchequer bills建议授权；cc334–335“Exports were not trade”及“we ought to have returns”（上半句网页把exports断成ex ports，含该句的笔记将断字接合）；cc338–340好票据仍贴现；cc342糖咖啡回款被欧市场阻断；cc345美国本土制造替代风险。
- 单场多方立场，不等于多份独立统计。网页抽取丢失部分发言人标题，正文有些归属依赖后续称谓；本卡尽量引用辩论/栏位而非过度指定个人。不能把1793授权/实放金额写成1811实放。

### P12s｜“Petition from Sheffield Against the Orders in Council”
- HC Deb 17 April 1812 vol22 cc424–425。
- https://api.parliament.uk/historic-hansard/commons/1812/apr/17/petition-from-sheffield-against-the
- `downloads/pages/0cf6ab7705f7.md`；正文全读。核心原文“the just rights and independence of the United Kingdom”与“they would willingly bear the pressure without a murmur”。
- 请愿是利益表达；不能将其病因叙述当独立检验，也不能抹掉其爱国附款。

### P12h｜“Petition from the Hallamshire Cutlers Against the East India Company's Charter”
- HC Deb 17 April 1812 vol22 cc422–424。
- https://api.parliament.uk/historic-hansard/commons/1812/apr/17/petition-from-the-hallamshire-cutlers
- `downloads/pages/ba2ab29e8259.md`，正文全读。主张开放公司垄断以“counterbalance, in some measure”欧洲/美国限制。其亚洲人口倍数、贸易可能额不当实际需求。

### P12b｜“Petition from Birmingham Against the Orders in Council”
- HC Deb 17 April 1812 vol22 cc425–440。
- https://api.parliament.uk/historic-hansard/commons/1812/apr/17/petition-from-birmingham-against-the
- 全页`downloads/pages/92274137edfc.md`已读，早期`b774a39e237e.md`只有excerpts，不作为最终完整来源。
- cc426–427资本、制造业、海军及“invaluable constitution”；cc429 Baring质疑开放印度就创造英制品需求；cc430–433 Rose/Mordaunt对灾荒程度反驳；cc437 Brougham熟练工工资与不能改征/赶农；cc439互助会、就业与贷款还款争论。
- 对救济税和失业的不同断言互相冲突，保留归属，不拼成全国数据。25–35先令到12先令不是纯时薪变动，故不代替W。

### N｜Katrina Navickas, “The search for ‘General Ludd’: the mythology of Luddism”
- *Social History* 30(3), 2005, pp281–295。
- `downloads/c16_navickas2005.pdf`；doc `3c4c39c32329`，复用上一轮材料。
- 本卡实读印281–282、291–292（PDF2–3、12–13），其他请求截断未称全读。p291：“It was not a blind reaction against economic change”；p292将部分恐吓信限定为“isolated and not indicative of any serious revolutionary danger”。
- 机制：地区/职业异质、社区网络、军事消息口传、神话与组织并非同物。史料经治安官/间谍/司法生成，不能直读为革命组织真实全貌。

### J｜François Jarrige, “Une « armée de justiciers » ? Justice et répression du luddisme en Angleterre (1811–1816)”
- Blois/SNES圆桌讲稿，15 octobre 2010，法语。
- https://www.snes.edu/IMG/pdf/BLOIS_-_Justice_et_luttes_sociales_-_Luddisme_-_Jarrige_1_.pdf
- `downloads/B5_Jarrige_Luddisme2010.pdf`，doc `4e8fe2aef689`，六页；实读pp2–6。
- p2转引Crouzet1987 pp770–781的9000/3000/2500/3500劳动调查；p2旧劳动规制与市场化；p5转引Thomis约12,000军人和Thompson的拒射个案；pp5–6镇压与1824/25法律路径。
- 原文误将Orders概括到1811初，不沿用此日期；未核其军人数与1808Wellington军人数比较，不使用比较。引用Navickas/Thompson/Crouzet，不能声称三个完全独立观察。详`notes_nonenglish.md`。

### CA｜Encyclopaedia Britannica，“Combination Acts”
- https://www.britannica.com/money/Combination-Acts
- `downloads/pages/72f263dafad6.md`，捕获首段，末尾截断；不是原法令。
- 使用1799/1800禁联合、3个月监禁/2个月苦役、两名治安官及对雇主执行不对称的概述。1824/25条目后文未获，本卡相应论证使用J，不偷引搜索摘要。

### T16/T19｜Robert Poole为英国国家档案馆撰写的两篇导读
- “Protest and Democracy 1816 to 1818, part 1”：https://www.nationalarchives.gov.uk/education/resources/protest-and-democracy-1816-to-1818/；`downloads/pages/6584f2f8b4f1.md`。
- “Protest and democracy 1818 to 1820, part 2”：https://www.nationalarchives.gov.uk/education/resources/protest-democracy-1818-1820/；`downloads/pages/0165ca641153.md`。
- 两篇Introduction正文全读。T16：复员/行业收缩/1816冷夏与粮法、1817请愿；T19：1818复苏—1819萧条，Peterloo（16 August 1819）、1820军人支持女王及guards哗变迹象。
- 导读所列60,000集会及退伍规模为作者综合，本卡未亲查原名册。某些地方标签/因果说法本身需另审；主报告只用一般机制和已定位事件，不伪称亲阅全部内政部档案。

### BR｜*Carta Régia de 28 de Janeiro de 1808*
- 葡萄牙文同时代王室敕函，巴西众议院法律库转录，Coleção de Leis do Brasil de 1808 vol1 p1。
- https://www2.camara.leg.br/legin/fed/carreg_sn/anterioresa1824/cartaregia-35757-28-janeiro-1808-539177-publicacaooriginal-37144-pe.html
- `downloads/pages/ead7fbfac794.md`，正文全读。关键语“interina e provisoriamente”、“em razão das criticas e publicas circumstancias da Europa”；友好/和平国家及本国船进口税24%；多数货物可自由择港出口，巴西木及专卖品例外。
- 不是1808即自由贸易零关税，也不是所有国家无条件准入。网站声明转录不替原刊，未假装核过原手稿。

### CE｜Javier Cuenca Esteban, “India’s contribution to the British balance of payments, 1757–1812”
- Carlos III WP06-03，封面March2006，正文October2005；**不是后来刊本**。
- https://e-archivo.uc3m.es/bitstreams/59818d76-9b1b-435d-80c8-857d7d7efafc/download
- `downloads/pages/ef0a274dde3a.md`；实读首部及pp14–23。
- pp14–16财政/公司/私人流量；pp17–20称估计“conjectural”；转口利润率5%、进口替代成本80%等假设明确；pp21–23市场与贸易价格。支持印度资源转移≠英制品订单，以及欧洲不买印度转口品会削弱英国兑现。
- 作者认为印度流入可为战争国际支付作重要贡献，不据此推定工业出口市场充足。未拿英制品、印度税收、转口利润重复加总。`notes_cuenca_discovery.md`。

### O｜Kevin H. O’Rourke, “The worldwide economic impact of the Revolutionary and Napoleonic Wars”
- TEP9/2005，May2005工作稿；**不是声称亲读2006刊本**。
- https://www.tcd.ie/Economics/TEP/2005_papers/TEP9.pdf
- `downloads/pages/dda4372be1f5.md`。实读引言/测量/模型及结论有关段L20–169、370–450（部分其他段未读）。
- 表4英国1.7–1.8%年福利损失是单要素简化贸易模型，非GDP、失业或投资损失；脚注18承认不计失业可低估。
- 结论讨论1815粮法、1786Eden条约及战后自由贸易路径；Crouzet1964的法国纺织保护论为本稿转引，没有写成直接阅读。
- 理论模型的结果不是又一套独立海关数据；参数和历史表有共同来源。

### C｜W. H. Chaloner对Crouzet专著的书评
- *Revue belge de Philologie et d’Histoire* 38-2（1960）, pp525–526。
- https://www.persee.fr/doc/rbph_0035-0818_1960_num_38_2_2317_t1_0525_0000_2
- `downloads/pages/e5b32951df65.md`，全文已读。
- 书评介绍François Crouzet, *L’économie britannique et le blocus continental (1806–1813)*，PUF1958，二卷949页。转引p855：“Nous pensons avoir démontré également que le Blocus Continental fut à l'origine de la crise de 1810, ce véritable ouragan qui secoua toute l'économie britannique ...”。
- 保留强反论：走私成本高且有限、扣船/保险损失、1810–12社会危机与战争能力削弱。书評“revolutionary situation ... without revolutionaries”是解释不是普遍革命组织观测。未获得Crouzet1958/1987原书，不假报原书全读。

### KF/KC｜英国议会公共历史页
- KF “The 1833 Factory Act”：https://www.parliament.uk/about/living-heritage/transformingsociety/livinglearning/19thcentury/overview/factoryact/；`downloads/pages/98f3132e9a36.md`，正文全读。
- 关键原文：a small, four-man “inspectorate of factories”；4,000 mills；“widely evaded”。用于正式规制/执行落差，不当1833原法条亲阅。
- KC “The Chartist movement”：https://www.parliament.uk/about/living-heritage/transformingsociety/electionsvoting/chartists/overview/chartistmovement/；`downloads/pages/cd205de92b28.md`，正文全读。
- 1832财产门槛、1838六点宪章、1839/42/48请愿；1848“the anticipated unrest did not happen”。不把申请者声称签名数当认证人数。两者是后世机构概述，不是独立原始调查。

## 复用、发现但未承重的材料

- 旧卡`t_f81a6f`的`c15_continental_economy.md`、`growth_debate.md`、`money_infrastructure.md`、`SOURCES.md`和`t_95ef51`的财政/信用定位用于发现；主报告相关H/P11/O已重读。旧模型、未识别结论、未经阅读的引文不继承。
- B2 BoE源资产及协调台账告知财政和海军口径，本文未复制其模型数字做独立实证。B1/B4国家安全与战争成本机制为接口，不以其卡名当书目来源。
- Neil Simpson, *Informal Empire*附录，`downloads/pages/2117b6d948bd.md`，三级转引Rory Miller1993←Davis1979，本卡读到但未作最终表来源；用于找到Davis口径，不能与D41计双重互证。
- Jacks/O’Rourke/Taylor/Yotov, *Distance, Empire, and British Exports Over Two Centuries*，NBER27904，实得July2026修订稿，`downloads/pages/2e0619dd75ba.md`，仅摘要/数据说明；十年间隔不填本卡年度空值。
- Crouzet1964 “Wars, Blockade, and Economic Change in Europe, 1792–1815”，*JEH*24(4), pp567–588，DOI10.1017/S0022050700061271，未得全文，只经O转引。Crouzet专著Anna查询不完整而无精确命中，不能说文献不存在。
- Gayer–Rostow–Schwartz、E.P.Thompson原书、Bairoch、Malm、John V.Orth、Baines等为检索线索或二手作者引书，未在本卡作为亲阅来源使用；不把搜索摘要数据填表。

## 独立性与缺口

1. H、P11/P12、D40/D41及M多源于英国海关/议会传统，互证可查传抄，不能按书本数量增加统计样本数。
2. N/J引用有重合，地方司法来源又经官方筛选；原始工人沉默和地下组织漏报可能同时存在。
3. BR属于葡萄牙—巴西独立文书谱系；其说明政策选择，不证明英国实际订单与现金回流。
4. O/CE为重建与模型，假设不同于观测；C为强反论的书评入口而非替代原书。
5. 真正会收紧区间的缺口：纯拉美本产年度净实现、商号应收/坏账/设备投资、地区工时就业、美国/葡西主动选择和法国长期封锁执行成本。现交付不伪造这些输入。

## 复现产物

- `B5_annual_exports_1803_1815.csv`：官方总货物年度表，原/校订列并存，1813缺。
- `B5_exports_declared_1805_1811.csv`：H逐图转录本产/转口；舍入差保留。
- `B5_market_benchmarks.csv`：D41地区均值，地区求和核验。
- `B5_industry_wages_1803_1848.csv`：I/W重定指数与人口尺。
- `B5_replacement_diagnostics.csv`、`B5_checks.json`：代理比率及检查，不当严格现金检验。
- `B5_scenario_parameters.json`、`B5_market_scenarios.csv`、`B5_growth_paths.csv`：公开假设与全部端点。
- `B5_export_substitution.md`：人读表；`build_B5_tables.py`可重建。
- `B5_data_metadata.json`、`B5_provenance_audit.json`、`B5_boe_manifest.json`：口径与SHA。审计只查字段，不授予来源为真。
