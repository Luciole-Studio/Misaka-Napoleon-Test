# 数表补取：限定检索结果

## 状态
找到用户指定的第二候选中两张可读收入表，停止扩展检索。Gabillard p.557 原表仍未取得，**不得据本次材料填入 An XIII / 1813 任何缺失格**。没有取得或保存原页影像。

执行障碍：bash 的 curl/目录创建遭环境拒绝，提示 `permissionMode=default requires parent approval for bash` 或 `Workspace safety requires approval`；未绕过权限。write 工具可向指定 sources 目录写入。网页提取工具自动把缓存写在 downloads/pages（工具没有指定保存路径参数），因此其自动缓存未遵守用户指定目录；本交付内容另完整写入本 sources 文件。

## 1. Gabillard p.557：仅定位，未恢复数字
Jean Gabillard, « Le financement des guerres napoléoniennes et la conjoncture du Premier Empire », Revue économique 4(4), 1953, pp.548–572，表在 p.557：« Progrés des recettes de l'an XIII à 1813 »（网页题名拼写）。
https://www.persee.fr/doc/reco_0035-2764_1953_num_4_4_406987

Jina 转读确实暴露 p.549 的图像 URL：
https://www.persee.fr/renderPage/reco_0035-2764_1953_num_4_4_406987/reco_0035-2764_1953_num_4_4_T1_0549_0000_710.jpg

按该路径构造的 p.557 **候选、未验证** URL：
https://www.persee.fr/renderPage/reco_0035-2764_1953_num_4_4_406987/reco_0035-2764_1953_num_4_4_T1_0557_0000_710.jpg
web_extract 对该地址返回 `no content returned`；这不能证明图像地址不存在，亦不能证明存在。没有视觉验读。税收行标签、An XIII / 1813 数字、单位、毛净口径均未恢复。

## 2. 第二候选其实是索引，不是缺图的表页
索引 https://www.napoleon-series.org/research/abstract/government/budget/france/an12/c_an12.html
经 Jina 读取可见其链接至 c_an12a.html（一般收入）、c_an12b.html（特别收入）、c_an12c.html（汇总）、c_an12d/e/f/g.html（支出）。本次仅读取 a、c 两表。表体能以文字提取，并非必须寻找 img。

### 2.1 一般收入逐行转录
页面标题：France: Income from General Funds in An 12。
引用定位：该页正文唯一收入表（无纸本页码）。
https://www.napoleon-series.org/research/abstract/government/budget/france/an12/c_an12a.html

【实际读取】网页对范围的原文说明：
> General summary of the receipts made in An 12, by the Treasury, as well on the discharge of this year as on the postponed discharge for the years 8, 9, 10 and 11
> Note: All monies are in Francs.

日期：1803年9月22日至1804年9月21日。单位：法郎。它是 An XII 国库收款，**包括往年账期补收，不是仅归属于 An XII 的应计税收；更不是 Gabillard 的 An XIII**。以下保留网页英语标签，不替其生硬译文恢复法文原称。

| 网页行标签 | An XII（法郎） |
|---|---:|
| Direct Contributions | 319,500,565 |
| Control of the recording and the customs. Various products | 194,804,087 |
| National Forests | 45,528,508 |
| National Fields | 6,158,777 |
| Customs | 59,603,317 |
| Post Offices | 8,946,876 |
| Currencies | 1,283,639 |
| Lottery | 15,659,400 |
| Saltworks | 2,700,000 |
| Various Receipts | 32,955,294 |
| Extraordinary and External Receipts | 141,178,023 |
| Various Negotiated or Recovered Effects: From le caisse d'amortissement (Note 1) | 1,493,768 |
| Various Negotiated or Recovered Effects: By Control of Records | 1,428,212 |
| Total（原网页） | 811,040,466 |

【核算警告】上述13个数字直接求和为831,240,466，比网页总额大20,200,000。尚不知是转录错误、项目包含关系或其他原因；不得改写某个数字以强行配平。未经原印本核对，不宜把这张网页表当成已校勘完毕的数据。

### 2.2 一般与特别收入汇总逐格转录
标题：France: Total Income from Special and General Funds in An 12。
引用定位：该页正文唯一收入汇总表及紧接的净额句。
https://www.napoleon-series.org/research/abstract/government/budget/france/an12/c_an12c.html
同一日期范围，单位法郎。

| 网页行标签 | 数值（法郎） |
|---|---:|
| From An 8 and previous years | 30,209,532 |
| From An 9 | 17,639,472 |
| Special Funds | 44,142,072 |
| General Funds (Note 1) | 811,040,466 |
| Total Cash Receipts | 855,182,538 |
| Various other Receipts | 33,333,456 |
| Total Receipts | 888,515,994 |

网页紧接原句：
> Actual Money collected from the General and Special Funds was only: 763,191,462 francs.

其前法文说明（网页抓取缺重音，照录）：
> Les recettes faites pendant l'an 12, sur les exercices antrieurs l'an 10, sont trs-considrables; c'est parce qu'en l'an 12 seulement les acquits reprsentant les avances faites par l'administration de l'enregistrement pendant les annes 7, 8, et 9, pour frais de justice, dpenses des prisons, etc., ont t verss pour comptant au trsor, et rgulariss par les ordonnances des ministres comptens. Ainsi, sur le total des recettes provenant des fonds gnraux, sur tous les exercices, il fait dfalquer les recettes fictives indiques ci-dessus, et reprentes par des rcpisses du cassier des recettes; savoir:

【毛净口径】说明称早年预付的司法、监狱等费用，到 An XII 才以凭据作为现金入账；须从一般收入中扣除这些虚记收款。这是对会计虚记款的调整，不能自动解释为扣除征税成本后的“税收净额”。本表还包括非税及非常收入。

【核算及内部矛盾】
- 811,040,466 + 44,142,072 = 855,182,538（与原网页相符）。
- 855,182,538 + 33,333,456 = 888,515,994（与原网页相符）。
- 30,209,532 + 17,639,472 = 47,849,004。
- 811,040,466 − 47,849,004 = 763,191,462。因此网页所谓 General and Special Funds 的“实际收入”数字，算术上只对应一般收入扣除虚记款，并未包含44,142,072特别收入。
- 如对一般与特别合计扣除同两项，结果为807,333,534；这是核算值，**不是史料明载数字，不得替换原句**。

### 2.3 出处层级
两网页将来源列为：Ferrire [网页如此拼写], Alexandre de, chef du bureau de statistique au ministre de l'Interieur, ed., Archives statistiques de la France: Juin/Juil. 1804–Dc. 1804/Janv. 1805, Paris: Archives Statistiques de la France, 1805。
**本次仅实际读取 Napoleon Series 的网页转录，经其转引该书；未读取1805年原印本，网页未提供纸本页码。** 未查询或读取 Gaudin / Marion IV。

## 可用边界
可引用本次恢复的第二候选网页表，并同时保留校勘警告；不能用它填补 Gabillard p.557，也不能把 An XII 与 An XIII 混同。主缺口仍在：p.557 原图、行标签、两年逐格数字及准确毛净/疆域口径。
