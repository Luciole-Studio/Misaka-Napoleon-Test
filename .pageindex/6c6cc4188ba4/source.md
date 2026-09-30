# P4后续来源即录与校对（2026-09-23）

- Richard Glover, “The French Fleet, 1807–1814; Britain's Problem; and Madison's Opportunity,” *JMH* 39.3 (1967), 233–252 DOI 10.1086/240080。JSTOR `https://www.jstor.org/stable/1876579`、芝大`https://www.journals.uchicago.edu/doi/10.1086/240080`抽取仅书目与权限墙，不纳入本文事实证据；缓存`downloads/pages/717b149d2bb0.md`、`ecb1c103e4af.md`。
- Glete 1993两卷原书未获取。实读Paul E. Fontenoy评Jan Glete，*Naval War College Review* 49.4 (1996), p160，本地扫描`downloads/P4_Glete_review_Fontenoy_1996.pdf`，doc`b75effed1b78` PDF p3图像。评者指出Glete认为海军持久性“the aggregation of domestic interests behind policy ... generally outweighs that of external threats”；这仅是评论者转述Glete之论，不是作者文本，也不是英1815—30数据。它构成反证机制：持续法威胁仍须英国财政/议会与船厂联盟支持，自动扩军不成立。
- Martin Wilcox, “‘These peaceable times are the devil’: Royal Navy officers in the post-war slump, 1815–1825,” *International Journal of Maritime History* 26.3 (2014), pp471–488, DOI 10.1177/0843871414543445，抽取`https://journals.sagepub.com/doi/10.1177/0843871414543445`、缓存`downloads/pages/1131eb224b3d.md`。只读开放Abstract，称和平后解雇124,000人，到1818约90%委任军官失业且领取半薪；全文未获取。支持真实裁军的阶层成本、半薪保留经验，但不能把124,000等同某一年度下水或1830陆战队人数。
- Andrew Lambert, “Preparing for the Long Peace: The Reconstruction of the Royal Navy 1815–1830,” DOI10.1080/00253359.1996.10656582检索题名；T&F extraction no content，未拿到正文，不引用细节。
- Rodger, *The Command of the Ocean* (2004) 在线XHTML `http://download.e-bookshelf.de/download/0002/5863/98/L-X-0002586398-0006544349.XHTML/index.xhtml`抽取仅书前引文与1649开头（缓存`downloads/pages/3b9ceec747c6.md`截断）；不称读过1812–15章节、不作P4数据源。
- Winfield & Roberts, *French Warships in the Age of Sail 1786–1861* (2015) WorldCat书目与出版商介绍可读，舰籍正文未获取，P4不得称书中逐舰数字已核。

## 算术和模型纠正

2026-09-23复算`build_p4.py`，发现P支1815舰体A12和英方均和W共同起点，但法方巡防/小巡航舰commissioned因`s`状态码套入和平系数，已改`bsame`，保证两支1815同状态。重新生成CSV；之前`P4_annual.csv`1815 P巡航活跃数应弃旧，现base法巡防41.08、小舰42.53，W相同。英国A12和四截面主比值不变。

1830中档无训练因子但保A12的等型排水效能：W=(84×3500)/(130×3600)=0.628，P=(111×3500)/(120×3600)=0.899；原含训练诊断的W0.449、P0.876。因A12内已经约束合格员Q，训练诊断可能重复折价，不能视作经外部实证校准的真实战斗力比。英方P对法强编军若及时改W，法国P同一存量下1830效能0.731，而非0.876（`P4_sensitivity.csv`最后两行）。
