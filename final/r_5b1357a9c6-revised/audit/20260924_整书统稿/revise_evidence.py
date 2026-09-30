from pathlib import Path
import json
B=Path(__file__).resolve().parents[2];C=B/'chapters';log=B/'audit/20260924_整书统稿/正文改动记录.json';changes=json.loads(log.read_text())
def edit(n,fn,why):
 p=C/n;s=p.read_text();t=fn(s);assert t!=s;p.write_text(t);changes.append({'chapter':n,'purpose':why})
def before(s,a,n):
 assert s.count(a)==1;return s.replace(a,n.strip()+'\n\n'+a,1)
edit('01_法国的能力与代价.md',lambda s:before(s,'## 八、继承：皇帝必须留下的，不止一个儿子','''帝国展示同意的方式，还需要同实际支持分开。共和八年公投公布约3,011,007张赞成票与1,562张反对票，近乎一致的外观容易诱使后人把它当作没有政治反对。Claude Langlois重读计票过程后指出，卢西安·波拿巴在期限压力下提交的结果包含操纵；已经汇齐的真实赞成票少于1793年约35万，军队表决的处理也有严重问题。几乎没有登记的反对票，不等于大多数人已经积极接受新宪制。〔统16〕

这条证据影响继承判断。皇帝能够组织一次赞成仪式，未必能够在欠饷、债务或宗教争执中获得同样合作；地方官员也可能把沉默写成拥护。反过来，弃权还可能来自恐惧、程序混乱或漠不关心，不宜全部改记为反对。**持久支持应以纳税、到营、法院使用、地方任职和危机中的续约交叉检验；任何一项官方投票总数，都不足以给王朝开一张四十年的信用证。**'''),'将民意代理失真嵌入继承论证')
edit('07_行省化的边界.md',lambda s:before(s,'### 2．比利时与皮埃蒙特：累计数字不是百分之百的忠诚','''降低抵抗，有时意味着少征一些，而非国家突然更善于强制。Rouanet与Piano研究1809—1810年的差异征额政策，在高抵抗省份的相关规格中，逃役差距下降约5.00个百分点，标准误1.73；同期人口征集份额也下降。地方接受因此改善，却不应把所有逃役减少都记成新增兵力。征募制度的进步，一部分来自重新分配负担。〔统17〕

这对省化有直接意义：巴黎若以降低征额换取稳定，就要把少征的兵从军事计划中扣除，不能一面赞扬和解，一面仍使用原最大军额。发表研究中额外逃役与额外送军人数还存在正文、附录表述不一致，细数保留在附编校勘；政策方向有证据，精确净增兵不冒充已经核定。'''),'补差异征额效果及其兵力代价')
edit('08_新秩序的经济与社会.md',lambda s:before(s,'O’Rourke估算的封锁福利损失，也不是年度GDP增长率。','''Buggle的研究把民法典的采用与后继政权继续保留一并纳入解释，说明制度延续可能比一次征服更重要；Lecce与Ogliari则发现制度移植同地方文化代理变量存在明显交互，提醒我们同一法典并非处处产生同样结果。两者并不抵触：制度可以改变社会关系，既有社会关系也会改变制度的作用。它们观察的时期和结果远晚于本书，不能把当代信任或1886年教师工资兑换成1815年对法国的忠诚。具体版本、样本与系数见附编。〔统13〕'''),'恢复法律持续性与地区异质性证据，避免正系数堆砌')
edit('10_资料附编.md',lambda s:before(s,'### 工业化的尺度与人口的尺度','''### 法律、文化与财政：另外几组已研究的证据

以下材料补足的不是一个“法国改革总效应”，而是不同机制的条件。版本也须分别保留：工作稿的表号只用于工作稿，不借刊本年份增加权威。

| 研究及实际版本 | 对象与结果 | 可用判断与限制 |
|---|---|---|
| Buggle，2013年SOEPpapers 566 | 德意志民法典历史边界附近样本；2003年社会信任，表4第5列系数0.0485、标准误0.0169，样本4,031 | 处理包括采用及后继保留；部分表6规格不显著。不是1848忠诚，也不直接排除迁移与空间相关 |
| Lecce、Ogliari，2019年3月作者稿 | 447个普鲁士县，1886男性小学教师年工资对数；表3第5列法国制度与新教份额交互−0.208、标准误0.0403 | 交互项不是新教的总效应；宗教、教育与既有制度相关，不能推出宗教优劣或整合阈值 |
| Dincecco，2009年刊本 | 11国长面板，黄金计价人均公共收入的对数；表6第2列集中专制0.2215、集中有限政府0.6206 | 相对同一碎片化专制基组；表中括号为绝对z值，不是标准误。两种制度维度相关而非随机实验 |
| Ploeckl，2010年牛津讨论稿84 | 第4—5节以联盟博弈和历史叙事解释关税同盟的序贯形成 | 外部选择、补偿与加入顺序可供机制比较；不存在待补的回归系数、标准误或福利净效应 |
| Franck、Michalopoulos，2017年NBER工作稿23936 | 法国革命流亡与长期发展；表4的1860年人均GDP对数系数−0.255、标准误0.0749；2010年0.176、0.0607 | 前期与长时段结果可能异号；处理早于1803年，尺度与气候工具的排除限制尚有问题，不作拿破仑增长参数 |

Buggle的0.0485不是民法典使信任提高4.85%的通用效应。Lecce—Ogliari交互项的普通近似95%区间为−0.287至−0.129；按前拿破仑政治单位聚类，标准误约0.0692，近似区间变为−0.344至−0.072。置信区间保持负值也没有排除宗教代理的内生性，更不能推导某个新教人口比例以上法国治理必定失败。〔统13〕

Dincecco同列的碎片化有限政府系数为0.5886，三个制度项各自相对基组；集中专制与集中有限政府之差为0.3991个对数点，但检验这个差需要二者估计的协方差。把0.6206称为“宪政多收62.06%税”，或把两个系数相减后直接报告显著性，均超过原表。该研究最有价值的用途，是让第一章的征收能力与第十章的支出约束成为两个须分别解释的制度。〔统14〕

Ploeckl没有回归效应，不是没有做完研究；它采用的就是另一种方法。法国若要借用其机制，须解释荷兰的海上出路、南德的王朝权益、普鲁士与奥地利的替代保护，怎样改变每一国的加入条件。以一个未经校准的欧洲福利总数代替这些选择，反而会丢掉论文最有用的内容。〔统15〕

Franck—Michalopoulos的跨期异号，则提醒我们不把土地与精英结构的变化都写成即时受益。革命时期流亡已经在1803年以前发生；它可以解释起点的社会结构，不能作为拿破仑1807年新选择的一项额外政策收益。此处只保留方向与原表参数，不将尚待对齐的处理尺度换成百分比。〔统18〕

### 征额调整怎样降低逃役，又改变资源

Rouanet—Piano刊本表4第4列，高抵抗第4、5类省1810年相对1809年的差距变化为−4.99631个百分点，标准误1.73068；普通正态近似95%区间为−8.39至−1.60。同期人口征集份额系数约−0.00024。两项并列，才说明降低负担参与了降低逃役，不能只取后一项政治收益而保留原征兵要求。最强控制样本又缺少比利时、德意志和意大利省份的部分资料，不足以替全体新省背书。〔统17〕

该文正文第1092页谈到3,256名额外逃役者，却又以10,499为基数称增加27%；补充材料第61页则区分2,812名额外逃役者与3,256名额外送军者。2,812÷10,499约26.78%，3,256÷10,499约31.01%，应保留这个内部差异。附录变量实现尚须同复制数据核对，本文既不宣称净增兵为零，也不把3,256−2,812＝444视为已识别净增兵。

### 通信量有时段，统治支持有分母

《通信全集》的几个卷次，提供行政工作密度而非处理极限：1806年卷收2,685封；1808年卷连同1809年一月收3,021封；1810年三月至1811年三月卷的导言列3,006封；1811年四月至十二月卷收3,144封；1812年卷收2,551封。九个月3,144封折年约4,192封，是机械年化，不是观测到的全年峰值。卷十导言与基金会年报另有3,006／3,214的差异，本文以导言陈述其收录量，不把不同版本拼成工作负荷曲线。〔统1〕

1811年九个月的两位陆军行政大臣收件合计1,396封，约占44.4%；导言所称陆军事务占60%，还包括其他将领与官员，二者不矛盾。德克雷320封，贝尔蒂埃238、达武229、马雷120、莫利安98、高丹40、约瑟夫1封等收件分布，显示注意力的集中，也不证明收件最少者完全失去其他沟通渠道。巴黎—马德里最快单程五六日，莫斯科方向约十四五日的回忆材料，支持必须地方授权；“西欧8—12日、伊比利亚3—4周、俄境4—5周”的完整决策回路仍属作者估算，不当作统一邮政时刻表。〔统1〕

公投也须同样处理。共和八年官方约301万赞成票与极少反对票，须连同计票操纵和参加程序判断，不能直接代表全国积极拥护。1815年的155万量级赞成票、不同参与率和军队票数，在研究笔记中另有精确数字，但本轮尚未逐项对齐原表；这些数保留在核查记录，不据它们计算一个虚构的“王朝生存阈值”。可采用的结论是公投不等于稳定支持，而非弃权者全部反对。〔统16〕'''),'恢复计量、征额、通信与民意证据，逐项界定版本和被解释变量')
# New notes carry full bibliographic identities rather than project card names.
p=C/'10_资料附编.md';s=p.read_text();s+='''

〔统1〕Thierry Lentz，〈Correspondance générale de Napoléon Bonaparte, tome 11 : Bruits de bottes, avril–décembre 1811. Introduction au volume〉，[Fondation Napoléon公开导言](https://www.napoleon.org/histoire-des-2-empires/articles/correspondance-generale-de-napoleon-bonaparte-tome-11-bruits-de-bottes-avril-decembre-1811-introduction-au-volume/)，以“Les 3 144 lettres”及“Et, bien sûr”起首段定位；Gabriel Madec，〈1808 : Expansions méridionales et résistances〉，[卷八导言](https://www.napoleon.org/histoire-des-2-empires/articles/1808-expansions-meridionales-et-resistances/)，收录范围及马德里—巴黎信使段；卷六、卷十导言分别见[1806年卷](https://www.napoleon.org/histoire-des-2-empires/articles/correspondance-generale-de-napoleon-bonaparte-tome-6-1806-vers-le-grand-empire-introduction/)与[1810—1811年卷](https://www.napoleon.org/histoire-des-2-empires/articles/correspondance-generale-de-napoleon-bonaparte-tome-10-un-grand-empire-mars-1810-mars-1811-introduction-au-volume/)；Marie-Pierre Rey，[卷十二序](https://www.napoleon.org/histoire-des-2-empires/articles/1812-la-campagne-de-russie-preface-de-mp-rey-au-tome-12-de-la-correspondance-generale-de-napoleon-bonaparte/)。2026年9月24日核读所存转录相关段；收件分布依编者，不冒称逐封重计。莫斯科时延据Caulaincourt回忆经卷十二序引述。

〔统2〕本书作者的分期资源配置，版本2026年9月24日；历史尺度参照Marion，*Histoire financière de la France depuis 1715*, t. IV（巴黎：Arthur Rousseau，1925），页317—324及第一章法13注；并参第三章第五节的海军计划、模型与敏感性。650／750／850是收入门槛，700／900法郎是兵均成本参数；1.45亿／1.65亿海军支出是所选预算，不是舰册预测。三档算式、共同基金及铁路复算完整写在第一、九、十章；模型类型与证据状态另见资料附编。各地未来税基尚未构成同年完整实收账，故算术闭合不冒称军政联合可行性已经证明。

〔统3〕盟国负担的历史参照见本书第四章第三、六、七节及第五章第三、五节：华沙预算据Dominika Rychel-Mantur，“Jean-Charles Serra wobec stanu finansów Księstwa Warszawskiego w 1808 r.”（2025），[DOI](https://doi.org/10.35765/rfi.2025.3103.15)；莱茵邦联义务据1806年7月12日邦联条约；意大利与那不勒斯财政据Alexander Grab，*Napoleon and the Transformation of Europe*及John A. Davis，*Naples and Napoleon*，两章原注所列版本。此处表格后两栏均为本书拟议政策，没有把它们归给上述作者或未签署条约。

〔统4〕安特卫普安排是本书条约方案，六艘上限并无已签历史协议作为依据。事实参照为第三章第三、五节既有基地能力与海军模型、第二章第二节1806及1812年谈判文书。它用于明确安全对价、预算取舍与违约后果，不用于证明英国必然接受。

〔统5〕National Library Board Singapore，〈Temenggung Abdul Rahman〉，2019年8月5日，[机构条目](https://www.nlb.gov.sg/main/article-detail?cmsuuid=20ede07c-76e3-4932-8816-4810e9528a72)，尤其“Treaty of Friendship and Alliance (1824)”及1819年安排各段；〈Treaty of Friendship and Alliance〉，1824年8月2日，通称Crawfurd Treaty，第2、3、10—12条，[文本转录](https://en.wikisource.org/wiki/Crawfurd_Treaty)。2026年9月24日核读机构叙述与条约转录；新加坡在本书世界仍被选为首选候选，是作者推断，不是史实条约的预测。

〔统6〕Stuart Woolf，*Napoleon’s Integration of Europe*（London and New York：Routledge，1991；所读为Taylor & Francis e-Library，2003），页232及该页注71—72。正文采用作者对流亡公务员职业构成、蒂罗尔邻区消费税与贝格工业危机的叙述；2026年9月24日复核本地电子本该页文本，未重查底层流亡名册。

〔统7〕墨西哥王朝自治与巴西自治王国为本书作者的终局排序；历史前提分别参第六章第五及第八节所引Marichal财政研究和Kirsten Schultz，*Tropical Versailles: Empire, Monarchy, and the Portuguese Royal Court in Rio de Janeiro, 1808–1821*（Routledge，2001）。墨西哥北疆另以1848年2月2日《瓜达卢佩—伊达尔戈条约》第5、8—9条作为史实边界与居民权利的比较，[美国国家档案馆原件及转录](https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo)，Record Group 11, Perfected Treaties, exchange copy；访问2026年9月24日。条约证实的是实际战后处分，并不证明反事实墨西哥同样失地；正文较少失地的判断仍是条件推演。

〔统8〕希腊外交部外交与历史档案服务，〈International Treaties and Protocols〉，[机构文书展览](https://200years.mfa.gr/en/international-treaties-en/)，1827年7月6日伦敦条约、1829年3月22日及1830年2月3日伦敦议定书项目，访问2026年9月24日。本文核读机构所述文书内容与展示说明，未宣称校勘每一份手稿；自治向独立的史实变动用于比较政策选择，反事实独立终局由作者排序。

〔统9〕National Army Museum，〈First Sikh War〉，[机构研究说明](https://www.nam.ac.uk/explore/first-sikh-war)，尤其“Treaty”节，访问2026年9月24日。1846年条约后的王朝、英国驻地官与驻军关系为历史参照，不按同年战争套用本书世界；更早锡克财政军备见本章所引H. T. Prinsep，*Origin of the Sikh Power in the Punjab*（1834）。

〔统10〕1814年5月30日《巴黎和约》第8条，印度据点另参第8—9条，[法文文本转录](https://www.napoleon-empire.org/texte-officiel/traite-de-paris-1814.php)，以及第七章第七节所引1810年前后岛屿作战材料。法国战败后的条约不是未败法国必须接受的命令；本文取其为英国据点优先级与分拆交换的参照，选择毛里求斯归英、波旁归法是较晚停战下的作者判断。

〔统11〕1842年8月29日《南京条约》，第3、5条；The National Archives，〈Hong Kong and the Opium Wars〉，Source 4，[原件节选与转录](https://www.nationalarchives.gov.uk/education/teaching-resources/hong-kong-and-the-opium-wars/)，馆藏号FO 93/23/1b，访问2026年9月24日。网页图像说明与转录均须以实际条号辨识；本文仅用已展示的基地与公行条款，不把整页通俗概述当作对中国全境“自由贸易”的法律授权。

〔统12〕M. G. Buist，*At Spes Non Fracta: Hope & Co. 1770–1815*（The Hague：Martinus Nijhoff，1974），页61—62；2026年9月24日复核文本及第62页图像。8,300万及替换为7,600万是从四项名义数作的加总，并非作者给出的统一新现金流量；西班牙贷款含旧债及息票转换，那不勒斯含商行与王室承接。不得据此年化阿姆斯特丹融资能力，也不据此宣布1810年后全部市场活动归零。

〔统13〕Johannes C. Buggle，*Law and Social Capital: Evidence from the Code Napoleon in Germany*，SOEPpapers on Multidisciplinary Panel Data Research 566（Berlin：DIW，2013），页15—21、36表4第5列及表6，[所用工作稿](https://d-nb.info/1152137301/34)。2026年9月24日重核第36页表格文本和图像；不以2016年*European Economic Review*刊本页码替代。Giampaolo Lecce、Laura Ogliari，*Institutional Transplant and Cultural Proximity: Evidence from Nineteenth-Century Prussia*，2019年3月作者稿，表3第5列、表A4，[所用稿本入口](https://aisberg.unibg.it/retrieve/e40f7b8b-9205-afca-e053-6605fe0aeaf2/Lecce_Ogliari_2019.pdf)；刊本题录为*The Journal of Economic History* 79(4)，2019，页1060—1093，[DOI](https://doi.org/10.1017/S0022050719000366)。所用系数据已保存作者稿文本，未把尚未逐格校影的作者稿冒作亲核刊本。

〔统14〕Mark Dincecco，“Fiscal Centralization, Limited Government, and Public Revenues in Europe, 1650–1913”，*The Journal of Economic History* 69(1)，2009，页48—103，尤其表1、表6第2列，[DOI](https://doi.org/10.1017/S0022050709000345)。本书据保存的刊本排版文本重核系数与括号z值，未新做回归；表6图像校验仍待补。财政集中与有限政府的机制比较，不构成拿破仑改革的随机因果效应。

〔统15〕Florian Ploeckl，*The Zollverein and the Formation of a Customs Union*，University of Oxford, Discussion Papers in Economic and Social History，No.84，2010年8月，第4—5节，[所用工作稿](http://www.nuff.ox.ac.uk/economics/history/paper84/ploeckl84.pdf)。共同基金的金额、表决和退出程序为本书方案；历史构件另参1804年莱茵共同航行安排及第十章终5注，不声称法国曾批准本书拟议条款。

〔统16〕Claude Langlois，“Le plébiscite de l’an VIII ou le coup d’État du 18 pluviôse an VIII (suite)”，*Annales historiques de la Révolution française*，no.208，1972，页231—246，尤其“Le pouvoir et l’organisation de la consultation”下“Interprétation des résultats”，[原刊转录](https://www.persee.fr/doc/ahrf_0003-4436_1972_num_208_1_4643)。2026年9月24日核读保存转录及注35—43相关段；计票操纵并不等于本次查阅全部投票原册。1815年各精确票数另列待核，不用于本书定量结论。

〔统17〕Louis Rouanet、Ennio E. Piano，“Drafting the Great Army: The Political Economy of Conscription in Napoleonic France”，*The Journal of Economic History* 83(4)，2023，页1057—1100，尤其页1065、1077注33、1088—1092与表4第4列，及在线补充材料第61页，[DOI及附件入口](https://doi.org/10.1017/S0022050723000360)。本文恢复项目已校页的刊文估计与内部数字差异，未获取完整复制数据或重跑回归；近似区间是按已刊系数与标准误复算，不是作者另报的新估计。

〔统18〕Raphaël Franck、Stelios Michalopoulos，*Emigration during the French Revolution: Consequences in the Short and Longue Durée*，NBER Working Paper 23936，2017，表4—5，[工作论文](https://doi.org/10.3386/w23936)。本文采用所存2017年稿第49—50页表值，尺度与工具变量限制沿该稿而不补造成后出刊本结果；表值用于说明时间异质性，不转为1803年以后法国军费的新增税源。
''';p.write_text(s)
log.write_text(json.dumps(changes,ensure_ascii=False,indent=2))
