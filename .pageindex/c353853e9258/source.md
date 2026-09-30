# F2有界补查：年度征额、实际编入与战后军额

## 交付结论与冻结等级

【事实：核读结果】本次复用了指定三份本地文本；完成8次外网搜索后停止，没有进行总体反事实推演，没有继承旧卡的容量结论。

1. **找到1803—1813连续年度“命令征集额”序列，但仅能冻结为旧综合史网页转录所载数值，不能冻结为实际编入序列。**来源为《Histoire de France contemporaine》第三卷、第四编第一章第一节“L’armée impériale”；网页标Lavisse，具体卷作者、纸本页码本次未对校。1814缺数。
2. **全国年度实到序列仍缺。**可冻结Houdaille转引Darquenne的累计“appelés/ incorporés”对照及地域、时期口径，不得摊成年度。
3. **Woloch确有目标表的明确线索**：1986年论文p.110，Table 1 “The Napoleonic Levies”；本次只读到他文对该表的指引，未取得原表，不能声称核读。
4. **1818年24万人可以冻结为制度规定军额，不是1818年实有人数。**七月王朝不能笼统冻结为“30—40万和平军队”：同时期刊载1833年1月1日实额421,494人，且包含宪兵、外国军团及北非部队。

## 补记：Elting摘录的独立口径判读

本节依据用户核读Elting XVI、索引p.88后提供的摘录；**我未独立见原页**。以下是对时间、统计对象与重复计数风险的判断，不是对Elting原文的复核。不增加外网检索，不合成统一年表。

|用户提供的记录|独立判读|处理决定|
|1806：160,000，含60,000 reserve|160,000可能是事件集合，80,000可能是单一年级征额；但单凭摘录不能确认是否跨两年级或追加征召。reserve也不等于已经到营。|与旧综合史1806年80,000保留冲突；不自行拆为两批80,000；160,000减60,000所得100,000不命名为实到。|
|1807调用1808级80,000，含20,000 reserve|征令年1807、年级1808，是明确的两个时间轴；与此前1808级80,000可相容。|保留80,000授权及20,000预备标签；剩余60,000仅是非预备分类差额，不是已编入。|
|1808调用1809级80,000|与本次核读1808年1月文书、1809年级80,000吻合；它只是一项征令，不应等同1808全年合计。|可作为逐令锚点的相互支持；不据此否定240,000年度多项合计。|
|1809：60,000，再75,550|“再”提示不同批次，但尚不清楚是否都是新授权、一个是计划另一个是执行，或有互相包含。|两条事件分存；不把135,550冻结为全年征额。75,550与旧综合史76,000近似，不足以认定只是取整。|
|1811：167,000，其中90,000 reserve|不能直接拿来与1811年级120,000或1810年授权相比：年级、批准日、预备调用状态均未确定。|167,000/90,000按用户摘录保留；差额77,000不当实到。与120,000授权、草案80,000现役目标并存待核。|
|1811年12月120,000；1812另两次245,000，约半为National Guard|前项有明确征令年月，年级仍未由摘录证实；后项混入国民卫队，不能称全部为新征陆军。|不相加成1812征额；不把“约半”改写为精确122,500人。|
|1813新增350,000；1812年9月120,000仍在depots|这是最显著的流量/存量混合：1812年征令形成的人力可能在1813年仍处补充营；在补充营不等于未被军队编入，更不等于已进入野战军。|350,000的统计截止日及“新增”定义待查；120,000单列为旧征令关联的补充营状态，禁止作为1813新增再计。也不默认120,000就是后来所列1813级137,000的全部或子集。|

【裁量】这些记录首先揭示**跨年提前征召、预备兵分类、国民卫队与正规军混合、征募流量与补充营存量混合**，而不是证明某一作者“算错”。其中1807→1808级、1808→1809级能清楚定位；1806、1809、1811及1813汇总仍有真实待核冲突，不能强行调和。旧综合史年度表继续降格为来源原样附表，不进入统一容量计算。

### 战后类比的优先冻结决定

- **1818：240,000只作制度目标/法定军额；40,000为通常年度征召上限，六年为通常役期。**此三项不能证明1818实际在营240,000，更不能证明该规模是财政或人口最大承受能力。
- **七月王朝：用带日期的观测替代“30—40万和平军队”泛称。**1831年9月编制452,195、报道所指同期实额400,371；1833年1月1日实额421,494。它们不是全时期平均，也不是野战可用军额。包含宪兵、老兵部队、外国军团和北非部队，不能直接与仅法国本土正规野战军口径比较。
- 【裁量】这组资料能支持“后拿破仑时期存在24万法定军额、另有超过40万报告实额的制度与时点案例”，**不能单独支持“拿破仑和平霸权可持续维持多少军队”**。本卡不进行该推演。

## 1. 口径规则

- `order_year/date`：征令颁布年/日期，不等于部队报到年。
- `class`：征兵年级，不等于命令年；共和历年亦不机械替换为单一公历年。
- `authorized`：置政府支配/法定征额；`activated_target`：计划投入现役；`departed`：离省；`incorporated/arrived`：实际编入/到队，分别保留。
- 命令额中的国民卫队动员、海籍人员与常规陆军新兵不得默认同口径；重复征召同一年级不等于重复编入同一个人。
- 以下“—”均指本次未核得，不代表零。

## 2. 连续年度征令额：可引用，尚非最终数据冻结

【事实：来源陈述】所读网页第一节首段：

> “Napoléon fit appeler 30.000 hommes en 1800, 120.000 en 1802, 120.000 en 1803 (soit 270.000 sous le Consulat), 60.000 en 1804, 210.000 en 1805, 80.000 en 1806, 80.000 en 1807, 240.000 en 1808, 76.000 en 1809, 160.000 en 1810, 120.000 en 1811, 237.000 en 1812 et 1.140.000 en 1813 (soit 2.403.000 sous l’Empire et 2.673.000 au total).”

|征令年（来源编年）|征集命令额：人|年级|实际编入|
|---|---:|---|---|
|1803|120,000|未逐令分解|—|
|1804|60,000|未逐令分解|—|
|1805|210,000|未逐令分解|—|
|1806|80,000|未逐令分解|—|
|1807|80,000|未逐令分解|—|
|1808|240,000|未逐令分解|—|
|1809|76,000|未逐令分解|—|
|1810|160,000|未逐令分解|—|
|1811|120,000|未逐令分解|—|
|1812|237,000|未逐令分解|—|
|1813|1,140,000|多次征召，未逐令分解|—|
|1814|—|来源明确称另有levée en masse|—|

【事实：限定原句】同节第二段末明确警告：

> “L’effectif des levées ordonnées représentait moins le résultat réalisé que l’effort demandé.”

同节第一段说明统计还须加1814年总动员、志愿者、续服者、军校军官及外国团/分遣队；并把帝国期2,403,000分为常规年级征召1,237,000、旧年级召回746,000、国民卫队动员370,000、海籍人员特别征召50,000。故它不是纯陆军首次入伍人数。

**来源质量警报**：网页后文有“en 1803 … (24 septembre 1805)”自相矛盾年份，以及“en 1803 … classes 1804 à 1800”等需校勘表述。不能自行订正，更不能以此直接确定每令日期。其“征兵成效不断下降”叙述也不能替代JEH关于1806—1810逃避征兵率下降的实证。

- URL：http://www.mediterranee-antique.fr/Auteurs/Fichiers/JKL/Lavisse/Histoire_contemporaine/T3/T3_41.htm
- 本地：`downloads/pages/fb00e45c56a7.md`
- 定位：Livre IV, chapitre premier, I，前三段。仅核读网页转录，未核纸本。

### 按年级的另一组征额（不得与上表相加）

【事实：来源陈述】上述第三段：

> “60.000 pour les classes de 1801 à 1805, 80.000 pour celles de 1806 à 1809, 110.000 pour la classe 1810, 120.000 pour les classes 1811 et 1812, 137.000 pour la classe 1813, 150.000 pour la classe 1814, et 160.000 pour la classe 1815.”

|年级|该文所载每级征额|实际编入|
|---|---:|---|
|1803、1804、1805|各60,000|—|
|1806、1807、1808、1809|各80,000|—|
|1810|110,000|—|
|1811、1812|各120,000|—|
|1813|137,000|—|
|1814|150,000|—|
|1815（1803—1814征令研究所涉及的提前征召）|160,000|—|

这里的“各”是原文按classes分组表达的展开，不是累计总数的年均摊分。是否包含每级后续补征，须逐令校对。

## 3. 两项可分解的同时代文书锚点

### 3.1 1808征令／1809年级／80,000授权

【事实：文书转录】Napoleon Series《Decree for raising Conscripts》，网页题日期January 23 1808，第1—2条：

> “Eighty thousand conscripts of the conscription of the year 1809 are placed at the disposal of government.”
> “They shall be taken from among the youths born between the 1st of Jan. 1789, and Jan. 1, 1790.”

- 冻结字段：征令年1808；网页日期1月23日；年级1809；授权80,000；出生区间1789年1月1日—1790年1月1日（原文端点未细释）；实到—。
- 这是网站转录《Annual Register … for the Year 1808》，未提供具体页码；只可标“同时期刊文书，转引自Napoleon Series”。
- 与上节转录的1月21日有日期差异，本次不裁定是议决/公布日期差异还是转录错误。
- URL：https://www.napoleon-series.org/research/government/legislation/c_conscription.html
- 本地：`downloads/pages/97294cdeb4b6.md`，Decree条1—2及Bibliography。

### 3.2 1810授权／1811年级／120,000，草案计划现役80,000

【事实：草案转录】《Projets de Décrets Relatifs à la Conscription de 1811》，Section de la guerre，Dumas报告，2e rédaction，第1条：

> “Sur les cent vingt mille conscrits de 1811, dont l’appel est autorisé par le sénatus-consulte du 13 décembre 1810, quatre-vingt mille seront mis en activité ; le reste formera la réserve.”

第8条：
> “Le premier détachement de chaque département sera mis en route le 1.er avril.”

- 冻结字段：所引授权日1810-12-13；年级1811；授权120,000；草案现役目标80,000；草案预备40,000（120,000减80,000的算术）；计划首批启程4月1日；实际编入—。
- **这是第二稿建议，不能写成80,000人已到队，亦未核得最终颁布版本。**第二条另有沿海县及荷兰地区海军征募规定，陆海军分配边界应保留。
- URL：https://www.napoleon-series.org/military-info/organization/France/Conscription/1811/c_conscripts1811.html
- 本地：`downloads/pages/43dacbcb242e.md`，条1—4、8。

## 4. 指定本地材料核读：哪些能用，哪些不能

### 4.1 Forrest：机制、警告与档案线索，不是已取得年度表

Alan Forrest, *Conscripts and Deserters: The Army and French Society during the Revolution and Empire*, Oxford, 1989。

【事实：核读】pp.35—36（本地行1470—1510附近）只给征募阶段描述：
> “The needs of that state oscillated wildly from year to year…”
> “Between 1806 and 1813 the government demanded levée after levée…”

不能由此补齐各年数字。p.40附近（行1660起）讨论Hargenvilliers 1808年报告及前五个年级的省际不均，特别区分：
> “the numbers of men incorporated, a much more real index of sacrifice”

注111（行9618）定位：AN AF IV 1123，1808年Hargenvilliers “Compte général sur la conscription depuis son établissement”。注104（行9790）定位1806年“État général des déserteurs”，其正文p.63附近警告：
> “les mots déserteur et réfractaire se prennent ici dans le même sens”

【未验证】未直接读到上述档案原件。Darquenne地方研究书目由Forrest注91提供：Roger Darquenne，“La conscription dans le Département de Jammapes, 1798–1813”，*Annales du Cercle archéologique de Mons*, 67 (1968–1970)。地方标题不能当全国年度表已获。

- 本地：`downloads/pages/81f2084d72ce.md`（OCR；原句中的软断字符此处按词连接）
- URL：https://rodrigomorenog.files.wordpress.com/2019/01/forrest-conscripts-and-deserters_-the-army-and-french-society-during-the-revolution-and-empire-oxford-1989.pdf

### 4.2 JEH：1806—1810省级数据存在，但不能把平均逃避率乘总征额

Louis Rouanet and Ennio E. Piano, “Drafting the Great Army: The Political Economy of Conscription in Napoleonic France”, *Journal of Economic History* 83(4), 2023, pp.1057–1100，DOI 10.1017/S0022050723000360。

【事实：核读】“DATA DESCRIPTION”第1段：
> “Measures for these variables refer to France’s 110 departments (plus the island of Elba) for each year between 1806 and 1810.”

第2段：
> “Lacuée regularly reported to Napoléon how many conscripts left their departments and arrived in their units.”

第3段：
> “Lacuée’s data provides figures only for individuals from the former category … draft dodgers.”

【方法限制】其逃避征兵率不是部队服役后的全部逃亡率；省份未加权平均也不是全国按人数加权率。本文网页没有给本次所需的完整全国年度“授权/实到”表。注13指AN AF/IV/1124及Rouanet and Piano (2022)数据代码；注17明确离省/到队报告在AN AF/IV/1122。Figure 1来源为AF/IV/1124 n.1、n.9。数据包本次未下载、未求和，不能假称已经重建系列。

- 本地：`downloads/pages/ee71889de366.md`，DATA DESCRIPTION、注13、17。
- URL：https://www.cambridge.org/core/journals/journal-of-economic-history/article/drafting-the-great-army-the-political-economy-of-conscription-in-napoleonic-france/FDBA5D70BC85C24186EF7C9767D249BF

### 4.3 Houdaille：累计征额与编入可冻结，仍非年度系列

Jacques Houdaille, “Pertes de l’armée de terre sous le premier Empire, d’après les registres matricules”, *Population* 27(1), 1972, pp.27–50。

【事实：转引自Houdaille pp.48—49】“Nombre d’hommes ayant servi sous l’Empire”：
> “Au total, d’après ces documents, 2 655 000 conscrits auraient été appelés de l’an VII au 15 novembre 1813 et 2 480 000 auraient été incorporés ces chiffres se rapportant à la France dans ses frontières de 1804 (rive gauche du Rhin et Piémont).”
> “retrancher environ 330 000 hommes incorporés de l’an VII à l’an XI ce qui laisse un total de 2 150 000 hommes”

|时段|地域|appelés|incorporés|证据性质|
|---|---|---:|---:|---|
|共和VII年—1813-11-15|1804边界，含莱茵左岸及皮埃蒙特|2,655,000|2,480,000|Houdaille转述Darquenne分析征兵局资料；原文条件式|
|扣除VII—XI年约330,000后|同上|—|约2,150,000|累计差额，不是逐年实到|
|Houdaille军籍抽样扣重、扣除XII年前入伍者后|为与上述范围比较而整理|—|约2,025,000|作者估计；与行政统计不是同一数据过程|

原文明确：
> “nous ignorons si les volontaires figurent parmi les soldats incorporés”

【文献推断：Houdaille】他把125,000差额解释为可能属于未在1813年转入陆军的舰队人员，措辞为“correspondrait”；不可冻结成已证实海军人数。pp.47—48亦警告重复逃亡/再编入，不能把所有记录条次当独立人数。

- 本地：`downloads/pages/b4cf5e9825fc.md`，行515—557附近。
- URL：https://www.persee.fr/doc/pop_0032-4663_1972_num_27_1_15097

### 4.4 Woloch表：明确定位但未核得

Isser Woloch, “Napoleonic Conscription: State Power and Civil Society”, *Past & Present* 111 (1986), pp.101–129，DOI：https://doi.org/10.1093/past/111.1.101。

【未验证原表】DOI提取只返回元数据：`downloads/pages/5fa8192aac32.md`。Stephan Rosenke，2003年大学课程论文 *Die Napoleonischen Feldzüge. Wehrpflicht, Réfractaires und Deserteure*，注41原句：
> “vgl. Tabelle 1 ‘The Napoleonic Levies’ bei Woloch: Napoleonic Conscription, 110.”

- 该指引本地：`downloads/pages/8c0c23fc4ef9.md`，行516。
- URL：https://de.readkong.com/page/die-napoleonischen-feldzuge-wehrpflicht-refractaires-und-7167994
- 它只证明明确的查表线索；学生论文不是原表替身，也不能说明表内有实际编入列。后续最优查证目标是Woloch p.110而非漫搜总兵力。

## 5. 战后类比：必须改正存量口径

### 5.1 1818的240,000：制度规模，非观测实额

【事实：档案馆编制说明】Archives départementales de la Somme, *Sous-série 1 R (en partie), Recensement militaire et registres matricules (an IX–1940), Répertoire numérique*，2024-02-22修订，p.6“1818”：

> “Le total de l’armée est fixé à 240.000 hommes. Les appels sont destinés à compléter ce chiffre dans la limite annuelle de 40.000 hommes (en cas de besoins supérieurs, une loi est nécessaire).”
> “La durée du service est fixée à six ans, sauf pour la classe de 1816 (cinq ans).”

可冻结：1818年3月10日法律所定军额240,000、通常年度征召上限40,000、通常役期6年。**不能冻结“1818年军队实有24万”，也不能仅按6×4万证明实际存量。**这次读的是档案馆法律摘要而非法律原刊。

同页1832年法摘要还区分“mis en activité”与“laissés dans leurs foyers”，七年法定役期乘年度contingent亦不能当在营兵力。

- URL：https://archives.somme.fr/document/r1_rep_militaire
- 本地：`downloads/pages/e07f5916248e.md`，p.6。

### 5.2 七月王朝：同时期刊给出实额421,494，不支持固定30—40万和平军额

【事实：同时期刊转引报告】*L’Écho de la Fabrique*, 21 avril 1833, no.16，“Variétés—Effectif de l’armée française”：
> “Le Moniteur publie un rapport du ministre de la guerre, dont nous extrayons les passages suivans”
> “Les ordonnances rendues en septembre 1831 avaient fixé le complet de l’armée à 452,195 hommes … mais ce complet n’a pas été atteint … l’armée n’était que de 400,371 hommes”
> “Au 1er janvier 1833, l’armée présentait un effectif de 421,494 hommes et 82,057 chevaux.”

|日期/状态|人数|性质|
|---|---:|---|
|1831年9月敕令|452,195|编制额complet|
|该报道所指同一时期|400,371|报告实额；具体统计日未列|
|1833-01-01|421,494|报告实额effectif|

1833表中“troupes françaises”413,424，其中宪兵15,982、退役老兵部队8,995等；另含外国军团4,473、Zouaves 1,055、Chasseurs d’Afrique 2,334、土耳其辅助部队210。不能把421,494当可外征野战兵力，也不能写成欧洲驻军净额。原文没有称其为“和平正常军额”；本次不据此推算稳定和平容量。

- URL：http://echo-fabrique.ens-lyon.fr/document.php?format=search&id=2542
- 本地：`downloads/pages/a21d8807b909.md`
- 页内锚点：EFFECTIF DE L’ARMÉE FRANÇAISE，首三段及表；电子转录含原刊[4.2]栏标。
- 引用链：战争部长报告→《Moniteur》→《Écho》摘录→ENS Lyon电子转录；本次未核《Moniteur》原刊。

## 6. 边界、后续最短路径与检索台账

【裁量】F2可以立即采用：两项逐令/年级授权锚点；Houdaille累计appelés/incorporés对照；1818法定军额；1831/1833编制与实额对照。1803—1813年度列表只能以“旧综合史征令额，待逐令对校”附表列出。全国1803—1814年度实到仍不得填写。

检索严格8次（无进一步搜索）：
1. Napoleon conscription annual levies table 1803 1814 Hargenvilliers
2. conscription “1803” “1804” “1805” “1813” “incorporés” tableau
3. “Woloch” “conscription” “1806” “1810” 1986 table
4. “Woloch” “The Napoleonic Levies”
5. “Napoleonic Conscription: State Power and Civil Society” pdf
6. “1818” “240 000” “armée” “1830”
7. armée loi 1818 “240.000” “1832”
8. “monarchie de Juillet” “armée” “400 000” “300 000”

技术限制：已加载agent-reach及search reference；按其Exa CLI路由调用mcporter时，bash要求父级批准，未执行成功。改用本会话web_search/web_extract的可用Exa后端。未安装工具、未修改技能、未请求绕过授权。

仅作下一阶段线索，不冒称读过档案：
- AN AF IV 1122：逐期离省/到队报告（JEH注17）；AF IV 1123：Hargenvilliers汇总（Forrest）；AF IV 1124：1806—1810省级统计（JEH）。
- Woloch p.110 Table 1：优先补原页，确认是levy授权表还是含实现额。
- SHD检索命中“Levée, mise en activité et répartition … 1807–1811”：https://www.servicehistorique.sga.defense.gouv.fr/ark/24989，仅目录线索，未核原件。
- SHD“2121 Organisation de l’armée au XIXe siècle”，D.3 p.1有1831—1866平均军额表：https://www.servicehistorique.sga.defense.gouv.fr/ark/924569，仅检索目录摘要，未取原表。

**未完成项明示**：无全国1803—1814实到逐年表；1814年度命令总额空缺；Woloch原表空缺；Hargenvilliers/Darquenne原表空缺；七月王朝长期平均“和平军队”系列空缺。不存在用累计总额、地方样本或平均逃避率填补这些空缺的操作。
