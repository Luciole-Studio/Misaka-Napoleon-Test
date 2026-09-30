# M1 来源核读摘录2：Monnet、Antipa、DFIH、Lloyd's

2026-09-23。本页随读记，原文件只以所列路径及页格引用。独立性：Monnet月度法债、BoE/Neal月末英债；Antipa英债研究引用Neal而非英债第二独立序列；Antipa agio 与其2013/2014 working papers彼此非独立；DFIH门户元数据不能与Monnet报价混充独立实际序列。

## 法国可计算月度序列
- `downloads/M1_tauxFrance1800_2015.xlsx`，Didómena https://didomena.ehess.fr/downloads/2227mq56p?locale=fr；SHA256 827092b8dd98f922e3901bb4b682a091829bacf595cfa109dc2a0b0171648ebb。母页面 https://didomena.ehess.fr/concern/data_sets/1v53jx639?locale=fr 说明 Levy-Garboua & Monnet, 2016, *Les taux d'intérêt en France: une perspective historique*, REF 121, pp.35–58；此表 `mensuel!A3:A194` 日期 `1800M01`—`1815M12`，`C`列 `TXLONG (long-term interest rates)`（值如 C39=9.362390454，1803M01；C43=9.534187374，1803M05；C72=9.346355749，1805M10；C73=8.515569034，1805M11；C93=6.680938870，1807M07；C168=8.125693326，1813M10；C172=11.191732718，1814M02）。这是收益率百分数而不是债券价格，更不是事件日现货。
- 方法原文 `downloads/M1_LevyGarboua_Monnet2016.pdf` doc ceab86f88d13，待读4–6页来源定义；在核读前不要确称每月收益率取自某一唯一5%券。

## 巴黎DFIH元数据／不当同一化禁令
- https://dfih.fr/issuers/100/securities （保存 `downloads/pages/e4e61b27e2fb.md`）列证券65 `5% JOUISS. DU 22 SEPT. 1851`，现货1798–1999；证券68 `5% CONS. JOUISS. DU 22 MARS`，现货1802-12-02至1817-09-01；证券13009 `5% CONS. J. DU 22 SEPT. 1818`，现货1809-03-15至1852-03-31。分别逐页 https://dfih.fr/securities/65 (`downloads/pages/ce5fba5d0919.md`)、/68 (`downloads/pages/e34ce1ee7054.md`) 已读。65的后期命名与早期起点不可当作同质连列。
- https://dfih.fr/securities/68/prices 与 /13009/prices (`downloads/pages/f5a0d0005f56.md`, `08dbd5566e75.md`)仅显示登录方可下载；https://dfih.fr/use (`downloads/pages/0cd45211a68f.md`)称未登录可见信息可引，但CSV账户界面开发中。没有拿到其逐日报价。
- https://dfih.fr/issuers/104/securities (`downloads/pages/561bc56ff575.md`) 识别法兰西银行股价证券63 `BANQUE DE FRANCE (ACTIONS DE LA)` 元数据1801-10-26至1945-12-17；无可下载报价，不能报价格变化。DFIH 1807 doubled shares另列105214，比较须控增资权益。

## Antipa 2016（独立论文、复用Neal英国债券）
- Pamfili M. Antipa, ‘How Fiscal Policy Affects Prices: Britain's First Experience with Paper Money’, *JEH* 76.4 (2016), 1044–77, DOI 10.1017/S0022050716000978；完整版 `downloads/M1_Antipa2016_JEH.pdf` doc 52a1e16a8dad，网页全文 `downloads/pages/ceba572cafc2.md`，https://www.cambridge.org/core/journals/journal-of-economic-history/article/how-fiscal-policy-affects-prices-britains-first-experience-with-paper-money/4EB0EEBFB77E80F4C03734D27EFB4407 。网页‘Interest Rates on Public Debt’（本地行378–420）明确：‘The agio did not fluctuate between May 1802 and October 1808 ... Data are available until October 1805. For the period spanning the years from 1805 to 1808 the agio's stability simply reflects the lack of observations.’ 务必不能把缺报误写作市场无反应。
- 该文Figure 7和Table 5，PDF p28（印页1071）为1250项1805–08日度consol收益率的Bai-Perron断点，不等于我们拿到日度报价：1805-11-14断点（特拉法加伦敦消息11-06已到、期待普鲁士参与）收益率均值5.10%→4.95%；1806-06-14（谈和）4.95→4.74；1806-10-08（谈判破裂，随后耶拿消息）4.74→4.93；1807-01-29（1807预算信号）4.93→4.78；1807-11-12（英Orders in Council）4.78→4.69；1808-04-14（原始盈余预算公告）4.69→后均值未在表中展示、正文说4.5%。这些是断点**区制均值**，不能冒充前后1日回报。PDF原表的1806-06-14信赖区间印有1805年，显系年号排印错误，不擅自修订。
- 网页脚注12（本地行460）原句：‘The absence of any sizable departures from the increasing trend in the stock price casts doubt on whether financial markets perceived the threat of French invasion as an imminent one.’ 谈英格兰银行股票，不能推断伦敦完全无入侵忧虑。
- 本文详细引英国伦敦消息日期：特拉法加1805-11-06（正文），西班牙首都陷落1808-12-04，伦敦12-19才知（本地行340附近），故按消息日而非战役日。该文的agio是**英国纸镑对金价溢价**，绝不是汉堡银行货币agio。战费预期、英国纸币金值与主权存亡概率不等价。
- 同作者2013/14 working paper `downloads/M1_Antipa2014_fiscal_sustainability.pdf`, doc 27a81e006bc2，不能和2016论文当两份独立证据。

## Lloyd's 一月生存保险：补充但不泛化
- Charles Wright & C. Ernest Fayle (1928), *A History of Lloyd's*, 原文University of Illinois OCR `downloads/pages/00bd118bdd34.md`，https://brittlebooks.library.illinois.edu/brittlebooks_closed/Books2009-09/wrigch0001hisllo/wrigch0001hisllo_ocr.txt ；图版目录印p.xvi载‘POLICY ON LIFE OF NAPOLEON, 1813 ... Issued 21 May, 1813, to pay a loss “in case Napoleon Bonaparte shall cease to exist or be taken Prisoner, on or before the 21st day of June, 1813.” Premium, three guineas per cent.’ 图版face p96。更早《Ships and Shipping》第16章 https://kellscraft.com/ShipsandShipping/ShipsandShippingCh16.html (`downloads/pages/9058a83137c2.md`)转录合同：3 guineas / £100，签署£100 R. Heath、£150 A. F. Kemp、£150 B. I. Mitchell。该保单给*死亡或被俘并集*、21 May–21 June 1813的**个别underwriter毛保费3.15%/保额**，不是拿破仑政权1848存续概率，更不是全市场均衡价格；载有保险费开销、承保风险溢价及违约风险，不得当作精确风险中性概率。注意两来源共享同一底层保单，不构成独立互证。

## 优先的反证
对英国耐战力假说，不能仅从BoE月末未剧烈波动推定；Antipa日度断点显示英债反应确实对外交、预算、海权政策敏感但幅度有限。若用户所谓‘大陆失败反应弱’，必须对提尔西特、埃尔福特、1809、1812等日期用同频英国收益率和消息到达窗口检验，并以可比安慰剂（月末相同跨度）衡量。
