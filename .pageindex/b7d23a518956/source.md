# C17独立复算与引文抽查

审查者10043；2026-09-20。只读原交付，未运行会覆盖原CSV的生成器，改以独立`csv.DictReader`、`Counter`及`datetime.date`检查既有文件。没有进行军事能力模拟。

## 复算结果

- `c17_timeline.csv`：156行、156个唯一(path,quarter)键；S1/S2/S3各52行。
- `treasury_FRF`、`treasury_GBP`、`available_effectives`各156个NA；合468个数值单元。
- S1自1805Q4的41季均为未闭合状态；S3自1810Q4的21季均为分叉状态。
- 状态计数与`c17_checks.json`完全相同：PRE_WINDOW 3；BASELINE_CONTEXT_NOT_CAPACITY_TEST 45；LOW_BRANCH_UNVERIFIED 1；UNRESOLVED_AFTER_DIVERGENCE 41；CONDITIONAL_NOT_CLOSED 28；CONDITIONAL_AVOIDANCE_ONLY 1；MAINTENANCE_UNVERIFIED 16；POLICY_CONFLICT_REQUIRES_FORK 21。
- 六组日期相减（不含起日）：1805-08-26→10-07=42；→10-20=55；1805-08-22→10-07=46；→10-20=59；1806-09-25→10-14=19；1807-06-14→07-07=23日。
- Montreuil算术：36×130＋108×100＋72×66＝20,232；24,853−20,232＝4,621。本项只重算给定输入；影像来源核验交由战争证据子审。

**判断：结构及算术通过，不是登陆后还能按期返欧的工期证明，不是国家能力或任何路线可行性认证。**

## C17引文抽查（12组）

下列源均已实际读原缓存相关上下文，而非只核卡内重述；没有再次对校出版扫描或档案原件。Corbett和Fortescue各是一个出版来源家族，重复出现不当独立互证。

|#|主张/短引|实际核读位置（项目根目录起）|结果及限制|
|---|---|---|---|
|1|英俄条约4月11日签署；“Treaty signed on the 11th of April”|`downloads/c11_corbett.txt` 21721–21739，附录A，6月7日指示|通过；签署≠批准或协同作战|
|2|奥地利8月9日正式加入；“formally joined the alliance”|`downloads/c11_fortescueV.txt` 13671–13674，印p263|通过；史家叙述而非独立亲核加入文书|
|3|8月23日信保留舰队希望同时东调；“My decision is made”“I strike my camps”|`downloads/c11_corbett.txt` 13786–13842，印pp274–275|通过；同文“there is still time”确存，不能改成明确放弃所有渡海可能|
|4|Berthier 8月26日收行军令|同上13858–13904，印pp276–277|通过；收令不等于全军出发日|
|5|10月7日多瑙河节点与20日Mack投降|`downloads/c11_fortescueV.txt` 14035–14055，印pp271–272|通过；没有由此证明42/55天为不可压缩工期，C17已自限|
|6|1808四月条件承认Ferdinand；“si l'abdication…est de pur mouvement”|`downloads/pages/0dae11bc01f3.md` 10820–10869|通过；同时含法国干预与威胁语境，不证明内心保王或真实可接受套餐|
|7|Nesselrode五项谈判议题|`downloads/c12_vandal3_full.txt` 20965–21287，附录III，注670|通过；“Les principaux objets…”为内部建议，未变成双边接受|
|8|西班牙消耗使拿破仑更肯让步|同上21030–21049一带，“plus coulant”及随后土耳其战事句|通过但重要补充：原文立刻说Kutuzov在土耳其的胜利“ont réparé ce mal”，和平可能令当下“plus propice encore”。西班牙不是报告唯一、不可替代的谈判条件；C17称理由之一正确，若综合据此单向断定俄国更不肯接受则超源|
|9|意大利军预算≤3000万；另伊利里亚炮兵辎重≤400马|`downloads/pages/df27e5314cf3.md` 1576–1627|分别通过；400马与裁营裁骑属前段伊利里亚，不能归意大利军。意大利部分含跨地区重配、让法国并合部门分担，不能单读为全国净削减；综合括号压缩须分清地区|
|10|1811草案8万现役、其余预备；首批4月1日出发|`downloads/pages/43dacbcb242e.md` 第1、8条，及标题“2.e Rédaction”|通过；明确草案，未证明实际到队|
|11|1811年600万商业救助是拟上限|`downloads/pages/3b8b8e348c6d.md` 行28，c332–333|通过；“not with the supposition that that sum would be required”，不是实发|
|12|1811-05-20贷款合同仍待议会同意|`downloads/pages/bff7e2ccf088.md` 行18，c210|通过；“subject to the approbation of parliament”，不是即日国库到账|

另核1806-09-25、09-28、10-14与11-16节点：`downloads/pages/b8bc84d9143a.md` 212–264；1807 Eylau、Friedland、Tilsit日期：`downloads/pages/fcff28bd1292.md` 行30。均与表内所引读本相符。没有亲核1807停战文件日期异文，亦未补足指定Chandler/Schroeder双校。

## 旧旗标A/B的版本判定

最新`c17_victory_paths.md`第九节⑦已经明确列伙伴及军队、汇付供应、交通与战役时机、国内供款共同触发；⑨列北方目标有价冲突、1812-07-16请求→08-24批50万→09-13拨款及现金/采购/干部/训练门槛；末段明说提前贷款只属扩张波兰备选，不能加进S2。

因此综合十三节将A写成尚未显式、将B当现版遗漏，是旧版状态未刷新。**可关闭覆盖形式旗标；能力、概率与东线现金仍未知，不能一并关闭实质缺口。**不需要为此启动新历史调查。
