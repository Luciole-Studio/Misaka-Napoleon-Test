# F2提交后接口勘误（2026-09-23）

卡状态仍为done。本件是已交成果的限定性勘误和迟到材料登记，不重新开启资料搜集或改变任务范围。

## V77：20万人不是实际抵莫斯科的观测

B4指出歧义后，本卡重新核读doc `5b7b985b0f78`工具p13中印页64；本地 `downloads/pages/5b7b985b0f78.md`，Martin van Creveld, Supplying War（本卡原引用1977版），第二章。

原句（跨行空格合并）：
> Even if he were to arrive in the Russian capital with only one third of his original 600,000 men, taking sixty days to do so (in fact he took eighty-two) overall consumption during this period would have come to 18,000 tons for the men alone

以及：
> Furthermore, daily consumption in Moscow would have come to 300 tons, and to cater for this at a distance of 600 miles from base (assuming a very high performance of twenty miles per day by the supply columns) 18,000 tons of transport would have been needed.

【判定】20万人、60天行军、日耗300 tons是作者反事实算例；距基地600英里、20英里/日也是该算例参数。另一项往返60天是本卡 `2×600/20` 算术，与前句假定前进60天不能混作一次史实行程。此段未指定tons是否公吨。主模型采用1.5kg/人日只能写作按公吨近似归一的规划输入，不是实际发放配给。若原tons为英制长吨，该除算约1.524kg/人日；不据此断定本书一定使用长吨。50万人/12.5万马的2000公吨/日继续是本卡说明案，不因修辞校正改变兵员模型。

## 230m和350m为什么差120m

【模型接口】F4无盟约转移中心：750净经常收入−300非军/既有息养−25新增补偿−195海军=230m陆军余量，尚未扣另行储备。F2法国50万在册×700法郎成本代理=350m；相差120m/年。固定350m陆军时，陆海合425m的中心只余75m海军；要海军170–220m，需额外经常收入或可靠净转移95–145m，或等额减支。不是历史财政赤字观测。高收入另有盟约的300+195闭合案属于另一组输入，不能用来抹掉本组120m缺口。

## 外籍三口径

- Grab p26：1812俄征60万中过半non-French，战役国际军队，不能改成全国陆军比例。
- Elting第三章（本次重读doc工具p19）：“Napoleon had some 324,000 troops in Prussia and Poland, possibly a third of them Confederation of the Rhine and Polish troops.” 含医院2万、不含失踪/擅离等约2.5万。故为1807普波战区“可能约三分之一莱茵邦联与波军”，不是1812同分母。
- Houdaille印p49（本地 `downloads/pages/b4cf5e9825fc.md` L534–549本次重核）：为累计服役数、按1804前并合地区来源校正，111000莱茵、105000弗拉芒、69000瓦隆、104000意大利=389000；与1915000名1815疆界法国人合计后，还须扣An XII以前服役。不能把389000添入任一某日战区兵额，也不是1812非法籍军总数。

## PIG98：迟到来源，已读范围与暂不并表理由

Alain Pigeard, « La conscription sous le Premier Empire », Fondation Napoléon网页，F5来信标原刊RSN420(1998),pp3–20。实际读到版本：`downloads/pages/f1e37b9d69b9.md`，URL https://www.napoleon.org/histoire-des-2-empires/articles/la-conscription-sous-le-premier-empire/ 。本次读L1–152，涵盖制度、历次征令、E法令表和F旧法国表；未核Bulletin des lois原刊。

有用新锚：亚眠后军额作者报30万、30729份退休俸；正文有1813逐令构成，能进一步拆LAV的年度授权。但网页本身须保留冲突：
1. 同时写“3 germinal an XII (24 mars 1803)”——共和年和公历年不合，不能把网页日期全冻为已核原法。
2. 1805、1806法令日期正文与表内不同；E表排版流失导致额度与行归属不稳。
3. F表题为“par années (Ancienne France)”却列到1816，内有帝国提前调用年级；不能直接作为日历年实际入营序列。表中另列40000海军等范围，须与陆军调用分开。
4. 作者“Du 1er septembre 1812 au 20 novembre 1813, 1 527 000 hommes avaient été appelés en quinze mois.” 是来源所报，不是本卡复原后的去重实征；不拿来替换H72累计编入。按来信列项120000+17000+350000+180000+30000+280000+300000+40000=1317000，比作者1527000少210000；构成不能互相推得，不擅补缺项。E表另有45000而正文增额40000，需原法/表格对校。
5. “Effectif total appelé sous l'Empire 2 432 335 hommes”与开头“environ 2 200 000”不是本卡能静默合一的口径。
6. Pigeard制度叙述写“durée du service est de cinq ans”，与E97对和平四年的概述不合；须辨征兵义务年龄窗、实际服役与时期，未核原法律前不选一个消灭另一个。F2六年仍是1818制类比下的模型参数，不因该冲突改写为帝国法定役期。

【机制与结论】F5关于减额、兑现役期、教会合作改善合规，与F2和平路径相容。但“年征≤8–10万可无限期”“>20万/年12–18个月合规崩溃”是F5条件推演，不是该文识别的历史定律；还需年级、疆界、死亡、征免承诺和地方执法结构共同解释。F2不把单一réfractaire率用作全年训练到队s。此次不重建年度征令系列，原CSV保持来源降格/缺测状态。

【跨卡实质审计】已核F5定稿§4 E1/E2：E1用>20万门槛，结论先行用>30万，均附12–18月崩溃，口径未统一；E2把8–10万×6–7年约55–65万法籍，与该行55–70万总额含15–25万外籍也不一致。F2不采用该直接乘数。取s=.9、μ=.025的固定役期6–7年模型，8–10万年征约维持40.1–57.8万法国在册；本卡财政后的40–45万若按常退役1/6近似需年征约8.52–9.58万。几项军额包络可相容，但不能说社会层面已排除所有流量瓶颈。
