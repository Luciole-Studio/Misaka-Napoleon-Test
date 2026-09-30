# Q2来源目录与阅读范围

仅列本卡实际使用或明确审计的材料。档案号为原作者出处谱系，不代表本卡亲阅。来源缩写用于CSV，每行含页码/口径。

|ID|书目与阅读范围|本地材料／定位|来源层级|
|---|---|---|---|
|RP23|Louis Rouanet & Ennio E. Piano, “Drafting the Great Army: The Political Economy of Conscription in Napoleonic France”, Journal of Economic History 83(4),2023,1057–1100，DOI10.1017/S0022050723000360；重点读印1065–1078、1088–1092；Table1页图核、数字复读|`downloads/Q2_Rouanet_Piano_2023.pdf`，doc `af39ee876dd3`，PDF页=印页−1056；HTML `downloads/pages/ee71889de366.md`|正式刊本亲读，未重跑复制代码|
|RP23A|上文Online Appendix，读pp4–7、26–27、51–52、61；p61页图核|`downloads/Q2_Rouanet_Piano_2023_appendix-1.pdf`，doc `37023fec7ede`，SHA256 37023fec7edebbad1b96936d302292c8fb23b2a289f680581fd4a1d8d095130c；`https://static.cambridge.org/content/id/urn:cambridge.org:id:article:S0022050723000360/resource/name/S0022050723000360sup001.pdf`|正式附录亲读；本地另有同内容文件，不计独立证据|
|R03|Michael Rowe, From Reich to State: The Rhineland in the Revolutionary Age, 1780–1830, Cambridge UP,2003；亲读pp178–181、200–202；Table3页图核|`downloads/D1_Rowe_From_Reich_to_State__49f41cfc7013.pdf`，doc `efa2c87c4afb`，PDF页=印页+14|复用D1下载、本文亲读；Table3转Vallée/Hargenvilliers与AN AFIV1124|
|F90|Francesco Frasca, “La conscription dans les départements piémontais de l’Empire français (1800–1810)”, Mélanges de l’École française de Rome. Italie et Méditerranée 102(1),1990,211–221，DOI10.3406/mefr.1990.4089；亲读法文正文211–221及相关脚注，两图未图核|`downloads/pages/e8dd4f1e586c.md`；`https://www.persee.fr/doc/mefr_1123-9891_1990_num_102_1_4089`|Persée正文提取；数量转原档案，非本卡直接阅档|
|W91|Stuart Woolf, Napoleon’s Integration of Europe, Routledge,1991；亲读pp74–77、87–90、156–164相关段|`downloads/D1_Woolf_Napoleon_Integration_Europe__35001edb4643.pdf`，doc `46acd720f176`，PDF页=印页+11|行政比较专著；不少兵役统计同源于Hargenvilliers/Lacuée|
|M25|Marcel Marion, Histoire financière de la France depuis 1715, tome IV, Paris,1925；亲读法文pp320–323|`downloads/F4_Marion_IV_1925.pdf`，doc `1f18be55f219`，PDF340–343；OCR `downloads/F4_Marion_IV_1925.txt`，doc `ecd835dcb3e0`；原下载`https://archive.org/download/histoirefinancir04mari`|原扫描亲读；p321为预算预期，AN AFIV1072仅转引；Mollien回忆录为回溯性且经作者转引|
|G13|Alexander Grab, “Conscription and Desertion in France and Italy under Napoleon”, in Napoleonische Expansionspolitik: Okkupation oder Integration?,2013,102–119，DOI10.1515/9783110293524.102；亲读pp102–104、108–109、115–119提取正文|`downloads/pages/fc4c533d40d3.md`；`https://perspectivia.net/servlets/MCRFileNodeServlet/pnet_derivate_00002421/Grab_Conscription.pdf`|公开正文提取；下载PDF原字节遭HTML响应，故不称已得PDF；其引Grab1995、Woloch、Della Peruta、Leggiere均为转引|
|F89|Alan Forrest, Conscripts and Deserters: The Army and French Society during the Revolution and Empire, OUP,1989，pp70–72|`downloads/pages/81f2084d72ce.md`；旧卡`nodes/r_b55f2c1cf5/cards/t_208a11/conscription_occupation_evidence.md`，doc `d4948d2bf64d`|本卡复用旧核读摘录：地域逃役与警力/民意区分；未重新阅原档|
|OLD10|旧制度因果审计，复用方法与来源线索，不继承旧“未识别”结论|`nodes/r_b55f2c1cf5/cards/t_f3c44f/c10_causal_evidence.md`及`SOURCES.md`；ACJR2011 doc8835f54b20f5，Buggle2013、Lecce–Ogliari等按旧卡层级|未新跑这些研究；长期城市化/信任不代替1800–13财政军役结果|
|AUDIT|本卡数据可比性/覆盖检查|`notes_method.md`；`Q2_validation.json`|研究者审计，不是历史材料|

## 复用接口及不重复计证
- D1：`nodes/r_5b1357a9c6/cards/t_40198e/notes_conscription_tax.md`用于定位Rowe/Frasca；本卡之后亲读其原文，不能将两卡算两份独立史料。
- F2：`nodes/r_5b1357a9c6/cards/t_0e763d/`的年度流量/可用库存/安全成本区分与既有“第10年净正”压力测试作接口。本文不将其3‰治安+1‰边防、60%可靠假设当实测。
- F4：`nodes/r_5b1357a9c6/cards/t_9f10b6/notes_marion_model.md`帮助定位财政表，之后亲读Marion。预算净额≠最终对巴黎净贡献。

## 未取得的关键材料（不当不存在）
1. Rouanet–Piano复制包：ICPSR175583，`https://doi.org/10.3886/E175583V1`。网页元数据Public/CC BY4.0可读，文件未取；公开HTTP路由403，未证明原因。未用登录凭据或绕过限制。脚本`retrieve_icpsr.py`和`raw/icpsr_landing.html`仅访问日志，后者是错误页。
2. Woloch1986原表、Grab1995原全文没有通过本卡渠道取得；已读相关后作转引，绝不写成两篇原文亲读。
3. 1800–13省级财政实收/应征/地方成本、统一军役原簿；司法案件/匪患/官员密度省年序列。可追查Vallée编Hargenvilliers、AN AFIV1123/1124、F9系列、各省收税账及Bulletin des lois。系列名只是后续路线。
4. 非英语要求：亲读法文Frasca、Marion两项；未取得第二种非英语语种的同口径实收/实到材料。德意档案和意文Della Peruta等主要经英法文转引，外推置信随之下调。

## 工具限度
ICPSR直取403；Monid未配置API key；Perspectivia原PDF下载收到HTML但正文提取成功。旧运行曾有上下文截断；本轮每次小段读取、随读写笔记。附件页图只核RP23 Table1、附录p61、Rowe Table3，不声称其余所有页图已目视核验。
