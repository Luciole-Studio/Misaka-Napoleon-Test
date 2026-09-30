
### 本章注释

〔海1〕本章舰队模型：`final/r_5b1357a9c6-revised/models/navy/`（`navy_model.py`、`make_summary.py`、`README.md`、`out_annual.csv`、`out_snapshots.csv`、`out_sensitivity.csv`、`out_summary.md`、`out_params.json`、`out_validation.txt`）。模型以研究卡F3（t_b1a536）的舰体—人员存量流量与"一年内可动员整舰"公式为核心，加入第一章海军预算约束、英国反应规则、三条轨道的初值与事件；研究卡目录未改动，所用原件的未改动副本在`source_copies/`。关闭预算与英国模块、换回F3外生下水表时，模型逐年重现F3卡`F3_capacity.csv`的156行（舰体误差≤5×10⁻⁴，为四舍五入；可动员数逐项相同）。一切输出都是条件算例。表中"单因素区间"是只改变英国反应（r、g、a、c、议会上限）或只改变法国参数（成本、人员流量、产能）时的最小—最大；"外包络"把法国不利参数与英国强反应、法国有利参数与英国弱反应配成两端，见`out_summary.md`。吨位比沿用研究卡P4的约定：法国战列舰平均排水量3,500吨（3,200—3,800），英国3,600吨（3,400—3,900），均为混合舰型的假设尺度；詹姆斯表中的载重吨（tons burthen）是容量计量，不与排水量相除。训练系数不再相乘，因为"可动员"已受合格海员约束；若按P4的训练诊断（1830年法国和平分支0.925、英国0.95）折算，最可能轨道1830年的比值约由0.69降到0.67。

〔海2〕五个量的定义沿用研究卡B3（t_998052，`B3_royal_navy.md`"口径先行"）、F3（"三档舰数及边界"）与P4（t_24b942，`P4_naval_gap_projection.md`第1节）。"一年内可动员"是本项目的模型口径，要求修复、武装、配员三者同时满足；詹姆斯原表没有这一栏。

〔海3〕William James, *The Naval History of Great Britain*，1837年版；年度表据Paul Benyon网页转录（1803年表：https://sites.rootsweb.com/~pbtyc/Naval_History/Vol_III/Abstract_No_11.html ；1808年表：…/Vol_V/Abstract_16.html），并经研究卡B3整理（`table_historical.md`）；1803—1805年经影像核对，其余为转录。在役与储备是原表分类；"在役"指编成配员，其中同一天在海上的只是一部分，"储备"（ordinary）也包括等待修理的船。1808年若把海勤、港勤、在建与订购全部相加约237艘，海勤战列舰只有126艘。1803—1814年新建数据自原表"上年建成"栏（Built）加总，是毛流入。詹姆斯在年表注释里说明了三处口径变化（本地影像版第三卷"Notes to Annual Abstracts"，印页507—508）：自No.11表起，首栏扩大到一切已经或即将为海勤装备的舰船；"&c."指未派港勤、在储备中等待出售或拆解的舰，有时一等数年；以"Built"取代"Launched"，因为此前各表把新建舰既算进上年的"订造"、又算进当年的"增加"，"became reckoned twice over"。例如"希伯尼亚"号1790年订造、1792年开工、1804年才下水（同处No.13表注a）。1803年动员与员额表决：James第三卷（本地`downloads/James_Naval_History_v3.pdf`）印页167（PDF第183页），原句"To the 32 line-of-battle cruisers, then in commission, were added, before the 1st of May, 20 additional ones and, by the 1st of the following month, the number of ships of the line in commission was augmented to 60"。塞平斯的斜撑试验见同书相关年份。

〔海4〕英国下院海军预算辩论（api.parliament.uk historic-hansard）：1812年2月22日，cc.885—893（145,000人，含31,400陆战队）；1817年2月17日，vol.35 cc.408—409（19,000人，其中陆战队6,000人，表决六个阴历月）；1820年5月17日，vol.1 cc.459—460（23,000人，含8,000陆战队，十三个阴历月）；1826年2月21日（1817—1825年员额序列：1818、1819年各20,000人，1823年25,000人，1824年29,000人）；1830年3月1日，vol.22 cc.1121—1143（计划29,000人，含9,000陆战队，实际一度超过32,000人）。本地缓存`downloads/pages/f42cec953d4b.md`、`245fa51bae26.md`、`7aa4f576eb19.md`、`990e6312e3fa.md`、`597653e3e3aa.md`。阴历月表决的年度长度不同，不按全年平均折算。

〔海5〕Martin Wilcox, "'These peaceable times are the devil': Royal Navy officers in the post-war slump, 1815–1825," *International Journal of Maritime History* 26.3 (2014), pp.471—488，DOI 10.1177/0843871414543445。只读到开放摘要（`downloads/pages/1131eb224b3d.md`）；124,000人与约九成委任军官领半薪两数出自摘要。

〔海6〕研究卡B3（t_998052），`model_assumptions.md`与`B3_response.csv`：人员包M＝650×在役战列舰＋280×现役巡防舰＋110×现役小巡航舰＋岸上等人员；年度规划费用C＝K＋vM，K为400万—600万镑、v为每人年85—105镑（1812年费用水平）；武装和平包约6万—9万人、900万—1,530万镑，持续战争包约13万—14.7万人。本章模型把K拆成固定项与按舰体计的保养项，并按和平时期价格取每人年80镑，1820年验算约600万镑（实支634万镑）。同卡`B3_royal_navy.md`第1节（"若有可信的海上和解，则转为约6–9万人的武装和平"）、第34行（武装和平须扩大志愿招募、保留核心人员及改善待遇）、第48行（休姆报告1821年初债息含管理费、不含偿债基金为£31.253m；议会坚持减税而法国扩舰时，冲突"先表现为远征退出、舰修延误或外交妥协，不一定直接违约"）、第93行（稳定工资、晋升、轮换）、第117行（1820年代蒸汽拖曳、测量、通信，1830年代辅助舰，1840年代螺旋推进与重炮）。

〔海7〕Nicola Peter Todorov, "Le redressement naval de 1810–1813 napoléonien et la géographie maritime de l'Europe," *Cahiers du Centre d'études d'histoire de la défense* 36 (2008)，HAL作者稿（本地`downloads/F3_Todorov_redressement_1810_1813.pdf`），页码按作者稿：p.3（1810年方案：两三年内60艘新舰、总数约110艘；甘托姆备忘录与三百艘双桅船训练艇队建议，拿破仑改用炮艇）；p.4（43艘中37艘武装，英国125—130艘，英12万对法3万海员，一些海军会议成员估4万）；p.13（1810年10月13日报告：格斯特河—威悉河164根大桅、149根小桅、270块板，布雷默弗尔德282、510、213；里加滞留1,009根桅材）；p.14注64（1811年2月27日报告：«les produits de la France et de l'Italie suffisent aux besoins du service»，铁向由法国自产，铜有储备）；p.15（舰体表）；pp.16—18（甘托姆1810年估计；荷兰、丹麦、挪威人员；1812年普鲁士与丹麦的舰员义务；1811年两万沿海征募、七成来自今日法国以外；汉萨到员不足；伊利里亚逃亡与向英国通报）；pp.23—25（1812年2月4日德克雷备忘录，引句"Les équipages se formeraient dix fois plus dans ces mers difficiles que dans les mers de l'Inde"；1813年巡防舰巡航：21次出航损失10艘，约13个舰员组4,000人航海二十天至近五个月）；p.25注116（1810年8月23日海军会议记录：每年约2亿；AF/IV/1208：1812年223,404,900法郎、1813年255,746,100法郎、1814年维持145,919,400法郎；1812年预算削至1.9亿）。档案号均为作者所引，本书未亲阅原档。舰体表按所在港计存量，与建造地、在役数是不同口径。

〔海8〕J. Muracciole, "Napoléon et les arsenaux de la Marine," *Revue historique des armées* 1974/1, pp.83—98，DOI 10.3406/rharm.1974.7813（`downloads/pages/21ae17eda88c.md`）：104艘"à flot ou en chantier"；安特卫普工人1804年500人、1807年2,850人，船台1809年由9座增至12座，每年领得六百万以上；斯海尔德距海约五十海里，外水道约二十海里，下河五至十五天，凯尔桑组建引航连；1812年米西西在霍格普拉特集结21艘战列舰并驶达外海；布雷斯特1807年逾5,200名工人，土伦约3,500人，1814年土伦17艘在役、3艘在建；热那亚造舰送土伦；斯佩齐亚1810年尚在形成；罗什福尔与鲁埃勒；北方港口工程作为"笼络政策"的一部分；瑟堡的大防波堤"devaient exiger près d'un siècle"，其掩护下开挖拿破仑港池，港口1813年由玛丽—路易丝启用，时有四艘舰完工、四艘在台，拿破仑预计可容十五至二十艘，英国在瑟堡外常驻小分舰队；"Dans les bonnes années les ports recevaient à peu près la moitié du budget total de la Marine"。1814年2月报刊所称土伦"23艘浮存"是另一种口径。

〔海9〕Nicolas Mioque, 2014年3月26日转录1820年《Annales maritimes》所载《Réduction progressive du nombre de nos vaisseaux (1814–1819)》，https://troisponts.net/2014/03/26/reduction-du-nombre-de-nos-vaisseaux-1814-1819/ （`downloads/pages/b63d35ce3cb6.md`），经研究卡F3（S08）核读：1814年4月23日战后口径52艘浮存、19艘在建；1819年底48艘浮存、10艘在建；旧舰平均约十四年后须考虑重建。

〔海10〕英国下院1839年3月4日海军预算辩论（https://api.parliament.uk/historic-hansard/commons/1839/mar/04/navy-estimates ，`downloads/pages/ab124a162bee.md`），海军部秘书发言：法国22艘战列舰浮存、27艘在建，1838年现役8艘、连换防10艘在海（据图皮尼耶男爵的报告）；1835年检阅法国登记海员9万人，其中3.7万为船长、陆地人员或学徒，1.8万超龄或未龄，可用3.5万，其中1.8万已在王家海军，可扩充1.7万；英国1835年1月1日在役战列舰11艘，1837年1月1日20艘；员额1835年17,500人，1836年22,500人；船坞工资票1835年30万镑、1838年38.4万镑；物料38.3万镑增至59.3万镑；物料足供"between fifty and sixty sail of the line"；俄国1787年45艘、1801年61艘、1807年与1839年各43艘（浮存）；英国在役战列舰与俄国之比1817年15对30、1823年12对37、1832年11对36；英国战争汽船1835年各阶段24艘、1839年36艘，1835—1839年完工1、1、4、6、9艘；商用汽船679艘（200马力以上65艘、100—200马力136艘）；登记海员20万；帆船1833年24,385艘、1837年26,037艘；"The French carry publicity to a fault"。同一发言另述：1835年11月清点下桅，"no less than 161 lower masts were found defective"，战列舰下桅将近一半被判报废；1836年储备舰检查后改为库存保管桅杆与物料；储备舰看管人员1839年1月1,449人、补满后约2,200人；造船木材年消耗1830年前七年平均21,600 loads、1836年前四年9,600 loads；工资票1829年£480,000、1833年£390,000、1834年£300,000；木材储备由1826年规定的两年用量增到五年；麻价由每吨£30涨到£45；意大利橡木与落叶松合同；商船水手年薪£25 4s或£30，王家海军£22 2s；美国战列舰2艘在役、3艘可出海、2艘待修、4艘在台。转录中无发言者姓名，发言人自称海军部秘书。英国可动员数"五六十艘"是物料口径。

〔海11〕研究卡F3（t_b1a536），`yards_launches_1807_1813.csv`与`notes_yards.md`：逐舰下水最小清单，据法国战列舰总表、各舰级表与Three Decks威尼斯船厂记录，上游多引Winfield & Roberts、Roche、Demerliac，原专著未逐页复核；Gallica"查理大帝"号1807年4月8日下水版画目录为一舰的独立佐证。各厂持续扩军时的年均新下水区间、全国有效新下水（前期每年8—12艘、后期6—10艘）、原料需求（前期约6.1万、3.8万—9.5万源单位等效材/年，1830年约5.4万—5.7万）与放弃安特卫普的极端检验（1830年和平分支可动员71艘），见`F3_french_navy_capacity.md`专题A与`F3_material_requirements.csv`；这些区间是该卡依厂史、计划与已见舰例作的推演，属生产安排区间，厂级技术极限另待核实。

〔海12〕Gregory Fremont-Barnes, *The Royal Navy 1793–1815* (Oxford: Osprey, 2007)，pp.41—50（王家与私人船厂、建造周期），p.44（1803—1815年"Extra"与"Ordinary"两项、员额与海军总拨款表：1805年£1,553,690／£1,394,940，1808年£2,351,188／£1,142,959，1813年£2,822,031／£1,700,135，总拨款£20,096,709）。本地缓存`downloads/pages/7f93512d05f7.md`。两组船厂数字与詹姆斯年表的时期、分类不同，不互相核销。

〔海13〕A. N. Ryan, "The Defence of British Trade with the Baltic, 1808–1813," *English Historical Review* 74, no.292 (1959), pp.443—466（直接读到pp.443—454）；James Davey, *War, Naval Logistics and the British State: Supplying the Baltic Fleet 1808–1812*，博士论文，University of Greenwich，2009（本地`downloads/R2_Davey2009.pdf`）。俄麻"逾九成"是贸易消费口径；戴维在注50提醒阿尔比恩对短缺的描述有夸大倾向。

〔海14〕Robert G. Albion, *Forests and Sea Power: The Timber Problem of the Royal Navy, 1652–1862* (1926)，pp.356、368（北美大桅材1807年4,442根、1808年16,729根，原句"the exports from British North America jumped from 4,442 to 16,729 in a single year"；北美橡木1810年逾17,000 loads、1811年逾24,000 loads；柚木与孟买造舰）。加拿大木材出口与新南威尔士羊毛据研究卡B6（t_0fed70）所引议会与殖民地贸易统计；loads是木材贸易单位，不折成吨。铜材回收据B3卡所引古德里奇整理的船厂档案目录。

〔海15〕Royal Museums Greenwich研究指南："The Spithead and Nore Mutinies of 1797"（B8）与"Press Gangs and Impressment"（M2）。本地缓存`downloads/pages/2d8d72a79507.md`（B8："In April 1797, 16 ships-of-the-line of the Channel fleet refused to sail"）与`1b22dbe49e2a.md`（M2："After 1815, though not abolished, it was not used"）。

〔海16〕Hans Christian Bjerg, "To Copenhagen a Fleet: The British Pre-emptive Seizure of the Danish-Norwegian Navy, 1807," *International Journal of Naval History* 7.2 (2008)，https://www.ijnhonline.org/wp-content/uploads/2012/01/Bjerg.pdf （`downloads/pages/71106f9334bc.md`）。作者指出英国因缺员从未把俘获舰全部投入使用。返航队列约一百五十艘船包括英国船与运输商船。

〔海17〕Davey 2009（同〔海13〕），pp.235—240，附录4（pp.279—280），p.239表26（原档TNA ADM 102/241）。三组平均日数可由表内四、五、四个日数复算；它们是不同到达记录的局部样本，彼此独立。病员数是各统计时点的现患人数。

〔海18〕Éric Schérer, "La Marine sous l'Empire"，marins-traditions.fr刊布的PDF，2025（`downloads/pages/bcf22d70f791.md`），转引Pierre Lévêque, «Les préfets maritimes», *Revue du Souvenir napoléonien* 541 (2024), p.256：1810年拿破仑预计1812年底连同荷兰、意大利与那不勒斯的舰只可有110—115艘战列舰；1811年修正为1813年103艘战列舰与76艘巡防舰，年造舰由6艘提到8艘。同文据Tramond《Manuel d'histoire maritime de la France》（1949），pp.825—826，记1805—1815年法国海军损失26艘战列舰、46艘巡防舰与66艘其他舰船。转引，原书未读。同文注8转引Las Cases, *Le mémorial de Sainte-Hélène*（Lequien fils, 1835），p.25，拿破仑的抱怨：«Sire, cela ne se peut pas. – Et pourquoi ? – Sire, les vents ne le permettent pas, et puis les calmes, les courants»（回溯性材料，转引）。

〔海19〕*Correspondance de Napoléon Ier*，napoleon-histoire.com月度转录：1811年3月5日致德克雷（安特卫普十八船台、每舰占台三年、年造六艘）；1811年10月2日自安特卫普致德克雷，原句"mon intention serait de construire chaque année huit vaisseaux au lieu de six. En effet, je m'étais contenté de six parce que je craignais la difficulté des équipages; mais huit équipages hollandais sont tout prêts"（`downloads/pages/550652301685.md`）；1810年11月6日（北方桅材采购：至多五分之一有担保预付，余款在但泽、吕贝克交货后付，列三百万法郎，`775f980f1a64.md`）。现代转录，未校手稿与纸本。

〔海20〕Treaty of Paris, 30 May 1814, Wikisource英文本（https://en.wikisource.org/wiki/Treaty_of_Paris_(1814)，`downloads/pages/23a7a98922ae.md`）：第八、九条（殖民地归还），第七条（马耳他归英国），第十二条（归还的印度商站不设防、只驻警察），第十三条（纽芬兰大浅滩、纽芬兰沿岸与圣劳伦斯湾邻近岛屿的捕鱼权"shall be replaced upon the footing in which it stood in 1792"），第十五条（被归还海港中的舰船、火炮、物资与造舰材料按三分之二归法国、三分之一归该港所属国分配；和约签字后六周内未下水的在台舰拆作材料；荷兰所有的舰船，特别是特塞尔舰队，不在此列；"Antwerp shall for the future be solely a commercial port"）。本书读到的是英文本。

〔海21〕研究卡D1（t_40198e），`D1_annexed_inner.md`第68行：安特卫普1800—1805年商业复兴，1808—1813年封锁期海运枯竭、转为军港。

〔海22〕Nicola Todorov, "La géographie des ressources forestières et les ambitions navales de Napoléon après Trafalgar : l'exemple du bois de chêne," *Revue de géographie historique* 5 (2014)，DOI 10.4000/geohist.4373（`downloads/pages/171e7ef70128.md`）：§3，一艘80炮舰需3,737 stères（108,982立方法尺）；§10，1805年清查的地图显示"Le seul bassin d'Anvers concentre presque 62 % de l'ensemble des arbres de chêne d'au moins 5 pieds de tour"，同段转述拿破仑在圣赫勒拿说安特卫普是他1814年没有在沙蒂永签约的原因（回溯性）；733.8万棵、543,937棵与7.4%据研究卡E1（t_02f417）转引同一作者。旧版第三章把62%写成"安特卫普相关供材区在计划中承担的比例"，与原文不符，本章据原文改正。stère是堆积体积单位，一stère所含实木不足一立方米；同作者2008与2014年两文依据同一清查，不算两份独立证据。

〔海23〕Hamish Graham, "A Matter of the King's Service: Supplying Ship Timbers for the French Navy in the Eighteenth Century," *Drassana* 30（刊期2022，2023年接受），pp.80—100，DOI 10.51829/Drassana.30.691（本地`downloads/E1_Graham2023_FrenchNavalTimber.pdf`）：p.87（1775年2月塞贡达在克莱朗林估一万五千至两万棵，海军只选中228棵，约4,000立方法尺）；pp.90—91（巴拉德森林：1715年由八千余棵减到三千棵，1728年只剩724棵；林主抱怨树被标记后无人采运、无人付款，"capital tied up and often lost entirely"）。这些是十八世纪的个案，本章只用它们说明采购制度的机制；1810年以后帝国的原料需求见研究卡F3的原料账（〔海11〕）。

〔海24〕*Correspondance de Napoléon Ier*，napoleon-histoire.com月度转录：1810年7月致德克雷（"un corps de 66,000 matelots, qui monteraient 400 bâtiments de flottille destinés à garder les côtes et 50 vaisseaux de ligne et 30 frégates"；艇队在须德海、马斯河与斯海尔德航行，"les équipages pourraient s'amariner en peu de temps"，`downloads/pages/82a063e7e022.md`）；1811年3月8日致德克雷（"Je ne veux pas que mes escadres sortent, mais qu'elles soient approvisionnées comme si elles devaient sortir"，`f042c1f13d31.md`）；1811年7月31日致欧仁（`6864746209f3.md`）；1811年10月3日致米西西（`550652301685.md`）。

〔海25〕Patrick Villiers、Pascal Culerrier, "Du système des classes à l'inscription maritime," *Revue historique des armées* no.147 (1982), pp.44—53（`downloads/pages/f9f391a5effc.md`）：pp.49—50（1795年登记制，十八至五十岁，按家庭类别，真正职业海员约六万人）；p.51（1822年恢复八年长役志愿制）；p.52（1825年登记94,611人，其中军士、海员、见习与少年73,053人；1845年125,272人与101,306人）。登记数与在役数是两个口径。

〔海26〕Julian S. Corbett, *The Campaign of Trafalgar* (1910)，pp.323—324（1805年10月7—8日加的斯军事会议，普里尼之语），据证据包E项1核读（`audit/20260925_复审与修缮/E_上帝视角可行性锚点.md`，本地`downloads/c11_corbett.txt`）。同书pp.33—34（1805年1月维尔纳夫出土伦遇大风，"he found it beyond the power of his raw crews and officers to face the gale"，19日决定返航，21日回到土伦），本地文本直接核读。

〔海27〕威洛梅兹1806年巡航与1809年巴斯克锚地火船夜袭的细节，据上一轮报告草稿（`final/r_5b1357a9c6-report/20_第六部_上一轮成果与改判.md`第51行）所引William James, *The Naval History of Great Britain*（1886年版）第四卷pp.108—117、390—393、400—408，经草稿补回台账S10核对为书稿缺失项；第四卷原书本章未读，属转引。

〔海28〕"The French Navy After 1815 Part I"，WarHistory.org，2019年11月30日（2024年12月更新），未署作者（`downloads/pages/a8db4b456088.md`）：1814年4月中104艘战列舰、54艘巡防舰（浮存或在建），8月73与42，1819年底58与34；波塔尔1820年方案（1824年定稿：40艘战列舰、50艘巡防舰，十年，年6,500万含殖民地600万；1820年只拨5,000万；1830年普通预算达6,500万）；1831年削至6,050万，1838年回到6,500万；1837年方案；1840年近东危机法国9艘对英国约14艘，12艘巡防舰因纽芬兰渔船队未归而配不齐人员；1842年40艘战斗汽船计划，1845年100艘，1846年马考方案七年另拨9,300万、1847与1848年各拨1,330万；1844年儒安维尔小册子。研究卡F3把此文降为线索级；本章只用其量级与年份，未核其上游出处。

〔海29〕John R. Elting, *Swords Around a Throne*（Da Capo Press, 1997年版；本地`downloads/pages/3762a4f8f4e3.md`为Scribd网页文本，无印刷页码），第十五章"Matters Nautical: La Marine"："In 1813 a report on navy personnel at Antwerp showed 3,413 'old' French and 4,771 from the recently annexed departements reunis"；拿破仑令德意志人与新兵调往土伦，"where they would be out of temptation's way"。同章另述：大革命关闭海军学校，候补生"spent three years aboard ship earning an ensign's commission"；布雷斯特与土伦两所浮动海军学校，"stiff three-year courses"；1808年3月设五十个海军营作战列舰的固定舰员，后改称équipages de haut bord，两年后增设二十四个艇队舰员营；1813年海军炮兵约八千人、平均二十三岁，改编为四个步兵团；复辟后"Napoleon's school ships were abolished, to be replaced by an inland academy"，只收极端保王派子弟，固定舰员营与海事长官制被废，复职军官肖马雷使"美杜莎"号触礁。作者未注该报告的档案出处；研究卡F3（t_b1a536）来源笔记S16据同一缓存作过摘录。

〔海30〕研究卡F3（t_b1a536），`F3_french_navy_capacity.md`专题A"军官、水手与训练时间"：1810年征外籍水手须有三年、150吨以上帆船经验；浮动军校三年课程（据Elting电子章节转述）；穆拉乔勒以"船长需二十年"概括领导骨干的长周期；1811年给威尼斯新舰配员，先调一二等水手200人、服役超过六个月的新兵200人、再调新征200人（据拿破仑通信S05）；较可靠水手2—4年、初级军官3—5年、舰长梯队8—15年以上、分舰队指挥文化10—20年，是该卡的规划推演，没有统一的航海日志统计校准。

〔海31〕Patrick Villiers, "Piraterie, flibuste et autres guerres de course dans les conflits européens de l'époque moderne," 收于B. Deruelle等编，*La construction du militaire*, vol.3 (Paris: Éditions de la Sorbonne, 2020), pp.159—178，§§39—40，DOI 10.4000/books.psorbonne.91295。英国下院1811年6月14日"French Prisoners of War"，vol.20 cc.634—639（`downloads/pages/581d84a8bc6e.md`）：在英法国战俘45,933人（病321人），假释2,710人（病165人）。累计俘获是流量，英国商船存量要扣除补充才看得出净变化；战俘数是一时断面。

〔海32〕第十二章（`v5/drafts/12_行省化三轨道与总判.md`）昙花一现一节与总表"最先断的环节"：1812—1815年荷兰与汉萨的怨气主要表现为逃役和少交税，外圈从1817年起逐块失控（荷兰、罗马、伊利里亚、埃布罗以北），1821年藩属与同盟转向，1822年放弃西班牙，1822—1825年缩回自然疆界、交出荷兰与汉萨；动态行省化模型`models/p2d/out_events.csv`。本章模型让荷兰分舰队在1816年离开，比该章早一年。

〔海33〕第一章（第五版）的收入门槛与海军预算：750档（1815—1830年）海军全部经费1.45亿法郎，850档（1830—1848年）1.65亿，650档（1808—1812年收缩方案）0.90亿，均按约1810年的成本尺度；据快照`01_法国的能力与代价.md`第199—203行与资料附编〔统2〕。第一章是否调整这些数，以第一章定稿为准。

〔海34〕Marcel Marion, *Histoire financière de la France depuis 1715*, t.IV (Paris: Arthur Rousseau, 1925)（本地`downloads/F4_Marion_IV_1925.txt`）：页325（"La marine varia davantage : 180 millions en l'an XII, 140 en l'an XIII, avec les préparatifs de la descente en Angleterre : 105 à 110 dans les années suivantes, puis relèvement à 155 en 1811, à 159 et 167 en 1812 et 1813"）；1813年高丹预算中海军1.72亿（1812年11月）；页377（1814年4月1日以前的积欠中海军1.42亿）；页399—400（1816年预算海军4,800万，原列5,100万）。OCR本，页码据版面页眉。

〔海35〕Henri-Joseph Paixhans, *Nouvelle force maritime et artillerie* (Paris, 1822)，第八卷，ETH e-rara影本（本地`downloads/P4_Paixhans_1822_Nouvelle_force_maritime.pdf`，PDF第59页），印页342"Matériel et dépenses de la marine militaire"：1819年海军部声明（此后重申）若年支出限于4,500万，"la marine française aura totalement cessé d'exister en 1830"，即使年支6,500万、到1830年共7.15亿，"elle sera réduite à cette époque à 38 vaisseaux et 50 frégates"。本书按页面影像核对为50艘巡防舰；研究卡P4笔记把此数记为30，属误读。这是帕克桑为推销新式舰船所引的官方声明，带有游说目的。

〔海36〕研究卡P4（t_24b942），`P4_naval_gap_projection.md`第3、7节与`P4_sensitivity.csv`：1830年持续海战分支舰体吨位比0.742、训练加权0.449；武装和平分支0.902与0.876；法国和平扩张而英国保持战时准备时0.731。P4的法国预算"165／195／245"是标签，不入算式；英国是B3的静态配对包络。

〔海37〕英国下院1813年11月10日Committee of Supply，vol.27 cc.69—75（https://api.parliament.uk/historic-hansard/commons/1813/nov/10/committee-of-supply ，`downloads/pages/3b214d7b54fb.md`）：动议1814年员额14万海员、3.1万陆战队；政府方面说敌人"had not relaxed his maritime efforts"、"had still fleets in most of his leading arsenals, ready for sea"、"had, in fact, been accumulating his marine forces by rapid strides"，并说"If we suddenly disbanded, it would not be so easy a task, on an emergency, to recal our seamen to the naval force of the country"；反对者称特拉法加时英国海员比现在少一万人。经研究卡B3（H13）定位。

〔海38〕英国下院1815年6月14日单列费用辩论，cc.806—813（`downloads/pages/156d03703582.md`），范西塔特："that expense now incurred for our armies would cease, and the supplies at present demanded for them could be applied to the service of our navy"；蒂尔尼的反驳见同栏。据研究卡B1（t_c69786）与B3转引定位。

〔海39〕休姆1821年6月27日的节约提案（vol.5 cc.1345—1442，转引年度估算与财政账）与"with the prospect of a long peace"一语，据研究卡B3`sources/postwar/read_evidence_and_notes.md`；英国下院1822年2月27日海军预算辩论（`downloads/pages/9198b046bbb7.md`），克罗克与休姆争论和平编制与造船账。

〔海40〕英国下院1830年3月1日海军预算辩论，vol.22 cc.1121—1143（`downloads/pages/597653e3e3aa.md`）：政府方面发言"If a country were called upon suddenly to build and man ships for war, it was admitted that two years must pass"；"our naval force must partly depend upon that of other powers"，去年夏天地中海俄国6艘、法国6或7艘、英国8艘；估算总额£5,595,000。转录中无发言者姓名。休姆的发言在cc.1128—1132：和平部署清单合计20,750人（c.1131），原句"In 1792 the naval power of France, of Spain, of Holland, was much more formidable than at present"；"5,000 naval officers, and were not able to employ one third of them"。

〔海41〕G. R. Porter, *The Progress of the Nation*（本地`downloads/E1_Porter_ProgressOfNation_1847.txt`；所含数字至1849年，实为1851年增订版），第四编"War Expenditure"，页505—506，"Amount Expended from 1801 to 1849"：海军实支1810年£20,021,512，1814年£22,124,437，1817年£6,473,063，1820年£6,337,799，1830年£5,309,606，1835年£4,090,430，1838年£4,520,428，1846年£7,803,464，1847年£8,013,873，1848年£7,922,287。1835—1849年一页的OCR把列名错置，本书以1834年三列相加等于合计核定列序。同书第四编第二章"Public Income and Expenditure"：页472—473（1814年当年支出£76,780,895、债息£30,051,365，合计£106,832,260）；页474（1816年1月5日国债本金£885,186,323、年负担£32,457,141）；页476"Abstract of Public Income and Expenditure"表，税收进入国库：1830年£50,056,616，1835年约£45.8百万（OCR残缺），1842年£46,965,631，1843年£52,582,817，1848年£53,388,717；索引页607：1842年皮尔提出所得税。表中是名义值，与本章模型的1812年价格尺度不同。研究卡与旧稿此前都没有用过这份材料。

〔海42〕Paul E. Fontenoy评Jan Glete, *Navies and Nations: Warships, Navies and State Building in Europe and America, 1500–1860*，*Naval War College Review* 49.4 (1996), p.160（本地`downloads/P4_Glete_review_Fontenoy_1996.pdf`，PDF第3页影像）：书评转述格莱特之论"the aggregation of domestic interests behind policy ... generally outweighs that of external threats"。转引，格莱特原书未读。

〔海43〕旧版第三章（快照`02b_英国海权与和平_舰队海峡与帝国.md`第241—248行）与研究卡B3`model_assumptions.md`"封锁／全球任务的必要舰体"、P4第5节：H＝ceil((rF＋g)／a)，在役≥rF＋g，r＝1.05—1.20，g＝15—25，a＝0.75—0.85。本章把F推广为和平时期的"一年内可动员"口径，加入盟国与俄国权重、三年在建舰预估与议会费用上限；推广是本章的模型选择。

〔海44〕研究卡B1（t_c69786）：`B1a_landing_decision.md`第三节"登陆后决策树"与"两条并列主分支及压力备选"表（A：伍斯特境内政府续战；B：军事压力下的有限和平，占城后二至六周正式探询、一至三个月争取停战缔约；F：法国要求交舰、长期驻军时抵抗联盟变宽，"阻力方向高；终局低"）；`B1b_acceptance_equilibrium.md`第十二节"对法国B1–B8菜单的反应函数"（"真实可收款开放最有利于和平多数"）；`B1c_1815_1848.md`第十五节"触发与响应阶梯"（法国重新威胁本土、低地沿海或约定航路时，第一反应是"造舰/保在役兵力、海军部署、外交最后通牒"，升级为大陆联盟须有愿意作战的大陆伙伴与议会供款；拿破仑去世或继承冲突时先"请求确认条约，观察谁控制军队与财政"）。第六节第4小节的反应表与第八节第5小节的五个分支，是本章把这些推演与本章史实锚点合并的结果，置信由本章评定；登陆规模与预警的对应见〔海62〕。

〔海45〕特拉法加与罗西利分舰队的数字据证据包E项1（`audit/20260925_复审与修缮/E_上帝视角可行性锚点.md`），该项核读了Corbett, *The Campaign of Trafalgar* (1910)，pp.295—296、323—324、331—332；A. T. Mahan, *The Influence of Sea Power upon the French Revolution and Empire*（Gutenberg本，`downloads/pages/4c05b3e278f4.md`），pp.186—195；James第三、四卷相关页：出港33艘（法18、西15）、5艘巡防舰、2艘双桅船；战后11艘（法5、西6）回加的斯；迪马努瓦尔4艘11月4日在奥特格尔角被俘；1808年6月14日罗西利率5艘法舰与约4,000名水兵投降。维尔纳夫获悉罗西利行程的日期有10月11日（马汉）与约10月17日（科贝特）两说。第十三章第七节第7小节采用同一组数字。

〔海46〕1812年4月17日巴萨诺致卡斯尔雷与4月23日复信，据第二章所引同期刊本（1813年3月13日《爪哇政府公报》第8页转载）及研究卡B1（t_c69786）第七节转述；本章未另读原信。

〔海47〕昙花一现轨道的设定据《三条轨道设定》（`audit/20260925_复审与修缮/P2_三轨道设定.md`）第二节；1812年法俄妥协登记为决定D-F1。

〔海48〕运气L1、L2、L3与奇迹M2的登记与可能性据《三条轨道设定》第三、五节；L1的偶然变量据证据包E项1；乙层法西同盟不破、罗西利5艘舰不失，与第十三章第七节第7小节一致；丙层荷兰条款（保全公债利息、约7,800万法郎年息、五年免征兵、保留荷兰语法院与市政）据同一设定。B′₁（1803年4—5月接受俄国调停马耳他）、B′₂（1805年6月暂缓并合热那亚）两个决定型入口及"三处共享同一个价格：英国保有马耳他"，据同一设定第三节1806年行；乙层1803年对圣多明各的安排（停止追加远征、事实停火通商、1814年和约后承认海地）据同节1803年行。

〔海49〕Emilio La Parra López, *Fernando VII. Un rey deseado y detestado*（Barcelona: Tusquets Editores, 2018；电子版ISBN 978-84-9066-515-2；本地`downloads/SP1_LaParra_FernandoVII.txt`，无印刷页码），论1817—1818年购买俄国舰船一节："Rusia vendía a España cinco navíos de línea de 74 cañones y tres fragatas de 44 por un total de 68 millones de reales"；舰队1818年2月到加的斯后"quedaron abandonados durante varios meses en el puerto de Cádiz, sin carenarlos ni reparar los desperfectos"。关于这些船船龄不长、及时修理本可使用，作者引用近期研究（其注92），本章未另读；其参考书目列有Mitiuckov与Anca Alamillo, *La escuadra rusa adquirida por Fernando VII en 1817*（2009）。

〔海50〕研究卡B6（t_0fed70），`B6_british_overseas_empire.md`第⑧节推演（"主线中英国更努力避免再与美国长期海上冲突"）与第⑭节五情景年表"1812"行（S1"中立化"情景一栏："优先美英海事和解，减加拿大战险"；该卡的S1大致对应本书较早议和的轨道）。英美战争的两项诱因（搜查中立船只、强征海员）是通行的史实概括；它们在较早议和的轨道上减弱，是本章的推演。

〔海51〕Paixhans 1822（同〔海35〕），印页287（"on peut lancer de grosses bombes horizontalement comme des boulets ordinaires"）、288（蒸汽机"pourquoi ne donneraient-elles pas la force de quarante mille marins à la France ?"——倡议者的设问，属于愿景）、346—347（其他国家采纳后英国仍可重得优势，法国新海军的得益"seulement transitoires"），经研究卡P4核读。

〔海52〕1824年布雷斯特试射："From Shot to Shell: General Paixhans' Revolutionary Artillery," *Naval History* 38.6 (December 2024)（`downloads/pages/50491bf9c17b.md`，二手）；1827年订购50门、1830年代每舰二至四门、1837与1841两种采用年份：法国炮兵协会"Nouveautés dans l'artillerie de la Marine"（`downloads/pages/a29ef989aeb1.md`）与证据包E项3；"斯芬克斯"号：法国国家海军博物馆"Machine à vapeur de la corvette à roues le Sphinx"（`downloads/pages/04c2ed9cef98.md`），原句"sa machine à vapeur fut construite par une entreprise de Liverpool, W. Fawcett"；1845年螺旋桨试验：Royal Museums Greenwich, "H.M. Steamship Rattler and Alecto"（藏品说明）。原试验报告均未读。

〔海53〕证据包E项17（Cockerill父子1799—1817年在韦尔维耶、列日与瑟兰；1826年焦炭高炉，1835年欧陆第一台机车；英国1825年起机器出口改许可制、1843年全面放开）。

〔海54〕Édouard Desbrière, *Projets et tentatives de débarquement aux îles Britanniques*, t.IV (Paris, 1902)（本地`downloads/c11_desbriere_01.txt`，页11）转录拿破仑1804年7月2日致拉图什—特雷维尔信（出自《通信集》）：«Que nous soyons maîtres du détroit six heures, et nous serons maîtres du monde !»；同信所称1,800艘船、12万人、1万匹马与英国各处舰数。甘托姆1803年的警告与职务（土伦海事长官）据旧版〔陆海1〕所引Desbrière文书汇编；1804年9月爱尔兰北部方案（奥热罗率布雷斯特约1.8万人、特塞尔2.5万人第二波）据研究卡IE所引Wheeler & Broadley (1908)转录的《通信集》第8063号；1805年3月集中令据旧版所引Desbrière。这些后出叙述部分同源于Desbrière，不算独立证据。

〔海55〕Desbrière，t.IV（`downloads/c11_desbriere_02.txt`与相关页图）：pp.398—400，圣奥昂1805年8月3日（共和十三年热月15日）报告"Appareillage général de la flottille impériale"，原句"La nature du port de Boulogne, défendant jusqu'à la pensée d'en sortir dans une marée, la totalité, la moitié même des bâtiments qui y sont réunis"、"Dans moins d'une heure toute la flottille est sous voiles, faisant route dans l'ordre prescrit, par escadrille, division et section"，编者在p.398前注明早先公认一潮可放出一百艘且此数不断下降；pp.442—445，蒙特勒伊军团1805年3月30日装载文件（兵位、马位与待配车马份额）；1804年7月20—21日（热月1日）风灾，拉丰报告损失12艘（第一种炮船3艘、第二种1艘、小艇4艘、卡伊克4艘）、29人（`downloads/c11_desbriere_01.txt`）。六潮方案出自Richard Glover关于布洛涅运输的研究，据旧版〔陆海2〕转引。时间预算与每小时卸载人数是明示条件下的推算。

〔海56〕J. W. Fortescue, *A History of the British Army*, vol.V (1910)（本地`downloads/c11_fortescueV.txt`），及*The County Lieutenancies and the Army, 1803–1814* (1909)（`downloads/B4_Fortescue_CountyLieutenancies1909.txt`），入侵准备与年度兵力附表。各表的时期、地域与军种不同，不以大数代替小数；三十八万志愿兵含骑兵与步兵全军衔。

〔海57〕Kevin Barry Linch, *The Recruitment of the British Army 1807–1815*，博士论文，University of Leeds，2001，pp.22—29、121—122（本地`downloads/B4_Linch_recruitment_1807_1815.pdf`）：1810年驻英格兰39个营24,764人、病7,677人，"leaving only 17,087 men fit for duty"；1811年55,938名相关兵员仅五营可外派；1807—1813年年均减员约22,695人。

〔海58〕Fortescue, vol.V，pp.231—232（约克公爵的车辆建议，原句"waggons should likewise be marked, set apart, and provided with seats to convey the men from the remoter districts to any threatened point"）；Christopher Chilcott, *Maintaining the British Army, 1793 to 1820*，博士论文，Bath Spa University，2006，pp.242—244（本地`downloads/B4_Chilcott_Maintaining_British_Army_2006.pdf`；补给车辆二十四小时备齐、日行二十五至三十英里，作者认为偏乐观；马尔泰洛塔与皇家军用运河）；John Cary, *Cary's New Itinerary*, 6th ed. (London, 1815)，印页11—12、50、84、535—536、546（`downloads/B4_Cary_itinerary_scan.pdf`）。1815年的道路是1805年的地理代理；8弗隆＝1英里。

〔海59〕Fortescue, vol.V，pp.231—232："driving the country"方案1779年首次提出，1803年"was so strongly opposed by such capable authorities as Sir John Moore and the Duke of Richmond that it was abandoned"；Chilcott 2006引1803年11月19日索尔兹伯里郡会议命令。西德尼·史密斯1803年8月致基思的信据旧版第三章转述，基思文书原件未读。

〔海60〕乔治三世1803年11月30日致赫德主教，据研究卡B1（Wheeler & Broadley, *Napoleon and the Invasion of England*, 1908, vol.I, pp.xiii—xiv转印）；Fortescue, vol.V，p.265（"every provision had been made for transporting the seat of Government to Worcester"，该处未附原始出处；同页关于法军入伦敦后纪律涣散的描述是作者1910年的推想）。葡萄牙王室1807年离开里斯本，见第七章。

〔海61〕Martin van Creveld, *Supplying War*（本地`downloads/pages/5b7b985b0f78.md`），p.64的假设算例（二十万人每日约需300吨），据研究卡B4（t_b9e29c，`notes_interface_french.md` S19）定位；每人每日1.5千克由此折算，马匹比例与饲料量是本书的规划假设。

〔海62〕研究卡B4（t_b9e29c），`B4_british_army_home_defence.md`与`B4_landing_scenario_matrix.csv`：两万、四万、八万、十二万四档与预警三档的条件判断。

〔海63〕"Walcheren 1809: A Medical Catastrophe," *BMJ*/PMC公开论文（https://pmc.ncbi.nlm.nih.gov/articles/PMC1127097/ ）。本地缓存`downloads/pages/37f8d3b81593.md`。

〔海64〕大军自布洛涅到多瑙河与乌尔姆的日数：自8月26日（科贝特记贝尔蒂埃收令）或8月22日（福蒂斯丘记初令）起算，本书独立复算。Robert Fulton 1804年7月英国合同（月薪200镑）；*London Gazette*, no.15742, 6 October 1804, pp.1237—1238（据旧版〔陆海8〕转述；本章未另读原件）。

〔海65〕1805年6月第三次同盟几近流产、意大利王冠与热那亚并合使其复活，据修缮总规划第八节所列A5核查（舍维格与恰尔托雷斯基训令），详见第八章。

〔海66〕研究卡IE（t_c8b161），`IE_ireland.md`第0、5、14节：1803年8月8日方案（Wheeler & Broadley 1908转录，引Bingham II:25），英文原句"provided that 20,000 of their countrymen joined the French army on its landing"；爱尔兰军团点名数据据旧版〔爱2〕（Desbrière；Kleinman 2005）；1798年洪贝尔与基拉拉；1803年都柏林约八十人（埃米特起义日期为7月23日）。Wheeler & Broadley与Carles均大量转引Desbrière，不算独立证据。

〔海67〕研究卡IE（同上）：动员上限函数与四档投送、三种终局的次序（其作者给出的主观区间为：留在联合王国并较早解放0.45—0.60，法系王国0.20—0.35，稳定共和国0.05—0.12；本书只用其次序）、占领所需兵力3.3万—6.6万（由人口乘假定驻军密度得出，未经可比案例校准）、饥荒变量的排序、B4保留西班牙波旁时爱尔兰选项重新可行的判断；1811年英爱民兵互调法据Fortescue 1909。

〔海68〕Ivan F. Nelson, "'The First Chapter of 1798'? Restoring a Military Perspective to the Irish Militia Riots of 1793," *Irish Historical Studies* 33, no.132 (2003), pp.369—386，注82（据Ferguson）；1801—1802年的20%据研究卡IE；Allan Blackstock, "A Forgotten Army: The Irish Yeomanry," *History Ireland*。补充分母主要是爱尔兰民兵、地方防卫团与1798—1800年调来的英格兰民兵。以上据旧版第三章〔爱4〕所引，本章沿用，未重读原文。

〔海69〕James Deery, "The Irish Soldier in the British Army during the Napoleonic Wars 1808–1815," *British Journal for Military History* 9.2 (2023), pp.162—169, DOI 10.25602/GOLD.bjmh.v9i2.1716。以上据旧版第三章〔爱5〕所引，本章沿用，未重读原文。

〔海70〕"Proclamation of the Provisional Government," 1803（Wikisource文本），第二条原句"From the same date, all transfers of landed property are prohibited, each person, holding what he now possesses, on paying his rent until the national government is established, the national will declared, and the courts of justice organized"（`downloads/pages/92f15cedf046.md`）。

〔海71〕James S. Donnelly Jr., "Captain Rock: Ideology and Organization," DOI 10.1353/eir.2007.0030；Stephen Randolph Gibbons, *Rockites and Whitefeet: Irish Peasant Secret Societies, 1800–1845*，博士论文，University of Southampton，1982（只读到题录与摘要）。以上据旧版第三章〔爱7〕所引，本章沿用，未重读原文。

〔海72〕History of Parliament, 1820—1832, Survey IV: Ireland；1829年爱尔兰选举法。约216,000→37,000与215,000→40,000是不同汇总口径。以上据旧版第三章〔爱11〕所引，本章沿用，未重读原文。

〔海73〕"Two Centuries of Irish Agriculture"，都柏林三一学院研究库（http://hdl.handle.net/2262/3927 ）；英国下院1849年7月13日所述爱尔兰债务与国库合并，据研究卡IE。英镑与爱尔兰镑、barrel与quarter分别保留。以上据旧版第三章〔爱8〕所引，本章沿用，未重读原文。

〔海74〕Gillian Boazman, "Ballincollig Royal Gunpowder Mills: the vaulted magazine," *Journal of the Cork Historical and Archaeological Society* 112 (2007), pp.54—75，引TNA WO 55/2285（原档未读）。以上据旧版第三章〔爱3〕所引，本章沿用，未重读原文。

〔海75〕H. F. B. Wheeler and A. M. Broadley, *Napoleon and the Invasion of England* (1908)（本地`downloads/pages/5550fd06ab38.md`，epdf网页文本，无页码）：1796年12月21日三十五艘到达爱尔兰海岸，22日"Bouvet anchored at Bear Haven with eight sail-of-the-line and seven other vessels"，其余被吹回海上；格鲁希部约6,500人，布韦未执行登陆命令；奥什座舰"Fraternité"失散（作者引Mahan, vol.I, pp.355—356）；1797年方案：亨伯特六千人加达恩德尔斯一万五千人，德温特16艘战列舰与12艘巡防舰，布雷斯特12艘舰载六千至八千人（作者引Desbrière, vol.I, p.258）；坎珀当"Duncan, who took nine ships out of a possible fifteen"。出航规模（约43艘，14,450—15,000人）据研究卡IE（t_c8b161）`notes_ie.md`A1所引UCC图书馆与napoleon-series两说。

〔海76〕Cormac Ó Gráda, "Ireland's Great Famine: An Overview"；Eric Vanhaute、Richard Paping、Cormac Ó Gráda编，*The European Subsistence Crisis of 1845–1850*，表1.3；Ó Gráda, "Migration as Disaster Relief"。以上据旧版第三章〔爱9〕〔爱10〕所引，本章沿用，未重读原文。

〔海77〕英国下院1823年2月25日殖民收支辩论，cc.248—254（1820年军需账）；1830年5月10日辩论，cc.509—513（宣读1827年财政部信）。各殖民地数字是本地年度账，不含所有海陆军与运输成本；累计亏空跨越多个年度。

〔海78〕英国下院1848年7月25日《殖民地政府》辩论（莫尔斯沃思的估算与政府答辩）。本地缓存`downloads/pages/c7337a608bc3.md`。

〔海79〕Roger N. Buckley, "The British Army's African Recruitment Policy, 1790–1807," *Contributions in Black Studies* 5 (1981), DOI 10.7275/6931，转引其*Slaves in Red Coats* (1979), pp.55—56；1817—1836年驻军死亡率资料据旧版〔帝3〕。一万名白人与五千名黑人的假定组合每年约需补充935—1,413人，是按这些比率的试算。

〔海80〕Seymour Drescher, "Le « déclin » du système esclavagiste britannique et l'abolition de la traite," *Annales ESC* 31.2 (1976), pp.414—435；*Slavery Abolition Act 1833*, 3 & 4 Will. IV c.73，第六十四、六十五条（本地`downloads/B6_SlaveryAbolition1833.pdf`）。Drescher一文据旧版第三章〔帝4〕所引。

〔海81〕《亚眠和约》第六、十条；Desmond Gregory, "The British Presence in Mediterranean Islands 1793–1815," *Storja* (1998)（本地`downloads/B6_Gregory1998_Mediterranean.pdf`）："Between 1794 and 1815 Britain occupied no less than eighteen islands"；英国在西西里"a force of never less than 10,000 and sometimes as large as 20,000 troops"；科顿1811年致海军部论米诺卡对封锁土伦的必要。此文此前未入书稿。

〔海82〕Haris Dajč, "The British-French Naval Rivalry in the Ionian and Adriatic Basins 1807-1814 from an insular perspective," *Povijesni prilozi* 67 (2024), pp.287—305, DOI 10.22586/pp.v43i67.32824（本地`downloads/pages/56707f7ed50c.md`，据https://hrcak.srce.hr/file/469145 ）：1807年11月"HMS Glatton with a few small boats conducted a successful blockade of Corfu"；1809年"The British fleet that conquered Zakynthos had only three frigates"；维斯岛及其主镇科米扎的居民1803年4,218人、1809年3,310人、英国控制时期约12,000人；1810年10月13日拿破仑令与10月21日迪布尔迪厄到维斯；利萨海战双方人数、炮数、舰数与伤亡；1812年2月22日"里沃利"号被俘。作者的战斗细节主要依据Safonov、Hardy与Sondhaus，属转述；本章未另读这些原书。

〔海83〕据研究卡B6（t_0fed70）第⑬、⑭节与"1848版图"表，按三条轨道重排；James D. Wilson, *The Anglo-Dutch Imperial Meridian in the Indian Ocean World, 1795–1820*，博士论文，Cambridge，2018（本地`downloads/B6_Wilson2018_AngloDutch.pdf`，只读导论与结论）说明荷兰海外属地在英荷合作下的命运取决于荷兰本土的政治地位。爪哇"1814条约议定归还、1816荷兰政府接收"，据研究卡B6第⑫节所引Wilson。表中归属是推演。

〔海84〕National Library Board Singapore, "Temenggung Abdul Rahman"（2019年8月5日）与"Treaty of Friendship and Alliance"（1824年8月2日，Crawfurd Treaty，第2、3、10—12条）；旧版资料附编〔统5〕。以上据旧版第三章〔帝7〕所引，本章沿用，未重读原文。

〔海85〕Canning—Polignac备忘录（1823年10月9日），刊于英国下院1824年3月4日记录，cc.708—719（`downloads/pages/3dbf2623d42f.md`），原句"it would consider any foreign interference, by force or by menace, in the dispute between Spain and the colonies, as a motive for recognizing the latter without delay"。这是较晚政策利益的证据。
