# A6 笔记01：downloads 逐文件检索方法与初步结果（2026-09-26）

## 方法
- 285个顶层文件按"著作组"归并（同书pdf/txt/epub、页图png归同组），共约190组；每组设拉丁作者名+中文译名+题名关键词正则，逐行grep合稿（5179行）；统计命中行数、其中脚注行数（以"[^"开头）、分布章节。
- 已剔除的假阳性（语境核读后修正）：戴维(Davey)≠戴维斯(Davis)；Ralph Davis(英格兰银行A41)≠John A. Davis；"卡里卡尔"≠Cary；"波特兰"≠Porter；"波韦斯"≠Weis；"戈登—墨菲"≠Stewart Gordon；"托恩(John Lawrence Tone)"≠Mark Lawrence；"贾吉尔"≠Gille；"毛利文/意大利文"≠利文；"Censorship"≠Censo；海地1805年宪法≠意大利1805章程；"Gregory Fremont-Barnes"≠Desmond Gregory；立法团特别委员会≠EIC Select Committee；1806 Negociation with France≠1812 EIC Negociation。
- 研究卡引用：扫描 nodes/ 下5350个文本文件中出现的下载文件名（dl_card_refs.json，scratchpad）；.pageindex/meta.json 的 task_ids 给出抓取卡。
- pages/ 918个网页：以 source_url/final_url 在合稿中查URL（117页被URL引用）；对218个与大陆/外交/省化相关标题页另设中文主题键核对（pagekeys）。

## 零引用（书稿0命中）的顶层著作组（按与三块相关度粗排）
高相关：A_Jobst_Kernbauer(奥地利银行货币国家)、A_Kaps(哈布斯堡贸易统计)、NL_Verheijen(荷兰1801–13党争与建国，博士论文314页)、PR_Takaoka(柏林国民军)、PR_HGIS(普鲁士疆域行政)、B1_Chambray(1812波兰问题)、c12_Makarov2024(俄文)、D1_Broers_Politics_Religion(意大利宗教政治=抵抗机制)、EG_Driault_Crise1839–41(东方危机)、PS_Aitchison(波斯/信德条约集)、X1_Wolff/Ouvrard(乌弗拉尔与西班牙白银——外交财政)、X1_Ziegler(霸菱)、X1_Gille(罗斯柴尔德)、X1_Herries(英国对大陆补贴与军需)、f1_Mollien(财政部长回忆)、f1_Roederer(拿破仑谈话实录)、f1_Lavalette(驿政/情报)、IT2_LeBrethon(缪拉书信集3卷)、IT2_Colletta(那不勒斯史)、IT3_Haussonville(教会与帝国)、IT3_Sanhedrin(犹太大公会)、SP2_Portillo(大西洋危机)、B6_WilsonAD(英荷帝国子午线=荷兰殖民地)、B6_GregoryMed(英国地中海岛屿)。
中低相关：F4_Juglar、F4_Oosterlinck、E1_Tooke、E1_OWID、E1_WardeKander、E1_Porter、E1_NunnQian、M1_Leonard、M1_LlorcaJana、M1_LevyGarboua(实为错误下载：Kotz & Le Cacheux文)、P4_Glete、P8_OBrien、c16_Navickas、c5_Sanchez、c8_Maras、c9_Cretet、f1_GouvernerNaples、f5_Senat、Tetlock、IN1大部分议会文书、IN2_Compton/Malleson、SA_Depons、SA_Sassenay(实为Gallica验证码页，无内容)、MX_Hidalgo。

## 只被浅用（1–2行）的高相关著作组
SC_Glenthoj(1，仅书目)、G2_Schmidt(1，仅附录E一封信)、c18_Czubaty(1)、PL_Filipiak(1)、c12_Troshin(1)、R1_Czartoryski(2)、R3_Riehn(2)、NL_Joor(2)、SC_Barton(2)、PR_Murau(2)、CH_Mediation(2)、CH_Capitulation(2)、D2_Madelin(1)、IT2_EsdailePR(1)、f1_Metternich(1)、c11_Corbett(1，仅为汉诺威外交转引)、OT_Puryear(1)、IN2_Cooper(1)、X1_Assereto(1)、R1_Vandal(3，其中1处在东方章)。

## pages/ 中未入书的外交/大陆一手或专题页（主题键0命中）
1808埃尔福特对英和平提议往来文书(5084a8cc6d63/de8523a58eb6)；并合省总督府制度(748b696ca1ca)；瓜分奥斯曼方案1807–12(8304138e1ae4)；普鲁士1810财政敕令(a0a178c08a7e)；库拉金1808–09俄外贸(aab94e1f905a)；法俄外交1810–12(bfa7029b08dc)；"波兰王国复国"1812同时代期待(ce13bc8c21a9)；古利斯坦条约(fdd97c5429ee)；1811匈牙利议会与贬值(9a8e1d55620d)；1813奥军再评估(848ad5b3b9ea/d5c627631093)；哈布斯堡与英国外贸比较(7b11d8a7dad4)；符腾堡国王(LEO-BW，4e950a03a636)；莱茵邦联成员表(cde736773ad3)；威斯特法利亚货币(a5357a9d2c1c)；贝格民法典(4fa9933e2508)；AHAD大陆封锁行政(f8bbb3026c57)；Grab征兵与逃役(899384be0eda)；欧洲人面对征兵(ab6a44ffb405)；国务会议1811征兵建议(43dacbcb242e)；塔列朗致拿破仑书信(d95f216d7fd1)；英国战略外交1806–15(06336e780629)；Hosking(83fff8e6b841)；俄国贵族西化成本(f4d2943372ac)。
