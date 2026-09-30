# C17 来源键、引文与使用范围

【工作记录】本表为`c17_timeline.csv`的来源字典。键后冒号是主题/条目别名，不一律等于原报告章号；以下以明确标题/定位为准。项目根目录为相对路径起点。依赖报告是证据交接层，不是独立原始证人；原件未读、转引与回溯限定不得因进入CSV而消失。

## 一、输入路径

|键|报告/附件（均在nodes/r_b55f2c1cf5/cards/之下）|有效定位与限制|
|---|---|---|
|BOUND|t_3dc3c2/c1_pod_dossier.md；项目PROJECT.md|C1条目01；1803年5月干预下限为任务边界，不是史料推断|
|C1|t_3dc3c2/c1_pod_dossier.md|冒号后的01–20为编年条目；事实存在置信度不能继承为成功率|
|CAL|t_a8401d/calendar_evidence.md|:1=第一节1805日期链；:2=第二节1806–07；OCR未逐页对图|
|C11|t_2c338c/c11_invasion_england.md；fleetplans.md|:7–8=登陆后终战、分支概率与四门槛；主报告节名与上下文优先；各门槛非独立概率|
|C12|t_26cd47/c12_russia_problem.md；russian_evidence.md|:4/:4.2A=双方条件与分支A；:4D=分支D；:7=长期均衡。D4=报告引用的1811法贸易通融证据，不是另一个原始档案|
|R1811|t_26cd47/c12_russia_problem.md 引D3；本卡另核downloads/c12_vandal3_full.txt|Vandal卷III所录Nesselrode十月报告，行20965起；不是共同接受条约|
|C13|t_75e9a5/c13_settlement_design.md；treaties_evidence.md；peace_evidence.md|CSV :2=和约条文及退出约束（主报告第一节）；:3–4=1806/1808和谈及埃尔福特；:7C=分支C。以主题定位，不将键号冒充原书页码|
|SPAIN|t_3dc3c2/bayonne_source_warning.md；t_c2dbca/spain_evidence.md|枫丹白露、3月23/27日、4月条件承认；3月29日伪信排除|
|C5|t_c2dbca/c5_iberia_americas.md|第一、二及七节；保波旁≠保证立宪或殖民完整|
|C2|t_104134/c2_naval_econ_data.md；c2_series.csv；c2_gaps.csv|财政子表fiscal/war_taxes_1804_1809.csv与cotton_1808_1812.csv；非完整国库账|
|C3|t_7ee3b0/c3_naval_race_model.md|开头结论及第一节；没有可识别1830追平年|
|C4F|t_95ef51/fr_crisis_checks.md|E1=1805条件停饷信；E2=1810贷款；E3=1811巴黎破产。非财政总模型|
|C4U|t_95ef51/uk_fiscal_checks.md|英国国债、1815服务负担与口径检查；不同日期存量不可直接相加|
|C9|t_bef693/c9_war_finance.md；extraction_evidence.md；uk_evidence.md|财政类型及和平转型；征服收益减少与军费减少同时核算|
|C14|t_208a11/c14_army_sustainability.md；conscription_occupation_evidence.md；horse_cadre_evidence.md|第二/五节兵员与1810行政口授；和平1815/1820/1830需求未识别|
|C16|t_b7b7b1/c16_britain_under_defeat.md；trade_evidence.md；evacuation_evidence.md|:1=五级终点；:2=议会；:3=贸易与和谈；:6=续战/终战。政治行动不能自动转为承认霸权|
|H1811M|downloads/pages/3b8b8e348c6d.md|HC Deb 11 March 1811 vol19 cc327–50；行28、c333附近：600万是提议授权上限|
|H1811B|downloads/pages/bff7e2ccf088.md|HC Deb 20 May 1811 vol20 cc210–23，开头：贷款合同须议会同意；非现金即时到账|

【方法限定】未新增事件季度的C1/CAL定位表示阶段来源与检索分辨率，不为整季“无事件”背书。每个事实字段有来源键；每个行动字段是模型选择，不假称有一条史料逐字规定本卡整个行动包。所有NA的出处是输入缺口声明，绝非数值证据。

## 二、抽查锚点（短引可用于红队回放）

1. 【事实·出版转引】Corbett附录A：`arrangements proposed in the Treaty signed on the 11th of April`。`downloads/c11_corbett.txt`行21721–21739，6月7日指示，来源署Foreign Office Russia 58。支持1805-04-11签署，不支持当日所有盟国即能协同。
2. 【事实·史家叙述】Fortescue V p.263：`On the 9 th of August that power formally joined the alliance with Russia and England`。`downloads/c11_fortescueV.txt`行13671–13674。奥方加入原件未亲读。
3. 【事实·出版转引】Corbett pp.274–275：`My decision is made`；`I strike my camps and replace my war battalions by my third battalions`。同txt行13786–13820，注行13842署Correspondance XI.117、Aug.23。支持调兵竞争，不证明布洛涅零守军。
4. 【事实·史家叙述】Corbett pp.276–277：`Berthier received the marching orders on August 26 th`。行13858–13904。收令而非所有部队同日出发。
5. 【事实·史家叙述】Fortescue V pp.271–272：`by the 7th of October one hundred thousand men had reached the Danube in his rear`；`on the 20th of October ... Mack surrendered`。行14035–14055。作者兵数不填为C17同日可用兵力。
6. 【事实·刊本通信，非原折】Panckoucke1821《Oeuvres》IV所刊1808-04-16信：`si l’abdication du roi Charles est de pur mouvement ... je reconnais V.A.R. comme roi d’Espagne`。`downloads/pages/0dae11bc01f3.md`行10826–10857。日期13/16异文未解；条件表态不证真诚。3月29日信不采用。
7. 【事实·出版转引】Nesselrode十月报告：`Les principaux objets ... 1. Les intérêts des ducs d’Oldenbourg; 2. La diminution des forces respectives sur la frontière; 3. La situation présente et future du duché de Varsovie; 4. La situation présente et future de la Prusse; 5. Les relations commerciales de la Russie.` `downloads/c12_vandal3_full.txt`行20965–21074范围，Vandal注670署Archives de Saint-Pétersbourg，原件未读。
8. 【事实·同源关键反证】同报告：`les revers qui épuisèrent les armées françaises en Espagne auraient rendu l’empereur Napoléon plus coulant`。同范围。**若S2避免半岛消耗，原备忘录对法国让步意愿的一个理由也随之减弱**。因此该报告只能作议題存在锚，不能原样搬入反事实1811并保证接受。
9. 【事实·现代文书转录】1810-01-30行政会议口授：`Le budget de l’armée d’Italie ne doit pas dépasser 30 millions`；`pas plus de 400 chevaux`。`downloads/pages/df27e5314cf3.md`行1576–1627。分别为地方预算上限与炮兵辎重马匹上限，不是实付/实马/全国和平定额；1.7与53百万矛盾数字不入账。
10. 【事实·草案转录】1811征兵第二稿：`quatre-vingt mille seront mis en activité; le reste formera la réserve`；`Le premier détachement ... sera mis en route le 1.er avril`。`downloads/pages/43dacbcb242e.md`第1、8条。12万授权分8万拟现役与4万预备；不能当完训到队。
11. 【事实·议会发言】1811-03-11：`grant relief to the extent of six millions, not with the supposition that that sum would be required`。H1811M行28。600万≠实发；所述1793发出220万不能移成1811数字。
12. 【事实·议会发言】1811-05-20：`concluded a contract, subject to the approbation of parliament, for the Loan`。H1811B行18。支持融资交易仍存在，不证明无限信用或最终实收。
13. 【事实·转引自Plessis据Ramon】1805-08-24：`j’arrêterai, s’il le faut, la solde de mes troupes pour la soutenir`。`downloads/pages/54a70cc2111c.md`搜`Le 24 août`；Plessis2000 pp.35–43注21，Ramon1929 pp.66–67未读。条件表态，非实际停军饷。
14. 【文献推断·Gabillard】`un prêt au Trésor de 45 millions pour solder les arriérés des exercices de 1801 1809`。`downloads/pages/e4f61139af7d.md`，Gabillard p.562；单源二手，非1810税收或季度流水。
15. 【文献推断·Branda】`En janvier et février 1811 ... 122 faillites ... dans la capitale`。`downloads/pages/414d9ffcebd4.md`，Branda2012 pp.26–33，“D’une crise à l’autre”。巴黎企业件数无分母，非国家违约。

## 三、来源独立性与未读谱系

【事实·工作记录】C1/C12共同依赖Vandal时计为同一文本链；C11与CAL共同用Corbett/Fortescue不是增加两个独立证人；C4/C9共同用Gabillard、Branda、议会账也不能叠加置信度。Hansard中反对发言和政府发言是不同观点，但对同一会计表的重复引用仍为同一数据源。

【未验证】本卡未直接读取Chandler或Schroeder编年原页，故以实际可得Corbett、Fortescue和Fondation年表替代，不能声称满足原合同的指定编年双校。未取得C4完整跨国财政主模型，仅复用两件有界财政备忘。TNA FO/ADM、AN AF IV、SHD GR/MV、AAE CP Russie、圣彼得堡档案均仅按依赖转引谱系列名，不宣称亲调档。Caulaincourt、Mollien、塔列朗回忆材料一律回溯性；后出的1815制度仅作镜像，不能提前成为1807既有工具。
