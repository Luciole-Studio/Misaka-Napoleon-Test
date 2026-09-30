# C3｜法国海军何时追近英国：不可识别的年份与可检验的条件

## 结论与交付状态

【裁量｜高置信度，限证据状态】**现有C2不能算出法国达到英国战列舰存量80%或100%的年份，也不能算出1830年海员效能比例。**本卡交付存量—流量约束结构、条件门槛、证据及112行年度缺值登记，不交付伪装成校准结果的预测。缺值不是法国没有能力，更不是追平永不发生。

【事实｜输入审计】C2的53条记录是不同指标、年份、地理范围的部分核验切片，另有16项缺口；法国全国1807—14产出及1814实力、英国后续同口径存量、训练日、实际海军支出及船厂能力不足。故“先复现史实1807—14”的前置条件未满足。[D1—D3]

【裁量】合同三项证伪标准应这样记账：
- 校准误差：**不可计算**，不是已测得大于20%，也不是小于20%；采取同样保守的定性降级。
- 1830年训练存量代理低于英国70%：**未检验**，不能据此宣判“实质缩减被否”。
- 英国反馈抵消法国追赶：机制有证据，幅度和时滞**未识别**，不能报“差距必然扩大”。

【文献推断｜本卡综合E1—E9】需要纠正两个预设：法国并非一律出不了海；英国也并非在特拉法尔加后可以不理法国重建。小舰训练安排、真实跨洋巡航和英国保编论辩同时存在。**“船壳可逼近、效能长期不能”仍是待检验假说，不是本卡算出的结论。**

**两线回答**：吨位差距——不可识别，舰数不能代替吨位；效能差距——有训练、配员、集中与后勤约束证据，无可校准百分比。差距最小年份——NA。该年能否护送跨洋远征——NA，不能由全国舰数门槛推出。

## 一、输入口径与唯一执行的数量计算

【事实｜C2，D1物理行2—4】英国年初战列舰分别如下；表中“海勤类别舰体”仅指sea commission与sea ordinary之和，不等同已整备、配员或在航。

|年初|海勤现役|海勤预备|两栏合计|包括港勤、在建/订购的大总数|
|---|---:|---:|---:|---:|
|1803|32|79|111|172|
|1804|75|40|115|172|
|1805|83|33|116|181|

来源为James 1837版卷III Annual Abstracts 11—13，经C2完整折页图取数；图在上游`naval/James1837_p395.png`至`p397.png`，口径注释见印刷373—374页。这里复核C2行及加总，不声称本卡完成独立档案互证。1805是年初，不是特拉法尔加战后。

【模型推演｜条件算术】若法国存在完全同口径存量F，同期英国为B，则达到目标α的必要舰数是⌈αB⌉：

|仅作参照的英国时点|80%所需法国同口径舰数|100%所需法国同口径舰数|
|---|---:|---:|
|1803|89|111|
|1804|92|115|
|1805|93|116|

这些数字**既不是法国实际实力，也不是未来追平年份**。不得把1805英国116艘固定至1830。大总数172/181仅用于校验分类加总，不进入追赶门槛。

【事实｜执行记录】`build_c3.py`只对上述C2三行做整数加总与有理数门槛运算。`c3_calibration.csv`中的三个零误差是分类算术自检；四项真正历史校准均为`not_executable_missing_inputs`。这不是“模型校准通过”。

## 二、约束模型：先列不能绕过的账，再谈追赶

以下全为【模型推演｜待数据估计的结构】，没有借模型形式授予史实真实性；脚本没有执行本节动态方程。

### 2.1 舰体、在建、可战与集中分开

按国家i、船型k、港口p建立：

- 在建量：W(t+1)=W(t)+开工(t)−下水(t)−取消(t)。
- 浮存舰体：H(t+1)=H(t)+下水(t)+俘获接收(t)+转入(t)−灭失(t)−拆解(t)−转出(t)。
- 分类桥：H分为待舾装、维修、预备、已整备；与James海勤/港勤分类对照，记录重分类，不把重分类当造舰。
- 完整可用舰A受制于已整备舰体、合格船员、军官、炮械、弹药与出港条件。每艘船均须满足各项，不能用全国平均弥补某舰无人掌舵或某港出不了船。
- 任务可集中的舰C(t,m)≤A(t)：还须满足航程、季节、到达时间、通信与其他站任务。多个港口的舰数不能无时滞相加。

【文献推断｜Corbett】双方参谋部不只数舰，明确区分三层炮甲板与两层舰。[E3] 因此吨位T=Σ吨位(k)H(k)、舷侧火力、舰型组合要分列；本卡没有可验证舰型吨位权重，T比率留NA。

### 2.2 实物与财政平衡

【模型推演】每一材料r：期末库存=期初库存+本地产出+实际到货进口+回收−新建耗用−维修耗用−日常运行耗用−损失。橡木、桅木、大麻、焦油、帆布、火炮及口径兼容弹药不得合并为一个“木材”指标。全国拥有森林不等于船厂收到合格干燥曲材；进口合同不等于入库。

【模型推演】船台与修理坞分别核算占用工时；开工到下水再到舾装服役有不同滞后。工匠时间须在新建、维修、沿岸小舰与运输船之间分配。预算约束为海军实际可用资金≥新建+维修+工资+伙食+运输采购+训练+设施维护；海军份额须与陆军、债务及民政同账，不能把少打一场陆战的全部费用无损转成战列舰。

|约束|已读锚点|可支持什么|缺什么，不能算什么|
|---|---|---|---|
|船台/船厂|1810-07-03致Decrès，拟新增威尼斯五舰且要求报成本[E1a]|确有扩建意图；追加计划须另找预算|各厂实际开工/完工、台年、工匠及舾装；不能给年产能|
|木材与国内运输|1810-07-13安排运输船运舰材[E1]|同一沿岸体系兼负训练、运输、防卫|合格材库存、干燥及运抵时滞；不能给木材约束上限|
|桅杆/大麻/波罗的海|Davey注40—53[E6]及C2补遗[D3]|依赖真实，护航、执照和海军运输提供适应机制|替代进口、价格及库存年度表；不能把封锁令当断供量|
|火炮/弹药|Corbett舰型论[E3]；1811信调海军炮手[E2]|火力配置与炮手不同于舰体|铸造交付、库存、口径、弹药及训练射耗；不能默认充足|
|海员/军官|1810训练方案、1811调员[E1—E2]|人员分级与由小舰向大舰转移是同期政策|实到、逃亡、病亡、战俘按军种、留任及考核；不能用征额当现役|
|财政份额|1810追加成本询问；1813英国保编争论[E1a、E7]|决策者面对预算和陆海资源竞争|双边实支/价格/借款条件；不能估军备竞赛弹性|

### 2.3 训练存量不是离港日历时长

【模型推演】分列个人航海技能S、炮术G、舰队协同K；海上人日按沿岸小舰、单舰远洋、舰队演练分类。经验更新可写为：保留的技能存量+经考核的新学习+调入经验−死亡/俘虏/离职/调出所带走的经验。若估计沿岸经验向主力舰转移率，必须用人员履历、训练项目与考核证据；**本卡不给自由设定的学习率、折旧率或“法国0.6”质量系数**。

【事实｜同期书信现代转录】1810-07-13明确说沿海水域航行可使舰员熟悉海上工作，并计划抽取最熟练者填补战列舰；1811-07-31规定大舰不能离开Malamocco时，由半数舰员乘轻舰巡航、护岸、练习。[E1—E2] 因而“封锁使全部海上训练日为零”不成立。命令证明方案存在，不证明所有人按令受训。

【裁量｜中高】远洋经验、舰队协同仍可能落后；但它们不是沿岸练习的同义词，也不是可从败仗剩余项恢复的变量。新造舰越多，若老船员总量不增，每舰骨干可能被稀释；若和平使商业航海恢复，征集与民间工资竞争又须同时考虑。这两条是待检验机制，不是已测效应。

### 2.4 追赶条件与反馈敏感性

【模型推演】设同口径舰体年度净增分别nF、nB：

F(T)−αB(T)=[F(0)−αB(0)]+Σ[nF(t)−αnB(t)]。

故达到α所需累计相对净增至少为αB(0)−F(0)。若简化为恒定净增、初始未达标且nF−αnB>0，年份步数为⌈[αB(0)−F(0)]/[nF−αnB]⌉；若分母≤0则在**该恒定假设**下不能追上。实际初值、净增及政策反馈未知，公式不能产出历史年份。

【模型推演】若法国额外净增x引出英国额外净增βx，则对目标缺口的年度净改善为(1−αβ)x：80%门槛的抵消界β=1.25，100%门槛的抵消界β=1。β未估计，且这里只是舰体反馈；英国保留海员、提高整备或改变部署可在新舰下水前改变效能，不必表现为增建。

【模型推演｜另一个诊断恒等式】若仅为展示遗漏变量，定义综合效能比R=舰数比h×其余因素比q，则R≥目标r要求q≥r/h。文件`c3_quality_thresholds.csv`给出：h=0.8时达到R=0.7需q≥0.875，达到R=1需q≥1.25；h=1时分别需q≥0.7、1。**q包含舰型、整备、技能及集中等，不是海员质量测量；这些数不得用于触发合同“海员70%”规则。**这也不是海战胜率公式。

## 三、逐项检验史料：支持与反证放在一起

### 3.1 1805、1806、1809并不构成同一个质量试验

【文献推断｜Corbett，1910，pp.33—34】1805年1月Villeneuve首次出航遇风暴，舰只受损、编队失序，英巡防舰跟踪又加重回航考虑。Corbett引其1月21日致Decrès解释，来源转经Desbrière IV p.299；原折未阅。Corbett把生手船员作为解释之一，而非给出可跨年份使用的质量折扣。[E3]

【事实｜据James，1886版IV pp.108—117】1806年Willaumez确有远洋巡航、巴西补给及加勒比会合；巴西停泊16天，足以反驳将整段远征日历直接计为海上日。好望角基地不可用及食物需求改变任务。8月风暴打散法舰，也打散附近英国分队；法舰有临时舵桅修复与返航。选出分队的经验不能代表全部法国海军，风暴失散也不能独立识别国别技能差。[E4]

【事实｜据James，IV pp.390—393、400—408】1809年2月封锁舰因恶劣天气离站，Willaumez出港；Lorient会合受到潮深限制；4月火船攻击时指挥者已为Allemand。法方有防火艇规章，但强风潮使实际执行受阻，英方部分火船方案也受天气改变。Océan军官信英译转引描述邻舰迫使断缆、碰撞和积极灭火；并非无行动能力。[E5]

【裁量｜高】锚地火船、搁浅、碰撞、天气、指挥与海上炮战不是同一个试验。不能把1809损失率外推为1830全国效能折扣。James强烈评价、法方叙述与署Ed.编者异议必须分开；详见`sortie_evidence.md`八项证据。未以O’Meara所载圣赫勒拿回溯谈话作当时能力证据。

### 3.2 英国舰材脆弱性存在，但“有依赖”不等于“已断供”

【文献推断｜Davey】1808年4月粮秣委员会仍称大麻短缺；1809年Saumarez组织运回桅材，供应商要求护航，特殊执照和海军运输被用于获得物资。[E6，注40、43—46、51—53] 这既支持封锁有成本，也反驳英国完全没有应对。

【事实｜Davey转引，非新增模型输入】C2迟到补遗记录1801俄国大麻进口37,000 tons、超过21英寸Riga桅杆1,186根及同尺寸美国桅杆198根；1809组织运输5,188根pine sticks。前者不是纯海军采购，后者不是已到货全年量，吨制及上游统计未完成核对。本卡只用来辨认材料约束，不以它们补年度平衡。[D3、E6]

【裁量】Davey所述1806—15下水375,000吨包括大量低等级小舰，不是战列舰吨位，更不是法国扩舰所引起的英国新增量。其注50同时警告Albion夸大短缺倾向；不能只摘其最悲观引文。

### 3.3 英国反馈：保编有证，增建弹性未证

【事实｜1813-11-10议会辩论】政府方以法国持续积累海军、全球任务压力及海员遣散后不易召回为由要求维持编制；反对方质疑法国整备状况，主张陆战优先。讨论将新建、修理另留后续预算。[E7] 所以“威胁→保留现役人力”有同期锚点，“每增法国一舰→英国新订若干舰”没有本卡可用估计。

【事实｜1807-09-07投降条款，公报OCR】第III条要求丹麦交舰和海军物资、立即交出船坞仓库；第V条涉及交还城堡及撤军，不是归还舰队。[E8] 【文献推断｜Bjerg】英国不具备立即使用全部夺得舰只的人力，夺舰又使丹麦转向法国并提供海员。[E9] 因此夺舰是“剥夺潜在对手”机制，不等于英国有效舰队等量增长；也不能假设每个设防港都能复制哥本哈根。

【模型推演】所谓“双重封锁”应显式拆成主力港监视/拦截与沿岸/商业航路封锁的兵力配置，受巡防舰、补给和各站任务约束。本卡不声称已经取得一种固定的历史“双重封锁”兵力配比。

## 四、四情景与1803—1830年度表

【模型推演】全表按年初登记；S2/S3约定提尔西特后才分岔，故继承1803—05的英国观测；亚眠延续只继承1803年初状态。每种情景28年，共112行；法国同口径存量、舰数比、吨位比、训练代理比及护航指数全部NA。

|情景|同期锚点与入场状态|条件下的变化机制|未消除的败因/置信度|
|---|---|---|---|
|(a)史实|C2分类观测；1806/1809行动[E4—E5]|用于检验命令、产出、战备是否分离|1807—14全国校准不可执行；对不可识别判断高置信|
|(b)亚眠延续|真实亚眠和平提供背景，但本卡未取得1803年5月双方可接受且获授权的延续方案|若和平维持，可恢复航海机会、降低战损；英方亦可修理补充或重配预算|只是用户指定诊断分支，未获同期方案准入；追平/持久和平概率不可评|
|(c)S2大陆整固|海军政策组件有1810建舰与训练、1811小舰替代方案[E1—E2]；不废西王/不侵俄的外交准入由C5/C12/C13负责|若减少陆上过载并稳定港口控制，可持续维修、配员与训练；若仍对英交战，不能假定远洋开放|盟国自主、法国预算分配、英国保编及封锁；机制成立中置信，数量成败不可评|
|(d)S3封锁强化|1806-11-21柏林敕令第I—II条提供敌对贸易禁令原型[E11]，非完整执行证明|若更多舰材截留可增加英采购/护航成本；同时法方沿海贸易与海员来源可能承压|泄漏、执照、俄瑞选择、替代供应及英国先发；净效果方向不能排序，绞杀成功低支持度而非已测低概率|

【裁量】更正前序沟通：亚眠延续**不必然越过PoD≥1803年5月边界**；可以设在破裂前的5月。真正欠缺是足以维持和平的同期可选交易与双方接受链，不能用日期理由替代证据审查。

【模型推演】S2不自动拥有史实1810吞并荷兰所得一切资源：若其外交方案保留自主盟国，就须重新核定港口、海员与税收调度权；不能同时取“没有强制引起的反弹”和“全部资源绝对服从”两项好处。S3同理不能同时假定对英国零泄漏而法国进口/训练完全不受影响。

## 五、跨洋护航：给C5/C7/C17的接口

【文献推断｜E3—E6】1806证明选定分舰队能航至远海，不能证明其能护送一支大型运输舰队按时抵达、维持补给、压制当地英国舰队并安全返回。Corbett pp.33—34呈现运兵负担、受损舰速与敌侦察之间的联系；James p.108呈现海外基地丧失后的改道。全国存量平齐不解除这些任务约束。

【模型推演】护航判断至少须给：目的地和季节、运输吨位与航速、护航编成、可集中窗口、沿路补给维修基地、当地敌舰及其增援、返航和持续补给安排。未给这些条件，就不设“护航指数=舰数比”。

【裁量｜高】供综合稿采用：“法国重建和局部出航能够继续牵制英国，英国海权不是没有成本；但现有资料不能证明1830前达到全球等效制海，更不能从陆上胜利推导可稳定护送拉美或印度远征。”‘靠联盟与英国财政疲劳获得局部窗口’仅为可检验支线，财政疲劳和窗口长度须另证，不能作为未测70%规则的自动替代结论。

【未验证项】本卡不把蒸汽或Paixhans炮当追赶捷径。1820年代技术变化应另设舰队更新、训练与财政成本；未取得足够材料，不计算其提前应用或效能增益。

## 六、解释竞争与来源独立性

【文献推断｜Hickey转述Glover】Glover的准确题名是“The French Fleet, 1807–1814; Britain’s Problem; and Madison’s Opportunity”，JMH 39(3), 1967, pp.233—252，DOI 10.1086/240080。**元数据已读、正文未读**。Hickey 2008第15项评论称其论证法国1812已接近战列舰数量匹敌，英国造修能力承压；同时明确否定“Madison据此宣战”有证据。[E10] 本卡保留数量逼近论作为强反证，不把评论当已核全国舰表。

【文献推断｜Corbett及Battesti】操作—制度解释强调舰型、实际训练、风潮、港口与协同，把总舰数与可执行战略分开；Battesti“Une marine française surclassée”一节还强调军官、配员和船厂问题。[E3、E12] 其判断不能直接否定另一时期法国的重建，也不能变成永久民族素质差。

【裁量】这两种解释未必互斥：数量接近可以同时造成英国保编压力而未带来法国全球制海。只有同年同口径舰体、配员、训练和任务集中资料才能裁定程度。**未完成Rodger、Glete及Glover全文的两大学派独立专著核读**；这是验收欠项，不能用两位作者名字冒充完成。Battesti关于英国“必然”先发的措辞是其解释，不作历史定律。

【事实｜来源谱系】James各版与C2引James是一条史料链；Corbett常转引Desbrière，两者非完全独立；Hickey对Glover的复述只有一条原论证链；Davey对Albion/Morriss及ADM的引文不等于本卡读过三套原件。拿破仑命令、英国议会和公报在制度来源上不同，但各自证明命令/论辩/条款，不共同证明训练完成或全数实到。

## 七、可复查短引文与书目

网页缓存行号不是纸本页码；现代转录未与《Correspondance générale》原卷对校。James为扫描OCR，未完成全部影像逐字对校。下列引文均以实际读取的缓存/文本为范围。

- **D1** `../t_104134/c2_series.csv`，物理行2—4；上游说明`c2_naval_econ_data.md`。C2原始类别保留，不合并盟国。
- **D2** `../t_104134/c2_gaps.csv`，16项缺口；不是零值表。
- **D3** `../t_104134/manpower/late_supply_addendum.md`；未并入D1的四个舰材二手锚点。
- **E1a** 拿破仑致Decrès，1810-07-03：“Comme ceci sera en sus de votre budget de cette année, faites-moi connaître ce que coûteront ces cinq vaisseaux tout équipés”。追加建舰的成本询问，不是完工/付款凭证。缓存`downloads/pages/82a063e7e022.md`，行72—77；[现代转录](https://napoleon-histoire.com/correspondance-de-napoleon-ier-juillet-1810/)。
- **E1** 同收信人，1810-07-13：“les équipages pourraient s’amariner en peu de temps”；“on prendrait les matelots les plus amarinés et les plus habiles des flottilles”。同缓存行615—660。前句为预期、后句为人员转换规则，非实际海上日。原转录内部人数和船数有不一致，不用于冻结编制总量。
- **E2** 致Eugène，1811-07-31：“la moitié des équipages restera à bord et l’autre moitié, embarquée sur ces bâtiments légers, battra l’Adria­tique, poursuivra les corsaires, protégera les côtes et s’exercera”；“les Anglais, qui en auraient l’éveil, tiendraient des vaisseaux de guerre dans l’Adriatique”。`downloads/pages/6864746209f3.md`行1348—1356；[现代转录](https://napoleon-histoire.com/correspondance-de-napoleon-ier-juillet-1811/)。后一项是预期敌方反应，不是事后部署统计。
- **E3** Julian S. Corbett, *The Campaign of Trafalgar* (London: Longmans, Green, 1910)，pp.33—34、44—45；`downloads/c11_corbett.txt`行2200—2297、2670—2765。[扫描来源](https://archive.org/details/campaignoftrafalOOcorb)。p.44：“neither the British nor the French naval staffs were content to count numbers only”；p.34转引Villeneuve：“it being out of our power to make much sail with the ships so much maltreated, we agreed to return.” 转引自Desbrière，未阅原折。
- **E4** William James, *The Naval History of Great Britain*, new ed., IV (Richard Bentley & Son, **1886**)，p.108：“After a stay here of 16 days, the French squadron weighed and set sail for Cayenne”；p.114：“a gale or hurricane overtook the squadron, scattering the ships in every direction”；p.116记英舰也失散。`downloads/pages/d6e755fb0b5d.md`行1690—1703、1765以下；卡内`materials/James_1886_IV_sortie_passages.md` A—F。[扫描PDF](https://www.ibiblio.org/hyperwar/NHC/NewPDFs/UK/UK,%20Naval%20History%20of%20Great%20Britain%204.pdf)。不是1837版同页。
- **E5** 同卷pp.390—393、400—408、423—427。p.393：“owing to the state of the tide, had not a sufficient depth of water”；p.402：“Some very excellent regulations were drawn up for the guidance of these boats”；p.405：“owing to the strength of the wind and tide, were obliged to put back”；p.407所转截获军官信：“Our engines played upon and completely wetted the poop”。同缓存行5911附近、6123—6180；卡内摘录G—J。原信身份、日期和档号未核。
- **E6** James Davey, *War, Naval Logistics and the British State: Supplying the Baltic Fleet 1808–1812* (PhD, Greenwich, 2009)，舰材讨论注40—55；`downloads/pages/b92bac3d423e.md`行477—546，印刷页码映射未核。[论文](https://gala.gre.ac.uk/id/eprint/5653/4/James%20Davey%202009%20-%20redacted.pdf)。注40引1808-04-12委员会：“the present scarcity of hemp”；注44引Saumarez：“affording protection to the Ships employed by him in obtaining Hemp for His Majesty’s Service”。原ADM文书未阅。
- **E7** HC Deb, 10 November 1813, vol.27, cc.69—75, “Committee of Supply”；`downloads/pages/3b214d7b54fb.md`。[文本](https://api.parliament.uk/historic-hansard/commons/1813/nov/10/committee-of-supply)。c.72：“He had, in fact, been accumulating his marine forces by rapid strides”；c.73：“If we suddenly disbanded, it would not be so easy a task, on an emergency, to recal our seamen”；c.74将“new buildings, repairs, and other items”另列。辩论双方判断冲突，不能冻结其法国整备数字。
- **E8** *London Gazette*, no.16067, 16 September 1807, p.1231；投降条款1807-09-07，第III、V、VII条。`downloads/pages/7b34f7d2c4ab.md`；[原页](https://www.thegazette.co.uk/London/issue/16067/page/1231/data.pdf)。OCR第III条：“The Ships and Vessels of War osevery Description, with all the Naval Siores…”；保留OCR错误，不称影像校本。全文及限制见`rebuild_feedback_evidence.md`。
- **E9** Hans Christian Bjerg, “‘To Copenhagen a Fleet’: The British Pre-emptive Seizure of the Danish-Norwegian Navy, 1807,” *International Journal of Naval History* 7(2), August 2008；`downloads/pages/71106f9334bc.md`行265—330，页码未核；[论文](https://www.ijnhonline.org/wp-content/uploads/2012/01/Bjerg.pdf)：“The British had no intentions to make use of all the confiscated ships and were never able to do so at that time due to lack of human resources.” Gambier 1807-09-05信仅转引自Bjerg注7，WO1/187未阅。
- **E10** Donald R. Hickey, “The Top 25 Articles on the War of 1812,” *The War of 1812 Magazine* 9, May 2008，第15项；`downloads/pages/d49295b7a7ca.md`行84；[评论](https://www.napoleon-series.org/military-info/Warof1812/2008/Issue9/c_top25articles.html)：“by 1812 had come within striking distance of matching the British in ships-of-the-line.” 关于Madison则说“There is simply no evidence to support this claim.” Glover书目元数据缓存`717b149d2bb0.md`；[DOI](https://doi.org/10.1086/240080)，正文未取得。
- **E11** 柏林敕令，1806-11-21，I—II条：“The British islands are declared in a state of blockade”；“All commerce and correspondence with the British islands are prohibited”。英文转录`downloads/pages/c0e5e2069d0d.md`，条号定位；法律要求不是执行绩效。
- **E12** Michèle Battesti，“Napoléon et la ‘descente’ en Angleterre. 1re partie : Les multiples projets de 1778 à 1803”，*Revue du Souvenir Napoléonien* 444，pp.3—17（网站转载）；`downloads/pages/326b19e197a6.md`，“Une marine française surclassée”及“Doutes…”小节；[网页](https://www.napoleon.org/histoire-des-2-empires/articles/napoleon-et-la-descente-en-angleterre-1re-partie-les-multiples-projets-de-1778-a-1803/)。本卡只用机制论述，不把未核数字加入D1。

### 后续能改变判断的材料

【未验证项】法国全国逐舰存量/年度下水及退出：Glover全文、Winfield & Roberts和SHD MV BB4及船厂清册；英国James其余Annual Abstracts、Winfield与TNA ADM造舰订单、点名表、部署和账目；逐舰航海日志及实弹/编队操练；木材按品种规格的库存和到货；海军战俘按军种/技能与交换流量。档案系列名只是谱系，没有假称读过原折。Davey引用的ADM 111/187、ADM 119/33和Bjerg的WO1/187均为转引线索。

【裁量】优先补法国1814同口径全国端点和1807—14下水/灭失，其次英方同期分类，才有资格启动校准；训练与护航仍要独立验证。即使未来得到“舰数已接近”，也只解决第一层，不会自动解决全球制海。

## 八、文件与复算

- 主报告：`c3_naval_race_model.md`。
- 年度登记：`c3_scenarios.csv`，112行，1803—1830；NA不插值。
- 条件舰数：`c3_thresholds.csv`；诊断恒等式：`c3_quality_thresholds.csv`。
- 校准状态：`c3_calibration.csv`；脚本及哈希：`build_c3.py`、`c3_replay_manifest.json`。
- 证据备忘：`sortie_evidence.md`、`rebuild_feedback_evidence.md`，以及`materials/James_1886_IV_sortie_passages.md`。

在项目根运行：`python3 nodes/r_b55f2c1cf5/cards/t_7ee3b0/build_c3.py`。算法只有整数求和与Fraction门槛，无拟合、回归、随机抽样或船队仿真。可重放不等于史实校准；本卡降级交付保留未满足的数量验收项。
