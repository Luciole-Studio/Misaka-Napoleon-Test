# B3来源与口径清单

本卡写作日期2026-09-23。只列实际使用版本；“已读”包括本卡子任务实际读原文并写入逐条摘录、主笔复核的范围，不等于通读专著。URL为来源、路径为复查入口，**路径不能替代作者与文本内容**。网页转录与PDF/OCR均不冒充亲阅档案。主报告分项以以下键引用。

## 1. J：William James年度舰表

William James, *The Naval History of Great Britain*，1837版年度附表体系，Paul Benyon现代HTML转录；网页标2002更新。索引：https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/Abstract_Index.html 。本轮读到表头“An ABSTRACT ... at the commencement of the year ...”，即年初；四态为Sea-service in commission／in ordinary、Harbour-service两类，另有Building or ordered。Built的King's／Merchants' yards位于上年度增减区，不是当年库存新增。

|键／表年|所读位置与URL|本地版本／核读方式|
|---|---|---|
|J3，J11／1803|III, Abstract11；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_III/Abstract_No_11.html|旧ETH影本PDF395页；James1837_p395.png；网页146cbc594a66.md作比较|
|J3，J12／1804|III, Abstract12；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_III/Abstract_No_12.html|旧ETH影本PDF396页；James1837_p396.png|
|J3，J13／1805|III, Abstract13；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_III/Abstract_No_13.html|旧ETH影本PDF397页；James1837_p397.png|
|J14／1806|IV, Abstract14；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_IV/Abstract_No_14.html|downloads/pages/ee9e07ba451b.md，Line/Cruisers及注a–f|
|J15／1807|IV, Abstract15；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_IV/Abstract_No_15.html|downloads/pages/83c66266952e.md，Line/Cruisers及fir舰注|
|J16／1808|V, Abstract16；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_V/Abstract_16.html|downloads/pages/d39fd55b29e2.md；Line原行首113/197350/13/25089/126/222439|
|J17／1809|V, Abstract17；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_V/Abstract_17.html|downloads/pages/00a2dabd2063.md|
|J18／1810|V, Abstract18；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_V/Abstract_18.html|downloads/pages/ddccd80edb3a.md|
|J19／1811|V, Abstract19；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_V/Abstract_19.html|downloads/pages/b5b76ec14c26.md|
|J20／1812|VI, Abstract20；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/Abstract_20.html|downloads/pages/682e933f431c.md|
|J21／1813|VI, Abstract21；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/Abstract_21.html|downloads/pages/e62d2b040709.md|
|J22／1814|VI, Abstract22；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/Abstract_22.html|downloads/pages/1fe8a9e1b008.md|
|J23／1815|VI, Abstract23；https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/Abstract_23.html|downloads/pages/c2105af935e9.md|

1803–05影图全路径前缀`nodes/r_b55f2c1cf5/cards/t_104134/naval/`，相应CSV为`UK_1803_1805.csv`。原文档`downloads/James_1837_v3_ETH.pdf`，doc_id `a178739fd84c`；PDF398–400页读取附表说明，对应印刷373–375附近，不能以PDF页称原书印页。说明称Sea-service涵盖“every ship fitted or about to be fitted for sea-service”；港勤ordinary不自动等于可动员储备。1803 Cruisers总吨原图356400，HTML356399，一吨差保留。

新七张表：`sources/annual/evidence.md`列每行40数原序列、映射、完整捕获文本SHA256；`extract_captured_tables.py`提取及加法检查；`checks.json`28项残差均0。**零残差不证明原数据正确；现代转录尚未逐影对七张原表。**初次子代理未获工具，曾生成全空接口；本轮主笔已获取全文并重写，生成脚本以七行所有关键字段非空才报告annual_source_loaded=true。直接HTTP失败的`fetch_annual.py`只是过程记录，不作为复算数据源。

其他已读James内容：

- **J-VI40**：VI p40，https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/P_040.html ，`downloads/pages/05ae2a02c794.md`。关键句：“seamen and marines, voted ...145,000”；军官数为名册存量。正文不独立证明票数等于实员。
- **J-VI152**：VI p152，https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/P_152.html ，`c8f3fb7e8d62.md`。1813人员票与造舰讨论，仅作补充。
- **J-VI417**：VI p417起，https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/P_417.html ，`391f1c758def.md`。Seppings斜撑用于试验、维修、重建及新造的先后，不从颂扬词句反推可用率百分比。
- **J-App9**：VI Appendix9，https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_VI/P_500.html ，`1f6907a51a1d.md`。1814前7阴历月86,000海员＋31,400陆战队、后6月74,000＋16,000；交通、战俘、造修等费用各列。
- **J1814text**：1902 Macmillan新版本VI p116（实际读过版权页及正文），https://www.ibiblio.org/pha/USN/Navy/navalhistoryofgr06jameuoft.pdf ，`95e1bd14b0d8.md`。正文称前7阴历月140,000、后6月90,000。与Appendix9前期总117,400有版本／正文与表格冲突，未定谁误。**不混称1837影本亲读。**
- **J1886-IV390**：1886 Richard Bentley版IV p390（相邻p391可定位），https://www.ibiblio.org/hyperwar/NHC/NewPDFs/UK/UK,%20Naval%20History%20of%20Great%20Britain%204.pdf ，`d6e755fb0b5d.md` L5900附近。原句称westerly gales使Gambier离Ushant站位，Willaumez于1809-02-21出航；证明局部天气窗口，非长期突破概率。

## 2. FB、JB：现代综合表，不能冒充原始财务簿

**FB** Gregory Fremont-Barnes, *The Royal Navy 1793–1815*, Osprey, 2007。所读第三方OCR：https://epdf.tips/the-royal-navy-1793-1815.html ；`downloads/pages/7f93512d05f7.md`。

实际用于：军官、强征与舰员结构章；pp41–42奖金、军法与驻区司令；pp44–49拨款、海勤舰队、行政与造船；pp55–57舰型/编制。保留的事实内容：
- “Total naval supplies granted”1812 £19,305,759、1813 £20,096,709；“Number of seamen and marines”145,000而非纯海员。
- “List of active ships,1803–15”1803总Line111，恰为James海勤现役32＋ordinary79，故书表标题active不得照字面解释为全现役。不是独立档案双源核验。
- 1793–1815皇家坞战列41/其他78，私厂战列60/小舰600余；双甲板通常2–3年建造，另需舾装，船工多年学徒。战争全期累计不当单年容量。
- 1808以前奖金舰长3/8、commissioned officers1/8、warrant1/8、petty1/8、其他含marines1/4。1808修改规则，此次未读到完整新分配，未补造。
- 军官考试年龄／年资、不可购买委任但有interest、地区舰队任命不等于在场；用作制度机制，而非全舰队经验年数的量化。

OCR少量地理／组织简化不采用：Deptford不按该图注误作私坞、印度不以Bengal代表全部、Victualling Board地位用RMG分期。其泛称人员从未达票数也不外推到1820后borne系列。

**JB** Paul Benyon网站 *Budget Figures and Manning Levels for RN*，https://sites.rootsweb.com/~pbtyc/Naval_History/Reports/Budgets/Budgets.htm ，`downloads/pages/46ca470fcc48.md`。虽然页面title出现James，系列延至1855且有编辑自注，**整张表不能称James1837原表**。编辑说不知道13 lunar months转12 calendar months确切时点。1815–20数额单位£000、1821后为整镑；“Actually borne”时点未清。B3将其作为有来源但证据等级较低的汇编观测，独立Hansard核1817/1820/1826/1830部分票数，绝不假装读过全部点名册。

军官名单辅助表：https://sites.rootsweb.com/~pbtyc/Naval_History/Reports/Budgets/Officer_Nos.html ，`dc6c3ac4195b.md`；1813/1816缺行。仅说明名册延续，不转换成现役熟练人员。

## 3. H：Hansard（实际网页转录；当时辩论报道非录音逐字稿）

|键|辩论与定位|URL及缓存|实际承重内容|
|---|---|---|---|
|H12|Navy Estimates,22 Feb1812,vol21 cc885–893|https://api.parliament.uk/historic-hansard/commons/1812/feb/22/navy-estimates ；f42cec953d4b.md|Yorke保编：“if once the naval force was to be lowered ... it would be difficult to increase it”；Johnstone资源转大陆反驳；铜回收争论、坞工所得税请愿、牧师／教师、Cochrane沿岸袭扰提案|
|H13|Committee of Supply,10 Nov1813,vol27 cc69–75|https://api.parliament.uk/historic-hansard/commons/1813/nov/10/committee-of-supply ；3b214d7b54fb.md|“If we suddenly disbanded, it would not be so easy a task, on an emergency, to recal our seamen”；政府说美国／波罗的海压力，反方批错误分配。开头140,000 seamen及31,000 marines措辞与其他汇表冲突，不直接相加成171,000|
|H14|Navy Estimates,13 May1814,vol27 cc871–873|https://api.parliament.uk/historic-hansard/commons/1814/may/13/navy-estimates ；0055bf372201.md|退ordinary之前必须修理、半薪增幅尚不确定、和平回运仍花钱；不把和平红利当即刻全额可用|
|H15|Separate Charges,14 June1815,vol31 cc799–822；重点806–807、809–817及818–820|https://api.parliament.uk/historic-hansard/commons/1815/jun/14/separate-charges ；156d03703582.md|“the supplies ... could be applied to the service of our navy”；Tierney反对假定支出自然下降；财相借贷以短期紧急为理由，不是永久财政保证|
|H17，HPOST|Navy Estimates,17 Feb1817,vol35 cc408–409|https://api.parliament.uk/historic-hansard/commons/1817/feb/17/navy-estimates ；245fa51bae26.md|“19,000 ... including6,000 royal marines”；仅6 lunar months；£6 6s是复合人月估算不是工资|
|H20，HPOST|Navy Estimates,17 May1820,vol1 cc459–460|https://api.parliament.uk/historic-hansard/commons/1820/may/17/navy-estimates ；7aa4f576eb19.md|23,000含8,000，13 lunar months；工资£650,325；预拨£500,000不另重复累加|
|H21|Economy and Retrenchment,27 June1821,vol5 cc1345–1442；本次读L1–769重点No28–35|https://api.parliament.uk/historic-hansard/commons/1821/jun/27/economy-and-retrenchment ；95e29ff1c015.md|Hume转引Annual Estimates/Finance Accounts，毛、抵旧物资、实支分栏；No31在役/ordinary；No32造修；No35未完坞工费用；“with the prospect of a long peace”才主张裁船工|
|H22|Navy Estimates,27 Feb1822,vol6 cc783–800|https://api.parliament.uk/historic-hansard/commons/1822/feb/27/navy-estimates ；9198b046bbb7.md|Croker/Hume争当年服务、旧债和旧物资，揭示和平预算为何多个总额皆有来源|
|H26，HPOST|Navy Estimates,21 Feb1826,vol14 cc678–689|https://api.parliament.uk/historic-hansard/commons/1826/feb/21/navy-estimates ；990e6312e3fa.md|30,000含9,000；Hume称估算£6,135,004；半薪军官应在需要时同意召回，非全可立即服役|
|H30，HPOST|Navy Estimates,1 March1830,vol22 cc1121–1143，尤其1136–38|https://api.parliament.uk/historic-hansard/commons/1830/mar/01/navy-estimates ；597653e3e3aa.md|计划29,000/当时>32,000；“our naval force must partly depend upon that of other powers”；陆战队9,000中4,500在舰/4,500在岸；海防缉私与邮船转隶改变账面人员|

表内缓存前缀均`downloads/pages/`。战后全文所读选段及逐项表完整保存在`sources/postwar/read_evidence_and_notes.md`与`rootsweb_crosscheck_addendum.md`，包括1800–55网络汇表的出处警告。Hume表是**议员转引报表**，未亲阅底层Annual Finance Accounts。

## 4. 舰材、采购、给养与北方贸易

### A｜Robert Greenhalgh Albion

*Forests and Sea Power: The Timber Problem of the Royal Navy,1652–1862*, Harvard UP,1926。实际IA全文OCR相关页：https://archive.org/stream/ForestsAndSeaPower/Forests%20and%20Sea%20Power_djvu.txt ；`f9c908249692.md`。已用p355、356、361、367–368、导言ix。原句：

> “the exports from British North America jumped from 4,442 to 16,729 in a single year” (p356)
>
> “Up to 1812, only one cargo of teak had reached England” (p368)

前者是北美大桅贸易，不是海军领用；后者是原木运英而非只有一艘印度柚木军舰。加拿大橡木1810/11超过17,000/24,000 loads，作者load定义50立方英尺，但本卡未换重量。未用损坏的1810运费OCR；未用1811地区桅数微差做精确比例。作者引用海关／ADM底档属转引。

### D｜James Davey

*War, Naval Logistics and the British State: Supplying the Baltic Fleet1808–1812*, Greenwich PhD,September2009。https://gala.gre.ac.uk/id/eprint/5653/4/James%20Davey%202009%20-%20redacted.pdf ；复用`b92bac3d423e.md`。

摘要p.v原句：“By 1810 a fleet lying in the Baltic was as well supplied as one lying off Deptford”。注50：“Albion's tendency to exaggerate shortages should be noted however.” 另读注44–46附近Saumarez/Solly特别护航、表27及前文（p244以前）1809不足／1811改进。正文页映射部分丢失，只给注号与缓存行497/529/3260–3270，不伪造精确印页。Knight1986批Albion经Davey转引，未亲读Knight。

### N｜Patricia K. Crimmin编选的同时代附件

*The Naval Miscellany VII*, Navy Records Society vol153(2008)，学会2021-04-20公开片段 *The Supply of Timber for the Royal Navy,c.1803–c.1830*。https://www.navyrecords.org.uk/members_blog/the-supply-of-timber-for-the-royal-navy-c-1803-c-1830/ ；`01cf29aa1f98.md`。定位Melville致Wellesley1804-07-04附件条2–3：进口外橡木修旧舰，保英橡木新造，“we propose to repair ships upperworks with fir”。3,000 loads加拿大木是订约量非到货量。只读公开附件，不冒充通读NRS卷。

### G｜Science Museum档案目录

Robert Sharp编 *GOOD A: Papers ... Simon Goodrich ... c.1797–1847*。http://archives.sciencemuseumgroup.ac.uk/Documents/SCM/Finding%20Aids/Named%20Archives/GOOD%20A.pdf ；`c611b1f1059d.md`。

仅目录，未读原信：GOOD/A/0205(1807-02-07)旧铜制新片，/0213(1807-05-06)昼夜开铜厂增十人，/0249(1808-07-21)首年产量信；/0232精炼困难。表明资料和命令存在，不提供未知吨数。待取最低成本原档：/0113、/0236、/0249、/0180、/0278。

### M｜Roger Morriss

*Science, Utility and British Naval Technology,1793–1815: Samuel Bentham and the Royal Dockyards*, Routledge,2020，Perlego公开预览“The Admiralty response”。https://www.perlego.com/book/1712747/science-utility-and-british-naval-technology-17931815-samuel-bentham-and-the-royal-dockyards-pdf ；`95d2152c26cf.md`。仅所见预览，无印页；1779–82铜包皮的效能由舰队指挥官报告，不能重复当1808技术新红利，未读第11章铜厂全文。

### Ryan｜A. N. Ryan

“The Defence of British Trade with the Baltic,1808–1813”, *English Historical Review* LXXIV(292),July1959,pp443–466，DOI10.1093/ehr/LXXIV.292.443。作者／刊卷元数据经出版商搜索记录补齐，DOI页面抓取403；**正文实际读的是开放转载** https://www.reenactor.ru/ARH/PDF/Defence.pdf ，`e47ab045c32f.md`。本卡只用读到的pp443–444、450–451及453段（缓存页眉OCR有455误写），不声称读完466页。

俄麻占英国总消费>90%的说法由Ryan转引早期研究，不是皇家海军采购独立份额；pp450–451商人、Lloyd's、Saumarez护航协调，冬季冰冻及晚归风暴。1810挪威47商船被俘是孤立事件，未当平均风险。Drusena别名情报联系为网络机制例。

### BJ｜Hans Christian Bjerg

“‘To Copenhagen a Fleet’: The British Pre-emptive Seizure of the Danish-Norwegian Navy,1807”, *International Journal of Naval History* 7(2),August2008。https://www.ijnhonline.org/wp-content/uploads/2012/01/Bjerg.pdf ；`71106f9334bc.md`。实际读开头及L264–301转引Gambier1807-09-05信：若丹方不毁船，“it will require the whole of the force now with me to equip and navigate them to England”。这是Bjerg转引原信，说明俘获配员和拒敌使用两种收益，非本卡亲阅Gambier档案。英语成文但提供丹麦视角。

舰材十二条逐字摘录和用途限制均在`sources/stores/B3_stores_evidence.md`；主报告采用其内容而非只列文件。

## 5. RMG：制度、劳工与技术的博物馆公开说明

- **RMG-A** Research guide B6: Royal Navy administrative records：https://www.rmg.co.uk/collections/research-guides/research-guide-b6-royal-navy-administrative-records ；`775d373548f6.md` L165–230。Admiralty是分权体系部分、Navy Board1832并入、给养独立；ADM180 Progress Books在1800左右有合并/省略。不把指南指向的ADM/A、ADM/B原件当已阅。
- **RMG-I** Research guide M2: Press gangs and impressment：https://www.rmg.co.uk/collections/research-guides/research-guide-m2-press-gangs-impressment ；`1b22dbe49e2a.md` L160–170。原句“After1815,though not abolished,it was not used.”；“Only seamen should have been pressed,but ... all types of men were drawn in.”目录中的错征／保护证仅线索。
- **RMG-M** Research guide B8: Spithead and Nore mutinies1797：https://www.rmg.co.uk/collections/research-guides/research-guide-b8-spithead-nore-mutinies-1797 ；`2d8d72a79507.md` L157–165。Spithead16艘拒航、工资待遇诉求与让步；Nore更广要求及镇压。不是“亲法革命已蔓延全海军”的证据。
- **RMG-S** SLR0709, HMS Lightning模型说明：https://www.rmg.co.uk/collections/objects/rmgc-object-66670 ；`453f975faa96.md`。正文1823下水木质明轮炮艇、测量用途；馆藏模型约1979制作，不是1823实物；Vessels元数据1829与正文日期冲突。本卡采用正文并明记此差异，不据同名Comet搜索补造1822史实。
- **RMG-R** PAH0923,Rattler and Alecto牵引试验版画：https://www.rmg.co.uk/collections/objects/rmgc-object-140870 ；`b71a637044ed.md`。完整实体说明已读：题名载1845-04-03、螺旋桨与明轮、Rattler拖动Alecto；版画不是受控实验报告，不用它估效率或证明舰队全面蒸汽化。

## 6. 两种非英语文本（均法语；不伪称两门语言）

**FR1** Michèle Battesti,«Napoléon et la “descente” en Angleterre.1re partie:Les multiples projets de1778 à1803»,Fondation Napoléon,napoleon.org。https://www.napoleon.org/histoire-des-2-empires/articles/napoleon-et-la-descente-en-angleterre-1re-partie-les-multiples-projets-de-1778-a-1803/ ；`326b19e197a6.md`。阅读主体有关布洛涅、潮汐、英国反小艇和主力封锁的段落；对其“上岸无人可挡”断言不照收。涉及拿破仑／梅特涅1810回忆、圣赫勒拿等**回溯性转引**，未作为1803意图的硬证据。

**FR2** Napoléon致Eugène,31 juillet1811（Saint-Cloud），Robert Ouvrard站网页书信转录：https://napoleon-histoire.com/correspondance-de-napoleon-ier-juillet-1811/ ；`6864746209f3.md` L1348–1360。原句：“Si les deux vaisseaux restent à Malamocco sans pouvoir sortir ... [équipages] ... s'exercera”；末句“l'année prochaine les Anglais ... tiendraient des vaisseaux de guerre dans l'Adriatique”。信件证明轮训命令和英方响应预期，不证明命令全执行。原编书信号未在此网页核定，不补造。

语言限制：满足两种非英语材料而非两门非英语语言；俄／瑞／丹的采购者声音主要经英语研究、丹麦作者英语文章转入，印度船工直接声音不足。此偏差限制对供应商能动性和劳动政治的精细裁定，不把他们视为被动资源。

## 7. 跨卡接口与上一轮复用

- **F3接口**：`nodes/r_5b1357a9c6/cards/t_b1a536/F3_capacity.csv`、`F3_model_parameters.json`、`F3_model_keypoints.md`。实际读取生成端点与参数，1830 W A12=84/I73、P A12=111/I61。全部model_not_observation，未把F3传来的Todorov/森林研究片段冒称本卡原文独立核验。P4应以最终同口径版本为准。
- **B2接口**：t_044211的£18–22m海军高档意见及1815-06-14引文线索；后者本卡已亲读H15。B2报告1811-05-20海军预算£20,276,144与FB差£454,144；只列跨卡冲突警告，未称本卡逐分项核定。主笔未获得国家总账对本卡全部端点的最终验收。
- **B1接口**：伦敦陷落后的条件续战，与B1的1–3个月有条件议和／法军被孤立则续战窗口兼容；本卡不擅定内阁必降。地方基地不是1803撤移实令。
- 旧C2 `nodes/r_b55f2c1cf5/cards/t_104134/c2_naval_econ_data.md`与naval CSV/影图，复用经核观察，**旧英国1806–15全NA已作废**。
- 旧C3 `nodes/r_b55f2c1cf5/cards/t_7ee3b0/c3_naval_race_model.md`仅复用分层存量—流量逻辑；其“不足以定追平年”不是本轮终局。本卡没有继承旧代码作为已拟合动态模型。

## 8. 仍有冲突，未读文献不包装为证据

1. James1814前期140,000／117,400，以及H13开头140,000加31,000措辞冲突；保留各自文本，不自造平滑均值。
2. 1818 Hume毛估算6,547,810−旧物资309,205应得6,238,605，网页印6,138,605；保留原表误差，模型不使用该净数。1820实际支出同辩论两表差£400，wear项目不同日期差£3；不解释成已查明调整。
3. Benyon1826金额“6,7.35,004”原串损坏，容量表source_corrupt空数值；单列Hansard£6,135,004。1817网页£7.646m含£1.660m债务与Hume年度服务差近似相符，不叫逐镑对账。
4. 1803 Cruisers一吨图文差；新七年表未影本逐核；FB可能同源于James。
5. 实麻库存月数、替代验收、铜年产、逐舰大修吞吐与召回实绩缺口，直接约束A12与封锁压力窗口置信度。
6. 源策略中的Rodger、Glete、Lambert、Lewis及其他Knight著作未在本卡新增亲读；不列其为本卡论据。Crimmin公开片段不等于NRS卷全读；Morriss仅预览。
7. Martin Crevier2019 *Itinerario*43(3),466–488,DOI10.1017/S0165115319000561只得摘要书目；Davey2018“Serving the State…”只有搜索结果，均未作为事实互证。*Counter-Theatre during the1797 Fleet Mutinies*抓取了部分正文但未进入最终承重论证，不以页面存在声称通读／多源验证。

## 9. 数据与模型复核说明

`B3_capacity.csv`：ships、James_tons_burthen、voted persons、nominal_GBP；史实舰表年初非季调，票数／拨款有分段阴历月口径。模型费用单位GBP_at_1812_cost_level，不是平减后的历史实际支出序列。所有section=model及B3_assumption为研究者假设，不提供统计概率。

`build_B3.py`生成容量、16行配对响应、历史表和费用JSON；`model_assumptions.md`完整列系数及失败条件。此前econ-integrity元数据检查仅证单位、版本、来源等字段齐，不证明来源独立、所有数字正确或推演必然。数表分类加总、端点I≤A12≤H和人员公式可复算；材料实物平衡未闭合，不能从算术正确升级到可行性已证。
