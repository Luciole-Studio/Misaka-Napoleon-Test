from pathlib import Path
from collections import Counter
import csv,json,hashlib,re,difflib
from urllib.parse import unquote
from bs4 import BeautifulSoup
B=Path('/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised');E=B/'audit/20260924_逐项补订';W=E/'M001_结论强度与缺口分层';D=B/'audit/20260924_出版验收复核/第二轮_引注与材料回源'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def writecsv(p,rows):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
expected={'00_导论.md','09_另一条十九世纪.md','10_资料附编.md'}
manifest=json.loads((W/'修改前指纹.json').read_text());changed=[];same=[]
for r in manifest:
 p=Path(r['path']);(same if h(p)==r['sha256'] else changed).append(str(p))
changedchapters={Path(p).name for p in changed if '/chapters/' in p}
assert changedchapters==expected,changedchapters
assert all(h(Path(r['path']))==r['sha256'] for r in manifest if '/r_5b1357a9c6-report/' in r['path'])
old=(W/'修改前/胜利之后的欧洲_完整修订稿.md').read_text();new=(B/'胜利之后的欧洲_完整修订稿.md').read_text()
def notes(s):return dict(re.findall(r'^\[\^([^\]]+)\]: (.*)$',s,re.M))
on,nn=notes(old),notes(new)
assert len(on)==209 and len(nn)==210
assert set(nn)-set(on)=={'终6'}
assert all(nn[k]==v for k,v in on.items())
oldrefs=Counter(re.findall(r'\[\^([^\]]+)\](?!:)',old));newrefs=Counter(re.findall(r'\[\^([^\]]+)\](?!:)',new))
assert newrefs-oldrefs==Counter({'终6':1}) and not oldrefs-newrefs
assert 750-300-25-300-195-20==-90
assert 800+40-300-25-300-195-20==0
for phrase in ['前面的推演已经给出一条能够运作的主线','它们限制的是精确范围和时点','它会改变什么精度']:
 assert phrase not in new,phrase
def tables(s):return re.findall(r'^\|.*(?:\n\|.*)*',s,re.M)
ot,nt=tables(old),tables(new);assert len(ot)==len(nt)==62
changedtables=[i for i,(a,b) in enumerate(zip(ot,nt)) if a!=b];assert len(changedtables)==1
for s in ['法国全国逐年到营','指定五家兵工厂','1812年同口径文官','荷兰、汉萨、罗马','布兰达各表','全部海军编制','英法海军约束','汉堡汇水','所有殖民财政','法奥婚姻与意大利继承']:
 assert s in nt[changedtables[0]]
soup=BeautifulSoup((B/'胜利之后的欧洲_阅读版.html').read_text(),'html.parser')
ids=[x['id'] for x in soup.select('[id]')];assert len(ids)==len(set(ids))
missing=sorted({unquote(x['href'][1:]) for x in soup.select('a[href^="#"]') if unquote(x['href'][1:]) not in set(ids)})
assert not missing,missing
assert len(soup.select('section.footnotes > ol > li'))==210
assert len(soup.select('table'))==62
assert len(soup.select('.table-scroll > table'))==62
proof=[]
anchors={
'00_导论.md':['本书的核心判断是：','这一路径有真实的军事'],
'09_另一条十九世纪.md':['前面的比较将本书的选择','这里先作三项取舍','因此，下文把法国','**本书首选的胜利','〔终6〕'],
'10_资料附编.md':['这些缺口的作用并不相同','| 尚未完整取得或尚未完成','**据此，本书仍将','现有材料已经足以作出这种优先排序']}
for name,starts in anchors.items():
 lines=(B/'chapters'/name).read_text().splitlines()
 for start in starts:
  hit=[(i+1,line) for i,line in enumerate(lines) if line.startswith(start)]
  assert len(hit)==1,(name,start,hit)
  for n,t in hit:proof.append(dict(file=name,line=n,text=t))
 allold=(W/'修改前/chapters'/name).read_text();allnew=(B/'chapters'/name).read_text()
 (W/name.replace('.md','.diff')).write_text(''.join(difflib.unified_diff(allold.splitlines(True),allnew.splitlines(True),fromfile='修改前/'+name,tofile='修改后/'+name)))
writecsv(W/'本项正文落点.csv',proof)
verification=dict(changed_chapters=sorted(expected),other_chapters_unchanged=9,original_report_files_unchanged=23,old_note_definitions_preserved=209,new_note='终6',current_note_definitions=210,old_note_calls_preserved=386,current_note_calls=387,tables_preserved=62,tables_unchanged=61,table_expanded=1,original_gap_topics_preserved=10,budget_checks=['750−300−25−300−195−20=−90','800+40−300−25−300−195−20=0'],missing_internal_anchors=missing,duplicate_html_ids=[],visual_verified=False,limits='完成源文件、算术、表列、注释与HTML内部链接静态核验；未作本轮逐屏视觉检查，未声称完成所有来源核验或联合可行性模型。',current_hashes={str(p.relative_to(B)):h(p) for p in list((B/'chapters').glob('*.md'))+[B/'胜利之后的欧洲_完整修订稿.md',B/'胜利之后的欧洲_阅读版.html']})
(W/'补订核验.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2)+'\n')
# 历史缺陷与原位置保留；修订状态另成当前工作账。
master=list(csv.DictReader((D/'当前缺陷总账_含撤回记录.csv').open(encoding='utf-8-sig')))
for r in master:
 r['position_basis']='第二轮审计时的书稿位置；章内增补后行号可能移动'
 r['revision_evidence']=''
 if r['id']=='M001':
  r['state']='部分修复：结论强度与缺口分层已订正；联合方案待验证'
  r['review']='已改写导论、末章两处总括及附编十项缺口；明确路径排序和失效后的任务削减。仍保留具体疆域、年度预算、盟约与海军的联合可行性检验，不据文字订正宣告整项通过。'
  r['revision_evidence']='M001_结论强度与缺口分层/本项正文落点.csv；补订核验.json'
writecsv(E/'当前缺陷工作账.csv',master)
progress=dict(id='M001',state='部分修复，尚未关闭',implemented=['导论与末章统一为有明确排序的条件主线','增加防务、偿付、区域海权、盟国合作的取舍顺序','附编十项缺口逐项区分规模、时点、可行性和情景选择，并写入不利结果的改判','新增终6注，明确预算与舰队敏感性为书内试算，未将模型当史料'],not_claimed=['未完成统一疆域、年度税兵预算与外交安排的持续性检验','未关闭M005–M012、M034、M038等关联缺陷','未修复本轮未处理的引注与材料遗漏'],next_id='M002',next_topic='区分政策首选与拿破仑实际行为；为主动改革、危机迫改及拒改排序')
(E/'逐项进度.json').write_text(json.dumps({'items':[progress],'whole_book_accepted':False},ensure_ascii=False,indent=2)+'\n')
report='''# M001补订：有根据的首选，不是已被证明的胜利

本项已把语言和论证层次写回正文，合并稿及阅读版同步更新。**状态为部分修复，不因改掉过强措辞就宣布联合可行性已经验证。**

## 已补进书里的内容

1. **导论给出明确选择。**有限直辖、盟国合作与对外妥协仍是首选；它的依据是减少法国必须同时承担的任务，而不是假定所有好处都会一同出现。
2. **末章补出有代价的取舍。**大陆防务与既有偿付先于海军扩张，区域海权先于全球制海权，保存盟国合作先于新增直辖省。预算和盟约不足时，先收缩新增任务，而不自动提高征敛。
3. **附编逐项说明什么会改变答案。**原十项研究任务全部保留，扩成“影响层次—当前判断—不利情况下改判”的表。海军实付、税兵净贡献和英法安排不再被称作只影响精度。
4. **补充出处性质。**新增终6注定位第一章两项预算和第三章敏感性，给出可检查算式。预算为本书试算；来源中的历史财政尺度不被冒充另一条时间线的决算。

## 为什么仍未关闭M001

原缺陷不仅涉及措辞，还要求具体疆域、预算与外交状态组成同一套持续运作的方案。这部分依赖后续M005—M012等项。现在已经撤掉“全案已能运作”的过强总括，并明确不足会如何改变主线；尚未把模型未做的联算假称为已经做完。

## 保全与核验

- 改动3个章文件，其余9个章文件未变；原报告23文件未变。
- 原209条注释内容与386处引用均保留；新增1条注释、1处引用。
- 62张表全部保留；其中61张未变，原10项缺口表增补一列并细化内容。
- 两项预算算式、注释定义、表格列数与HTML内部链接通过静态检查。
- 本轮未做逐屏视觉检查，也未重新认证所有原始来源。

原句、完整差异及修改前版本保留于本目录。当前落点见[正文定位表](本项正文落点.csv)，检查结果见[核验记录](补订核验.json)。
'''
(W/'本项补订说明.md').write_text(report)
(E/'逐项补订进度.md').write_text('''# 逐项补订进度

**从审计转入正文修订；整书尚未通过验收。**历史审计报告保留原状，最新修订状态以此页与工作账为准。

| 顺序 | 问题 | 已完成 | 尚未完成 | 状态 |
|---|---|---|---|---|
| 1 | M001：条件方案被写成已经能够运作 | 改写导论、末章总括；十项缺口分层；加入任务取舍与不利情况下的改判；同步合稿和阅读版 | 具体疆域、年度税兵、舰队预算与外交安排的联合验证 | 部分修复，保留未关闭 |
| 2 | M002：应当自限与实际上会自限混同 | 尚未开始本项正文订正 | 比较主动改革、危机迫改、拒改；交代行动者、利益与约束 | 下一项 |

[第1项详细说明](M001_结论强度与缺口分层/本项补订说明.md) · [当前全部缺陷工作账](当前缺陷工作账.csv)

39项结论/论证问题中，1项已有正文订正但待联动验证，38项尚未进入本次逐项修订。M011仍为已撤回的审计误判，不重新计入。100处引注缺口、10组材料吸收不足、5项结构问题和1项术语误译仍保留原登记；本次没有用新增一条注释抵销其他欠项。
''')
(B/'audit/20260924_出版验收复核/当前验收索引.md').write_text('''# 当前验收与补订入口

**现已开始逐项修改正文；整书仍未通过全部验收。**第一、二轮报告记载的是修订前状态，其“书稿未改”只适用于当时审计。

- [最新逐项补订进度](../20260924_逐项补订/逐项补订进度.md)
- [当前缺陷工作账](../20260924_逐项补订/当前缺陷工作账.csv)
- [M001正文补订与核验](../20260924_逐项补订/M001_结论强度与缺口分层/本项补订说明.md)

M001已完成结论强度与缺口分层的正文订正，联合方案验证仍保留，因此状态为部分修复。其余缺陷尚未因本次修改而关闭。

## 修订前审计记录

- [第二轮复核报告](第二轮_引注与材料回源/第二轮复核报告.md)
- [第二轮全部缺陷与证据](第二轮_引注与材料回源/当前全部缺陷_逐项证据.md)
- [第一轮历史报告](出版验收_缺陷总报告.md)

第二轮确认39项结论/论证缺口、100处引注缺口、10组材料未充分入文、5项结构/覆盖问题、1项术语误译。不同类别交叉，不求和为独立错误数。M011已撤回；书稿原有英国反应和安特卫普敏感性，不再指控它完全没有这类计算。
''')
print(json.dumps({k:v for k,v in verification.items() if k!='current_hashes'},ensure_ascii=False,indent=2))
print('Progress recorded as partial, not falsely closed.')
