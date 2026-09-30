# X2 · 大陆体系机器：封锁执行装置的能力包络、租金分配与反事实演化（1803–1848）

**卡片** t_6f3beb ｜ **Sister** 10038（数理马克思与异端政治经济）｜ **运行** r_5b1357a9c6
**单位定义**：不是"大陆封锁政策"，而是**执行该政策的物质装置**——帝国海关总署（Direction générale des douanes）及其边境旅（brigades）、宪兵与协助缉私的野战军、海关法庭（tribunaux ordinaires / cours prévôtales des douanes）、许可证签发链（内政部→皇帝亲笔）、特里亚农税则与枫丹白露焚货程序、以及与之共生的**反向装置**：保险人、承包商、背货人、转口港、受贿官员。
**方法标记**：【锚点】＝史实／文书（带来源）；【机制】＝史实类比或理论机制（带适用条件）；【推演】＝情景下的具体演变（高／中／低置信）。所有"MODEL"值可由本目录 `x2_model.py` 复算，输出在 `X2_enforcement_model.csv`（131行）。

---

## §0 判决先行

**主线判决（中高置信）**——本卡的核心论点，其余各节都是它的展开：

> 大陆体系的执行机器有一个**可量化的能力上限**，而这个上限的数值恰好落在灾难性的位置上：它能把走私的从价成本推到 **50–62%**，**足以排除英国工业品，却远不足以排除殖民杂货**。1810年的特里亚农-枫丹白露转向不是拿破仑的意志薄弱或腐败，而是**一台机器在触到自身上限后的理性重整**：既然抽租比禁绝更可行，就把走私成本国有化。由此产生的结构性后果是：**封锁越严格，法国财政越依赖它所要禁止的贸易**，而**执行失败的每一次修补都以新的兼并为代价，新的兼并又制造更长、更不可守的边界**。这条螺旋——而不是俄国的冬天——是大陆体系内生的、可以在1803年就推算出来的自毁机制。

**衍生判决：**

1. **（高）执行强度是可观测的价格，不是二值状态。** 莱茵边界的走私保费序列 6%(1800) → 10%(1801–02) → 26%(1806.10–1808.6) → 30%(1809.7) → **50%(1809末–1811)**，是本卡最硬的数据。Rowe明确给出成功判据："insurance rates pushed to a level where non-French wares simply became uncompetitive."（Rowe 2015, 印p.195）
2. **（中高）边际执行产出在保费≈50%处饱和。** 编制从1808年25,700增到1812年35,500，莱茵保费自1809年末的50%再未被推高；1809年新设的Rees–Bremen线保费只有**6–8%**，即**新建一条线的边际执行力接近于零**。
3. **（高）两渠道定理。** 批发渠道（整船整车、有承保、有合同）可被定价到近禁止水平；零售"渗透"渠道（filtration，妇孺背货）按重量的缉获率**≤5%**（1810年8月汉堡-阿尔托纳城门实测），按人次的缉获率才是1/3–1/4。前者供给一个大陆，后者供给一个城市。**机器能改变贸易的规模结构与地理，不能改变其存在。**
4. **（中高）财政自负盈亏在最严格年份即告失败。** 1809年法国关税净收 **11.6百万法郎**；同年海关编制27,200人，仅按最低级 préposé 年薪500法郎计的纯工资即 **13.6百万**——**工资吃掉关税收入的117%**（MODEL；注：海关同时征盐税，故不能把全部人事费记在关税账上，但方向不因此逆转）。
5. **（中高）Ellis法则：封锁效力与大陆军事投入成反比。** "the efficacy of the Blockade stood in inverse ratio to the extent of Napoleon's military involvements"（Ellis 1981, 印p.202）。**推论对本项目至关重要：S3（最严封锁）与大规模战争不相容；要最大化封锁，必须先停止战争——而停止战争又拆掉了封锁的理由。**
6. **（中高）对英伤害的最大值不是法国单方面能生产的。** Ellis：封锁对英国外贸打击最大的时段，是"大陆严格控制"与"英美关系破裂"**同时出现**时——1808上半年与1810–12（印p.203）。法国只掌握合取式的一半。
7. **（中）S5的体系终局不是关税同盟，而是"高关税财政国家＋条约化优惠市场"。** Ellis的裁决是明文的：拿破仑设想的"不是真正的关税同盟，而是服务法国利益的巨型**非**共同市场"（Ellis 2015, 印p.35）。但史实中**确实**长出过一条同盟原则的萌芽——1810年底各国重复课税逼出的"**按消费税征收、一次完税后自由流通**"安排（Heckscher 印p.227）——它由财政压力内生，而非制度设计。本卡给出S5下关税同盟化的概率带（见§⑯）。
8. **（高）"执行失败→兼并"的螺旋有完整的史实链**：Kehl 1808-01-21并入以保莱茵渡口 → 荷兰 1810-07-09 → 汉萨与北海岸 1810末 → 提契诺 1810-10 被5,000–6,000意军＋"一支好的海关与宪兵分遣队"占领 → 贝格1811年4月4,000人签名请愿求并入**被拒**。**被拒的理由是纯粹的执行地理学**：莱茵河是可守的线，贝格东界"devoid of any major natural obstacles"（Rowe 印p.195）。这条史实给出了**行省化的一个非政治的、技术性的边界判据**。

---

## §1 这台机器是什么：规模、编制与地理

### 1.1 人力（【锚点】）

| 年份 | 海关人员 | 来源与层级 |
|---|---|---|
| 1801 | 12,500 | AHAD转Schneider 2020／Clinquart（二手）|
| 1808 | 25,700 | 同上 |
| 1809 | 27,200 | AHAD转《Cahiers d'histoire des douanes》n°24 (2001) |
| **1812** | **≈35,000**，其中 **agents de bureaux 4,000＋brigades 30,750** | **Rowe 2015 印p.187（本卡首选口径，因其给出内部构成）** |
| 1813 | 35,500 | AHAD |
| 1814 | 23,000 | AHAD |

配套力量：帝国宪兵队 **1810年逾18,000官兵**（Ellis 2015 印p.32，转Emsley）；共和十一年霜月16日敕令准许省长征调 **50名步兵＋20–40名骑兵**的分遣队协助缉私，约 **1,300步兵＋220骑兵** 分配于安特卫普、克莱沃、科隆、美因茨、斯特拉斯堡、贝桑松、日内瓦七个总监区，**军人同样分缉获提成**；AHAD的结论一句话："Séduisante, l'expérience est finalement un échec, **les soldats se faisant fraudeurs**!"（`downloads/pages/c829da0ae0b4.md`）
1810年秋另有**正规野战军**直接充当缉私队：Oudinot（原Masséna）军团布防布洛涅—布拉班特—荷兰海岸，最强一师驻埃姆登；达武第三军——Thiers称为"the finest, most reliable, and best organized"、大陆和平期**全军唯一保持战时编制**的军——三个师六十个步兵营、80门炮、胸甲骑兵一师、轻骑兵一师、攻城列车、河口炮艇队；1810-09-28致达武信"expressly declared that the two divisions stationed along the German North Sea coast had as their sole task the prevention of smuggling"（Heckscher 印p.224）。
**本卡判读**：把帝国唯一的战备军团用作缉私队，是"执行能力已触顶"的最直接指标——因为再往上加，就只能加战争机器本身。

### 1.2 地理与密度（【推演·MODEL】）

- 地区总监区（directions）1800年**25个** → 1812年**40个**，分四大区；第四大区含安特卫普、鹿特丹、阿姆斯特丹、格罗宁根、埃姆登、汉堡、吕讷堡、韦瑟尔、科隆、美因茨、斯特拉斯堡（AHAD）。
- 莱茵并合四省的边境旅 **3,200人 ＝ 每十万人口241人**，Rowe指出"matches almost exactly the relative number of police in present-day England and Wales"（印p.187）。
- **MODEL**：以1812年疆界估计须守线长 8,000／10,000／13,000 公里三档（海岸线长度随量尺变化，故给区间），则30,750名边境旅人员对应 **3.84／3.08／2.37 人/公里（在册）**；扣除三班轮值与病假、押解、出庭，取同时在岗比例 0.20／0.28／0.35，得 **同时在岗哨兵 0.47–1.35 人/公里**，即**每名哨兵的视距责任段 0.74–2.1 公里**。
- 自校验：莱茵优先线按荷兰边界—巴塞尔约700公里计，3,200人＝ **4.57 人/公里**，约为帝国平均的1.5–2倍，与"莱茵是重点线、Rees–Bremen是薄弱线"的定性叙述一致。
- **人员来源**：莱茵四省海关人员仅约 **3% 为本地人**，**逾80% 来自"旧法国"**，其余主要为比利时各省（Rowe 印p.187）。→ 机器是**外来占领式**而非**本地嵌入式**：情报差、语言隔阂、合法性为零，且全部薪饷是纯外流。

### 1.3 法律装置（【锚点】）

| 文书 | 日期 | 核心内容 |
|---|---|---|
| 柏林敕令 | 1806-11-21 | 宣布不列颠诸岛处于封锁状态 |
| 米兰敕令 I / II | 1807-11-23 / 12-17 | 凡曾停靠英港或受英舰检查者"去国籍化"并没收 |
| Rees–Bremen 海关线 | 1809-07-18 | 新设内陆关线拦截自荷兰入德货流；**保费仅6–8%，实质失败** |
| **缉获品法令** | **1810-01-12** | 军舰或持照私掠船所获敌货，缴 **48%** 关税可入境（"origines permises"）；《Bulletin des lois》4e sér., bull.260, no.5,122 |
| **圣克卢敕令** | **1810-07-03** | 对敌贸易特别许可证扩及"旧法国"港口（Ellis 2015 印p.37）|
| 荷兰并入敕令第10条 | 1810-07-09 | 存货按价值 **50%**（或按申报时点40%/50%）课税；**距法国边界四日行程内的殖民品存货一律受法军检查**；可实物或期票缴纳 |
| **许可证敕令** | **1810-07-25** | 自8-01起，赴外国港口的船必须持**皇帝亲笔签署**的许可证；域内航行需 acquit-à-caution 加保结。理由：无 grand commerce 可不停靠英港，而停靠即构成米兰敕令下的没收事由 → **许可证在法理上是对帝国两大基本法的逐船豁免权** |
| **特里亚农税则** | **1810-08-05**（9-27补充约三十税目）| 殖民品按 **每100公斤** 从量征收；战利品货与许可证货仍分别适用40%／50% |
| **枫丹白露敕令** | **1810-10-18（档案作19）** | 走私首领十年苦役＋右肩烙印 **"V.D."**（＝ *Voleur des Douanes*；德语边区亦读作 *Viel Dumm*，Ellis 印p.202注10引Dufraisse）；殖民品走私四年苦役；禁品（工业制品）**公开焚毁**；设 **cours prévôtales des douanes** |
| 意大利王国配套令 | 1811-01-29 | 十八条，仿枫丹白露；第十一条规定公开焚货（Grab 2015 印p.106）|

**焚货的法源不是拿破仑的独创**：Heckscher指出其先例在**英国十七世纪立法**，至乔治三世初年（3 Geo. III, c. 21）仍重复；1810-12-09《Moniteur》即拿英国近例做文章（印p.203）。**本卡判读**：焚货是重商主义惩罚传统的重启，其功能是**示范**（"a very cunning display of power"）而非**执行**。

### 1.4 特里亚农税率（【锚点】，据Heckscher附录II页图人工读取，OCR失败）

每100公斤法郎，"1810"列即特里亚农：

| 货品 | 1802–03（外国殖民地）| 1806 | **1810** |
|---|---|---|---|
| 原糖 | 45 | 55 | **300** |
| 黏土糖(clay) | 75 | 100 | **400** |
| 咖啡 | 75 | 150 | **400** |
| 可可 | 75 | 200 | **1,000** |
| 绿茶 | — | 3（另从价10%）| **600**（其他茶150）|
| 丁香 | 9 | — | **600** |
| 胡椒（白／黑）| 60 | 150 | **600／400** |
| 优质肉桂／胭脂虫／肉豆蔻 | 旧税则未列 | — | **2,000** |
| 靛蓝 | 15 | — | **900**（1813-01再升 **1,100**）|
| 原棉（正文，非附录）| 1804 ＝ **1** | 1806 ＝ **60** | 南美与长绒佐治亚 **800**；黎凡特海路 400；其他（那不勒斯除外）600 |

⚠️ **口径警告**：附录II在扫描本中为**旋转90°排版**，OCR全部失败，上表由 `doc_page_image` 渲染后人工读取。**1810列字号大、位置明确，可冻结**；1802–1806各列字号小且有花括号合并格，**个别数（尤其胡椒、可可、丁香的旧率）可能误读，不得单独引用**。其中原糖300、咖啡400、可可1,000、肉桂/胭脂虫/肉豆蔻2,000、靛蓝900五项与Heckscher正文印pp.201–202独立吻合，可用。

**MODEL**：以1812年伦敦最优质糖 1.35–2.00 法郎/公斤为计税基准，特里亚农原糖税 3.00 法郎/公斤的**从价等价为 150%–222%**——**远高于任何观测到的走私保费（最高62%）**。这在数学上决定了：**只要走私渠道物理可用，合法渠道在价格上永远劣于走私渠道**。特里亚农之所以仍能收到钱（1810-08至1811年底 **105.9百万法郎**，Heckscher 印p.221），靠的不是竞争力，而是**四日行程强制申报＋法军搜查＋实物缴税＋期票缴税**这一整套**存量清算**手段，即对**已在境内的库存**一次性课税，而非对**新增流量**常态课税。→ 这是个**一次性掠夺**，不可作为长期财政基线（与F4卡"1810高关税是S3被松动＋一次性掠夺的产物"的判定独立同向）。

---

## §2（单位模板①）决策结构与政治制度

【锚点】**谁决策**：海关总监（directeur général）Collin de Sussy，继任 François Ferrier；总署设巴黎 Uzès 府，1805年起已近百人办公；四名总监察负责巡查各总监区（AHAD）。**但真正的决策节点是皇帝本人**：1810年8月起许可证由拿破仑**亲笔签署**，并**每周**过目"tableau des résultats généraux du Commerce par licence"（AHAD `downloads/pages/f8bbb3026c57.md`）。

【锚点】**否决点与派系**：
- **财政派 vs 封锁派**：Collin de Sussy 与 Montalivet 提出"国家与走私者竞争"的方案——关税率"精确对应此前走私业所需成本"，货量不变而利润归国家（Heckscher 印pp.197–198）。这是**帝国内部对封锁原教旨的第一次成功颠覆**，且颠覆者是执行机器自己的首脑。
- **军政派**：达武是"very few persons who from the beginning to the end really made the resolute execution of the Continental System the lodestar of all his conduct"（Heckscher 印p.197）——**严格执行者是稀缺品，且其稀缺性本身是体系的结构特征**。
- **藩属否决**：特里亚农税则起初"remained a dead letter in all the states of the Confederation of the Rhine, **except Baden**"；普鲁士与萨克森试图把原料排除在税则外；"the somewhat more independent states, such as **Russia, Austria, and Sweden, never, so far as is known, introduced the tariff as a whole**"（Heckscher 印p.225）。Heckscher判断正是1810年8–9月这种消极抵抗逼出了10月的枫丹白露敕令。
- **地方法团否决**：科隆商会为本市争取豁免；但1811年贝格制造商请求并入法国后，科隆商会**立刻改口赞美莱茵关税**（Rowe 印p.194）——**执行边界的位置决定了地方资产阶级的立场，而非相反**。

【锚点】**正统性**：机器没有任何本地正统性来源。1798-11科隆约1,200人围攻查扣咖啡的海关员，**市政当局与市民卫队旁观**，事后不上报并称"全是海关员的错"（Rowe 印p.192）。

【推演·中高】在S2／S5（大陆和平）下，这台机器的**决策结构会向财政派倾斜并固化**：皇帝亲签许可证在和平期不可持续（F1卡给出中枢书面决策容量≈3,000–4,200封/年，1811年折年4,190为峰值），必然下放到总监署，**许可证由"皇帝恩典"变成"可预期的行政许可"**——这正是它从"配给租金"转为"稳定商业权利"的唯一通道，也是本卡认为S5存在"有限关税同盟化"入口的行政前提（见§⑯）。

---

## §3（②）法律司法与行政渗透

【锚点】**司法产出的可量化侧面**：
- 1812年汉堡 *Le Grand Prévôt* 在**两周内判出120个六月徒刑**，全部为违反封锁令；汉堡监狱爆满，**100名囚犯转送安特卫普苦役船**；不来梅监狱条件致 **22½% 的囚犯死亡**（Heckscher 印p.223，据Rist与Bourrienne）。另有死刑判决并执行，而枫丹白露敕令本身并无死刑依据。
- 莱茵四省送至南锡 cours prévôtale 的 **123案中仅2例处死**（Rowe 印p.192）。
- 科隆初审法院1803–1811：受审走私者**三分之二只处罚金**（Rowe 印p.192）。
- 科隆监狱结构变化：1806年6月100名囚犯中走私犯**5名**；1811年9月106名中**39名**为海关罪（Rowe 印p.192）。
- 罪刑差别被走私者精确利用：**contrebande（禁品）** 可至五年徒刑／十年苦役加烙印乃至死刑；**fraude（应税品逃税）** 最高六个月轻罪刑＋通常为货值三倍的罚金＋五年警察监视（Ellis 1981 印pp.201–202）。Ellis读出："the customs tribunals were disposed to convict on the lesser offence where they could not reasonably acquit suspects"。南锡法庭与警务记录显示走私者**熟知**：个人被捕比结伙被捕判得轻；携带"两用"器具（刀）比携带火器判得轻（Rowe 印pp.193–194）。

【机制】**司法渗透的三重漏斗**：本地陪审／法官同情 → 罪名降格 → 刑罚打折。结果是**名义刑罚的威慑力与实际预期刑罚脱钩**，而走私业的保险精算恰恰定价**实际**预期刑罚。这解释了为什么枫丹白露敕令（名义刑罚暴增）没有把保费推上60%以上。

【锚点】**行政渗透的反面**：克莱沃总监 Turc 任期十二年缉获极少，**其手下400名海关人员中超过三分之一从未有过任何缉获**（Rowe 印p.191）。日内瓦七个月内**80名海关官员因共谋舞弊被撤职**（Heckscher 印p.196）。利沃诺海关总监估计**其部下三分之二受贿**（Marzagalli 1996, p.70）。

【推演·中】S5和平期，若（i）取消 cours prévôtales 回归普通法院、（ii）把海关人员本地化比例从3%提到30%以上、（iii）把 préposé 薪资从500法郎提到能覆盖贿赂机会成本的水平（利沃诺案：月薪40法郎 vs 单次贿赂200–300法郎，即一次贿赂＝5–7.5个月工资），则**保费可在不增加编制的情况下再上推10–15个百分点**（MODEL，无直接史实校准点，置信中低）。但（iii）的财政账立刻失衡：把35,000人年薪从500提到1,500法郎，年增支 **35百万法郎**，已超过1809年全部关税净收的三倍。**这是执行机器最干净的不可能性证明：它无法同时廉价与廉洁。**

---

## §4（③）财政货币金融：这台机器的收支

### 4.1 收入侧（【锚点】，三套口径并列，禁互填）

| 口径 | 1806 | 1807 | 1808 | 1809 | 1810 | 1811 | 1812 |
|---|---|---|---|---|---|---|---|
| Heckscher 印p.197（法国关税净收，百万法郎）| 51.2 | 60.6 | 18.6 | 11.6 | — | — | — |
| Marion IV（F4卡，净额）| — | — | 18.559 | 11.552 | 普通35.881＋非常61.046 | 推算普通34.42＋非常44.88 | — |
| AHAD／《Cahiers》n°24（不含盐税，疑为毛额）| — | 77 | — | 30 | 70 | — | 109.5 |

**口径裁定**：Heckscher与Marion几乎同数、方向一致，**但极可能同源于法国官方海关账，不构成独立互证**；AHAD一列高出一个台阶，未给原表，**本卡列为"毛口径上界"不入计算**。

另有一次性大额：
- 特里亚农起至1811年底海关收入 **105.9百万法郎**（Heckscher 印p.221）；Marion记1810-08→1812-01非常关税累计 **105.927667百万**（F4卡）——**几乎同数但区间端点不同**，引用须标区间。
- 1810年剩余月份**没收品拍卖现金≈150百万法郎**（Thiers，转引自Heckscher 印p.222）。
- 荷尔斯泰因存货按特里亚农税率放入汉堡：**实物缴税19.7百万，合计42.5百万**（Heckscher 印p.226）。
- 法兰克福1810年10月一役对法国国库产出 **9百万法郎**（Darmstädter，转引自Heckscher 印p.226）。
- 1808年3月意大利王国把查获英货变卖后**向巴黎解送150万法郎**（Grab 2015 印p.102）。

### 4.2 支出侧（【推演·MODEL】）

- préposé 年薪 **500法郎**（Rowe 印p.191）；利沃诺海关人员**月薪40法郎**（Marzagalli p.70）——两数不矛盾（480 vs 500），互为旁证。
- MODEL：35,000人×500法郎 ＝ **17.5百万法郎/年**（纯最低级工资）；计入军官、总监、办公、船艇、武器、诉讼与监狱的间接费乘数1.6／2.2，得 **28.0／38.5百万法郎/年**。
- **关键比值**：1809年编制27,200人，纯工资 13.6百万 ÷ 当年关税净收 11.6百万 ＝ **117%**。若用1812年编制与同年AHAD毛收入109.5百万比，则降至16%——**这正是"严格版"与"许可证版"的财政分水岭**。
- 限定：海关自1806-03-16起兼征盐税，故不可把全部人事费记在关税账上；但（a）盐税是内地税、其征收不需要30,750人的边境旅，（b）比值的方向与量级不因此逆转。

### 4.3 货币与金融面（【锚点】）

- 拿破仑1810-05-29致Gaudin：**"My intention is to favour the export of foodstuffs from France and the import of money from abroad ... I should be very much inclined to let the smugglers in only at Dunkirk"**（Heckscher 印pp.192–193）。→ 走私者被编入**贵金属回流政策**，敦刻尔克因此"exempt from the general crippling of economic life in the ports"。
- 1811-01 科隆警务报告指控当地海关与 **Oppenheim、Schoeffen、Cassel** 三家金融号合谋从事**货币投机**（Rowe 印p.191）。
- 普鲁士允许以**市价59.5%的政府债券按面值**缴纳特里亚农税，再用普鲁士完税证明放货过境；1811年春夏该证明被宣布无效并二次查抄（Heckscher 印p.227）。→ **执行机器同时成了藩属国债券的做市商**。
- 皇帝把贿赂收归己有：柯尼斯堡领事 Clérembault 放行14艘英船（货值280万法郎），一案得80万、合计150–160万法郎；皇帝令其上缴外交部，并拟令 Bourrienne 缴200万、Lachevardière 缴50万给偿债基金；Clérembault 已先自付50万入皇帝私库(caisse de l'extraordinaire)。1811-01-01致Champagny信结语：**"You will see that I shall get the money for a really handsome palace which will cost me nothing."**（Heckscher 印pp.203–204）

【推演·中高】**S3严格版的财政结构是自毁的**：取消许可证与特里亚农，则非常关税→0–15百万/年、总关税由1810年的≈97百万落到 **15–35百万/年**（F4卡补订②），而执行成本**不降反升**（越严格越需人力）。以本卡MODEL的28–38.5百万执行成本计，**S3严格版下海关系统在国库净账上为负**。这一点在1809年已经实测过一次。

---

## §5（④）它管制的贸易：结构、转口港与价格

### 5.1 四大转口港（【锚点】）

| 港 | 关键数字 | 来源 |
|---|---|---|
| **黑尔戈兰** | 1808年英国花 **£500,000** 在这个约150英亩的小岛上修港、筑垒、建仓；约 **200名**英商与商号代表迁入并组成专门商会，人称"Little London"；1808年8–11月三个半月内**近120艘船**卸货；英商自估年进口 **£8,000,000**≈1808年英国出口总额(£50,000,000)的近六分之一——**Heckscher明说"almost certainly too high"** | Heckscher Part III ch.II（econlib全文对照；本地PDF印pp.178–179）|
| **哥德堡** | 1810-09 总督 von Rosen 记锚地 **19艘英国军舰＋1,124艘商船**，"such an appearance as it had never had since the Creation"；某日东风转向"several hundred vessels sailed away at the same time"。进口1807→1809翻两番，1810再增至五倍。**1810年原糖出口14,500,000磅（约为上年两倍）、咖啡4,500,000磅**（1808年为2,900,000磅与1,300,000磅）。11月给 von Rosen 的训令：对挂美旗等可接受旗的瑞典臣民货船，"His Majesty does not require you to recur to extremities of diligence, but on the contrary to **suppress facts and facilitate traffic**" | Heckscher 印p.236；1808数据见Part III ch.II |
| **马耳他** | 英国对马耳他出口年均 **£95,000(1801–05) → £3,000,000(1808) → £5,000,000(1812)**；在马英商 **5(1802)→20(1807)→60(1812)**；**1812年运往欧洲的英货有25%经马耳他**；Crouzet另记"at one point, 8.8% of exports from Britain were taken into Europe via Malta" | Grab 2015 印p.103；Crouzet 1987 转引自 Juhász (AER 2018) |
| **直布罗陀** | 1706年即为自由港，不受《航海条例》约束；1809年靠港船 **1,014艘＝1806年的三倍**，其中为本地市场载货者增至348艘；另有868艘以上西葡小船的周度记录（实际逾千）；1813年降至771艘 | Benady, um.edu.mt PDF（Gibraltar Chronicle 逐年统计）|

另有**里斯本**与**萨洛尼卡**两端：Heckscher记走私"from Gothenburg in the north-west around all the coasts of Europe to **Saloniki** in the south-east, without any great variation in the methods"（印p.191）；巴尔干段用不超过200公斤的小箱由驮畜经波斯尼亚、塞尔维亚、匈牙利运往维也纳。

### 5.2 贸易的地理再排（【锚点】＋【机制】）

Bacher（法国驻莱茵邦联公使）**1810-10-02**报告已把结果预言完毕：
> "the **Danube will now take the place of the Rhine** as the channel through which the states of the Confederation of the Rhine will in future be able to provide themselves."
并预言：即使萨克森王把关税警戒线从维滕贝格延到波希米亚边界并对原棉课税，"this painful sacrifice, which would reduce the whole of the mountainous part of Saxony [Erzgebirge] to the deepest misery, **would be no profit to France. It would only enrich the government and merchants of Austria**"；棉纺工人将"be compelled to emigrate from Saxony and Voigtland, and even from Bavaria, Baden, and Switzerland, in order to seek their livelihood in **the Austrian factories erected and managed by Englishmen**"（Heckscher 印pp.231–232，据Schmidt《Le Grand-duché de Berg》刊本）。

史实兑现：维也纳取代莱比锡成为大陆贸易枢纽；货路两条同赴**加利西亚的 Brody**——北线经普俄波罗的海港绕华沙公国，南线先自敖德萨过黑海、法俄开战后改经君士坦丁堡与萨洛尼卡至伦贝格；再经**巴伐利亚免税过境**输往南德、瑞士并走私入法（Heckscher 印pp.232–233）。1811年夏起莱比锡集市上英货"practical cessation"、殖民品亦降至微量（印p.230）。

**Heckscher对"为什么萨克森反而守法"的解释是本卡反应函数的关键机制**：萨克森有"a genuine good-will to obey the system"，因为其繁荣的纺织工业**受益于排斥英国竞争**，而法兰克福无此利益（印p.230）。→ **执行力最强处＝本地产业利益与禁令一致处**。这不是宪兵密度的函数，是产业结构的函数。

### 5.3 价格与数量（【锚点】）

**殖民品价格（涨）**
- 莱比锡糖价"rose almost uninterruptedly until 1813, when it was approximately **three and one-half times** the amount it had been seven years earlier"；巴黎糖价1810年为 **4法郎/livre**、其后 **6法郎/livre**（Heckscher折为 **≈8与≈12法郎/公斤**）；1812年伦敦最优质糖仅 **1.35–2.00法郎/公斤**，即法国价为伦敦价的 **4–9倍**（Heckscher 印p.292）。
- 靛蓝在莱比锡通常为原价 **2倍**，有时 **3、4乃至5倍**；胭脂虫、染木等通常翻倍（印pp.289–290，转引König）。

**出口农产品价格（跌）**
- 梅梅尔：木材大量烂在码头，**谷价1806→1810跌60–80%**（转引Hoeniger）；
- 不来梅：殖民品价"increased many times"的同时，**小麦价1806→1811跌62%**，黑麦同（转引Schäfer表IX）（Heckscher 印p.319）。
- 罗斯托克出港船：1809-08至1810-07为 **249艘**，而1808/09为55艘、1810/11为31艘（转引Stuhr）——**波罗的海的高峰由法瑞芬兰战争结束后的对瑞贸易造成，随后被许可证制度亲手掐死**（Heckscher 印p.319）。

**MODEL｜双向贸易条件冲击**：以"糖涨3.5倍÷麦跌62%"计，大陆内地农业出口者的实物贸易条件恶化约 **9.2倍**；若用梅梅尔的−80%，恶化 **17.5倍**。这是一个**大陆内部的**、非跨境的剪刀差，**没有任何一笔法国关税收入能补偿它**。它也是Ellis所说"封锁末年波罗的海与地中海藩属国农产品价格蠕动式萧条 → 购买力下降 → 反过来减少对帝国出口品的需求"这一**自喷式需求回路**的定量表达（Ellis 2015 印p.37）。

**运费即关税**（Tooke《History of Prices》I, pp.309–310注，转引自Heckscher 印p.233），1809–12 vs 1837：小麦每夸特 **50先令 vs 4先令6便士**；大麻每吨 **£30 vs £2 10s**；木材每load **£30 vs £1**；一艘一百余吨的船自加来至伦敦往返的**运费加法国许可证费可达£50,000**，折靛蓝每英磅运费4先令6便士（1837年为1便士，即**1/54**）；一艘总值£4,000的船自波尔多至伦敦往返毛运费 **£80,000**。

**莱茵河上行通行税收入（Spaulding 2015 表7.1–7.4，法郎）**——本卡所见最好的数量序列：

| 1806 | 1807 | 1808 | 1809 | 1810 | 1811 | 1812* | 1813 |
|---|---|---|---|---|---|---|---|
| 1,273,645 | 1,386,585 | 715,498 | 380,773 | 405,127 | 365,997 | 330,415* | 294,833 |

（*1812为1811与1813之中点估计）**1811年仅为1807年的四分之一，1813年为五分之一。** 且衰减随距荷兰边界的距离而递减：1811占1807之比——埃默里希15%、韦瑟尔18%、科隆23%、杜塞尔多夫23%、科布伦茨33%、美因茨51%、曼海姆43%、诺伊堡78%；斯特拉斯堡上行到货1811年仍为1807年的53%。**下游崩掉四分之三，中游三分之二，上游不到一半。**

---

## §6（⑤）撷取与动员上限：**执行能力上限的正式表述**

### 6.1 唯一连续可观测的执行强度指标：走私保费

| 时期／地段 | 保费（占货值）| 来源 |
|---|---|---|
| 莱茵关税线设立半年后（1798-12，Wirion报告）| **6%** | Rowe 印p.189 n.6 |
| 莱茵 1800 | **6%** | Rowe 印p.195 n.27 |
| 莱茵 1801–02 | **10%** | 同上 |
| 执政府期（Eichhoff 备忘录）| **10、15，甚至20%** | Rowe 印pp.188–189 n.5 |
| 莱茵 1806-10 → 1808-06 | **26%** | Rowe 印p.195 n.27 |
| 莱茵 1809-07 | **≈30%** | 同上 |
| **莱茵 1809年末 → 1811** | **≈50%** | 同上 |
| 法国边界一般（1809）| **30%** | Heckscher 印p.194 |
| 斯特拉斯堡顶级承保人（1809）| **40–50%** | 同上 |
| **Rees–Bremen 新关线（1809设）** | **6–8%** | Rowe n.26＋Heckscher 印p.194（两源） |
| 荷尔斯泰因→汉堡（1809）| 与上同率 | Heckscher 印p.194 |
| 海岸→杜塞尔多夫／美因茨／法兰克福（1810-09警务简报，保险＋运输合计）| **＋50%** | Rowe 印pp.197–198 n.34 |

**Rowe给出的成功判据**（印p.195）：
> "A lower threshold for judging the intended 'success' of Napoleon's Continental System will do; **insurance rates pushed to a level where non-French wares simply became uncompetitive.**"

### 6.2 能力上限的三条定量命题

**命题1（执行的边际产出在≈50%处饱和）。** 编制自1808年25,700增至1812年35,500（＋38%），并在1809–11年间叠加了：Rees–Bremen线、荷兰并入、汉萨与北海岸并入、达武第三军全军缉私、枫丹白露刑罚暴增、cours prévôtales。**莱茵保费自1809年末的50%再未被推高**；而1809年新建的Rees–Bremen线只能把保费推到 **6–8%**——**新建一条线的边际执行力几乎为零**（这条线的失败Rowe明确归因于"devoid of any major natural obstacles"）。**→ 执行能力的上限不是人数，是地形与本地合作**。

**命题2（两渠道定理）。**
- **批发渠道**（整船整车、有合同有承保）可被定价到 AVE **50–62%**（保费50% ＋ MODEL绕道运输附加5/12/25%）。
- **零售渗透渠道**（filtration）：1810年8月汉堡—阿尔托纳城门查获 **9,300公斤**殖民品，Marzagalli据档案判断"this quantity seems to have represented **at most five percent** of the quantity smuggled"（p.69）→ 该门当月通过量 **≥186吨**。而Rist的描述是海关"每三四个背货人抓一个"（Heckscher 印p.190）——**两者不矛盾而是不同口径**：按人次高、按重量低，因为"a dense column was formed, some heavily armed persons in the van were sacrificed, and the others burst through like a whirlwind"。
- **推论**：批发渠道供给一个大陆，零售渠道供给一个城市。机器能关掉前者的**大部分**，关不掉后者的**任何部分**。它因此**改变贸易的规模结构与地理，而不改变其存在**。
- Ellis对两种形态有同期官方命名：1808-05-06 Magnier-Grandprez 报告称下莱茵省是 *contrebande par filtration*（渗透式），上莱茵省则是"a much more organized business, practised very often by roving bands of twenty or thirty racketeers"（Ellis 1981 印p.204）。

**命题3（上限的位置决定了政策的全部形态）。** 把命题1的上限（AVE 50–62%）放到需求曲线上：
- **英国工业品**：大陆有成本相近的替代者（萨克森、瑞士、阿尔萨斯、比利时），成本劣势估计在 **35–60%**（MODEL阈值区间）。50–62%的AVE**落在或高于**这一阈值 → 可以排除。史实兑现：1811年夏起莱比锡集市英货"practical cessation"（Heckscher 印p.230）；Rowe亦称1810–11年"it became more difficult to smuggle wares across the frontier"。
- **殖民品**：无替代者（靛蓝代用失败、甜菜糖1813年实产仅110万公斤），消费者愿付 **300–800%** 的溢价（巴黎糖价为伦敦的4–9倍）。50–62%的AVE**远低于**阈值 → 不可能排除。
- **∴ 特里亚农-枫丹白露的二分法（禁工业品／重税殖民品）不是拿破仑的妥协，而是对机器实际能力边界的精确描摹。** Heckscher自己也说，禁品焚毁这一半"the reason is the total absence of pecuniary interest, public and private, in obedience to the latter regulations"（印p.228），而财政这一半"formed beyond comparison the most effective half of the new system"（印p.221）——他把因果讲反了一半：不是财政动机腐蚀了封锁，而是**封锁的能力边界迫使它财政化**。

### 6.3 Ellis法则：效力与战争成反比

> "One general 'rule' is that the efficacy of the Blockade stood in **inverse ratio** to the extent of Napoleon's military involvements on the Continent at different times. When he was on campaign and needed his troops, customs surveillance tended to lapse and smuggling became easier. When he was at peace with Continental states, exception made for Spain after 1808, surveillance was usually tighter, never more so than in the newly annexed parts of northern Europe in 1810-12."（Ellis 1981 印p.202）

> "the Blockade had its greatest impact on British foreign trade when periods of comparatively strict customs control on the Continent **coincided with a rupture in Anglo-American relations**. Again this was the case in 1810-12, as it had been during the first half of 1808, before the general laxity which set in later that year and especially during 1809."（同上 印p.203）

**本卡对两条法则的推演（中高置信）**：
- 合取条件 **C＝（大陆严格控制）∧（英美断裂）**。1803–1814年间C只成立过两段：1808年上半年、1810–12年。**法国只能生产合取式的一半**；另一半由伦敦（枢密令）与华盛顿（禁运／非交往法／1812战争）共同决定。
- 由此得到**本项目最重要的政策推论之一**：**S3（绞杀版封锁）的效力峰值需要和平，而S4／对俄战争／半岛战争都在直接消耗它。** 1812年把30,750人边境旅所守的体系交给一场60万人的东征，等于在效力函数的两个自变量上同时取最差值。

### 6.4 能力上限的**空间**形式：可守线与不可守线

| 线 | 观测保费 | 地形判词 |
|---|---|---|
| 莱茵河（荷兰边界—巴塞尔，≈700km，3,200人，4.57人/km）| 26%→50% | 河流为天然线；Rowe：河比贝格东界"far more viable as a customs frontier **in policing terms**" |
| Rees–Bremen（1809-07-18设）| **6–8%** | "devoid of any major natural obstacles" |
| 阿尔萨斯—瑞士—巴登段 | 走私"more or less ubiquitous" | Crouzet：走私**沿内陆边界比沿海边界更活跃**（*Économie britannique* i.139，转引自Ellis 1981 印p.203）；原因＝次级道路网、河岛、林地山地，以及法兰克福、达姆施塔特、曼海姆、海德堡、拉施塔特、凯尔、奥芬堡、拉尔，**尤其是巴塞尔**这一串境外转口地 |
| 北海—波罗的海岸 | 1810–12最严，但黑尔戈兰/哥德堡仍在 | 岸线破碎；不来梅"amphibious nature of the coast"（Vandal语，转引自Heckscher 印p.190）|

**MODEL｜可守性判据**：一条线可被推到高保费，当且仅当（i）有连续天然障碍或单一渡口结构，（ii）两侧无近距境外转口地，（iii）本地产业利益与禁令同向。莱茵线满足(i)(ii)部分、萨克森满足(iii)；Rees–Bremen三项全不满足。**这条判据比"每公里多少人"更能预测执行绩效。**

---

## §7（⑥）军事：海关作为准军事组织，以及军队作为走私者

【锚点】海关被Clinquart（经AHAD转述）称为"une armée parallèle"；1810年拿破仑即要达武拟"把海关旅置于其麾下"的方案，1812年令Mathieu Dumas 说服 Collin de Sussy 起草**把35,000名海关人员组成武装力量**的法案，"ce projet resta à l'état d'embryon"。1813-08-17 达武下令以吕讷堡总监区人员编成两个800–900人营（第2帝国海关团，含步兵、一个骑兵中队、一个炮兵连乃至一支水上分队）；另有以布洛涅至巴约讷11个总监区 **10,685名 préposés** 编成19个不等员额营的方案（AHAD `downloads/pages/c829da0ae0b4.md`）。
【锚点】反向：军人参与走私。协助缉私的士兵领取缉获提成，结果"les soldats se faisant fraudeurs"；莱茵河上**七名将军**参与运送违禁品；Georgeon将军娶入科隆粮食走私家族并用宪兵职权协助（Rowe 印pp.192–193）。符腾堡国王"even appears to have had fraudsters acting on his account"（Rowe 印p.194）。

【推演·中】在S5（和平固化）下，海关旅的军事化会**完成**而非流产：35,000人的准军事边防军在和平期是**便宜的**（对照F2卡：法国常备40–45万在册，每兵年600–700法郎；海关员500法郎且不需马炮），且能吸收退伍军人。**这是S5下帝国最可能出现的新制度物种：一支不进攻、不会造反、按里程布防的经济边防军**——其1815年后的欧洲同类是普鲁士关税同盟的 *Grenzaufseher* 与奥地利的 *Finanzwache*。
【推演·中低】同一支力量在S3下会被战争抽空：1813年的实际结局就是海关员被编成营去打野战。

---

## §8（⑦）社会结构与阶层：**租金分配账**

### 8.1 谁拿到租金（【锚点】＋【MODEL】）

**（a）法国国库与皇帝私库。** 特里亚农起至1811年底海关 **105.9百万**；1810年剩余月份拍卖 **≈150百万**；荷尔斯泰因一役 **42.5百万**；法兰克福一役 **9百万**；贿赂收归的 Clérembault 50万＋拟收 Bourrienne 200万、Lachevardière 50万。**但这些是存量清算而非流量税**。

**（b）许可证持有人，其地理分布极度不均。** 1809–10年"ancien système"许可证中**波尔多独得三分之一以上**，利沃诺**一张未得**；1810年后的欧洲贸易许可证波尔多为利沃诺的2倍、汉堡的4倍；1810年恢复对美贸易的航行许可 **波尔多620、汉堡5、利沃诺1**（Marzagalli 1996 p.68）。许可证价：早期 30–40 napoleons（600–800法郎），汉萨出口证 800法郎＋小麦每吨30法郎／黑麦每吨15法郎"was regarded as cheap"，**自英进口殖民品的许可证高达300 napoleons ＝ 6,000法郎**（Heckscher 印p.216；AHAD同记6,000法郎上限）。MODEL：若年发2,000张、均价800法郎，得 **1.6百万法郎**；若2,000张按6,000法郎，得 **12百万**——**许可证费本身不是大钱；大钱是持证者赚到的垄断利润。**

**（c）走私业的资本层。** 枫丹白露敕令自己把这个行业分了层：`entrepreneurs / assureurs / intéressés / chefs de bande, directeurs et conducteurs / simples porteurs`——Heckscher评为"a complete hierarchy ranging downwards from the directors of the smuggling enterprises through the capitalists and officials to the unskilled workers"（印p.194）。而**风险分配与收益分配完全相反**：南锡海关法庭被审者中 **68.5%是较贫困者**（临时工、贫困工匠），**商人仅6.34%**，船夫／车夫／酒馆主合计略超10%（Rowe 印p.193，据Betrand档案研究）；Marzagalli：站在这些活动背后的商人"were almost never arrested"（p.70）。
**单项租金量级**：科隆一城一项商品——1811-12-04特别警务委员报告估计年经该城非法输入烟草 **逾100万公斤**；左岸帝国烟草3法郎/公斤、右岸16苏/公斤，每公斤差 **44苏＝2.20法郎**，**全年潜在利润220万法郎**；同期农业雇工日薪约 **1.50法郎**（Rowe 印p.197）→ 折 **约146万个农工日**。

**（d）受保护的内陆工业。**
- 阿尔萨斯：Ellis的总判是"Alsatian merchants and manufacturers were among those who **benefited most of all** from the inland orientation of the French economy ... the Blockade and the market design had done more to **enrich** than impoverish them"（Ellis 1981 印p.293）。斯特拉斯堡莱茵水运量"may have doubled and in certain peak months even **quadrupled**"（印p.289）；上莱茵棉业产出较1803–06均值升 **三分之一乃至一半**，约 **20–25%** 的产量出口（印p.290）。
- 克雷菲尔德 von der Leyen 丝织厂：1810年雇工 **3,000人**、年营业额 **300万法郎**，"higher than ever before"（Rowe 印p.193）。
- 萨克森棉纺：大陆体系最大工业赢家（Heckscher 印pp.230–232、302–306；G2卡已独立取证）。
- 科隆首富银行家 **Abraham Schaaffhausen** 大规模走私，所得部分用于投机国有财产；因非法出口小麦被罚 **10万法郎**而"hardly appears to have dented his finances"（Rowe 印p.194）——**同一人同时是保护租金与走私租金的收取者**。

**（e）执行机器自身。** 不来梅的原产地证明书等规费"increased tenfold during the first six quarters after the issue of the Berlin decree"（Heckscher 印p.195）；拿破仑估算 Bourrienne 在汉堡获利 **700–800万法郎**（印p.196）；Bourrienne 1807–10年签发的通行证每年放行 **约1亿法郎**货值（Marzagalli p.69）；1810年汉堡**约每六个居民中有一人靠这项舞弊为生**（法国驻汉堡海关总监语，同上）。

### 8.2 谁承担成本

- **沿海城市的劳动阶层**：Heckscher记"Unemployment, in particular, with its consequences in the way of mendicancy and vagrancy, is a consistently recurring theme"，"the death-like silence in the great coast towns, grass growing in the streets of La Rochelle"（印pp.320–321）。Marzagalli：商人"much more able than other professionals, such as artisans, shopkeepers, and longshoremen, to surmount difficulties"（p.65）。
- **东欧与北德的农业出口者**：见§5.3的−60~−80%与−62%。
- **藩属的竞争性产业**：贝格出口自封锁前6,000万法郎降至1811年1,100万（Grab，经上一轮卡 t_f81a6f 转引）；科隆1807→1809进口−38%、出口−63%，对荷进口−87%、出口−71%（Rowe 印p.194）；意大利王国丝织厂数 **489(1806)→401(1811)**（Grab 2015 印p.108）。
- **消费者**：糖3.5–9倍、靛蓝2–5倍。

### 8.3 分配的政治后果（【机制】）

租金的**集中度**与承担的**弥散度**恰好相反：得利者是少数可识别的大商号、内陆厂主与官员，受损者是港口工人、农业出口者与全体消费者。这产生两个后果：
1. **执行机器无法培育自己的支持联盟**：它最大的受益者（走私资本、受贿官员）在法律上是它的敌人，而它法律上的受益者（内陆工业）不需要机器本身、只需要关税。
2. **走私成为社会整合而非社会解体的形式**：Rowe指出走私"made Rhinelanders cohere rather than fragment. This was very much unlike banditry, which was the result rather of social breakdown"，并补上一句极重要的判断——这使镇压更难，因为"the authorities could not rely on the cooperation of elements within the local community who felt threatened"（印p.193）。**与西班牙、卡拉布里亚的对照在此**：莱茵兰不是无法统治，而是**被统治得很好却不服从这一条法律**。

---

## §9（⑧）社会运动与抵抗传统：走私作为政治行为

【锚点】三类形态，强度递增：
1. **司法不合作**：科隆初审法院1803–1811三分之二只判罚金；Ellis：海关法庭倾向于在不能合理宣告无罪时改定轻罪；“local 'notables' were called upon to judge local men”的普通海关法庭比军事委员会宽容（Ellis 1981 印p.202）。
2. **集体暴力**：1798-07-06莱茵关税生效后两日美因茨人群对峙查扪粮食的海关员；两月后宾根两名海关员被杀；Xanten一场“pitched battle”中海关分队被武装团伙击败；1798-11科隆约1,200人围攻（Rowe 印pp.191–192）。
3. **市政共谋**：市长们的共谋“might extend no further than hushing up smuggling activities. It might extend to providing smugglers with early warning of imminent searches by douaniers or, most seriously of all, it might culminate in **municipal administrations acting as the operational hub of smuggling operations**”（Rowe 印p.193）。

【锚点】**道德合法性的直接证言**：阿尔特基尔肯副专员报告：“l'opinion publique désigne plusieurs individus, **même des fonctionnaires publics**, qui doivent la faire ou la protéger; l'on peut dire que **grands et petits s'en mêlent**”；Lezay-Marnésia：“dans cette ville de marchands [Strasbourg], **il est reçu que l'on peut être en même temps contrebandier et honnête homme**”（Ellis 1981 印p.205）。拿抢勒斯经济学家 Galanti 称走私为“a useful trade, inasmuch as it prevents the ruin of the state”（Heckscher 印p.194）；伦巴底经济学家 Pecchio 称走私“so profitable that it seduced even honest merchants”（Grab 2015 印p.103）。

【机制】**走私是“最低成本的大众抵抗”**：Ellis称它“might even be regarded as **the most common form of popular resistance** to the rigours of Napoleon's customs severities, and beyond the frontiers it was often a function of local opposition to French rule as such”（印p.201）。Rowe给出了它与征兵、土医的**关键差别**：走私在莱茵兰人眼里是“victimless crime”，而土医有本地受害者、逃役使同乡青年被补征，故只有走私能获得**无异议的全社会支持**（印p.192）。

【推演·中高】对本项目“哪里能并、哪里必反”（Q1）的接口：**封锁执行产生的抵抗与征兵产生的抵抗是不同物种**。征兵抵抗产生逃兵、土医、局部暴动，可用武力镇压；封锁抵抗产生**全社会参与的、有组织的、不流血的不服从**，武力对它无效。前者威胁政权存续，后者只威胁政策效果——但后者的累积效果是**把地方精英与政权的利益绑定彻底切断**：1813年莱茵精英因恐惧骚乱而自掘腰包救济失业工人，**却拒不配合“Guards of Honour”的征集**（Rowe 印p.199）。

---

## §10（⑨）思潮、舆论与民族意识

【锚点】**马克思的命题及其反例**。Rowe以《德意志意识形态》一段开篇：“the lack of these products [sugar and coffee], occasioned by the Napoleonic Continental System, caused the Germans to rise against Napoleon, and thus became the real basis of the glorious Wars of Liberation of 1813.” 然后用实证反驳：科布伦ŭ的 Görres 在《Rheinischer Merkur》上谴责法国统治的理由是**征兵、重税、征发与法国官员的傲慢**，大陆体系“hardly figures in its pages”（Rowe 印p.187）。
【推演·中】但Rowe自己也承认贝格1813年1月起义“contributed directly”于经济困苦（印p.199）。**本卡裁定**：大陆体系不是民族觉醒的发动机，而是**合法性的慢性消耗剂**：它不制造民族主义话语，却使每一个商人、市长、法官与背货妇女每天都在**实践上**反对帝国法律。当民族主义话语1813年从外部到达时，它接管的是一个已经**习惯了不服从**的社会。
【锚点】体系内部的自由主义批评已在执政府期公开发表：Marc-Auguste Pictet 的七条——执行成本吞掉大部分收入；反欺诈措施反使欺诈增加；边境永久处于战争状态；执行者被暴露于腐败；窒息边境产业；苛法是雅各宾式紧急状态的倒退；强制进口替代把资本从法国有比较优势的农业转开，所生“faux”企业只能靠“artifice”维持（Rowe 印p.193）。→ **反事实推演不需要发明一套不存在的经济学：批评大陆体系的完整论证在1803年前已经印出来了。**

---

## §11（⑩）科技与生产力：代用品的三种命运

| 项目 | 【锚点】实绩 | 判词 |
|---|---|---|
| **Leblanc 制碱** | 发明约1789；Leblanc 1806年死前数年已破产；与西班牙的苏打供应中断后，价格自 **每100公斤80–100法郎降至10法郎**（Heckscher 印p.288）| **真成功**：封锁移除了一项已存在技术的采用障碍；衍生出肥皂、盐酸、氯、染料与印花（“Adrianople red”与Koechlin 1810–11年的进展“far exceeded what had been achieved in England”）|
| **菘蓝靖蓝** | 规定种植 **32,000公顷**、设三家帝国工厂、设奖；**1813年产出仅6,000公斤**，另意大利种植园500公斤印度靖蓝；1814年后仅一家工厂存活（印p.290）| **真失败**：“the whole episode vanished without leaving any traces behind” |
| **甜菜糖** | 1747 Marggraf 发现、Achard 1809发表；命令先种 **32,000** 后 **100,000公顷**（后项“never carried out”）；1813年2月内政部向立法院宣布可期 **7,000,000 livres（近3,500,000公斤）、334家厂“almost all”开工**；**同年稍晚向皇帝的报告：实得仅 1,100,000公斤，334张许可证中实用158张**；复辟后一家未存，两年后新开两家（其一为Chaptal）；**二十年代末在高殖民糖关税下重新站稳**（印pp.293–294）| **延迟成功，且成功条件是关税而非封锁**：“the contribution of the Continental System on this point turned out to bear fruit after the lapse of a decade and a half” |
| 葡萄糖 | 1810–11两年造出 **2,000,000公斤**并给补贴，但“black and did not crystallize ... repulsive and had an unpleasant odour”（印p.292）| 失败 |
| 咖啡／烟草代用品 | 菊苣、车厘、橡实、向日葵子、甜菜；烟草用鹅莓叶、栗叶、蓍草；**丹麦一国就有17家咖啡代用品工厂**（印p.291）| 消费降级的度量衡 |
| 意大利的官方试验 | 1810-09-12两道敕令：**150,000里拉**推广种棉、**50,000里拉**扶持葡萄制糖；“results remained limited”（Grab 2015 印p.106）| 失败 |

【推演·中高】**三种命运的判别规则**：封锁成功地傅育一项技术，当且仅当（i）技术在封锁前已成熟但因价格差而未被采用，（ii）投入品在大陆内部可得（海盐可得、热带靖蓝不可得），（iii）战后有关税保护接手。制碱全中，靖蓝一项不中，甜菜糖中(i)(ii)缺(iii)故延迟十五年。
【推演·中】**S5下的甜菜糖**：若帝国存续并维持高殖民糖关税（与复辟王朝同策），则甜菜糖产业的站稳时点不会早于1820年代末（因为制约它的不是禁令而是技术学习曲线与相对价格）；但**地理会不同**：史实中1814年后只有法国与普鲁士营建起产业，S5下会多出法属比利时、莱茵左岸、意大利北部三块（糖用与炼糖业集聚于已有化工与运输能力处）。置信度中；改判证据为1820年代比利时、莱兰糖厂数的实际分布。

---

## §12（⑪）生态、人口与资源

【锚点】Heckscher的总体判断（印pp.320–321）：与1914–18年的封锁相比，大陆体系对“人民需要的满足”的影响要小得多：纯消费品短缺“was little else than coffee and sugar, and, to some extent, tobacco”；其余短缺是工业原料（棉、染料，并及羊毛、亚麻、大麻、生丝），其后果是**失业而非缺衣少食**。Heckscher的术语是“continuous **dislocation**”而非生活水平持续下降。
【推演·中高】**这对反事实推演有两个强含义**：（a）大陆体系不会造成饥荒式的政权崩溃，所以它可以长期运行；（b）正因为不致命，它也不会自动产生“忍一忍就能赢”的厉害关系：受损者不会造反，但也不会服从。**它不是一个高张力的危机，而是一个低强度的、无终点的消耗战——而在消耗战中，输的是支付常设执行成本的那一方。**
【锚点】资源侧的反向例证：俄国对英贸易的结构性依赖——1804年彼得堡**35%的进口与63%的出口**掌在英商手中，**最大的三家（均为英商）单独占首都出口贸易的四分之一以上**（Oddy，转引自Heckscher 印p.318）；Savary 1807年7月报告称英人“took over all the timber from the nobility and thereby provided them with their safest source of income”。1807年11月拿破仑令Caulaincourt提议**法国政府为其船厂购买数百万法郎的桓材与海军物料**——“It is uncertain, however, whether this plan was ever carried out.”（印p.318）
【推演·中高，接R2卡】这条未执行的采购提议是**S2下最便宜的对俄政策工具**：它同时解决了（i）俄国贵族现金流、（ii）法国船厂材料（接F3卡木材约束）、（iii）大陆体系的政治信誉。R2卡已算出法国要替英国吸纳俄麻需扩市场≈**26倍**（直接）或**3.4倍**（广义大陆市场）——全面替代不可预支，**但定向合同可行**；本卡补上机制侧的理由：定向采购是**唯一不需要执行机器就能产生合作的工具**。

---

## §13（⑫）交流与流动：网络、情报、人员

【锚点】**走私业的情报优势强于国家**：利沃诺商人在1810-10-01（巴黎决定后**一周**）即得知自由港地位将被取消，而官方公告一个月后才发，商人因此有数周时间预先处置（Marzagalli p.69，据利沃诺商会议事录1810-10-01与10-31两次会议）。
【锚点】**人员流动即贸易路线**：汉堡商人大量现身于阿尔托纳、波罗的海各港与哥德堡；波尔多商人1806–13年申领护照的目的地分布“follow the new trade routes”：1809–10为波罗的海（当时皇家海军护送数百艘美英船入内），1807年12月禁运前与1810至1812年6月为美国（Marzagalli p.69）。
【锚点】**伪造业的产业化**：Brougham在下院宣读的利物浦商号通函：“we have established ourselves in this town, for the sole purpose of making **simulated papers** ... not only being in possession of the original documents of the ships' papers, and clearances to various ports… **Of any changes that may occur in the different places on the continent, in the various custom house and other offices, which may render a change of signatures necessary, we are careful to have the earliest information**”，附约二十个可伪造港口的清单（Heckscher 印p.213）。
【锚点】**走私者同时是情报商**：Boucher de Perthes（1811–12年布洛涅海关副监察）定义“smogglers”为“contrabandists of their (the British) nation, **who are attached to our police** and who at the same time carry on a traffic in **prisoners of war and guineas**… besides acting as **spies for both sides**”（Heckscher 印p.192）。
【推演·中高】**执行机器永远处于信息劣势**：它的对手是一个跨国的、按利润组织的、与它自己的官员和将军有契约关系的信息网络。加大执法强度只会提高该网络的**价格**，不会降低其**覆盖**——这是命题１（边际产出在≈50%处饱和）的微观基础。

---

## §14（⑬）对政策菜单 B1–B8 的反应函数

读法：“决策集合”是这台机器（及其寄生的反向产业）在该政策下物理上可做的事；“最可能选择”带置信；“机制类比”给史实锚点。

| 政策 | 决策集合 | 最可能选择（置信）| 理由与机制类比 |
|---|---|---|---|
| **B1 入侵英国** | 全力支持港口封锁／向登陆军输出人力／维持常规缉私 | **机器被派生任务掠夺（中高）**：海关员被抽去做船舶征用与岸勤，走私保费下降10–20pp | Ellis法则（印p.202）：皇帝出征时监管必弛；1809年奥地利战役期即实测 |
| **B2 对奥普宽严** | 严：索取关税一致／宽：容忍其变通 | **宽则失效、严则逆反（高）**：普鲁士以贬值国债面值缴税、再发完税证放行；奥地利从未整体实施特里亚农 | Heckscher 印pp.225、227；普证明1811年春夏被否 |
| **B3 提尔西特三版** | 取消普鲁士则莱茵—奥德线全归法系／宽俄则波罗的海不封 | **宽俄版使机器失去北方半壁江山（中高）**；取消普版可把关线东推至奥德，但该线无天然障碍 → 重蹈Rees–Bremen覆辙 | Rowe 印p.195：可守性判据；哥德堡与黑尔戈兰实例 |
| **B4 伊比利亚三版** | 史实（占领）／保波旁联姻／兼并至埃布罗 | **保波旁版是机器的最优选择（中高）**：不占领则无须守比利牛斯—地中海—大西洋三重线，直布罗陀的漏率由西班牙自己承担 | 1808后西班牙“relatively open”成为主漏口（Marzagalli p.70）；Juhász：西班牙起义使英国获得对法帝国的**陆路直通** |
| **B5 奥地利肢解／婚姻** | 剥亚得里亚海岸（伊利里亚）／留给奥国 | **剥岸只把执法责任从奥国转到自己头上（中高）**：伊利里亚建省后英国改占Lussin(1809)与Lissa(1812)，“failed, however, to deter British activity in the Adriatic” | Grab 2015 印p.103；F4卡：伊利里亚1812支出1,350万中军海990万、收入长期不敞 |
| **B6 1810兼并＋封锁加严 vs 许可证自由化** | 两端及中间方案 | **两者不可同时最大化（高）**：加严使关税基消失（1808–09实测），自由化使封锁目的消失（Heckscher印p.198）。机器在两者之间只能选一个相位 | 本卡命题3；1809年工资＞关税净收 |
| **B7 对俄三版** | 开战／有限战争／接受1810俄关税 | **接受1810关税是机器的最优选择（中高）**：开战同时摧毁（i）执法人力、（ii）受保护产业的东部市场、（iii）南线货路的政治基础 | Ellis法则；1812后南线改经君士坦丁堡—萨洛尼卡（Heckscher印p.233） |
| **B8 秩序建构（只采当时提过的方案）** | Beugnot／Bacher 的莱茵邦联关税同盟动议；“一次完税后自由流通”原则；Eichhoff 的科隆—美因茨自由港方案 | **机器自身会支持它们（中）**：因为一次性征税降低成本、消除重复征税的内陆走私动机；**阻力不在机器而在巴黎的“la France avant tout”** | Heckscher印pp.295–296（Beugnot/Bacher）与印p.227（消费税化）；Ellis 2015 印p.35 |

---

## §15 【专题一】S3严格版 vs 许可证版：成本收益对弈

### 15.1 两个版本的定义（不是强度差，是相位差）

- **严格版**：取消一切许可证与特里亚农通道，回到柏林-米兰敕令的字面；全部没收品焚毁或扣押；以全部可用武装力量封死海岸与内陆线。
- **许可证版**：保留禁英国工业品的实体禁令，但以许可证与高关税把殖民品与粮食贸易合法化并课税。

【不可同时性的理由（高置信）】Heckscher写得最清楚：“The object was no longer to exclude goods, but to make an income by receiving them instead; and **no sophistry in the world could make the latter compatible with the former**.”（印p.198）又：“the more prohibitive or protectionistic a customs tariff, **the less it brings in**”。

### 15.2 账（单位：百万法郎/年，除注明外；区间而非点估）

| 科目 | 严格版 | 许可证版 | 出处与口径 |
|---|---|---|---|
| 法国关税（常态流量）| **15–35** | **70–110**（毛口径）／**普通紦34–36＋非常45–61**（净口径）| F4卡补订②；Heckscher印p.221；Marion IV |
| 一次性清算（只能收一次）| 没收拍卖仅第一年可观 | 1810年拍卖≈**150**＋荷尔斯泰**42.5**＋法兰克福**9** | Heckscher 印pp.222、226 |
| 许可证费 | 0 | **1.6–12**（MODEL：2,000张×800或×6,000法郎）| Heckscher 印p.216 |
| 执行成本 | **28–38.5（且随严格度升）** | 28–38.5 | MODEL：35,000人×500法郎×1.6～2.2 |
| 税基损伤（其他税目）| **−60 至 −110** | 较小（未分项估）| F4卡补订③ |
| 对英伤害 | **条件性更大**，但仅当英美同时断裂 | 较小，且许可证主动向英国供粮 | Ellis 1981 印p.203；Heckscher 印p.215 |
| 对盟友的伤害 | 最大：丹麦船被扣至1812年春仍剩80艘 | 仍大，但丹麦、汉萨、意大利可得证（费率“unusually high”）| Heckscher 印p.219 |

【对弈结论（中高置信）】
1. **严格版在财政上自毁**：关税15–35，执行成28–38.5 → 海关系统对国库的净贡献在 **−3.5 至 +7** 之间摆动，再减去税基损伤−60至−110，**总账必负**。1809年已实测过这个结果（工资/关税＝117%）。
2. **严格版的军事代价隐藏在另一本账上**：它需要达武第三军长期驻北海岸。按F2卡口径（每兵年600–700法郎），一个十万人的常驻缉私集团年费 **60–70百万**，与整个海关系统同量级。
3. **许可证版在财政上可持续但在目的上自杀**：它使帝国**对其所禁止的贸易产生财政依赖**（1810–11的105.9百万），并产生一批**有组织的、与政权捷径相连的中标者**（波尔多620张 vs 汉堡5张），后者的政治忠诚是租金的函数。
4. **因此存在第三个版本，而它是本卡给出的最优策（中置信）**：
   > **“保护版”（能力内的封锁）**：▶ 对英国工业品维持禁令与高关税（已被证明在能力上饱和区内）；▶ 对殖民品改收**中率财政关税**（特里亚农税率的四分之一至三分之一，即从价约40–60%，恰在走私保费上限上方一线），**把走私贸易打成正规贸易**；▶ 取消逐船许可证改为**公布税则下的普遍准入**，消除配给租金；▶ 不再为封锁而并地。
   这个版本的收入估算（MODEL）：以殖民品大陆消费量回升至1805年水平一半、从价50%计，法国关税可稳定在 **60–90百万/年**，而边境旅可缩至 **18,000–22,000人**（只守海岸与主要道口、不再封死山地），执行成本降至 **14–24百万**。净额从严格版的负值翻转为 **＋36至＋76百万/年**。该估算的错误源：消费量回升幅度未校准、关税弹性未估、英方枢密令反应未入。

### 15.3 走私弹性区间（本卡的正式估值）

没有任何史料能给出“走私量对执法强度的弹性”的直接估计（走私量不可观测）。本卡改以**三个可观测的半弹性**代替，并声明其假设：

| 半弹性 | 估值 | 建构方式与假设 |
|---|---|---|
| **ε₁ 执法投入 → 走私价格** | 1806–09段：编制＋约38%＋兼并海岸＋军团入场 → 保费 26%→50%（**＋24pp**）；1810–12段：再加编制与刑罚 → **＋0pp** | 假设保费主要反映预期没收损失；无法分离兼并效应与人力效应 → **边际产出在≈50%处饱和** |
| **ε₂ 新建关线 → 保费** | Rees–Bremen：从零建线 → 保费仅 **6–8%** | 同期莱茵线50%→**新线的执行效率不足老线的七分之一** |
| **ε₃ 保费 → 贸易量** | 莱茵上行通行税收入 1807→1811 降至**26%**（同期保费 26%→50%）；但该降幅混入了合法贸易被禁的直接效应 | **不可读作弹性**；只读作“合法河运贸易被压缩至四分之一”的量级 |

**由此得出本卡对“走私弹性区间”的交付（MODEL，中置信）**：
- 在保费 **0–30%** 区间，执法投入的边际产出为正且较高：每增10%编制约推高保费 **4–7pp**。
- 在保费 **30–50%** 区间，边际产出陷落，需要**兼并源头土地**（荷兰、汉萨）而非增兵才能推动。
- **50%以上无观测值**；在当时技术与行政条件下，本卡把 **55±8%** 列为**能力硬上限**。改判证据：任何地段、任何年份出现稳定高于60%的保费报价。

---

## §16 【专题二】S5下的体系持续形态：会关税同盟化吗？

### 16.1 反方证据（强）
- Ellis 两次明文裁定：“**not a Continental Zollverein** ... but rather a vast '**Uncommon Market**' geared to French interests”（1981 印p.286）；“He might have ... **In fact, he did none of those things, but quite the opposite.**”（2015 印p.35）
- 制度实例：意大利 marché réservé（1806-06-10、1810-10-10敕令＋1808-06-20优惠条约）；1810年9月意大利生丝输法免税而输其他国每公斤课 **8法郎**；1810-10-10禁止除法国外一切国家的棉、毛、丝布输入（Grab 2015 印p.107）。
- 拿破仑致欧仁1810-08-23：“**la France avant tout**”；另一封更赤裸：“Italy should not make calculations separate from the prosperity of France … above all, it must guard against **giving France an interest to annex it; because if France has such an interest who could prevent it?**”（Grab 2015 印p.107）
- 荷兰并入后取消对法关线的安排屡次延期，莱顿1811、奥斯纳布吕克1812仍在请求自由通商（Heckscher 印p.299）。

### 16.2 正方证据（弱但真实，且被上一轮低估）
- **动议存在**：Beugnot 曾二三次提议把莱茵邦联发展为关税同盟，Bacher 支持（Heckscher 印pp.295–296；合并注，原呈文未取得，证据层级已由上一轮 t_f81a6f 审定）。
- **原则存在且被实施**：为解决中转邦被重复征税的“evidently fatal”局面，“gradually an arrangement was made whereby the tariff was generally applied as **a tax on consumption, not as a transit duty, but with freedom for goods that had once paid the duty**”（Heckscher 印p.227）。**这正是关税同盟的核心技术原则（境内自由流通➕共同外税）的一半，而它是被财政摩擦逼出来的，不是被设计出来的。**
- **行政基础存在**：帝国已有统一税则文本、统一度量衡、日耳曼币制的部分法郎化（上一轮 t_f81a6f 已核：1806-03-21意大利里拉及西伐利亚1808-01-11估值）、以及 **35,000人的现成关税官僚体**。
- **历史类比的时间尺度**：普鲁士自1818年关税法到1834年关税同盟耗时**十六年**，且其动机也是财政与反走私（飞地、飞地包围、关线不可守）而非民族情感。G1/G2卡已给出“关税同盟给小邦自主财源、其政治忠诚不自动”的限定。

### 16.3 裁定：S5下的概率带（本卡交付）

条件：拿破仑胜利后大陆和平（1815–1848），英法至少武装共存。

| 形态 | 1830视点 | 1848视点 | 关键条件 |
|---|---|---|---|
| **A. 法国优先的分层准入体系**（史实路径的和平延长：帝国内部自由、藩属单向开放、条约优惠）| **0.50–0.60** | **0.35–0.45** | 拿破仑在位，“la France avant tout”不变 |
| **B. 有限关税同盟**（帝国＋莱茵邦联＋意大利：一次完税自由流通＋共同外税＋收入按人口分配）| **0.15–0.25** | **0.25–0.35** | 需三件事同时发生：（i）许可证行政从皇帝手中下放（F1卡容量约束使之几乎必然）；（ii）继承时刻后的政权需要藩属精英的财政合作；（iii）走私成本在和平期下降使禁令无意义 |
| **C. 体系解体**（各邦自设关税、回到多税则并存）| **0.15–0.25** | **0.20–0.30** | 拿破仑死后继承危机（F5卡：无条件存续至1848≈40–55%）|
| **D. 逆向同盟**（奥地利或普鲁士领头的反法关税集团）| **0.05–0.10** | **0.05–0.15** | Bacher 1810已预言奥国会是受益者；PR卡：残普不自动取得1834领导权 |

**一句话结论**：**关税同盟化在S5下不是主线，但也不是零；它的概率随时间上升，因为推动它的不是理念而是财政摩擦，而阻止它的是一个会死的人。** 本卡提醒总装（P5/P7）：若采用B形态，其制度内容应照史实的两个锚点写，而非照後来的关税同盟写：（a）Heckscher印p.227的“消费税化➕一次完税自由流通”；（b）Eichhoff的“自由港➕关线后移”方案。

---

## §17（⑭）反事实年表 1803–1848：封锁执行机器的命运

读法：【A】＝锚点（史实，带出处）；【M】＝机制；【P】＝推演（情景＋置信）。情景代号同项目简报。

| # | 年 | 情景 | 事件 | 类型与置信 |
|---|---|---|---|---|
| 1 | 1803–04 | 全 | 阿美昂破裂后的禁运使走私业获得“第一次大推动”（共和十二年）；海关编制12,500人 | 【A】Ellis 1981 印p.204；AHAD |
| 2 | 1806.03 | 全 | 盐税征收交给海关（敕令3-16），机器获得第二项财政职能 | 【A】AHAD |
| 3 | 1806.11 | S0/S3 | 柏林敕令；莱茵保费自10%跳至26% | 【A】Rowe 印p.195 n.27 |
| 4 | 1807 | S0 | 法国关税净收见顶 60.6百万；同年英国再出口的30%去丹麦；1,500艘小船自通宁入汉堡 | 【A】Heckscher 印p.197；Marzagalli p.69 |
| 5 | 1808 | S0 | 关税净收崩至18.6百万；黑尔戈兰英方投入£500,000、200名商人、“Little London”；哥德堡进口翻倍 | 【A】Heckscher Part III ch.II |
| 6 | 1809.07 | S0 | Rees–Bremen关线设立，**保费仅6–8%**；同年关税净收见底 11.6百万，**低于海关纯工资** | 【A＋MODEL】 |
| 7 | 1810 | S0 | 缉获品法令(1-12,48%)→圣克卢(7-3)→荷兰并入(7-9)→许可证敕令(7-25)→特里亚农(8-5)→枫丹白露(10-18)：**机器在五个月内完成相位转换** | 【A】本卡§1.3 |
| 8 | 1810–11 | S0 | 拍卖现金≈150百万；荷尔斯泰42.5百万；法兰克福9百万；特里亚农至1811年底关税105.9百万——**全部为存量清算** | 【A＋【M】 |
| 9 | 1811 | S0 | 莱比锡集市英货“practical cessation”；贸易主轴转到多瑙河—维也纳—Brody；莱茵上行通行税降至1807年的四分之一 | 【A】Heckscher 印p.230；Spaulding 表7.1–7.2 |
| 10 | 1812 | S0 | 编制峰值35,000；拟立法把它正式武装化，“resté à l'état d'embryon” | 【A】Rowe 印p.187；AHAD |
| 11 | 1813 | S0 | 贝格1月起义；8-17达武令以海关员组营；机器被战争吞没 | 【A】Rowe 印p.199；AHAD |
| 12 | 1804–06 | **S1**（不列颠中立化）| 若英国中立，则机器停在**1803年形态**：纯保护主义关税、编制12,500–15,000、走私保费稳在**6–12%**；无特里亚农、无许可证、无海关法庭 | 【P·高】因两个数均有对应年份的实测 |
| 13 | 1807–15 | **S2**（大陆整固）| 保西班牙波旁、不攻俄、对英武装共存→ 机器保持**“保护版”**：编制18,000–22,000、殖民品中率财政关税40–60%、法国关税稳在**60–90百万/年** | 【P·中】MODEL；§15.2 |
| 14 | 1809–14 | **S3**（封锁绞杀）| 严格版运行：关税15–35、执行成28–38.5、税基损伤−60至−110 → **总账年净负约75–145百万**；每四至五年需一次新的并地式存量清算来填缺 | 【P·中高】MODEL＋史实1810并地实例 |
| 15 | 1810–12 | S3 | 对英伤害峰值只在**英美同时断裂**时出现；若美国不教合，封锁对英外贸的削减降至一半以下 | 【P·中高】Ellis 1981 印p.203 |
| 16 | 1812–15 | S3 | 严格版与大战不相容：Ellis法则使任何东方战役都把保费压回30%以下 | 【P·中高】 |
| 17 | 1815–20 | **S5** | 战后两三年内许可证由皇帝亲签改为总署行政审批（F1卡中枢容量约束）；“恩典”变“手续” | 【P·中高】 |
| 18 | 1815–25 | S5 | 海关旅转为常设准军事边防队（每兵年费约500法郎 vs 陆军600–700），吸收退伍军人；欧洲同类：普鲁士Grenzaufseher、奥地利Finanzwache | 【P·中】机制类比 |
| 19 | 1818–30 | S5 | 殖民品关税从“战争武器”定型为“稳定消费税”；因此**甜菜糖产业在十五年后站稳**（与史实同期，但多出比利时、莱茵左岸、意大利北部三个产区）| 【P·中】Heckscher 印p.294 |
| 20 | 1820–35 | S5 | 内陆贸易商（斯特拉斯堡、美因茨、法兰克福）与沿海口岸（波尔多、汉堡、利沃诺）的政治联盟因关税率而对立；前者要保护、后者要自由港 | 【P·中高】科隆商会1811变脸为机制锚点 |
| 21 | 1825–40 | S5 | “一次完税自由流通”原则从权宜升为条约；若成，即欧陆版关税同盟雏形（0.15–0.35）| 【P·中低→中】§16.3 |
| 22 | 1830–48 | S5 | 黑尔戈兰、马耳他、直布罗陀、哥德堡四转口港在和平下**不消失而降级**为普通转口地；马耳他的英商数从1812年60人回落，但地中海线不退出 | 【P·中】Grab 2015 印p.103 |
| 23 | 1830–48 | S5 | 走私保费回落至**8–18%**（和平期保护关税水平），执法从“政治任务”变“财政例行” | 【P·中】以1800–02观测值为参照 |
| 24 | 1848 | S5 | 边防关税官僚体成为帝国最大的**非军事民事雇主之一**，其地方利益与内陆工业资本绑定；“自由贸易 vs 保护”成为1848革命的一条阶级断层线 | 【P·中低】 |
| 25 | 1810–15 | **S6**（行省化最大版）| 机器是行省化的**驱动轮也是刹车盘**：每一次并地（凯尔1808、荷兰1810、汉薨1810、提契诺占领1810）都以执法为理由，而每一次并地都延长了新边界 | 【A＋【M】 |
| 26 | 1811 | S6 | **贝格4,000人请愿求并入被拒**，拒绝理由之一是纯执法地理学：莱茵河可守，贝格东界无天然障碍 | 【A】Rowe 印pp.194–195 |
| 27 | 1812–20 | S6 | 若继续并到奥德河—易北河线，则须守线由约10,000公里增至**13,000–15,000公里**；按帝国均密度（2.37–3.84人/公里）需加**7,100–19,200名**边境旅，年增纯工资**3.6–9.6百万**，含间接费（×1.6～2.2）**5.7–21.1百万** | 【P·MODEL·中】 |
| 28 | 1815–30 | S6 | **收敛判据**：行省化在执行账上可持续，当且仅当新并地区的关税净收＞新增守线成本＋当地民政赤字。按F4卡分地区参数，**沿海带均不满足**（伊利里亚、汉萨、罗马均为净耗）| 【P·中高】F4卡S6阈值表 |
| 29 | 1816–25 | S6 | 行省化使“境内走私”变“境外走私”：关线东移后，原为境外转口地的巴塞尔、法兰克福、拉施塔特等只会被新的境外点取代（莱比锡、布拉格、布罗茨拉夫）| 【P·中高】Bacher 1810预言的一般化 |
| 30 | 1817–22 | S5/S6 | 一次性存量清算的供给耗尽（无新并地则无新库存可抉）→ 财政上必须转向常态低率关税 | 【P·中高】§4.1的“存量 vs 流量”分析 |
| 31 | 1820–35 | S5 | 海关法庭（cours prévôtales）在和平期被废止或改为普通法院；刑事威慑下降但执行率上升（本地法官更愿适用中率关税下的罚金）| 【P·中】Ellis 印p.202：普通法庭比军事委员会受欢迎 |
| 32 | 1835–48 | S5 | 英法商约谈判中，法方的谈判筹码是**殖民品关税的降幅**而非工业品准入；英方关心的恰相反 → 协议难成但不破裂 | 【P·中低】 |
| 33 | 1846–48 | S5 | 若法帝国仍存，英国废除谷物法的时点未必提前（B5卡）；但**大陆侧的谷物出口商**会成为反对封锁残余的最强游说团体 | 【P·中低】§5.3的剖刀差 |

---

## §18（⑮）能力上限表

| 维度 | 历史峰值（带来源）| 崩溃点 | 未用潜力 | 判词 |
|---|---|---|---|---|
| **人力** | 35,000（1812）＝4,000内勤＋30,750边境旅 | 1813被编成野战营→崩 | 武装化法案未立（仅停留“embryon”）；本地招募未用（莱茵仅3%本地人）| 人数不是约束；**本地合作才是** |
| **密度** | 莱茵241人/十万人口、4.57人/公里 | — | 帝国平均2.37–3.84人/公里，可再抑制性地向关键段集中 | 集中可提高局部保费，但会把货流推到旁段 |
| **强制价格（核心指标）** | 莱茵保费 **50%**（1809末–1811）；海岸→内陆总加价 **＋50%** | — | 无观测值高于60% | **硬上限 55±8%（MODEL）** |
| **缉获率** | 按人次：1/3–1/4（Rist）；按重量：**≤5%**（1810-08汉堡门）| — | — | 批发渠道可打击，零售渗透不可 |
| **财政（常态流量）** | 1807：60.6百万净；严格期1809：11.6百万 | 工资＞关税（1809）| 中率财政关税未试：**60–90百万/年**（MODEL）| 严格与富裕不可兼 |
| **财政（一次性）** | 1810–11：105.9＋150＋42.5＋9 ≈ **307百万** | 库存池耗尽（17–22月）| — | **不可作基线** |
| **司法** | 汉堡2周120个六月徒刑 | 不来梅狱中死亡率22.5%；本地降罪率 | 死刑几乎未用（123案仅2例）| 名义刑罚与预期刑罚脱钩 |
| **地理** | 可守线：莱茵河；不可守：Rees–Bremen、6–8% | 新线无天然障碍即失效 | — | **可守性判据优于人力判据** |
| **政治** | 执行力最强处：萨克森（本地产业利益与禁令同向）| 法兰克福、贝格、汉萨（利益反向）| 未用：系统性地购买藩属产业利益（如对俄木材采购提议）| **利益比宪兵便宜** |
| **与战争的相容性** | 峰值必须在大陆和平期 | 任何大战役即崩 | — | **Ellis法则** |
| **对英效果** | 需合取：严格控制 ∧ 英美断裂 | 美国教合即失半 | — | **法国只持有一半变量** |

---

## §19（⑯）主线、备选结论群、置信与改判证据

### 19.1 主线（中高）
大陆体系的执行机器在**能力上有一个可测的、稳定的上限（走私保费55±8%）**，它能排除英国工业品、不能排除殖民品；因此它必然在数年内从“禁绝装置”转为“抽租装置”；而抽租装置的收入主要来自**并地式存量清算**而非常态流量，于是财政需求持续产生新的并地动机；每次并地又延长了不可守的边界。**这条螺旋是内生的，不需要俄国、不需要西班牙、也不需要拿破仑的性格缺陷就能启动。** 反事实中切断它的唯一干预点，是在1808–1810年之前把殖民品禁令**改为中率财政关税**，并把许可证从恩典改为公布税则下的普遍准入。

### 19.2 备选结论群

**备选一（中）“Heckscher弱版”：执行机器从未接近其上限，真正的约束是意志与腐败。** 最强论据：拿破仑自己收取贿赂分成、自己开许可证、自己在敦刻尔克接纳“smogglers”；若一个像达武那样的人掌握全线，保费可能推到70%以上。本卡不采纳为主线的理由：（a）达武全力治理的汉堡同时是“每六人有一人靠舒弊为生”的城市；（b）1812年编制升至35,000后保费未再升；（c）Rees–Bremen线由同一批人、同一套法律执行却只有10分之一的效果。但这一备选在**小尺度**上成立：具体地段的执法绩效确实高度依赖官员个人（Turc vs 特里尔）。

**备选二（中低）“技术不足版”：具备电报、铁路、现代户籍与统计后，同样的机器可以成功。** 对应现实：后来的关税同盟与民族国家确实把边境管住了。但反事实时间窗（1803–48）内这些技术不可得；且历史上真正结束大规模走私的不是技术而是**关税率下降**（英国1840年代、法国1860年代）——这反而支持主线。

**备选三（中）“对英有效版”：机器虽漏，但把英国成本推高到足以造成1810–12危机。** 本卡接受其**条件版**（需英美同时断裂），不接受其**无条件版**；B5卡的终局包络（S3下1848英国工业为史实54–79%）与本卡兼容。

**备选四（中低）“整合版”（Woolf命题的经济形式）：执行机器输出了统一税则、统一税官、统一商法，是欧洲市场整合的真实前驱。** Ellis 两次实证反驳（印p.286、2015印p.35），但本卡指出其反驳针对的是**意图**，而 Heckscher 印p.227 的“一次完税自由流通”是**后果**。这是两人都未充分展开的一道缝，也是本卡把关税同盟化概率定在0.15–0.35而非0的理由。

**备选五（低）“无关紧要版”：大陆体系的经济效应小到不影响帝国存亡。** Heckscher本人的消费侧比较（印pp.320–321）部分支持，但与关税收入崩塌、贝格起义、俄法破裂的贸易起因不相容。

### 19.3 改判证据（本卡自列，共六条）

1. **E1（直接推翻能力上限）**：任何地段、任何年份出现**稳定高于60%** 的走私保费报价（首选档案：A.N. F12系列、各省 série M 与 Meurthe 的 série U；Dufraisse《Contrebande... de la rive gauche du Rhin》原文）。若成立，本卡硬上限55±8%与命题3均须上调。
2. **E2（推翻“一次性”性质）**：找到 1812、1813 两年**分项的**法国关税净收（普通/非常分列），若非常关税在无新并地的年份仍稳在 40百万以上，则“存量清算”判词失效，许可证版的可持续性上调。（目标：Marion IV pp.304–308原卷未取部分；A.N. AF IV 1072）
3. **E3（推翻两渠道定理）**：找到任一年份、任一口岸的**系统缉获台账**（按券、按重量），显示重量缉获率稳定高于20%。目标：汉堡、利沃诺、安特卫普海关缉获登记簿（Staatsarchiv Hamburg；Archivio di Stato di Livorno；A.N. F12）。
4. **E4（推翻财政自毁命题）**：取得海关总署**分年总支出账**（薪饵、船艇、诉讼、监狱）。若实际总支出显著低于本卡MODEL的28–38.5百万，则“1809年工资＞关税”的量级判词需修订（但注意本卡下界已取最低级薪锅，偏保守）。
5. **E5（推翻Ellis法则）**：找到大战役年份（1809、1812）保费**上升**而非下降的地段证据。若成立，则S3与战争不相容的推论失效，S3的可行性上调。
6. **E6（推翻关税同盟化的概率带）**：取得 Beugnot 或 Bacher 关税同盟呈文**原件**（Darmstädter《Studien zur napoleonischen Wirtschaftspolitik》III pp.113ff. 与 Schmidt《Le Grand-duché de Berg》附录C所指档号）。若其中含收入分配与争端程序条款，则形态B的1848概率上限可自0.35上提；若只是单向准入请求，则下调。

### 19.4 已知缺口（诚实声明）

- **未亲阅**：Marzagalli《Les boulevards de la fraude》（1999）全书（仅得其1996年英文预告与目录）；Crouzet《L'économie britannique et le blocus continental》两卷（经Ellis与Juhász转引）；Dufraisse《Contrebande... rive gauche du Rhin》（经Ellis转引）；Tarlé《Kontinental'naja blokada》与《La vita economica dell'Italia》（经Heckscher与Grab转引）；Schmidt《Le Grand-duché de Berg》原卷（G2卡有OCR全文，本卡未就本题重读）。
- **未取得的关键序列**：（a）海关总署分年总支出；（b）分年分港缉获量值表；（c）许可证分年发放数与实收费总额（拿破仑每周过目的“tableau”应存于A.N.）；（d）特里亚农税则分税目实收。四项均为**可定位的档案缺口而非文献不存在**；它们能结束的是 E2、E3、E4 三条改判。
- **口径冲突（送总装）**：（i）法国关税收入三套口径（Heckscher／Marion／AHAD）；（ii）海关编制两套（35,000（Rowe，带构成） vs 35,500（AHAD））；（iii）缉获率两口径（人次 vs 重量）；（iv）donataires两套（Ellis“近6,000人／年3,000万法郎” vs F4卡“1810年初4,035人／>1,800万；1814登记≈2,473万”）。

---

## §20 供其他卡直接取用的接口

| 接口 | 内容 | 目标卡 |
|---|---|---|
| **执行强度价格序列** | 莱茵保费 6/10/26/30/50%；Rees–Bremen 6–8%；海岸→内陆＋50% | P8（概率带）、P6、P5、M1 |
| **能力上限参数** | 硬上限55±8% AVE；缉获率重量口径5–25%（主线10–15%） | P2、P8 |
| **财政对弈表** | 严格版关稁5–35 vs 许可证版70–110（毛）；执行成28–38.5；一次性池≈307百万 | F4、P2、P8 |
| **S6守线成本公式** | 每延长1,000公里守线需增2,400–3,800名边境旅（按帝国均密度），年增纯工资1.2–1.9百万法郎、含间接费1.9–4.2百万 | P2、D1、D2 |
| **可守性判据** | （i）连续天然障碍（ii）两侧无近距境外转口地（iii）本地产业利益与禁令同向 | P2、D2、Q1 |
| **转口港参数** | 黑尔戈兰、哥德堡、马耳他、直布罗陀四站实数 | B3、B6、P4、SC、IT2 |
| **贸易条件剖刀差** | 殖民品／粮食物价比9.2–17.5倍恶化 | R2、PL、SC、G2、P5 |
| **Ellis法则与合取条件** | 效力∵大陆军事投入；对英最大伤害需“严格控制∧英美断裂” | P6、US、B1、B5、P8 |
