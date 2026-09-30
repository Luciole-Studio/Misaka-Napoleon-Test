# Q2引文与数字核查

以下核对是本卡阅读/定位记录，不是独立红队审查。

|引文或数字|原文出处|核查与限度|
|---|---|---|
|We define the draft dodging rate as the proportion of people effectively drafted who dodged the draft.|RP23 p1067；doc af39ee876dd3 PDF11|doc_verify字符916；hash b1a95740a51a4788d1883ec039d690355c244fac87a1d56574eae64dd7baf954|
|these data were not available for the Belgian, German, and Italian departments.|RP23 p1077 n33；PDF21|字符2329；hash 992d2d4d0c5e8b17cea6e481b41cf5152476fbbdf757a572d29670c4895c6db4|
|Certainly, the state got its conscripts, but the management of their supply was partly on Rhenish terms.|Rowe p178；doc efa2c87c4afb PDF192|字符94；hash 203413dbca64102898b092804a514053d0882bc91fded31f94952bf927860fb7|
|For this, no ﬁgures exist|Rowe p202；PDF216|字符543；hash 7853fa84a18cce23c289a202356ae24afd9125a36ecbe92b4938f03e4cb38982；限定无净流量数字，不是税额不存在|
|Rhineland mobilised9081/24186；draftdodgers2763/8138；deserters1203/725|Rowe Table3 p179，PDF193|文本+页图亲核；比较的是两期，不扩为省年|
|Roer paid11138406、旧制估6250000|Rowe p201，PDF215|文本亲读；作者转1803备忘录，非亲阅实收账|
|额外逃役2812／额外送军3256|RP23 Appendix p61，doc37023fec7ede|页图亲核；与正文逃役3256冲突，未假称作者代码已更正|
|je ne sache pas qu’il y en ait 500 de partis|Frasca p218，Persée正文e8dd4f1e586c.md|正文亲读；这是修辞截至时点，不当精确500入伍|
|Par contre en l’an XIII la levée a donné de bons résultats, sauf dans le département de la Sesia|Frasca p218|正文亲读；反例紧随其后，1806抵抗并未消失|
|皮埃蒙特35281+2682+280=38243|Frasca pp214/219|组件亲读后计算；p214印38242、p219印38243；不无声平账|
|1813一轮127433、12月底到营72265|Grab2013 p118，fc4c533d40d3.md|正文提取亲读，转Leggiere2007p69，不是亲阅原征兵账|
|1812并合地毛342260044、净226389345|MarionIV p321，PDF341|上轮本卡亲读并留notes；上下文预期非实收；不把预算净理解为对巴黎最终净资源|
|a guide to police activity than as a measure of public opinion|Forrest1989 p70|复用旧卡t_208a11/conscription_occupation_evidence.md中已核摘录；本轮读该笔记，未重阅原档；非新增独立验证|

## 本卡自校正
- RP23 Table1初次小图抄录的四处数字在逐行读p1074后已修正：logruggedness col3SE1.06111/Conley1.35414；距离Conley1.43014/1.90045；border col5=4.66339。CSV已重建。
- 模型初算“五年役期＋一年训练”多计一批受训兵，最终采用总五年含训练，只有四批受训兵；CSV/正文均按最终版本。此修正使低摩擦下端不再保证净正。
- 未把手工核验当统计或来源独立验证；未运行新回归，未跑统计LOOCV。
