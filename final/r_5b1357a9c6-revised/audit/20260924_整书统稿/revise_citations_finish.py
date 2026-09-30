from pathlib import Path
import re,json
B=Path('/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised'); C=B/'chapters';W=B/'audit/20260924_整书统稿'
changes=[]
def note(fn,key,new):
 p=C/fn;s=p.read_text();pat=rf'^- \*\*\[{key}\]\*\*.*$' if fn.startswith('02b') else rf'^〔{key}〕.*$';s,n=re.subn(pat,lambda m:(f'- **[{key}]** ' if fn.startswith('02b') else f'〔{key}〕')+new,s,flags=re.M);assert n==1,(key,n);p.write_text(s);changes.append([fn,key])
N='02b_英国海权与和平_舰队海峡与帝国.md'
note(N,'法海4','Nicola Todorov, “La géographie des ressources forestières et les ambitions navales de Napoléon après Trafalgar : l’exemple du bois de chêne,” *Revue de géographie historique*, 5 (2014), [DOI](https://doi.org/10.4000/geohist.4373)，第3、7—10、19—22、28—31段，分别涉及单舰耗材、清查与流域分布、计划采伐及执行。库存、拟用量和运达量分列；这几组段落不是同一批已经交付的舰材。')
note(N,'法海5','Patrick Villiers、Pascal Culerrier, “Du système des classes à l’inscription maritime,” *Revue historique des Armées*, no.147 (1982), pp.44–53，尤其pp.49–51，“La période révolutionnaire”及“De la Restauration au second Empire”，[原刊全文与页图](https://www.persee.fr/doc/rharm_0035-3299_1982_num_147_2_7111)。作者姓名据原刊改为Pascal；抽调、登记及舰上训练不作同一种人数。')
note(N,'法海6','Patrick Villiers, “Piraterie, flibuste et autres guerres de course dans les conflits européens de l’époque moderne,” 收于Benjamin Deruelle、Hervé Drévillon、Bernard Gainot编，*La construction du militaire*, vol.3，Paris：Éditions de la Sorbonne，2020，pp.159–178，第39—40段，[DOI及全文](https://doi.org/10.4000/books.psorbonne.91295)。所引1793—1801和1803年以后各组捕获、私掠许可证及被俘海员数，保留作者不同起讫年；累计捕获不等于同时服役舰队。')
note(N,'陆海4','Kevin Barry Linch, *The Recruitment of the British Army 1807–1815*，博士论文，University of Leeds，2001年10月，pp.22–29、121–122，[大学库全文](https://etheses.whiterose.ac.uk/id/eprint/281/1/uk_bl_ethos_409358.pdf)。年均减员见p.22；1810年24,764名册、7,677病员、17,087适勤，以及1811年55,938名册却仅五营可外派，见p.26（PDF第27页）；征募赏金和两个半年6,081→2,537见p.121。后者伴随战和转换，未被解释为独立的赏金价格效应。')
note(N,'陆海5','Christopher Chilcott, *Maintaining the British Army, 1793 to 1820*，博士论文，Bath Spa University，2006，pp.242–244，[大学库全文](https://researchspace.bathspa.ac.uk/1461/1/Christopher%20Chilcott%20-%202006.pdf)；John Cary, *Cary’s New Itinerary*, 6th ed. with improvements，London：J. Cary，1815，印页（双栏）11—12、50、84、535—536、546，[所用版本影印](https://archive.org/details/carysnewitinerar00cary)。分别对应伦敦桥—梅德斯通—海斯、威斯敏斯特桥—伯恩、海德公园角—韦茅斯、白教堂—切姆斯福德—科尔切斯特—哈里奇／圣奥西斯。8弗隆＝1英里；只从同一起点的累计里程作差。1815道路是1805的地理代理，不证明当年路况和调兵速度。')
note(N,'爱4','Ivan F. Nelson, “‘The First Chapter of 1798’? Restoring a Military Perspective to the Irish Militia Riots of 1793,” *Irish Historical Studies*, 33, no.132 (November 2003), pp.369–386，注82，[DOI及刊物页面](https://doi.org/10.1017/S0021121400015893)。电子上线日期2016年3月21日并非首刊年。本书使用公开可见注释的统计范围，未据此声称通读付费全文。')
note(N,'爱7','James S. Donnelly Jr., “Captain Rock: Ideology and Organization,” [DOI](https://doi.org/10.1353/eir.2007.0030)；Stephen Randolph Gibbons, *Rockites and Whitefeet: Irish Peasant Secret Societies, 1800–1845*，博士论文，University of Southampton，1982，[大学库题录与摘要](https://eprints.soton.ac.uk/460381/)。后者在此直接核到的是作者、学位、年份和摘要所述土地、劳工、什一税与宗派议题；正文各社团精确年份仍待逐页核对，不把摘要冒充论文全本。天主教群众组织另参见爱尔兰虚拟档案馆1824年3月10日O’Connell致Laffan信，VRTI-CATH-1-1824-03-10。')
note(N,'帝7','National Library Board Singapore, “Temenggung Abdul Rahman,” 2019年8月5日，[机构条目](https://www.nlb.gov.sg/main/article-detail?cmsuuid=20ede07c-76e3-4932-8816-4810e9528a72)，1819年协定及“Treaty of Friendship and Alliance (1824)”部分；Archives New Zealand, “What te Tiriti o Waitangi says in English and te reo Māori,” [条约两种文本与差异](https://www.archives.govt.nz/discover-our-stories/the-treaty-of-waitangi/what-te-tiriti-o-waitangi-says-in-english-and-te-reo-maori)，尤其各文本第一、二条；Manatū Taonga, “Read the Treaty,” 2023年6月12日更新，[英文文本](https://nzhistory.govt.nz/politics/treaty/read-the-treaty/english-text)。访问日期均为2026年9月24日。条约文本的主权表述与当地实际接受分开，不以欧洲一方的文字替代毛利理解。')
note('01_法国的能力与代价.md','法10','John R. Elting, *Swords Around a Throne*，军马与运输论述；其所用版次和页码仍待补核。1813年重建的直接数据依据Paul L. Dawson, “Napoleon’s Equine Strategy in 1813,” *The Napoleon Series*，2013年9月，[作者全文](https://www.napoleon-series.org/military-info/organization/France/Cavalry/Remounts/c_remounts1813.html)，开头1813年2月25日马匹清查及表1以下采购、编配统计。采购、配马、死亡与退出属于不同统计对象，作者的档案引文属于转引而非本书亲查军马原簿。')
note('08_新秩序的经济与社会.md','经15','Alexander Grab，前引书，法国教育与法律诸节；V. Coffin, “Censorship and Literature under Napoleon I,” *The American Historical Review*, 22, no.2 (January 1917), pp.288–308，尤pp.288–291及审查分期表，[DOI](https://doi.org/10.2307/1834962)。审查机构和稿件数据另见本书终9注；Benjamin Constant, *De l’esprit de conquête et de l’usurpation*, 1814，第12—13章，以及1815年《附加法》相关文书。')
p=C/'08_新秩序的经济与社会.md';s=p.read_text();s=s.replace('本书Juhász的具体数字与表号据2018年4月2日作者稿，尤其第42、45页，未将作者稿页码冒充刊本页码。','本书Juhász的具体数字与表号据2018年4月2日作者稿，尤其第42、45页；[作者稿入口](https://www.rjuhasz.com/research/napoleonic_blockade.pdf)。以所用稿内日期识别版本，网页更新后的同址文件未必仍是该版；作者稿页码不冒充刊本页码。');p.write_text(s)
# 只调整面向读者的修订史话语；保留证据等级、反例及数量。
replacements={
'01_法国的能力与代价.md':{'盟軍':'盟军','再扣当地皇室岁费（liste civile）150万':'再扣当地已承担的皇室岁费150万'},
'02a_英国海权与和平_国家财政与社会.md':{'是经其转引的报告，不是本次亲查原账':'出自其转引的报告，证据层级为研究者转引','本次未完成舍维格原书全表复核':'尚缺舍维格原书全表的独立复核','旧稿援引的约 220 万英镑实际垫款':'常被并列援引的约 220 万英镑实际垫款'},
'02b_英国海权与和平_舰队海峡与帝国.md':{'但本次尚未取得相应原始执行命令':'但现有证据未含相应原始执行命令','### 2. 原模型的有用之处：让条件与结果同时出现':'### 2. 较高投入的对照情景：舰队怎样逐年积累'},
'03_大陆诸国.md':{'尚非本工程直接核查的团级军籍':'证据来自研究者转引而非逐团军籍复原'},
'04_西班牙与意大利.md':{'未获本次独立军籍核定':'尚无独立军籍核定'},
'07_行省化的边界.md':{'旧稿的抵抗比较，建立了':'一项跨地区抵抗比较整理了'},
'08_新秩序的经济与社会.md':{'但英方原始统计在本工程中未逐项复核':'但英方数值尚缺同口径原始统计的逐项复核','这是一份有价值的结构描述，却被旧稿施加了过重的解释。':'这份结构描述揭示了资本的分布，却还不足以直接计算全国工业的未来增速。','这与旧稿319公里的口径冲突':'另有319公里的统计口径，与前者尚未对齐','旧稿用每公里25万—40万法郎':'若用每公里25万—40万法郎'},
'10_资料附编.md':{'下面保留本工程经后续学术转录取得的三个年份':'下面列出经后续学术转录取得的三个年份','原研究把1830与1860之间线性插值得到':'在1830与1860之间线性插值，可以得到'}
}
for fn,rs in replacements.items():
 p=C/fn;s=p.read_text()
 for a,b in rs.items():assert a in s,(fn,a);s=s.replace(a,b)
 p.write_text(s)
# 把剩余空缺分成已经替代检验、待原始账、反事实选择，不再一律写作待研究。
p=C/'10_资料附编.md';s=p.read_text();needle='这些缺口的作用并不相同。'
addition='''当前的证据边界，应分成三类来读。**第一类，现有材料已能完成替代检验**：法国预算已列收入门槛与支出取舍；共同基金已计利息、还本和退出；铁路、海军与美洲援助已放入同一竞争关系；阿姆斯特丹贷款已区分认购、换债和新现金。这些改变可以支持政策排序，却没有把规划门槛变成历史实收。**第二类，仍需新账本或更细原表**：同一疆域逐年的可转用净收入、各盟国兵额与现金的联合履约、舰员流入退出及维修训练实付，尚未完整闭合。它们保留为承重缺口，主线相应缩小承诺，不用另一章的乐观上限填空。**第三类，是作者须承担的反事实选择**：西班牙政体、美洲各地区去向、意大利王冠、东方安排与王朝继承，正文已经给出首选及次选；档案能限定条件，却不会替作者写出未发生过的1848年。这些排序与附加假设均应接受反例，而不再伪装成等待发现的历史事实。\n\n'''
assert needle in s;s=s.replace(needle,addition+needle,1);s=s.replace('西班牙合法性是已核障碍之一；武装共存是计划底线，不预设英国裁军或承认法国一切海岸安排','主线要求可执行的海上停战，具体见第二、三章；安特卫普军用上限与贸易交换是作者方案，不预设英国裁军或已接受')
p.write_text(s)
(W/'引注修订记录.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2))
print('updated',len(changes),'notes plus version link, reader prose and gap classification')
