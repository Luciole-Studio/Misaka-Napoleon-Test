# B1笔记：政治能力包络与外卡定量接口

## K1 B2已构建BoE序列（本轮交叉输入；本人不重复解算整工作簿）
- 数据构建者Sister10041、卡t_044211；实际读取其 `B2_series.csv` 首段字段及1804/1805/1810/1811/1815行（grep完整财政/收益率字段），用户授权采用 `BoE_selected_cached_values.xlsx` 缓存数据。
- 底层：Bank of England, *A millennium of macroeconomic data*, v3.1；工作簿 `downloads/B2_BoE_millennium_v31.xlsx`；来源映射记录B2目录 `BoE_provenance.json`。本卡不把21世纪整理误称1811即时可见官方统计。
- 1810 calendar consol yield=4.4085408495%；1811=4.6741684621%，升0.2656276百分点≈26.56基点；单元A31!T130/T131。按财年列1810/11收入£73.0m、支出£81.6m、利息£24.4m；1811/12收入£71.0m、支出£87.3m、利息£24.6m（A27!AT/AV/AW134、135）。财年终点5 January，不能与calendar收益率同日比较。
- 1804/05收入£50.2m、支出£62.8m（A27!AT128/AV128）；1805/06收入£55.0m、支出£71.4m（129行）。这是观察到的支出尺度，不是财政绝对上限。
- 1815/16收入£79.1m、支出£99.5m、利息£32.2m（A27!AT139/AV139/AW139）；是史实战事和税制所得，和平分支不能继续无条件套入。
- 【解释】1811市场融资成本确恶化但谈不上由这两个年均数单独判崩溃；新债现金借款成本4.208→4.746%是另一口径，不与consol收益率混算。B2已向本卡说明此区分。
- 【推演】无大陆盟友一方面损失逆转大陆局势的希望，另一方面省补贴/陆战支出；政治求和可能早于国家偿债能力归零。伦敦陷落须独立压力测试付款、纳税与银行认可，不用这些和平/非占领年值证明可无限借债。

## K2 商品贸易边界（授权复用旧C16已核表）
- Eli F. Heckscher, *The Continental System: An Economic Interpretation* (1922), printed pp.244–245、353；`downloads/c15_heckscher1922.pdf`, doc 1baaae7f3185；本轮通过旧C16报告和trade_evidence复用，不称再次读图。
- 非美国美洲市场的英国国内产品出口：1810 £15.64m→1811 £11.94m，含西印度；不能叫纯‘新独立拉美市场’。1807–12现金补贴£14.722m不等于全部海外军费。
- 【机制】蓝水市场是缓冲而非无限吸收器；未有1808废西王/拉美主权危机分支不能照搬史实开放时间。资源项目的实际量上限交B3/B5/E1；本卡只据其进口/替代与支付是否中断设置政治阈值。

## K3 本土军政征发上限
- 协调者2026-09-23确认B4已核Fortescue V pp.231–232：Moore/Richmond反对撤粮指令而该案放弃（文本 `downloads/c11_fortescueV.txt`）；为本项目已核材料转引。
- 【推演】地方财产与农业收成构成执行约束；政府可征发不等于可以无补偿、全地域、无时滞地搬空粮草。征粮引发的地方失合作会缩短中央抵抗期。

### K1/K2补核（避免口径滑移）
- 已读B2 `BoE_provenance.json`：源URL https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/a-millennium-of-macroeconomic-data-for-the-uk.xlsx ，v3.1更新至2016，2026-09-23下载，sha256 4c23dd392a498691eac92659aec283fb43f28118bd80511dc87fc595974195eb；B2用openpyxl data_only读取缓存而非重算公式。
- 已读旧C16 `trade_evidence.md` 第一至三节：Heckscher p.244解释real是declared、不是不变价；**报关地域仅Great Britain不含Ireland**，UK produce只是产品类别。因此本卡数值写‘大不列颠报关的联合王国产品’。p.245全球该类毛出口1810 £49.98m、1811 £34.92m；美国1810 £10.92m、1811 £1.84m；美国以外美洲含West Indies £15.64m→£11.94m。源系Heckscher转引Hansard XXII appendix1 cols.lxi–lxii，非本卡亲读海关账。
- Heckscher p.240：“exporters could not get payment from their South American buyers”；p.241回款往往为殖民地产物。装船额不等于售出/收款，不设海外能无限接盘。

## 撤粮范围纠正
本笔记所述B4交接的‘撤粮案放弃’现限于Fortescue叙述的1803-10-31某版广泛方案；新L7（Chilcott pp242–243，本卡已读）证明1803年11月地方仍规划迁人畜与给养路线。不得扩大为全部准备终止，也不能由规划推执行实绩。见notes_local_evacuation_correction.md。
