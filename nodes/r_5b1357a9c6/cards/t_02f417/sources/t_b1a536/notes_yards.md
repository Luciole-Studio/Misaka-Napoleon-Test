# 船厂资料收束笔记

停止广搜。交付配套`yards_launches_1807_1813.csv`，52个不同舰体：指定七组50艘，范围外瑟堡补列2艘。只收实际读到网页正文中的下水记录；主要是注明专著来源的网页转录，非原书／档案逐行冻结。详细引证及既有研究过程保留在本卡`evidence/yard_evidence.md`，本次未再改写。

## 汇总及使用界限

|建造厂|1807—1813名单小计|
|---|---:|
|安特卫普|18|
|布雷斯特|3|
|罗什福尔|2|
|洛里昂|6|
|土伦|13|
|热那亚|3|
|威尼斯|5|
|指定七组|50|
|瑟堡（补列）|2|

指定七组逐年9、10、3、7、9、8、4；含瑟堡的1813为6。七组50/7=7.14，四个本土厂24/7=3.43，加瑟堡26/7=3.71。下限26不证明本土完整总量不足28；旧本土不能代表包括安特卫普的帝国。未列出的厂年不是已核零值。

CSV的source_codes对应下方实际读到的网页；定位均为相应舰级小节中的同名舰条目。evidence_status=web_text_secondary表示网页正文已读、上游专著未亲阅。conflict字段不空者保留异文。名单是有来源的暂定下水最小清单，不是已穷尽全国总表。舰名为舰体识别名，不强称均为下水当天名称。改名、俘获后转籍不重复计。

## 来源代码、URL及定位

- L：https://en.wikipedia.org/wiki/List_of_ships_of_the_line_of_France ，First Empire → 118/80/74-gun各节；缓存`downloads/pages/898ecb4eeeb6.md`行1029—1176。示例短引：“Charlemagne 74 (launched 8 April 1807 at Antwerp)”。
- T：https://en.wikipedia.org/wiki/T%C3%A9m%C3%A9raire-class_ship_of_the_line ，Duquesne/Danube/Small Variant各表；缓存`downloads/pages/07268e71e6e2.md`。分列开工、下水、完工；Commerce de Lyon为1803-11、1807-04-09、1808-03。
- B：https://en.wikipedia.org/wiki/Bucentaure-class_ship_of_the_line ，Ships in class；缓存`downloads/pages/06f099bfa047.md`。Friedland：“Launched: 2 May 1810”；“Completed: May 1811”。
- O：https://en.wikipedia.org/wiki/Oc%C3%A9an-class_ship_of_the_line ，Ships of the second (modified) group；缓存`downloads/pages/a33ec60b83be.md`。Héros：“launched on 15 August 1813 and completed in January 1814”。
- U：https://en.wikipedia.org/wiki/French_ship_Ulm_(1809) ，Construction and career；缓存`downloads/pages/f2fd5147bb31.md`；正文归土伦，转引Winfield–Roberts p.94。
- M：https://en.wikipedia.org/wiki/French_ship_Mont_Saint-Bernard_(1811) ，Construction and career；缓存`downloads/pages/dc7df5fbd91a.md`；“launched on 9 June 1811”。
- P：https://en.wikipedia.org/wiki/French_ship_Polonais_(1808) ，Construction and career；缓存`downloads/pages/a926b7531016.md`；“launched on 27 May 1808”。
- Ti：https://en.wikipedia.org/wiki/French_ship_Tilsitt_(1810) ，Construction and career；缓存`downloads/pages/5af51159c185.md`；“launched on 15 August 1810”。
- V：https://threedecks.org/index.php?display_type=show_shipyard&id=281 ，Events at Venice，1810—1812年各舰；缓存`downloads/pages/acacc4f22128.md`。除Rivoli外四舰标MIdN，页末解作Virgilio Ilari《La Marina Italiana di Napoleone》，原著未阅。该表英国Rivoli的1812条目属同一被俘舰，去重。
- G：https://gallica.bnf.fr/ark:/12148/btv1b69469265 ，BnF版画目录题名“Premier vaisseau de ligne, le Charlemagne de 74 lancé au milieu de l'Escaut, Anvers le 8 avril 1807”；缓存`downloads/pages/a6a9708fe694.md`。馆藏题名独立佐证，未目读版画图像。

L/T/B/O/U/M/P/Ti不能算相互独立来源，主要上游为Winfield–Roberts、Roche、Demerliac。V的Ilari谱系不同但未验证独立性。G仅独立佐证Charlemagne一舰。

## 厂级规划锚点：不进入实际下水CSV

1811-03-05致Decrès：https://napoleon-histoire.com/correspondance-de-napoleon-ier-mars-1811/ ，缓存`downloads/pages/f042c1f13d31.md`行188，起句“j’ai pris un décret pour porter à dix-huit”。已读现代全文转录：要求Anvers18船台，每舰占台三年，对应年6艘，并保留6—8艘待下水；属于目标，不证明18台已投产。点名六舰要1811下水，但名单中Gaulois和Conquérant为1812年4月。

1811-10-02安特卫普致Decrès：https://napoleon-histoire.com/correspondance-de-napoleon-ier-octobre-1811/ ，缓存`downloads/pages/550652301685.md`行40—54。原文“construire chaque année huit vaisseaux au lieu de six”，明确该厂；理由涉及荷兰配员、布洛涅人员重新分配及追加舰材工人。6→8不是全国实绩，不与Todorov全国20作直接冲突。两信纸本／手稿未校。

## 存量与未核项

1. Todorov2008已有25页电子稿`downloads/F3_Todorov_redressement_1810_1813.pdf`，第15页文字与图像已核：1810夏50、1812年72、1814年4月74；末期分项旧法港42、Anvers21、Hollande9、Gênes/Venise/Corfou2。这是所在港／控制范围存量，不是建造厂来源；意厂造舰移土伦可归旧法港，2不是累计产量。无armé/désarmé细分。
2. 同文p16全国满负荷“une vingtaine ... par an”未由逐舰名单复现；1810—1812当前7、9、8只是下限，不是全国上限，不能反向声称证伪20。
3. Muracciole1974《Napoléon et les arsenaux de la Marine》，https://www.persee.fr/doc/rharm_0035-3299_1974_num_1_1_7813 ，全文缓存`downloads/pages/21ae17eda88c.md`，104为“à flot ou en chantier”，无已核104=74+30分解。
4. 日期冲突：Mont Saint-Bernard总表1809 vs单舰/数据库1811；Polonais 5月25/27；Tilsitt 8月15/25；Ulm的厂别总表/单舰为土伦，舰级表为罗什福尔。暂采CSV主值，均不改变七年总小计。
5. 待核：Winfield–Roberts原书；荷兰新增舰Couronne、Piet Hein的日期异文；斯海尔德非安特卫普厂穷尽性；威尼斯法/意法律舰籍；104具体地域边界。原书入口获取仅得目录或错配文本，未假称读过。
6. 排除：1806下水而1807完工舰；1814及以后下水舰；未下水的在台舰；Royal Hollandais船架赴英国后以HMS Chatham在Woolwich下水；旧荷兰舰并入及全部改名／转籍重复。
7. 协调方8—12及后6—10艘/年属于模型假设，不是本资料表认证的史实区间。本卡不作预测、不提交卡。
