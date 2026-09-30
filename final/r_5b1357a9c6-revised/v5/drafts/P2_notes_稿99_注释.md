### 本章注释

〔区1〕模型文件：`models/p2d/p2d_model.py`与`regions.csv`（2026-09-26 v3.1版；v2的代码与输出存于`models/p2d/archive_v2/`）；逐年输出`out_hist_yearly.csv`、`out_flash_yearly.csv`、`out_trackA_yearly.csv`、`out_trackB_yearly.csv`、`out_trackC_yearly.csv`，逐地区逐年输出`out_region_yearly.csv`，事件`out_events.csv`，27组参数敏感性`out_sensitivity.csv`，变体`variants.py`与`out_variants.csv`；复算命令`python3 p2d_model.py --sens --regionlog`与`python3 variants.py`。官方逐地区输出只含抵抗指数、阶段与驻军需求；新兵、净税、藩属中的法军与盟军在场由`v5/drafts/P2_notes_05_逐地区拆账.py`从同一程序拆出：脚本只在地区循环末尾记录各分项，不改参数与公式，逐年核对合计与官方输出一致，并与`out_region_yearly.csv`逐行比对一致。官方变体表以外的组合见`v5/drafts/P2_notes_07_v3补充实验.py`。模型不产生概率。

〔区2〕分层与阶段见`audit/20260925_复审与修缮/P0_修缮总规划.md`第三节第4条。内圈驻军每千人3—5人的标尺出自研究卡P2（`cards/t_c98c24/territory_inputs.csv`第3行，D1内圈低/中/高3、4、5‰）。

〔区3〕三条轨道见`P2_三轨道设定.md`第一至三节；模型对应`trackA`（甲层）、`flash`（昙花一现）、`trackB`（乙层主线）、`trackC`（丙层）。强行成功轨道改为"1821年继承、1823年起摄政期联邦化"，见`models/p2d/README.md`"更新（同日）"一节，所据为研究卡F1（`t_08b9e7/F1_napoleon_center.md`第14、227—229、256行，经A3核查转述）。`P2_三轨道设定.md`丙层表仍写"1825年联邦化""皇帝健康到1836年"，本章按模型更新后的设定写，差异列入交稿说明。

〔区4〕研究卡Q1（`t_afeae6/Q1_resistance_determinants.md`第8、121—161行）。五个持续抵抗正例中宗教政策冲突5/5、外部军事机会5/5、精英吸纳1/5；"挑衅计数×外部机会"交叉表见同卡第152—161行。Q1的局限：目的抽样、单编码者、四条件均为空间型，缺"并合年资×征兵制度化"的时间型条件（同卡第12、95—98、134行）。

〔区5〕研究卡Q2（`t_1f7db4/Q2_integration_panel.md`第152—195行）。门槛式g*＝q×a∞×u×(1＋0.9＋0.9²＋0.9³)；低摩擦L型约3.96—7.32‰，中摩擦M型约2.68—6.19‰，高压H型约1.49—4.54‰；"安全负担宜压在约3‰"见第195行。Q2自我纠错：役期多算一年会把L型第10年的下端由正转负（第197行）。

〔区6〕研究卡D2（`t_e0038f/D2_annexed_outer.md`第65—71行）。四梯度为G1财政—军事国家性、G2正统性空缺度、G3封锁伤害×经济互补性、G4精英补偿到位度。

〔区7〕D1主线见`t_40198e/D1_annexed_inner.md`第9行；Q2年限窗口见`Q2_integration_panel.md`第12行，Q2对D1的更正见第308行（"不能拼成已识别的统一7–12年收敛期"）。P2阶段甲另有"三至七年改善行政程序，七至十二年才审整套税兵交付"的排程（`t_c98c24/P2_provincialization_verdict.md`第192行），同为案例区间。

〔区8〕内圈人口与省数见研究卡D1（`t_40198e/D1_annexed_inner.md`第19行）。1812年预期毛税：比利时8,300万、莱茵3,750万、皮埃蒙特3,300万、利古里亚1,600万法郎，合计约1.7亿，全部新并合地区毛额342,260,044法郎、净额226,389,345法郎；马里翁说新省"到头来花掉的比缴上来的多"。见Marcel Marion, *Histoire financière de la France depuis 1715*, t. IV, 1925, p.321（`downloads/F4_Marion_IV_1925.txt`第16838—16856行，引AN AF IV 1072）。

〔区9〕Alexander Grab, *Napoleon and the Transformation of Europe*, 2003, pp.77—82（本地文本`downloads/pages/2ad693d5ac13.md`第2065—2217行）：战争税8,000万法郎为奥地利年征额的六倍；1795年10月1日并入；1806年人口3,350,000；煤、兵工、韦尔维耶毛纺与根特棉纺数字见其注15—16，经研究卡D1（`notes_grab.md`）整理。

〔区10〕省长籍贯见Stuart Woolf, *Napoleon's Integration of Europe*, 1991, pp.77—81（经研究卡D1`notes_woolf.md`整理）；市长与语言政策见Grab, pp.78—79。

〔区11〕Grab, pp.77—78、81—82。

〔区12〕热马普省数字见Grab, p.79注13（引Delatte 1938）；国有财产出售与承认旧债作为争取精英的"一对"手段，见Woolf, pp.200—201。

〔区13〕Grab, p.78及注9；研究卡Q1（`Q1_resistance_determinants.md`第95行）。

〔区14〕征召225,147、入伍216,111、再收编前的逃征与逃兵合计89,267，见Frasca 1990注41（引Darquenne），转引自研究卡D1（`notes_conscription_tax.md`第9—21行）；逃征率与开小差率见Woolf, p.160；阵亡79,000见Grab, p.82注20；"6.12%"见Grab, p.81注19。7.14%按研究卡Q2的核算（`Q2_integration_panel.md`第91、308行）。

〔区15〕Horst Carl, "Religion and the Experience of War: A Comparative Approach to Belgium, the Netherlands and the Rhineland", in Alan Forrest, Karen Hagemann, Jane Rendall eds., *Soldiers, Citizens and Civilians*, 2009, pp.230—231（本地`downloads/NL_Joor_SoldiersCitizensCivilians2009.pdf`）。

〔区16〕评分见`D1_indicators.csv`第4、11行（Escaut、BE_TOT）；主教入狱与拒认新主教见Grab, p.82；1814年的态度见Grab, pp.82—83。净毛比按注8的马里翁合计（226.39/342.26≈0.66）。和平征额按Q2低摩擦剖面每年每千人1.8—2.8人计算（`Q2_integration_panel.md`第158行）；史实年均按216,111人÷15.3年。

〔区17〕条件算例：内圈聚合地区`d1_inner`的逐年抵抗指数见`out_region_yearly.csv`。模型对内圈不追踪整合阶段（初始状态固定为阶段2，`p2d_model.py`第235行），且以抵抗指数0.22起步，因此内圈的阶段判断以研究卡D1为准，模型只提供方向。

〔区18〕研究卡NL（`t_ccdcc8/NL_netherlands_switzerland.md`第354—363行，引Helmreich、Edmundson、Kossmann经IIASA IR-05-041与Hemstad）。

〔区19〕Michael Rowe, *From Reich to State: The Rhineland in the Revolutionary Age, 1780—1830*, 2003, pp.143—146（经研究卡D1`notes_rowe.md`整理）；幅员与小邦数见Grab, p.92。

〔区20〕Michael Rowe, "Economic Warfare, Organized Crime and the Collapse of Napoleon's Empire", in Katherine Aaslestad, Johan Joor eds., *Revisiting Napoleon's Continental System*, 2015, p.193（`downloads/X2_AaslestadJoor2015_Revisiting__fa6d9fd68f7f.pdf`）。并入时序见D1第19行。

〔区21〕Rowe 2003, pp.94—95、106—108。

〔区22〕宪兵见Rowe 2003, p.181；海关见Rowe 2015, p.187，经研究卡X2（`t_6f3beb/X2_continental_system_machine.md`第48—51行）核读。年薪约160万法郎按最低一级海关人员（préposé）年薪500法郎估算（年薪数见Rowe 2015同章），为下限。

〔区23〕Rowe 2003, p.179表3（据Vallée编Hargenvilliers与AN AF IV 1124）；差中差复算见研究卡Q2第65行；Woolf, p.161另记莱茵开小差由约10%降到不足2%，两说并存。

〔区24〕Horst Carl, p.230；"征前抵抗几乎消失"见Woolf, p.161；机动纵队见Rowe 2003, p.182。

〔区25〕Rowe 2003, p.173（1802年5月18日法律许可雇人顶替，须缴100法郎税，1805年起可在全省雇人）、pp.176—177表2（鲁尔省公证档案，合同数依次为9、15、14、12、4、10、22、14份）。农业工人日薪约50生丁、城市工匠约1法郎。

〔区26〕Rowe 2003, p.201（1803年法方备忘录）；预期毛税见注8。莱茵资产阶级买走1803年后上市的流亡者与教会土地一半以上，见Grab, p.93注17。

〔区27〕Rowe 2003, pp.109—113（选举团）、pp.184—187（萨尔起义：57人过特别军事委员会，16人判死，10人处决，28人判8—12年铁镣）；显贵归附的时序见pp.95—96与p.188（荣誉卫队）。

〔区28〕19%见D1第68行；科隆贸易与保险费率见Rowe 2015, pp.194—195。

〔区29〕D1第48、91行；Rowe 2003关于普鲁士1814年调查与"莱茵法"的论述，经D1`notes_rowe.md`整理。

〔区30〕人口两说见Frasca 1990, p.213，转引自D1（`notes_conscription_tax.md`第38行）；并入时序见D1第19行；1798—1799年的占领与农民起义见Grab, p.156。

〔区31〕Woolf, pp.77—78（首任六位省长的名字与出身）；1805年的撤换同见此处。

〔区32〕Frasca 1990, p.218注27，转引自D1（`notes_conscription_tax.md`第45—51行）。两卡分歧：D1把"500/4,000"写成"t0合规≈12.5%"（同文件第51行），Q2第83行认为那只是抱怨，不能写成配额完成率。

〔区33〕Frasca 1990, pp.213—219，转引自D1；塔纳罗省罚款与亚历山德里亚军事委员会见`D1_indicators.csv`第22、18行。

〔区34〕宪兵见Frasca注34，转引自D1；地主国民自卫军见Woolf, p.91；"秩序已恢复、统治有效"见Grab, p.169注30引Broers。

〔区35〕炮兵军官与纳税大户见D1第63行及`D1_indicators.csv`第19行（据Woolf）；边界争议上诉国务会议见Woolf, p.198；德·迈斯特1806年的信见D1第63行（据Woolf）。

〔区36〕Marion, t. IV, p.268（`F4_Marion_IV_1925.txt`第13936—13950行）、p.309（第16150—16161行）、p.335注3（第17589—17593行）。

〔区37〕Woolf, p.103（"给勒布伦六个月"）、p.116（1805年5月29日任命训令）、p.78（杜拉佐）。

〔区38〕Woolf, p.119（勒布伦因暂停热那亚水手征集受申斥）、p.120（"统治人民不能靠软弱"）、p.161；灯节与"奇迹潮"见Michael Broers, *Politics and Religion in Napoleonic Italy*, 2002, pp.28—30；评分见`D1_indicators.csv`第27行；1814年见Grab, p.173。

〔区39〕`D1_indicators.csv`第28行（LE_TOT）；Woolf, p.80；马里翁p.321的表中无莱芒省；D1第89行。

〔区40〕研究卡D2（`t_e0038f/D2_annexed_outer.md`第20行）。

〔区41〕Grab, pp.170—171（本地文本第4153—4158行），经研究卡D2（`notes_italy_units.md`）整理；`D2_indicators.csv`第3行（帕尔马）。

〔区42〕`D2_breakpoints.csv`第3行（帕尔马：断裂点、失败型、移除测试）。

〔区43〕Marion, t. IV, p.335注3（见注36）。

〔区44〕研究卡P2（`t_c98c24/territory_inputs.csv`第4行；`region_detail.csv`帕尔马各行：年名义征额600、年到营420、驻军1,200）。

〔区45〕条件算例：`out_events.csv`（乙层`trackB`1811年帕尔马"进入阶段2"，甲层`trackA`无此事件）；逐地区数字见`P2_notes_05_逐地区拆账.py`。乙层与甲层对帕尔马的差别来自收编参数（`p2d_model.py`中`coopt`0.8对0.5）与征兵系数。

〔区46〕Grab, pp.169—170（本地文本第4143—4151行）、p.156（1799年"万岁玛利亚"起义，第3817行），经D2整理；枫丹白露条约第1、9条见Toreno转录（`downloads/pages/a21397d83d22.md`），经研究卡PT（`t_219822/notes_core.md`第N1条）核读。

〔区47〕`D2_breakpoints.csv`第2行；D2第54行。

〔区48〕Marion, t. IV, p.321；`territory_inputs.csv`第5行（托斯卡纳税余低/中/高为−5、2、8百万法郎）。

〔区49〕轨道设定见`P2_三轨道设定.md`第一、三节；模型v3.1的甲、乙、丙三层都不并托斯卡纳（`p2d_model.py`第148、170、193行的注释："托斯卡纳（埃特鲁里亚）不并——不瓜分葡萄牙，王室无从补偿"），`models/p2d/README.md`称依据第七章。旧版书稿已指出"史实上的托斯卡纳兼并不能无条件挪到新时间线上"，见快照`r_5b1357a9c6-revised-backup-20260926-003436/chapters/07_行省化的边界.md`第157行与`04_西班牙与意大利.md`第405—417行的地图表。埃特鲁里亚国王与西班牙国王的祖孙关系见同一README的v3.1说明。

〔区50〕研究卡D2（`notes_valais.md`第1—20行，据Lechevalier的瓦莱档案指南、napoleon.org所载1810年11月12日敕令全文、verfassungen.ch所载1810年12月13日元老院令）。人口两说：D2据napoleon.org作12.6万，研究卡NL（`notes_primary_finance.md`第9条）作"约6—7万"；本章用12.6万。

〔区51〕1810年7月25日致克拉克信见拿破仑通信（本地`downloads/pages/82a063e7e022.md`约第1960行），经研究卡NL（`notes_primary_finance.md`第9条）核读：日内瓦集结宪兵连与1,200名葡萄牙兵，第23轻步兵团两个营1,500人过大圣伯纳德驻奥斯塔，1,200名意大利步兵与50骑集结多莫多索拉。敕令理由、宣誓、驻军裁减、两名副省长、法典德译请求见D2`notes_valais.md`（AN F/2(I)/405）。

〔区52〕瓦莱营兵力见D2`notes_valais.md`（据Picard与Tuetey编《未刊通信》经berjaud页转述）；高丹的评语见Marion, t. IV, p.321（引高丹1811年4月30日报告）；省长出逃见D2`notes_valais.md`。

〔区53〕研究卡NL（`NL_netherlands_switzerland.md`第424行，"切腊肠"备选，中置信）。

〔区54〕研究卡X2（`t_6f3beb/X2_continental_system_machine.md`第24行）：凯尔1808年1月21日并入以保莱茵渡口→荷兰1810年7月9日→汉萨与北海岸1810年底→提契诺1810年10月被意大利军占领→贝格1811年请愿被拒。

〔区55〕人口与城市化见Johan Joor, "'A Very Rebellious Disposition': Dutch Experience and Popular Protest under the Napoleonic Regime (1806—1813)", in Forrest, Hagemann, Rendall eds., *Soldiers, Citizens and Civilians*, 2009, pp.183—184（经研究卡D2`notes_holland.md`整理）；国债数见研究卡NL第53行（据Kossmann经Grab p.65注13）；年息7,800万法郎见Marion, t. IV, p.325（`F4_Marion_IV_1925.txt`第17034—17046行）；霍普—巴林财团见NL第56行（据Mark Hay 2024的出版摘要与Buist）。

〔区56〕海牙条约、三次政变、1805年公投与路易的政策见研究卡NL第37—39行；1808年10月来信见同处；进港船只数见Grab, p.70注24（引Schama）；瓦尔赫伦见Grab, p.71注28（经NL第68—79行整理）。

〔区57〕省长籍贯见Woolf（经研究卡D1`notes_woolf.md`整理）；莫利安信与附言见拿破仑1810年7月25日致莫利安（本地`downloads/pages/82a063e7e022.md`第1927—1929行），"保留荷兰行政，因为它比我们的更节约"见同文件第999行（另有海军行政一处，第320行）。

〔区58〕削债见Marion, t. IV, p.325；"灾难"见Woolf, p.201；多担约5,200万法郎的算术见研究卡NL第61行；动因比例见Joor 2009, p.191。

〔区59〕Joor 2009, pp.187—192；参加者画像与致死人数见Joor 2009, pp.192—193；东弗里斯兰与鹿特丹见Bart Verheijen, *Nederland onder Napoleon*（博士论文，2017）, pp.176—177（本地`downloads/NL_Verheijen_Nederland_onder_Napoleon.pdf`），该处并引拿破仑1811年4月21日致萨瓦里："下令当众处决三个最闹事的人。"

〔区60〕Joor 2009, p.191注26；Johan Joor, "Significance and Consequences of the Continental System for Napoleonic Holland", in Aaslestad, Joor eds., *Revisiting Napoleon's Continental System*, 2015, p.263。

〔区61〕Horst Carl, p.230；实征不足一半见Grab, p.72（经NL第80行整理）。

〔区62〕人口与救济见Joor 2015, pp.264—266；出逃与崩溃见同章pp.266—268；预期毛税与高丹的估计见Marion, t. IV, p.321；拿破仑的估算见`downloads/pages/82a063e7e022.md`第1927行。

〔区63〕研究卡NL第278—280行（"兼并不带毒针"反事实，中置信）。

〔区64〕研究卡NL第358—363行。

〔区65〕Katherine B. Aaslestad, "War without Battles: Civilian Experiences of Economic Warfare during the Napoleonic Era in Hamburg", in Forrest, Hagemann, Rendall eds., *Soldiers, Citizens and Civilians*, 2009, pp.123—126（经研究卡D2`notes_hansa.md`整理）。

〔区66〕研究卡G2（`t_cbaee3/G2_north_german_states.md`第67行；"外部成本定理"见第67、263行；据Vandal, *Napoléon et Alexandre Ier*, t. I，本地`downloads/R1_vandal1_full.txt`第17464、18492—18494行）。

〔区67〕Grab, pp.93—94（本地文本第2551—2553行）；Aaslestad 2009, pp.126、128—129；"关税壁垒照旧"一句见p.126。

〔区68〕Aaslestad 2009, pp.124—127；城门冲突与"吸血鬼"一语见pp.128—129（引贝内克日记）。

〔区69〕Aaslestad 2009, pp.129—131；罚款见研究卡G2台账；汉堡银行白银见旧版书稿快照`03_大陆诸国.md`第298行及其注[18]；预期毛税与高丹估计见Marion, t. IV, p.321。

〔区70〕G2第67行；涅谢尔罗迭五项要价见`downloads/c12_vandal3_full.txt`第20965—21287行（经上一轮研究卡核读）。

〔区71〕`D2_breakpoints.csv`第6行；模型`trackC`的征兵系数1808—1824年为0.9、1825年起为0.7，未对汉萨单列免征（`p2d_model.py`第204—205行）；汉萨的抵抗指数初值v3起为0.12（`regions.csv`汉萨行，备注"v3校准据第十章起草人交稿说明§七"）；阶段读数见`out_events.csv`（`trackC`1813年进入阶段2、1827年进入阶段3）。

〔区72〕Charles Schmidt, *Le Grand-Duché de Berg (1806—1813)*, 1905, p.384（迪德里希斯呈文；本地`downloads/G2_schmidt_berg_1905.txt`第18333—18342行）；缪拉与摄政见Grab, pp.96—98（经研究卡G2第46行整理）。

〔区73〕Grab, p.97（经G2第96、143行整理）。

〔区74〕Schmidt, p.386（罗德雷1810年12月报告）：正文作对法830万、对荷"0.650.000"（识读不清），注2所列罗德雷数字为对法8,350,000、对荷9,050,000、北方诸省4,000,000，本章用注中数字；Grab, pp.97—98；焚货与特里亚农、枫丹白露敕令的打击见Rowe 2015, pp.194—195；外迁见Schmidt, p.395所引伯尼奥信与pp.384、396。

〔区75〕三档要求见Schmidt, pp.386—387；伯尼奥信见p.395；代表团、签名数（注1：埃尔伯费尔德960名厂主，总计逾4,000名工业家，副本存AF IV 1839）、牧师上书与六月返回见pp.395—397；1811年11月杜塞尔多夫见p.371的章节提要；1813年1月起事见Grab, p.108（经G2第177行整理）。

〔区76〕科隆商会1810年9月16日答问书见Schmidt附录（AN F12 549—550），经研究卡G2第126行核读；科兰·德叙西复信见Schmidt, p.390（注1：AF IV 1080）；两个会议与联合委员会见pp.391—393；蒙塔利韦报告见p.394注2（F12 549—550）。

〔区77〕Rowe 2015, p.195；研究卡X2第24行；罗德雷对疆界的看法见Schmidt, p.387。

〔区78〕罗德雷1811年1月23日的谈话纪要，见P.-L. Rœderer, *Œuvres*, t. III, p.564，转引自Schmidt, pp.390—391。

〔区79〕Rowe 2015, p.195原文先写"in part because of lobbying by manufacturers within France"，再写"A second reason"；研究卡X2第24行称"被拒的理由是纯粹的执行地理学"，本章按罗原文并列两条，另加施密特所引拿破仑的谈话。

〔区80〕研究卡IT2（`t_8f2668/IT2_naples_sicily.md`第204行，B4行：若保留西班牙波旁，缪拉大概率仍留在贝格或另得他国，那不勒斯由约瑟夫续任）。

〔区81〕罗德雷的三种方案见Schmidt, pp.386—387、390（1811年1月23日）；"统一10%税率"是方案之一。"五年过渡"为本章的组合设计。

〔区82〕研究卡G2第42行（1807年11月15日宪法与同日两封致热罗姆信，据上一轮卡`rhine_notes.md`逐条核读）；等级会议只召集两次见Grab, p.99。

〔区83〕G2第42行；Rowe 2003, p.189。

〔区84〕G2"财政"节（引Berding手稿与Grab, p.101）。

〔区85〕多恩贝格起义见G2第175行附近（据《威斯特法利亚导报》1809年5月4日、Bickert 2009）；征兵、赴俄与1813年见G2兵员表（据Grab, pp.101、108）；北部并入法国见G2第258行。

〔区86〕莱茵邦联条约第38条（本地`downloads/pages/227f1cf6004e.md`第136—150行）；模型参数见`models/p2d/regions.csv`的west_rest行（ally_roster＝8000，备注"须按实际条约军额修正"）。

〔区87〕G2第50行（据Grab, pp.88—89、102）；贝克的判断见G2第280行（Karl Beck, *Zur Verfassungsgeschichte des Rheinbunds*, 1890）。

〔区88〕G2第258—271行（三轴承受度表）。

〔区89〕伊利里亚的法律地位见Grab, p.188（本地文本第4501行，"minor appendage"）与Marion, t. IV, p.321注1（罗马、特拉西梅诺、荷兰七省、易北三省与利佩省的财政行政到1811年底仍分立，"伊利里亚则一直分立"）；加泰罗尼亚1812年敕令的法律地位见研究卡D2（`notes_catalonia.md`，据napoleon.org、histoire-empire.org与法文维基三处互证）。模型把伊利里亚与加泰罗尼亚分别标为"occupation"与"war_control"（`t_c98c24/territory_inputs.csv`第11—12行）。

〔区90〕人口口径见`D2_indicators.csv`第4行（1810年7月帝国预算指令）；教皇国人口与教士数见研究卡IT3（`t_5b1d64/IT3_papacy_churches.md`第47、53行，据Grab注32）；托伦蒂诺条约见IT3第47行；1805—1809年的并合链见Grab, pp.170—171（本地文本第4160—4188行）；马尔凯并合敕令的日期见Madelin第10404—10406行（"par le décret du 2 avril 1808, la réunion définitive des Marches"）；"罗马的皇帝"一语见IT3第192行（通信全集第11445号，经Hicks转引）；绝罚令不许报复见旧版书稿快照`04_西班牙与意大利.md`第371行。

〔区91〕IT3第56、119行（Gabrielli照会，Pacca回忆录第二卷附件第XI号，IT3亲核）。

〔区92〕Broers 2002, pp.154—155、161（本书第6章；本地`downloads/D1_Broers_Politics_Religion_Napoleonic_Italy__4c3bc326766c.pdf`）。罗德雷语见p.155："You have to close your eyes to this mess"。

〔区93〕翁布里亚主教见Louis Madelin, *La Rome de Napoléon*, 1906（本地`downloads/D2_Madelin_Rome_de_Napoleon.txt`第18890—18966行），经研究卡D2整理；法律人拒誓见同书第20245—20272行（原文"1,156 Curiali sur 1,200"，OCR作1,456），市政与国民自卫军同处；六个月的期限见Woolf, p.103。

〔区94〕Madelin第17452—17462行（1810年首征，引AF IV 1509公报1810年8月17日、22日）；1811—1812年见同书第25920—26010行（经D2`notes_rome.md`第8—17行整理）。图尔农语见Madelin第25934行段注2（图尔农未刊回忆录）；"镀金的征兵"见第27271、33795行附近；45%为27÷60；D2第100行与`D2_breakpoints.csv`第4行误作54%，旧版书稿第八章已更正。

〔区95〕Marion, t. IV, p.321；1810年财政会议指令见`downloads/pages/82a063e7e022.md`第2028—2133行（经研究卡F4核读）；"并合不是一桩财政事务"、Luoghi本金约5,000万、教产估值1.48亿见Madelin第27868—27945行；1811年拍卖见第28120—28135行；出售放缓见第25615—25625行。

〔区96〕研究卡Q1第249行（引Madelin："un caractère insurrectionnel grave"）。

〔区97〕Broers 2002, p.167（诺尔万语）。

〔区98〕IT3第160—168、200行。

〔区99〕IT3第59、116行（据Consalvi回忆录第二卷，本地`downloads/IT3_Consalvi_memoires_v2_1864.txt`第7193—7518行；回忆材料，属回溯性），经研究卡A4复审核对。

〔区100〕Grab, pp.188—189（本地文本第4497—4501行），经研究卡D2（`notes_illyria.md`第5—10行）整理；达尔马提亚民政见旧版书稿快照`04_西班牙与意大利.md`第223—227行。

〔区101〕Grab, pp.188—192（本地文本第4507—4509、4554行）。

〔区102〕Grab, pp.192—193（本地文本第4554—4556行）；首年与累计两种口径见D2`notes_illyria.md`"本卡口径"。

〔区103〕Grab, p.194（本地文本第4560行，引Pivec-Stelè与Bundy）；支出见研究卡F4台账（据Grab, pp.188—191）；高丹估计见Marion, t. IV, p.321。

〔区104〕Grab, pp.194—196（本地文本第4564—4597行），1813年德累斯顿见p.201（第4682行）；D2第58—60行。

〔区105〕最可能与乙层的"1809年奥地利不开战"见`P2_三轨道设定.md`第一、三节；模型`trackC`的`"illyria": sched((1810, "A"))`见`p2d_model.py`第197行。旧版书稿已指出"1809年伊利里亚行省的设立依赖新的对奥战争"（快照`04_西班牙与意大利.md`第227行）。

〔区106〕`D2_breakpoints.csv`第7行（伊利里亚）。

〔区107〕棉纺工人数见研究卡SP1第47行（经研究卡A4复审整理）；船次见旧版书稿快照`04_西班牙与意大利.md`第47行（其注[3]）；洪塔决议见研究卡Q1第236行（据Esdaile ed., *Popular Resistance in the French Wars*, 2005, pp.91—94中Moliner Prada一章）。

〔区108〕研究卡SP2（`t_27c409/SP2_spain_society.md`第27—30行，据John Tone, *The Fatal Knot*, 1994, ch.2）；1640、1705的记忆见SP2第183—188行。

〔区109〕诈取要塞与2月24日照会见研究卡A4复审F5条（据Esdaile, *The Peninsular War*，本地`downloads/SP1_Esdaile_PeninsularWar.txt`第1993行）；赫罗纳见同书第2298行（经D2`notes_catalonia.md`整理）。

〔区110〕1810年2月8日敕令文本见xtec.cat档案页与Digitum所录"东北加泰罗尼亚未刊法国统治文献汇编"叙录；三任总督与1812年1月26日敕令见napoleon.org"Les départements réunis et les gouverneurs généraux"、histoire-empire.org与法文维基，均经D2`notes_catalonia.md`整理。

〔区111〕Mercader Riba, "L'oficialitat del català sota la dominació napoleònica", *Butlletí de la Societat Catalana d'Estudis Històrics*（raco.cat摘要），转引自D2`notes_catalonia.md`；1812年4月的评语为同文所引王家法院委员会意见。

〔区112〕普伊格见Esdaile, *The Peninsular War*，第3615行；宪兵见Woolf, p.91；1813—1814年见D2`notes_catalonia.md`。

〔区113〕纳瓦拉见研究卡SP2`notes_tone_fatal_knot.md`第39—48行（据Tone, *The Fatal Knot*, ch.6—7）；116个市镇与"五年产出的40%"见SP2第51行。

〔区114〕SP2第183—188行（B4c兼并至埃布罗）；Q1第236行。

〔区115〕研究卡Q2第228行：A相对B的军力收益＝(M_A−G_A)−(M_B−G_B)，财政同样作差分。

〔区116〕Grab, pp.158—165（经研究卡IT1`t_be9258/IT1_kingdom_of_italy.md`第35—38、60—66、86—92行整理）；赴俄人数见Grab, p.171注34。

〔区117〕1805年3月17日章程第3、4条见IT1第40—44行；立法团解散见IT1第37行（据Grab, pp.159—160）。

〔区118〕Grab, p.164（经IT1第88行整理）；普里纳遇害见IT1第109行（据《意大利传记辞典》）；征兵阈值见IT1第90—92行（推演，中）。

〔区119〕IT1第203—207行（"分支A行省化"，以研究卡F4所核罗马预算指令为标尺）；马尔凯见研究卡D2第180—182行（据Grab 2013论文第140行附近）；Q1区间见`Q1_resistance_determinants.md`第205—228行表（北意伦巴第行）。

〔区120〕IT1第207行；拉德茨基可用兵力约7万见本地`downloads/pages/7027396ad89a.md`（Hilleprandt 1867，转引）；军队过半效忠见`downloads/pages/977ad00e38d7.md`第22行（Sondhaus），均经研究卡A4复审整理。

〔区121〕研究卡D2第182行（备选，中低）。

〔区122〕调停法第26、28、29、31、32、33条见本地`downloads/CH_Acte_de_mediation_1803.pdf`，经研究卡NL（`NL_netherlands_switzerland.md`第141行、`notes_swiss_docs.md`第12—13行）核读；兵额与赴俄人数见NL第⑤节（卢塞恩州档案馆、Grab p.121等三源并列）。

〔区123〕NL第141—147行（"保守外壳＋革命内核"）；1810年见NL第④节与研究卡X2第24行；失业见NL第④节（据Guillon经Grab, p.120注19）。

〔区124〕NL第②③⑥⑦节（海尔维第时期与72,000法军见Grab, p.116；净损算术见NL第181行）。

〔区125〕NL第367—369行。

〔区126〕研究卡G1（`t_f55d87/G1_south_german_states.md`第24—28行），经研究卡A1复审整理。

〔区127〕邦联条约第38条见注86；赴俄人数见旧版书稿快照`03_大陆诸国.md`第242行；蒂罗尔见G1"专题C"第3条；里德条约见快照`03_大陆诸国.md`第244行及研究卡G1`notes_bavaria.md`第61—73行。

〔区128〕G1"专题C"（S6反应剧本，第113—117行）与第⑮节。

〔区129〕研究卡P2（`region_detail.csv`的C_province_pressure_1830南德行）；Q1第106—117、205—228行（"1111格"的警告）。

〔区130〕研究卡P2第173行与`P2_joint_optimistic.csv`第3行。

〔区131〕废封建的财政动机见Delpu等2018年导论（本地`downloads/f1_gouverner_naples_hal.pdf`），经研究卡A4复审整理；债务、修院、国有财产、驻军、军费比例见研究卡IT2第55—62行（据John A. Davis, *Naples and Napoleon*, pp.143—180；Rambaud）；卡拉布里亚见Davis（旧版书稿快照`04_西班牙与意大利.md`第319行及其注[22]）；迪朗训令见Davis, p.154（经A4整理）。

〔区132〕IT2第173行（专项A第1条，高置信）。

〔区133〕IT2第62、176—178行（专项A第2—3条）与第215行（1811年废王分支）；P2`region_detail.csv`那不勒斯行。

〔区134〕两个占领切片见研究卡SP2第15.1节（据Oman返表，`downloads/f2_oman_vol3.txt`、`f2_oman_vol4.txt`）；22.5万见研究卡F2（`F2_garrison_disaggregated.csv`，经A3复审整理）；P2中值见`region_detail.csv`西班牙其余行；Q1区间见第205—228行表；SP2的反证检验见第15.2节；约2.5万协作兵与"胜利后18个月内约七成"见研究卡SP1第153—157行（经研究卡A4复审整理）；"不省化西班牙"一语见D2第194行。

〔区135〕研究卡PL（`t_b5dab4/PL_poland_lithuania.md`第34—40、46—52、77、93、107—123、186行），经研究卡A2复审整理；赐地见Woolf, p.201。

〔区136〕PL第298—300、341行；Q1第205—228行表（波兰行）。

〔区137〕研究卡P6（`t_c87512/P6_victory_paths_wargame.md`第634行附近），经研究卡A3复审转述。

〔区138〕阶段与层级依据各地区小节的年表；模型读数见`out_events.csv`与`out_region_yearly.csv`。直辖人口：最可能轨道38.38百万（`out_trackA_yearly.csv`），托斯卡纳并入则加1.1百万；昙花一现1813年47.38、1814—1816年49.38、1817—1848年43.78百万（`out_flash_yearly.csv`）；强行成功55.38百万（`out_trackC_yearly.csv`），乙层38.38百万（`out_trackB_yearly.csv`，贝格留给缪拉）。丙层的意大利王国按1810年极盛口径6.7百万计，乙、丙两层把马尔凯归还教皇，实数略低（`models/p2d/README.md`v3.1说明）。

〔区139〕第十二章草稿（`v5/drafts/12_行省化三轨道与总判.md`）第四节第5小节"回到自然疆界"。1813年11月联军在法兰克福提出的"自然疆界"以莱茵河、阿尔卑斯山、比利牛斯山为界，见该章注〔行56〕。

〔区140〕D2第143—172行（外圈年表与回摆）；阶段读数见`out_events.csv`（`trackC`：汉萨1813年、威斯特法利亚1829年、荷兰1834年进入阶段2；北意、伊利里亚、瑞士无阶段2事件）；昙花一现的脱离与转向见同一文件的`flash`各行。

〔区141〕`models/p2d/README.md`"结构"一节；`p2d_model.py`的`simulate`函数与`PARAMS`（调整速度低/中/高剖面0.40、0.25、0.15；适应上限0.12、0.10、0.04）。

〔区142〕`PARAMS`中`g_base`＝1.5、`g_k`＝25；阶段门槛`stage2_R`＝0.30（3年）、`stage3_R`＝0.20（5年）、`regress_R`＝0.60；实收率＝1−0.8×抵抗指数（下限0.10）；逃役率＝0.05＋0.60×抵抗指数（上限0.85）；兵均年费700法郎，在场率0.85；新省净税的一半计入陆军预算。荷兰债息见`regions.csv`（debt_service 78、削后26）。

〔区143〕`p2d_model.py`第304—315行（叛离的三个条件）与第338—342行（藩属与同盟改换保护人）。

〔区144〕条件算例：`models/p2d/variants.py`的变体"同一地图改用史实方法（1813年后对英和平）"——以`trackC`的地图与日程为基础，教会冲突1809年起、市场排斥1810年起、征兵系数1808年起为1.3、收编0.3、荷兰1810年削债，去掉联邦化与贝格的市场准入；输出见`out_variants.csv`与`variants_log.txt`。1815—1820年余缺−8.4万至−12.6万人、缺钱6,900万—1.04亿法郎；1821年荷兰、北意脱离，罗马、加泰罗尼亚、埃布罗以北、西班牙其余、南德、那不勒斯改换保护人。皇帝活到1836年的版本由`v5/drafts/P2_notes_07_v3补充实验.py`算出（只改继承年份）：1821—1829年每年缺12.1万—12.4万人，1830年荷兰、北意脱离，此后无藩属转向。修缮总规划P0第八节第2条记为"1815—1825年缺兵17.6万—24.5万"，那是v2的读数；v3把外敌够不着之处的驻军需求折减以后，缺口约减一半，方向不变。

〔区145〕条件算例：`out_variants.csv`："摄政拒绝联邦化"1830年余0、1848年−2.3万人（缺约1,900万法郎）；"奇迹M1"（1836年继承、1825年联邦化）1848年＋4.4万人。"联邦化照做、英法战争延续"不在`variants.py`中，见`models/p2d/README.md`"变体"表，本章用`P2_notes_07_v3补充实验.py`复算一致：1815—1821年−1.8万至−5.3万人，1821年加泰罗尼亚、埃布罗以北、西班牙其余、南德、那不勒斯改换保护人，1822年北意脱离。

〔区146〕条件算例：`out_variants.csv`："永不放弃西班牙"1823—1848年每年−11.0万至−11.9万人、8,700万—9,800万法郎；"1814年放弃西班牙"1815年＋21.5万、1821年−2.4万，1822年荷兰、罗马、伊利里亚脱离，无藩属与同盟转向，1848年＋5.1万。西班牙其余的驻军需求见`out_region_yearly.csv`（1808年18.5万，1816—1821年23.66万）。

〔区147〕`out_sensitivity.csv`（27组：驻军密度系数18、25、32×调整速度0.8、1.0、1.25倍×收编−0.1、0、＋0.1；取1815、1830、1848三年）。

〔区148〕`models/p2d/README.md`"已知局限"第1条。

〔区149〕荷兰见Joor 2009, p.191注26（西荷兰平均约15,000人，至1813年底）；伊利里亚见D2`notes_illyria.md`（Grab：并合前法意达尔马提亚军团峰值28,562人）。模型读数见`out_region_yearly.csv`的`hist`各行（荷兰1811、1812年13,746、16,969人；伊利里亚1810—1812年21,076—24,594人；1813年荷兰39,456人、汉萨14,500人）与`models/p2d/README.md`"史实校验"一段。1809年的外部机会事件只写在`hist`轨道（`p2d_model.py`第108—111行），`flash`轨道（第118—143行）没有。

〔区150〕内圈见`regions.csv`的d1_inner行（R0＝0.22）与`p2d_model.py`第235行（内圈初始阶段固定为2）、第292—303行（阶段逻辑只作用于旧法国与内圈以外的A层与W层地区）；战争占领区的规则见第312行注释；伊利里亚、荷兰免征兵、瑞士范围分别对照`P2_三轨道设定.md`第三节丙层表。

〔区151〕研究卡P2第182—198行（新增岗位、宪兵与外调年流量表）。

〔区a1〕Horst Carl, pp.231—232：神父在教堂为出征新兵做弥撒与祝福；"几乎没有神父支持逃兵的证据"；帝国末年许多比利时神父被捕，是因为教皇被捕与皇帝离婚以后拒绝按规定为拿破仑祈祷；1806年帝国教理问答把拒服兵役与开小差定为死罪。

〔区a2〕Rowe 2003, p.176：直到1813年，连雇工、农夫、船夫、木鞋匠这样的普通莱茵人也组成互助会，为抽签投保、合伙雇人顶替。

〔区a3〕研究卡X2第497行附近（S6年表：关税线若东移到奥得河—易北河，守线由约1万公里增至1.3万—1.5万公里，需增7,100—19,200名边境旅，年增工资360万—960万法郎），经研究卡A3复审转述。

〔区a4〕Grab, p.174（经研究卡D1`notes_grab.md`整理）；D1第130行附近的备选B1反证（皮埃蒙特官僚与军官层此后参与萨伏依国家建设）。

〔区a5〕研究卡SP1（`t_3282da/SP1_spain_state.md`第135行附近方案表第15项：巴约讷九点补偿包，第③条"接受则得埃特鲁里亚王冠"，据La Parra《Fernando VII》经Cevallos的系统化转述）。

〔区a6〕D2`notes_valais.md`"3年内抵抗"一节（推演，中高）。

〔区b1〕研究卡NL第40—41行（"双重问责"机制与"五到八年"的推演，中高）。

〔区b2〕研究卡NL第④节与B6b行（1809—1810年路易的对英贸易执照；1810年荷兰存货课税50%，Marion p.306经研究卡F4核读）。

〔区b3〕20艘荷兰战列舰见拿破仑通信（`downloads/pages/82a063e7e022.md`第1171—1173行，经NL`notes_primary_finance.md`第6条核读）；"金融合作版"见NL第60—63行。

〔区b4〕研究卡D2第4节反应函数表B6行（据上一轮研究卡t_f81a6f《大陆经济秩序》）。

〔区b5〕研究卡G2第239行（B6行，高置信）。

〔区b6〕1811年4月10日拿破仑在四个半小时的接见中向俄国特使切尔尼绍夫开出的条件，包括以等值封地补偿奥尔登堡，见Albert Vandal, *Napoléon et Alexandre Ier*, t. III（本地`downloads/c12_vandal3_full.txt`第4780—4790行），经研究卡A2复审（`A2_俄国波兰_卡书比对.md`第37、265行）核读；轨道设定见`P2_三轨道设定.md`第一节1810—1811行。

〔区b7〕伯尼奥与巴舍尔的关税同盟倡议见G2第248行（据Eli Heckscher, *The Continental System*, pp.295—296）；"按消费地征税、一次完税后自由流通"见研究卡X2第7条（据Heckscher, p.227）。

〔区b8〕Schmidt, p.383（埃尔伯费尔德厂主1810年11月14日陈情书，AF IV 1839）。

〔区b9〕G2"财政"节（引Berding）。

〔区b10〕G2年表第20—22条（S5，1825—1835年与1830年代）。

〔区b11〕1810年3月3日赠产法令，据森科夫斯卡—格卢克的研究，转引自旧版书稿快照`01_法国的能力与代价.md`第189行（注〔法16〕）；轨道设定见`P2_三轨道设定.md`第三节乙层1813—1820行（"赠产转国内资产"）。

〔区b12〕IT3第37行（1800年威尼斯选举会议与"会议地理"）、第207、215行（1823、1846年选举会议的半否决权）、第193行（拿破仑接受1808年式方案的先验约0.15）；"胜利后十八个月内约七成"见研究卡SP1第157行引F1先验，经A4复审整理。

〔区b13〕IT3第43、150、161、166行；旧版书稿快照`04_西班牙与意大利.md`第377—381行。

〔区b14〕Madelin第17547—17607行，经D2`notes_rome.md`整理。

〔区b15〕谈判班底见Consalvi回忆录第一卷（本地`downloads/IT3_Consalvi_memoires_v1_1866.txt`，贝尔尼耶一名出现于第11370—15821行共41处），经A4复审整理；务实派与强硬派见IT3第38行；和解后的步骤见IT3第200—201行（"1801年三个月补齐全国主教团的行政先例"）。

〔区b16〕旧版书稿快照`04_西班牙与意大利.md`第223—227行。

〔区b17〕1812年法奥同盟条文见旧版书稿快照`03_大陆诸国.md`第186行附近，研究卡A把它当作C层同盟的模板（经A1复审）；德累斯顿见注104。

〔区b18〕`D2_breakpoints.csv`第7行；P2阶段地图（`P2_provincialization_verdict.md`第91—106行，伊利里亚行）。

〔区b19〕托雷斯韦德拉斯与1813年亲征见`P2_三轨道设定.md`第二节；絮歇在阿拉贡的办法见D2第6.3节（据Grab, p.135，本地文本第3364—3367行）。

〔区b20〕研究卡SP2第199—206、224行（经A4复审整理）。

〔区c1〕IT1第68、90—92行（推演，中）。

〔区c2〕IT1第157—171行（反应函数表：B4与B7两行）。

〔区c3〕IT1第44行；旧版书稿快照`04_西班牙与意大利.md`第253行；原句"je l'ai appelé au trône en cas que je n'aie point d'enfant"及两种读法见研究卡A4复审F9条；米兰四派见IT1第109—110行（据《意大利传记辞典》）。

〔区c4〕IT1第279行（1813—1814年巴伐利亚国王劝降）。

〔区c5〕NL第425行（米兰觊觎提契诺与拿破仑的拒绝）；提契诺占领的执法理由见X2第24行。

〔区c6〕NL第197行（拉阿尔普1814年力保新州格局）；"感激库存换成恐惧库存"见NL反应函数B6a行。

〔区c7〕G1第126、207行及`notes_zollverein_wirtschaft.md`第32—34行（宪法与关税同盟的年份）。

〔区c8〕G1第109行（王朝止损）与年表第23—24条（继承时刻）。

〔区c9〕IT2第204、230行；罗德雷不留账目与欠饷九个月见Davis, p.144（本地`downloads/IT2_Davis_Naples_and_Napoleon__56c91cc713a7.txt`第6470—6528行），经A4复审F10条核读。

〔区c10〕IT2第192—194行（三定理：藩属立宪周期律约5—7年；"法国将不得不做1821年的奥地利"）。

〔区c11〕PL"专题C"C2（据恰尔托雷斯基回忆录第二卷所载亚历山大一世1810年12月25日与1812年4月1日的信，本地`downloads/R1_czartoryski_memoirs_v2_real.txt`），经研究卡A2复审整理。

〔区a7〕六类读数的出处分见各地区小节；替身价格见注25，双语干部带见研究卡D1第29—30行（"每并合500万人需约12—15名省长、40—60名副省长与成建制的双语中层"），海关人员的本地比例见注22。

〔区a8〕研究卡SP2第15.2节"反面清单"（B4b的残余风险，按概率排序）。

〔区a9〕脱离规则见注143；各年读数见`out_flash_yearly.csv`与`out_events.csv`；1818—1820年一次性收入的耗尽见研究卡D2第26条年表（"以一次性掠夺滚动维持的贡赋帝国"）与研究卡X2第500行附近（存量清算约在1817—1822年耗尽），经研究卡A3复审转述。

〔区a10〕研究卡D1第9行；Q2第12行与第8.2节"结论群"；模型读数见`out_events.csv`。

〔区c12〕G2第278—293行（邦联条约第6、11条；1806年10月16日筹备会议；达尔贝格两份草案被退回；贝克据埃伯施泰因遗档的判断；三因分解与"窄版Fundamentalstatut"的可能性：大陆整固情景0.2—0.35，互惠关税下0.35—0.5）。

〔区c13〕研究卡X2第7条（引Geoffrey Ellis 2015, p.35）；南德的次级关税区见G1"专题D"；"反法国关税同盟"见G2年表第22条。

〔区c14〕G1"专题D"关税线（中高）；伯尼奥、巴舍尔与"一次完税"的出处见注b7。

〔区c15〕研究卡Q1第205—228行表（加泰罗尼亚行；A档类比格0.90而裁量区间取0.25—0.45，理由见同卡第236行）。

〔区c16〕"法国高于一切"见Heckscher（旧版书稿快照`04_西班牙与意大利.md`第215行及其注[14]）；威尼斯船厂见IT1第100—102行（据研究卡F3逐舰表）。

〔区c17〕IT2第60行（阿加尔1812年2月5日清单，据Davis, pp.150、156）；那不勒斯城人口见IT2第108行。

〔区c18〕条件算例：并入变体由`P2_notes_07_v3补充实验.py`算出（v3.1参数，只把托斯卡纳改回1808年并入）：`trackA`1810年进入阶段2、1814年进入阶段3，1821—1823年抵抗指数0.12—0.14；`trackC`1810年、1812年。`regions.csv`托斯卡纳行：抵抗指数初值0.12、消极抵抗权重0.10，备注"v3校准据第十章起草人交稿说明§七"。D1的7—12年见注7。

〔区c19〕轨道设定：`p2d_model.py`第171行`trackB`的注释（"缪拉留在贝格（约瑟夫不去西班牙），贝格以关税同盟的市场准入代替并合"）与`models/p2d/README.md`"当前结果"表乙层一行；请愿的三档要求见注75；缪拉在不废西班牙波旁的世界里留在贝格，见注80所引研究卡IT2。

〔区c20〕轨道设定：第七章（`v5/drafts/07_伊比利亚与意大利档案.md`）决定表D伊3（"撤回并合马尔凯的决定，不并罗马"，适用于最可能与强行成功两条轨道）；`models/p2d/README.md`v3.1说明；模型的意大利王国仍按1810年极盛口径670万计。马尔凯并合敕令的日期见注90所引Madelin。

〔区c21〕条件算例：全国合计见`out_flash_yearly.csv`1816年一行与`out_trackC_yearly.csv`1822、1830年两行（需求＝本土安全与野战预备33万＋新省与战区驻军＋藩属中的法军；供给＝陆军预算÷700法郎×0.85＋盟军在场）；逐地区的抵抗指数、阶段、驻军需求见`out_region_yearly.csv`，藩属中的法军、盟军在场、新兵存量、净税由`P2_notes_05_逐地区拆账.py`拆出。表中数字四舍五入。

〔区c22〕条件算例：`trackA`，1815—1848年；藩属中的法军＝条约派驻额×（0.5＋抵抗指数），到场本国兵＝条约兵额×（1－抵抗指数）×0.85（同盟为1－1.2×抵抗指数），见`p2d_model.py`第343—349行；逐地区数字由`P2_notes_05_逐地区拆账.py`拆出。荷兰、贝格、莱茵右岸诸邦分别为0.43万—0.48万、0.33万—0.40万、0.36万—0.41万。

〔区c23〕第七章（`v5/drafts/07_伊比利亚与意大利档案.md`）意大利王国三轨道表1815年一行（最可能轨道为"不含马尔凯与特伦蒂诺"的北意大利王国）与年表中1808—1809年"最可能"一行；1810年极盛疆域670万含1808年马尔凯四省与1810年特伦蒂诺，见同章王国概况表。
