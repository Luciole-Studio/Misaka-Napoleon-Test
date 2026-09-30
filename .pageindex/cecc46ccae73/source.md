# B2 来源、阅览层级与复核说明

对应《B2_britain_fiscal.md》；Sister 10041；2026-09-23。除另注，所有网页均为项目实际取得并复读的正文捕获，不把网页检索摘要当文献；缓存内保留source_url、final_url、文本摘要哈希。页码指作者印刷页，Hansard用卷/栏。PDF或书籍的网页抽取未必覆盖全书，本卡只对下列所列段落负责。

## 一、主数据

### D1　Bank of England, *A millennium of macroeconomic data for the UK*, version 3.1

- 官方说明：https://www.bankofengland.co.uk/statistics/research-datasets 。页面明确v3.1更新至2016；缓存`downloads/pages/bd9fbfa5c4e0.md`。
- 官方工作簿：https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/a-millennium-of-macroeconomic-data-for-the-uk.xlsx 。2026-09-23下载；`downloads/B2_BoE_millennium_v31.xlsx`，27,533,690 bytes。
- 原件SHA256：`4c23dd392a498691eac92659aec283fb43f28118bd80511dc87fc595974195eb`。
- **读取层级：**直接读取官方xlsx缓存值；原件Office工具因解压部件总和超过64MiB被拒，不是下载失败。本卡用openpyxl的read_only/data_only抽选工作表，并保留原表名和坐标，所得`BoE_selected_cached_values.xlsx`成功回读；没有擅算原工作簿未缓存公式。已检查主要原公式对应关系，但不是对历史档案的独立重新编纂。
- `extract_boe.py`、`BoE_provenance.json`记抽取过程；元信息完整性检查无缺项只说明字段齐全，不证明统计口径毫无争议。

**承重位置及来源谱系：**

|工作表|使用列／位置|口径与限制|
|---|---|---|
|A27. Central govt borrowing（原表名有尾空格）|右侧AR年、AT支出、AV利息、AW收入、AY净盈余、AZ初级盈余；原财年A/B及AA所得税分类|GB 1688—1801、UK 1801后为源表标识；早期转录Mitchell, *British Historical Statistics*（1988）, pp.575—593；1946年前Exchequer/Consolidated Fund，不是现代公共部门净借款|
|同表历年转换|1815在第139行，AW139=79.1、AV139=32.2；早期例AV117=0.75*H116+0.25*H117|财年到日历年加权由源作者实施，不是本卡补值。税目AA的年份仍是原财年，不跟着右侧历年转换|
|A29. The National Debt|AN年、AO综合债务、AP/GDP比；Y funded+unfunded汇总、AB期限年金资本估值|GB+Ireland合并、年金及估值/日期调整须同时说明；不是单独funded debt，不是市场值|
|同表1815|AO133=D133+L133+H133+V133+AB133；AB经A30c期限年金表|原债务公式包含年金资本值，不能拿它减现金赤字而称数据错误。没有单列年金的后期本卡不自行估值|
|A9. Nominal GDP (A)|P列历史疆界市场价格名义GDP及相关notes|不是现今固定UK疆界；反事实没有采用史实GDP作新世界精确分母|
|A31. Interest rates & asset ps|A年、T consol长利率；1797/98 T117:T118，1810/11 T130:T131|年平均二级市场收益率；不等于新债认缴现金票息，更不等于存量债务平均成本|
|M10. Mthly long-term rates|年/月、C raw consol、K spliced；源注明Neal（1990）|月末而非月平均；仅抽取1809—12共48个观测，不作为独立封锁因果估计|

**派生式：**现金赤字=总支出−收入；非息支出=总支出−利息；初级盈余=收入−非息支出；债息/收入=利息÷收入×100。数字单位£m名义值，未作通胀调整。年度样本1793—1848（含端点56行），缺失值留空。终检确认56年债务及年金组件均有源值，撤销早稿“1834年后无独立年金分列”的错误说明和未触发的置零后备分支；没有把缺失年金填零。

### D2　Bank of England, *Annual data on the Bank of England's balance sheet*, 1696 onwards

- 官方xlsx：https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/annual-data-on-the-boes-balance-sheet.xlsx 。本地`downloads/B2_BoE_balance_sheet.xlsx`；SHA256 `86121aeb2c91bcf8f6b277f1c80b1d6ffb7b5947b353d9a8b467dd435dc50589`；doc_id `86121aeb2c91`。
- 使用`A1. Bank of England B'Sheet`，A年、O Coin and bullion、S Notes in circulation；1791为101行、1797为107行、1810为120行。
- **实际阅览：**官方表格及表头/说明；单位£m、银行自身而非全英货币存量。1844以前为2月底，不是年平均；银行金银不是“英国全国黄金”。
- 限度：1699—1806硬币与银行所持票据的拆分沿用Smee估算；微小末位不代表真实盘点精度，见D3。

### D3　Bank of England, “Bank of England liabilities and assets: 1696 onwards”, *Quarterly Bulletin*, 1967 Q2, pp.159—163，附Table B

- URL：https://www.bankofengland.co.uk/-/media/boe/files/quarterly-bulletin/1967/boe-liabilities-and-assets-1696-onwards.pdf 。缓存`downloads/pages/5a55e6aeac33.md`。
- 定位：The present series段、日期表、Table B；缓存行75—138附近。
- 表述：“1766–1844 … End-February balance sheet”；1810纸币£20,120,486、金银£3,501,412。与D2同谱系，不是独立第三套观测。
- 明确说1806前cash未区分硬币与票据，采用现金中£9,000—10,000为硬币的估算。没有把这个不确定性删除。

## 二、同时代议会材料

Hansard是后期整理的当时议会发言记录，本卡读电子正文，不声称亲查手稿或原印张。财政大臣叙述、反对派判断和决议数值应按各自地位引用。网页OCR有断字、错位，下面只使用可明确辨认的段落；对错字不静默修出新数字。

|代号／正式出处|读取定位与所支持的窄主张|URL及保留件|
|---|---|---|
|H1　“The Budget”, HC Deb 20 May 1811, vol.20, cc210—223|cc210—211借款须议会认可及获准拨款；cc213—214净评定、实收、欠税；cc214—216股票组合、现金票息、偿债基金和管理费；cc216—223税种与棉花替代争议|https://api.parliament.uk/historic-hansard/commons/1811/may/20/the-budget ；`downloads/pages/bff7e2ccf088.md`|
|H2　“Separate Charges”, HC Deb 14 June 1815, vol.31, cc799—822|cc801—804贷款组合；cc805—807旧欠款及陆转海；cc809—813 Tierney批评支出估计。最重要：财政大臣承认欧洲安排后可转军费，不证明他赞成法国霸权或其节省预测一定实现|https://api.parliament.uk/historic-hansard/commons/1815/jun/14/separate-charges ；`downloads/pages/156d03703582.md`|
|H3　House of Commons, *Report, together with minutes of evidence, and accounts, from the Select Committee on the High Price of Gold Bullion*, 8 June 1810|**实际只读引言和结论的节录**，原报告pp.1—2、30—33；金条/金币、成色、可出口法律差价，及“两年后恢复”。不是完整证词集|World Gold Council保存的史料节录：https://www.gold.org/sites/default/files/documents/1810jun8.pdf ；`downloads/pages/523f4560156c.md`|
|H4　“Ways and Means”, HC Deb 28 March 1806, vol.6, cc573—586|cc576—578所得税到10%、银行代扣债息税；是提案讨论与制度交叉核验，非最终审计收入|https://api.parliament.uk/historic-hansard/commons/1806/mar/28/ways-and-means-1 ；`downloads/pages/d34063b29aef.md`|
|H5　“New Plan of Finance”, HC Deb 29 January 1807, vol.8, cc564—593|c567旧补贴欠款与有条件新增分开；c568税收评定预测；c580剔非经常补贴。表中部分贷款数字OCR错，主文12.2m可辨；1815数字是当时预测不是实绩|https://api.parliament.uk/historic-hansard/commons/1807/jan/29/new-plan-of-finance ；`downloads/pages/995bd30de2bb.md`|
|H6　“The Budget”, HC Deb 12 May 1809, vol.14, cc530—553|cc530—537海军拨款、奥方汇票；cc541—542未经授权、支付能力和汇率约束；后续有支持及反对援助者|https://api.parliament.uk/historic-hansard/commons/1809/may/12/the-budget ；`downloads/pages/1170b6cb87a9.md`|
|H7　“Finance Resolutions”, HC Deb 20 June 1809, vol.14, cc1131—1159|决议15，表头Net Produce of the War Taxes，Property Tax截至4月5日年度；1807/09总计与分项未对平，**只用单项**|https://api.parliament.uk/historic-hansard/commons/1809/jun/20/finance-resolutions ；`downloads/pages/d79be65764b5.md`|
|H8　“Commercial Credit”, HC Deb 11 March 1811, vol.19, cc327—350|cc332—333救助授权6m、有担保及偿还条件；cc338—341 Huskisson认为缺好票据而非单纯缺发行；政府与反对者归因不同|https://api.parliament.uk/historic-hansard/commons/1811/mar/11/commercial-credit ；`downloads/pages/3b8b8e348c6d.md`|
|H9　“Economy and Retrenchment”, HC Deb 27 June 1821, vol.5, cc1345—1442|cc1349—1351、No.3利息表；明确December年末、UK公众利息及管理费、不含Sinking Fund、引Annual Finance Accounts。本卡没有亲读该原账|https://api.parliament.uk/historic-hansard/commons/1821/jun/27/economy-and-retrenchment ；`downloads/pages/95e29ff1c015.md`|
|H10　“State of the Public Finances”, HC Deb 9 July 1817, vol.36, cc1336—1365|末尾Grant决议1—4：2月1日funded与1月5日unfunded不同日；短债分项相加与公布合计差£5。前文收入下滑而股价上涨的争论，不能把市价当税收现金|https://api.parliament.uk/historic-hansard/commons/1817/jul/09/state-of-the-public-finances ；`downloads/pages/29727e560586.md`|
|H11　“Report of the Bullion Committee”, HC Deb 9 May 1811, vol.19, cc1151—1169|末栏第一项75∶151；第16/最后项45∶180。没有把两个表决配反|https://api.parliament.uk/historic-hansard/commons/1811/may/09/report-of-the-bullion-committee ；`downloads/pages/de17c8036944.md`|
|H12　“Report of the Bullion Committee—Adjourned Debate”, HC Deb 7 May 1811, vol.19, cc919—1012|cc919—920最后项是实际建议，c955说明两年后。未另得第16项完整逐字提案，故不伪造其全文|https://api.parliament.uk/historic-hansard/commons/1811/may/07/report-of-the-bullion-committee ；`downloads/pages/c2fda522376a.md`|

**补充已读但不承担主线定量：**

- “Army Estimates”, HC Deb 4 March 1811, vol.19（使用c191、cc195—196、211—213、225以后），`downloads/pages/eff6555b7abe.md`：民兵训练21→14日、省0.110m；志愿军减少0.303m部分为当年不发衣，非永久撤半岛战争红利。减陆保海为当时政治选项，但Canning有牵制法国的反论。
- “Issue of Exchequer Bills for Purposes of Local and Temporary Relief”, HC Deb 28 April 1817, vol.36, cc27—48，https://api.parliament.uk/historic-hansard/commons/1817/apr/28/issue-of-exchequer-bills-for-purposes-of ，`downloads/pages/29931d6389d2.md`：回顾1793/1811先例，未提供本卡可用的1811实放审计额。

### 关键引文审查表（可供红队抽核）

引文是其发言/文本内容的证据，不自动证明发言者对经济因果的解释正确。

|编号|原文|来源定位|使用与防误读|
|---|---|---|---|
|Q1|“subject to the approbation of parliament”|H1，c210开篇|说明借款合同有议会许可条件，非泛称议会随时一致|
|Q2|“Last year the interest was 4l. 4s. 2d. per cent.; this year it was 4l. 14s. 11d.”|H1，c216|特定新增贷款现金票息比较，不是全部旧债调息|
|Q3|“For each hundred pounds subscribed … 100l. in the 3 per cents, reduced, 20l. in the consols, 20l. in the 4 per cents, and 6s. 11d. in the long annuities.”|H1，cc214—215；省略仅连接前后同一段|3+0.6+0.8+0.345833=4.745833；分期折扣与市价bonus另算，不称完整IRR|
|Q4|“4,864,267l. had been received”|H1，c214|当期11.8m净评定中的已收部分，不能把评定全当现金|
|Q5|“that expense now incurred for our armies would cease, and the supplies at present demanded for them could be applied to the service of our navy”|H2，c807|以法国与大陆列强达成安排为条件；不是从此英国所有陆军费用皆为零|
|Q6|“the numbers of persons returning from long voyages and claiming the arrears due to them, had made larger disbursements necessary”|H2，c807|裁撤和减员初期可能增现金开支，迫使模型承认滞后|
|Q7|“to grant relief to the extent of six millions, not with the supposition that that sum would be required”|H8，c332|授权上限非实际拨付；同段2.2m是1793，不是1811|
|Q8|“The Bank of England had now to complain, not that they had no funds with which to discount, but of a deficiency of good paper to discount.”|H8，c338，Huskisson|与“全是流动性冲击”竞争的同时代判断|
|Q9|“should the state of Europe continue to require it”|H5，c567|仅有条件新增补贴0.5m，不用作拒偿旧欠1m依据|
|Q10|“if it was to be done at all, it must be done with the consent of parliament”|H6，c542|奥方擅开英方票据不生无限财政权|
|Q11|“cannot safely be removed at an earlier period than two years”|H3，原报告结论pp.30—33|建议两年后恢复，不是编辑导语所谓立即恢复|
|Q12|“The Committee then divided on the first … Ayes 75—Noes 151”; “on the 16th, or last Resolution … Ayes 45, Noes 180”|H11，c1169；两段分别节引|第一项与最后项表决分开，不伪造同一连续引文|
|Q13|“not to enable Houses who have failed to compromise or settle with their creditors”|L6，先行版p.23，转引C.D. 28 February 1811 pp.521—522|特别贷款有偿付能力筛选；本卡未亲见董事会档案|
|Q14|“£.3.17.10½. per ounce of standard fineness”|H3，原报告p.1|铸币标准价而非市场现金价；黄金溢价和纸币折价分母不同|

Q3/Q12的省略号为编辑节录，不伪称连续原句。正文短引不含省略时均对应可直接找到的词串。

## 三、实际使用的研究文献

### L1　Michael D. Bordo and Eugene N. White, *British and French Finance during the Napoleonic Wars*, NBER Working Paper No.3517, November 1990

- 完整PDF：https://www.nber.org/system/files/working_papers/w3517/w3517.pdf 。`downloads/B2_Bordo_White_WP3517.pdf`；doc `ed2c1913a953`；SHA256 `ed2c1913a953d70e4ac436da4aea5a895a7c80fc0aaa0d714d12b086920d2800`。
- **版本必须写工作稿1990**。1991 *Journal of Economic History*正式刊本本卡没有核全文，不能套用其分页。
- 已读：摘要、英国信誉及限制期/税收平滑部分，印刷pp.17—25；表2（p.51，PDF物理p.53）与表3（p.52，PDF物理p.54）已旋转放大看图，不依破碎OCR。
- 表2为GB净收入而非D1的UK财政序列；源列Gayer–Rostow–Schwartz。1810/1811净收入约68.39/66.53，债务负担23.40/23.86；细末位使用“约”而非装作现代统一统计。
- 表3纸币行源注明Mitchell & Deane（1962）p.442；1810可稳读约22—23m，与D3严格2月底20.120486不同，末位和日期仍不作统一冻结。**终检撤销先前22.32的精确抄值，疑有邻年错位；主CSV不使用这套表3纸币数**。
- 看图件：`BW_table2.png`、`BW_table2_right.png`、`BW_table3.png`、`BW_table3_right.png`、`BW_table3_1810_1811.png`、`BW_table3_1810.png`，均在本卡目录。裁图不增加原影像信息。
- 论证用途：信誉有助财政平滑；作者自己强调宏观收入基准稀疏，检验只具提示性。本卡不把该理论当英国无条件长胜定律。

### L2　Patrick K. O’Brien and Nuno Palma, *Danger to the Old Lady of Threadneedle Street? The Bank Restriction Act and the regime shift to paper money, 1797–1821*, EHES Working Paper No.100, July 2016

- URL：https://ehes.org/wp/EHES_100.pdf 。`downloads/pages/a2034fc310ff.md`。
- 阅读§§1、2.3、3.1、信誉与支付网络论证；1797商人接受声明和法律日期经作者转引；**未将2020正式刊版分页当成本稿分页**。
- 与L5均部分引用Clapham，不能数作两套独立危机原始观察。

### L3　John F. Avery Jones, “The Special Commissioners from Trafalgar to Waterloo”, in John Tiley (ed.), *Studies in the History of Tax Law*, Vol.2, Oxford/Portland: Hart, 2007

- 实际读到出版社样章开头历史节、注6—29，尤其21—25；全章从p.3起，个别抽文页界缺失，以注号及文本定位，不虚构每条单页。
- URL：https://api.pageplace.de/preview/DT0400.9781847313461_A24074261/preview-9781847313461_A24074261.pdf 。`downloads/pages/ea9175ba3158.md`。
- 支持：税率1799 10%、1803 5%、1805 6.25%、1806 10%；扣缴不是1803首次出现；1806税制成为1842基础；委员会和地方征管。
- £6,046,624与£5,341,907明确**转引1870 Commissioners of Inland Revenue年报**，是“raised”而未完成现金/评定原表桥接。同章“almost twice … half the rate”与注21不一致，弃用其倍率；1806£12,822,056脚注年界不明，不冻结成1806现金。

### L4　K.O. Cousins, “The failure of the first income tax: a tale of commercial tax evaders?”, *Journal of Legal History*, 39(2), 2018, pp.157—186，接受稿

- DOI：https://doi.org/10.1080/01440365.2018.1484325 。实际稿件：https://eprints.whiterose.ac.uk/id/eprint/129898/19/The%20Failure%20of%20the%20First%20Income%20Tax-A%20Tale%20of%20Commercial%20Tax%20Evaders_.pdf 。`downloads/pages/dc631b5476f4.md`。
- 定位§III.1及注121—128；1799约5.8m、净评定/征收费的分别。正式刊页范围只是题录，不冒充接受稿对应单页。
- 用途：辨别actual yield、净收益不必为同年度财政现金；商业逃税与征管改进不能只用税率解释。

### L5　Pamfili Antipa and Christophe Chamley, *Monetary and Fiscal Policy in England during the French Wars (1793–1821)*，October 2017稿

- URL：https://people.bu.edu/chamley/Ec365-17/UKFR.pdf 。`downloads/pages/cf02c798c3f0.md`。
- 定位：§2，pp.6—7（融资工具与偿债基金）；pp.17—19（1797）；pp.25—27及战后讨论（银行购买国债、付息支持、短长转换和恢复兑现）。
- 不混同后来的“Regimes of …”2019版本。
- 用途：货币财政政策不断调整，暂停兑付并非取消国债付息。战后还BoE的£10m约为银行所持政府短债55%，不是全国国债55%；短转长不是等额净还本。
- 学术分歧：作者认为战时Sinking Fund有承诺和稳价功能；这可以与“借新债购旧债不等于净减债”的会计命题同时成立，不能把二者混成全有用或全骗局。

### L6　Carolyn Sissoko and Mina Ishizu, “Preventing financial ruin: How the West India trade fostered creativity in crisis lending by the Bank of England”

- DOI：https://doi.org/10.1111/ehr.13407 。实际PDF链接：https://researchonline.lse.ac.uk/id/eprint/126278/1/The_Economic_History_Review_-_2025_-_Sissoko_-_Preventing_financial_ruin_How_the_West_India_trade_fostered_creativity_in.pdf 。`downloads/pages/2f4fc6ec5d53.md`。
- **双日期说明：**所读正文为2025网络先行分页（1起，页脚2025下载印记），仓储封面更新题录为*Economic History Review* 79(1), 2026, pp.57—88。正文引用pp.23—24是先行分页，不把它与57—88混用。
- 定位§IV The 1811 policy of emergency lending、注117—123、§V结论。
- 实际档案谱系：BoE Court of Directors Minutes（文内C.D.），1810-02-15 p.219；1811-02-28 pp.521—522；以及Committee of Treasury minutes。**全为转引，不冒称直接读取档案。**
- 支持担保、检查人回避、暂时不流动但有偿付能力的甄别；注123明言成效未定且1816追款，问题贷款是否均发生于新制后不明。故不能将追款直接归咎新制度。
- 用途：信用救助与西印度奴隶商品网络紧密相连，既非完全市场自发，也非无差别公共保全。

### L7　W.H. Chaloner, review of François Crouzet, *L’économie britannique et le blocus continental (1806–1813)*（Paris: PUF, 1958）, *Revue belge de philologie et d’histoire* 38(2), 1960, pp.525—526

- 正文：https://www.persee.fr/doc/rbph_0035-0818_1960_num_38_2_2317_t1_0525_0000_2 。`downloads/pages/e5b32951df65.md`。
- **实际读的是英文书评，非Crouzet法文两卷原著。**书评法语转引Crouzet p.855：“… le Blocus Continental fut à l’origine de la crise de 1810 … [et] des difficultés monétaires … qui gênèrent sérieusement son effort de guerre”。该段可证明Crouzet的解释内容，不单独证明全部因果。
- 用途：补足英语传统低估封锁成本的反论；书评还保留Crouzet对工业活力和英国抵抗基础的强调，不能稻草人化成“主张英国马上破产”。

### L8　Larry Neal, “The Financial Crisis of 1825 and the Restructuring of the British Financial System”, *Federal Reserve Bank of St. Louis Review*, May/June 1998, pp.53—76

- DOI及正文：https://doi.org/10.20955/r.80.53-76 。`downloads/pages/004521d1e27f.md`。
- 使用“The Shock: From Wartime to Peacetime Finance in 1821”、1825危机及重组各节；网页无稳定单页边界，给节名而非伪造单页。
- 支持：所得税废除改变息收关系；货币紧缩与债务管理冲突；1825商业危机及之后银行/票据市场改革；1830重新贴现功能。
- 作者称1816所得税14.6m且约gross income20%，本卡不把这20%误写成债息/收入；与D1财年1815/16年界保留对账缺口。

### L9　Eli F. Heckscher, *The Continental System: An Economic Interpretation*, edited by Harald Westergaard, English text mainly translated by C.S. Fearenside, Oxford: Clarendon Press, 1922

- 实际读英译本相关节：国际支付与补贴pp.350—357、相关前后论证；未称读瑞典语原版。URL：https://oll-resources.s3.us-east-2.amazonaws.com/oll3/store/titles/327/0142_Bk.pdf 。`downloads/pages/70cc6a857e5f.md`。
- p.353补贴约14.722m依Porter/Tooke，OCR英镑符号常转成美元形状，**只作约数和机制支持，尚未以原影像冻结末位**；p.67亚眠前约14.3m又含贷款，不能相加。
- pp.354—355：以大陆开英财政部汇票与经Rothschild买现有当地资产的机制区别；Herries关于1813约0.7m票据采购**经Heckscher转引**；未亲阅Herries报告。
- Rothschild“经法国送金”为多年后对Buxton的口述（书中引1849第三版回忆录），**回溯性**，不是可独立核账的同期付款清单。
- 作者判断支付障碍主要为组织问题；本卡明确限制其外推，不认为真实资产/海运/汇率约束全部取消。

### L10　Leandro Prados de la Escosura and Carlos Santiago-Caballero, *The Napoleonic Wars: A Watershed in Spanish History?*, EHES Working Paper No.130, 2018

- URL：https://www.econstor.eu/bitstream/10419/247060/1/ehes-wp130.pdf ；永久入口https://hdl.handle.net/10419/247060 。`downloads/pages/769e05da23c9.md`。
- 定位Finance小节、图12前；英援西班牙1808—15 7.8m，**转引Sherwig pp.362—368**，包括money, weapons, supplies；与1854 Parliamentary Papers另计5.2m并列，不混为现金、更不相加。
- 这里只用援助口径，不将西班牙贸易或人口全部模型搬入英国。

## 四、已阅辅助材料与未亲得原书

### 已阅但不应误充主序列

- **Patrick K. O’Brien**, “The Political Economy of British Taxation, 1660–1815”, *Economic History Review* 41(1), 1988, pp.1—32；https://www.jstor.org/stable/2597330 ，所读公开稿http://slantchev.ucsd.edu/courses/ps143a/readings/O'Brien%20-%20Political%20Economy%20of%20British%20Taxation,%201660-1815.pdf ，`downloads/pages/bb07a813031b.md`。已读表1—3与表注。**表2的1810=五年均值、1815=三年均值；不是单年58.25/62.67**。其税款为Exchequer净流入且疆界困难、国民收入代理另有范围差。用于口径防错，不作D1分母。
- **Max E. Rossiter**, *“Money is a good soldier, sir, and will on” — The Bank of England in the Peninsular War, 1807–1814*, MA thesis, McGill University, August 2014；https://mcgill.scholaris.ca/bitstreams/6dcd38c6-a91e-4474-a50b-c89b1d8116c9/download ，`downloads/pages/3ac3b1dd88bf.md`。读导论注20—22附近，1794普鲁士硬币0.6及0.12m、荷兰0.4m贷款分别转引Sherwig pp.45—58、41；未冻结入主序列，不声称亲读Sherwig。
- **Luke Lanskey and Conor O’Loughnan**, *300 years of UK public finance data*, Office for Budget Responsibility；https://obr.uk/docs/dlm_uploads/300-Years-of-public-finances-Accessible-PDF.pdf ，`downloads/pages/7409d7aca2ed.md`。只作长期统计框架和来源交叉参照，未把图中粗读数字列入年度数据。
- **Gregory Fremont-Barnes**, *The Royal Navy 1793–1815*, p.44舰队拨款表，二手网页`downloads/pages/7f93512d05f7.md`，https://epdf.tips/the-royal-navy-1793-1815.html 。数字由B3卡回传：1810 18.975120、1811 19.822、1812 19.305759、1813 20.096709；**本卡按同伴提供标识、未逐表图独立核原书**，只与H1差额并列。获准拨款不等于净实支，含运输/俘虏项目。具体舰人木坞与海军预算由B3负责。
- **Kim Oosterlinck、Loredana Ureche-Rangau、Jacques-Marie Vaslin**的滑铁卢后英法利差工作稿，由F4回传EHES No.41（2013）文件`downloads/F4_Oosterlinck2013.pdf`、doc `1d550bd51998`。本卡未独立核相关页，**未将其>400→约100bp数值放入主论证或直接与1811新贷票息相减**。

### 存在但本轮未亲得正文／未对校

1. B.R. Mitchell and Phyllis Deane, *Abstract of British Historical Statistics*, Cambridge UP, 1962；p.442银行系列仅经Bordo–White表3转引。本轮查得IA重印入口https://archive.org/details/abstractofbritis0000mitc （`downloads/pages/6e6f2ee5c7e3.md`），借阅受限。Mitchell（1988）在D1有数字转录，不等于已核1962/1971原表。
2. John M. Sherwig, *Guineas and Gunpowder: British Foreign Aid in the Wars with France, 1793–1815*, Harvard UP, 1969。pp.362—368及全期援助表未亲读。网页书评中约66m只为检索线索，不作本卡核定总量；相关缓存`afa9eb650bc6.md`、`f4388af7a51c.md`。
3. A. Hope-Jones, *Income Tax in the Napoleonic Wars*, Cambridge UP, 1939；所得税早期年表经Avery Jones转引，样章缓存`1e04060345f8.md`仅有出版页眉，不称已阅正文。
4. François Crouzet, *L’économie britannique et le blocus continental (1806–1813)*, 2 vols., 1958；p.855通过L7转引。法国视角和非英语正文仍不足。
5. Silberling、Tooke、Knight、Hilton及Herries原账：列为来源谱系和后续线索，不因文献设计列过其名而冒充已经引用其未见页。

### 档案谱系（未查原折）

- **Bank of England Archive**：Court of Directors Minutes、Committee of Treasury Minutes、Discount Office账、日记账与资产负债表账；本轮数字经D1—D3，危机审查记录经L6。
- **英国财政与战争行政**：TNA Treasury（T）、Exchequer（E）、Customs（CUST）、Admiralty（ADM）、War Office（WO）、Foreign Office（FO）；需进一步确认具体系列号后再调卷。没有伪造盒卷号。
- **刊印议会财政账**：Annual Finance Accounts；*Accounts of the Public Income and Expenditure, 1688–1869*（Chisholm报告，PP 1868—69 XXXV）；1870 Commissioners of Inland Revenue年报；1811商业贷款专员账/回收表。这些是应补材料，不称本卡全读。
- O’Brien文中所列旧P.R.O. Customs 17/10—30等为作者实际档案引据；本卡仅读其引注，未把旧编号不加核实转换成新TNA编号。

## 五、数据字段与不能相加的附列

`B2_series.csv`的前21列为主财政年系列和来源；随后附银行、4月5日税年及少量贷款成本。把同一个year列放在一行只为检索便利，**不意味着各列都在同一天或同一财政年度计量**。

- `revenue/expenditure/interest_gbp_m`：D1历年转换后的流量。
- `debt_funded_unfunded_calendar_gbp_m`、`capital_value_terminable_annuities_gbp_m`、`debt_total_calendar_gbp_m`：D1综合债务及构成；全部56年均有源值；不存在本卡填零或以总额替代组件，各行`debt_component_note`明确标识。
- `debt_gdp_pct_boe_all_ireland`：沿用D1比率，不供法胜GDP预测。
- `direct_income_tax_category_fy_gbp_m`：A27税目AA原财年，依`fiscal_source_label`、`fiscal_end_convention`辨读。1799桥接季度不能当全年；1815/16指截至1816年1月的财年，不表示1816废税后新税。
- `boe_notes_end_feb_gbp_m`、`boe_coin_bullion_end_feb_gbp_m`：D2的银行存量；1844后本卡留空，不暗中改观察日。
- `property_tax_net_produce_year_to_april5_gbp_m`：H7原表分项，1804—09六点；不跟D1税目混接。
- `new_loan_cash_coupon_cost_pct`：1810=4+4/20+2/240=4.208333%；1811=355937.5/7500000×100=4.745833%；1815由H2认缴100所获130面额3%+44面额3%+10面额4%，等于5.62%。1815不含期初Exchequer bills转长债的另一批融资，**不是全年全部贷款的平均成本**。
- 1811票息包括组合与年金年度支付，未纳缴款时序折扣IRR；1810只是H1同段给的比较率，不声称已重建其逐券合同。市场bonus按当时市价计，不能再无时限地加成年度利率；管理费与偿债基金也分列。
- `B2_consol_monthly_1809_1812.csv`：raw和spliced均来自M10，保留原文source字段；48点是月末，不与年平均直接当同观测相减。

## 六、模型、独立复核与未完成检查的范围

- `B2_model.py`读主CSV真实起点，并公开R/G/y/g/还现款上限、起始利息调整与减支时滞；输出`B2_model_paths.csv`、`B2_model_assumptions.json`。8个主情景＋24个网格＋8个过渡版本，共40条。过渡首年维持原G，1或2个年度阶梯降至目标；金额属于情景参数，不是新找到的裁撤实账。S3过渡版1844—47触及60%，撤销对它的“1848前无探针压力”判断。
- 模型没有把全存量债券重定价；用3%等价永久债折价发行，新增票息进入下一期；面额变化与现金缺口之差单列stock-flow adjustment。旧本金含期限年金资本值，故称面额代理，不能当逐券法律本金。
- 60%、70%债息/收入和30m现金缺口只是审查探针；1797已超60%是明确反例。越探针后的爆炸数字不作为可融资预测，也不以“模型尚能借到”证明历史市场愿意认购。
- 年表各项推演引文支持制度和机制，年份由情景设定/计算给出，不声称史料能直接描述未发生的世界。
- 当前证据层级不支持统计显著性检验、封锁的识别性因果估计、整体贸易—税收弹性、首都失守后重组的直接历史概率。本卡给明确条件路径，不用这些缺口拒绝结论。
- 本卡另以`verify_B2.py`检查56年、48月、40条模型路径、现金与面额恒等式、旧券/新券票息时点、JSON检查点、8项反应函数、32个年表节点及14项引文片段（仅规范空白），结果写入`B2_validation.txt`。文字定位不是论证支持检验；SHA相符不是对原始账目的独立核验。只读代理fiscal-audit对原8＋24线静态审计有条件通过，确认旧券/新券、现金/面额和模板；执行权限限制使其未能独立全量复算。新增过渡公式及时序获其确认，但新数值由本卡复算。代理提出的立即节流/滞后接口和“探针不能指定调整事件”问题已修正，记录见`B2_independent_audit.md`。项目红队仍待另行抽查，不把本卡自检称作已通过全项目红队。

## 七、旧资产复用与语言偏向

- 上一轮C4补证：`nodes/r_b55f2c1cf5/cards/t_95ef51/uk_fiscal_checks.md`；相关财政子表：`nodes/r_b55f2c1cf5/cards/t_104134/fiscal/`；旧总索引：`final/r_b55f2c1cf5-material-index.csv`。只作为线索；主承重Hansard、BoE与工作稿已经复读，不继承“未识别英国耐力”的旧终局。
- 本轮分项备忘：`evidence_bank.md`、`evidence_tax_subsidy.md`保留子代理的逐条论证及限度；后续修正以本主报告/本表的显式更正为准，不抹去旧记录。
- 英语一手机关材料较强，法语Crouzet仅经转引，瑞典语Heckscher仅读英译；**未满足两种非英语正文来源**，已在主报告披露。需要法方与产业史卡进行反向交叉；不能为了计数塞入没有使用的外语材料。
