from pathlib import Path
from collections import Counter
from urllib.parse import unquote
from bs4 import BeautifulSoup
import csv, json, re, hashlib, shutil, difflib
B=Path('/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised')
E=B/'audit/20260924_逐项补订'; W=E/'M002_谁能推动皇帝接受约束'; R=W/'回源材料'
R.mkdir(exist_ok=True)
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def wc(p,rows):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for src,dst in [('m002_coffin_scan.pdf','Coffin_1917_原刊公开扫描.pdf'),('m002_coffin_scan.txt','Coffin_1917_扫描OCR.txt'),('m002_coffin_page-03.png','Coffin_第289页.png'),('m002_coffin_page-04.png','Coffin_第290页.png'),('m002_coffin_live.md','Coffin_FondationNapoleon_20260924网页.md'),('m002_coffin_ia_metadata.json','InternetArchive_公开本元数据.json')]:
 shutil.copy2(Path('/tmp')/src,R/dst)
manifest=json.loads((W/'修改前指纹.json').read_text())
changed={Path(x['path']).name for x in manifest if '/chapters/' in x['path'] and h(Path(x['path']))!=x['sha256']}
assert changed=={'00_导论.md','01_法国的能力与代价.md','09_另一条十九世纪.md'},changed
old=(W/'修改前/胜利之后的欧洲_完整修订稿.md').read_text(); new=(B/'胜利之后的欧洲_完整修订稿.md').read_text()
notes=lambda s:dict(re.findall(r'^\[\^([^\]]+)\]: (.*)$',s,re.M))
a,b=notes(old),notes(new);assert len(a)==210 and len(b)==213
assert set(b)-set(a)=={'终7','终8','终9'}
assert all(b[k]==v for k,v in a.items())
refs=lambda s:Counter(re.findall(r'\[\^([^\]]+)\](?!:)',s))
x,y=refs(old),refs(new);delta=y-x
assert not x-y
assert delta==Counter({'终7':1,'终8':1,'终9':2,'法1':1,'法15':1,'法16':1}),delta
assert sum(x.values())==387 and sum(y.values())==394
tables=lambda s:re.findall(r'^\|.*(?:\n\|.*)*',s,re.M)
assert tables(old)==tables(new) and len(tables(new))==62
qa=json.loads((B/'audit/verification.json').read_text())
assert len(qa['original_report_files'])==23 and all(z['unchanged'] for z in qa['original_report_files'])
soup=BeautifulSoup((B/'胜利之后的欧洲_阅读版.html').read_text(),'html.parser')
ids=[z['id'] for z in soup.select('[id]')];assert len(ids)==len(set(ids))
missing={unquote(z['href'][1:]) for z in soup.select('a[href^="#"]')}-set(ids);assert not missing
assert len(soup.select('section.footnotes > ol > li'))==213
assert len(soup.select('.table-scroll > table'))==62
assert 'les droits de la liberté, de la sûreté, de la propriété' in (B.parents[1]/'downloads/pages/d3da94a75442.md').read_text()
assert 185+386==571 and 39+4==43 and 10+11==21
assert 15+48+41+51+3==158
anchors={
 '00_导论.md':['不过，值得选择的政策'],
 '01_法国的能力与代价.md':['这不是一部现成的议会宪法','**最可能存续得更久的'],
 '09_另一条十九世纪.md':['所以，主线不是一组','### 3．谁能让皇帝','拿破仑并非从不纠正','这场纠偏也显出','一旦要求进入政治保证','1815年的《帝国宪法附加法》','从这些史实出发','**军队需要','**债权人和商人','**皇室最在意','较可行的顺序','- **以1807年','- **在已经避免','- **改判的界线','这些人群不会仅因','由此可以作出比','**在帝国继续存续','〔终7〕','〔终8〕','〔终9〕']}
loc=[]
for name,starts in anchors.items():
 p=B/'chapters'/name; lines=p.read_text().splitlines()
 for start in starts:
  hits=[(i+1,s) for i,s in enumerate(lines) if s.startswith(start)]
  assert len(hits)==1,(name,start,hits)
  loc += [dict(file=name,line=n,text=s) for n,s in hits]
 before=(W/'修改前/chapters'/name).read_text()
 (W/name.replace('.md','.diff')).write_text(''.join(difflib.unified_diff(before.splitlines(True),p.read_text().splitlines(True),fromfile='修改前/'+name,tofile='修改后/'+name)))
wc(W/'本项正文落点.csv',loc)
source_rows=[
 {'source':'Joseph Laîné, rapport, décembre 1813','local':'downloads/pages/d3da94a75442.md','locator':'报告末部权利段；网页编者导言记扣押与停会','adoption':'末章第二节第3小节：国防与权利交换遭拒','note':'终7','level':'官方议会网站转录；报告与后设导言分用；未核原档'},
 {'source':'Acte additionnel, 22 avril 1815','local':'downloads/pages/4ba9714f9fde.md','locator':'第2、21、23、34—40条','adoption':'预算征税征兵程序、解散与延征例外、皇权保留','note':'终8','level':'19世纪文集电子转录，非原刊图像'},
 {'source':'Coffin, AHR22(2),1917','local':str((R/'Coffin_1917_原刊公开扫描.pdf').relative_to(B.parents[1])),'locator':'第288—291页，注1—2；第289、290页图像亲核','adoption':'审查数据与行政纠偏；后段禁稿1纠正为11','note':'终9','level':'期刊原刊扫描核读；底层AF IV及Locré仍转引'},
 {'source':'Coffin网页及旧F5卡','local':'downloads/pages/bfc5cba262e2.md；nodes/r_5b1357a9c6/cards/t_7c3954/F5_french_society_succession.md','locator':'1812年分期叙述','adoption':'仅作为误录传播链；不作为独立数量证据','note':'终9','level':'网页实时复核；与旧卡不是两份独立历史证据'},
 {'source':'1813年摄政元老院决议','local':'downloads/pages/9f08012c5301.md','locator':'法文正文第1、5、10、22、24、26条','adoption':'摄政程序不等于对在位成年皇帝的同样限制','note':'法15（保留原注）','level':'既有法文转录定向核读；网页标题日期问题不转入正文'},
 {'source':'Senkowska-Gluck, Les donataires de Napoléon','local':'downloads/pages/de8da74a2316.md；nodes/r_5b1357a9c6/cards/t_9f10b6/f4_evidence_notes.md','locator':'1810年3月3日财产转移安排及受益者法律地位','adoption':'军功财产国内化是利益转换入口，不等于军队自动立宪','note':'法16（保留原注）','level':'论文转录定向核读，未核其所引法令原影像'},
 {'source':'Dard所录1805年塔列朗意见','local':'chapters/01_法国的能力与代价.md','locator':'第一章及法1注','adoption':'方案存在不等于大臣掌握独立否决权','note':'法1（保留原注）','level':'沿用书内已归属材料，未重新认证Dard全部原页'},
 {'source':'本书推演','local':'chapters/09_另一条十九世纪.md','locator':'第二节第3小节四类行动者及三线排序','adoption':'政治联盟、改革顺序、短期行为与长期存续路径的不同排序','note':'承接终7—9及法1、15、16','level':'作者机制判断；非史料所载事实，非统计概率'}]
wc(W/'材料到正文与引注.csv',source_rows)
source_root=B.parents[1]
base=json.loads((W/'使用材料指纹.json').read_text())
# 新增材料另存，不改变原检查点的阅读范围记录。
extra=[source_root/'downloads/pages/de8da74a2316.md',source_root/'downloads/pages/bfc5cba262e2.md']+sorted(R.iterdir())
dump(W/'新增回源材料指纹.json',[dict(path=str(p),sha256=h(p),bytes=p.stat().st_size) for p in extra if p.is_file()])
verification=dict(changed_chapters=sorted(changed),other_chapters_unchanged=9,original_report_files_unchanged=23,old_note_definitions_preserved=210,new_notes=['终7','终8','终9'],current_note_definitions=213,old_note_calls_preserved=387,current_note_calls=394,added_calls=dict(delta),tables_preserved_unchanged=62,missing_internal_anchors=[],duplicate_html_ids=[],exact_quote_checked='Laîné原文短引与保存转录一致',arithmetic_checks=['185+386=571','39+4=43','10+11=21','15+48+41+51+3=158'],source_image_verified=['Coffin原刊第289页','Coffin原刊第290页'],book_visual_verified=False,limits='书稿为静态保全、注释、表列、内部链接核验；原刊图像核读不等于书稿逐屏视觉验收。行为排序为作者判断，不是已验证概率；全书其余缺陷仍按工作账保留。',current_hashes={str(p.relative_to(B)):h(p) for p in list((B/'chapters').glob('*.md'))+[B/'胜利之后的欧洲_完整修订稿.md',B/'胜利之后的欧洲_阅读版.html']})
dump(W/'补订核验.json',verification)
master=list(csv.DictReader((E/'当前缺陷工作账.csv').open(encoding='utf-8-sig')))
for r in master:
 if r['id']=='M002':
  r['state']='已订正并复核：本项论证缺口关闭'
  r['review']='补入短期行为/长期存续两种排序、四类行动者的筹码与阻力、交易次序、拒改条件；以1811—1813审查、1813莱内报告、1815法条支撑；同步修订导论与后段。关闭指论证补齐，不代表未发生历史已获实证证明。'
  r['revision_evidence']='M002_谁能推动皇帝接受约束/本项正文落点.csv；材料到正文与引注.csv；补订核验.json'
 elif r['id']=='L004':
  r['state']='已补入并回源：材料缺口关闭'
  r['review']='审查统计与内政/警察权限冲突已入末章论证；回源原刊第289—290页，将网页与旧卡后段禁稿1更正为11，原有年度21得以核合。没有把总局样本当全国出版自由率。原刊周报159/158差异另记SRC001。'
  r['revision_evidence']='M002_谁能推动皇帝接受约束/回源校勘记录.md；正文终9注；补订核验.json'
 elif r['id']=='M035':
  r['state']='部分修复：M002联动订正；独立比较待补'
  r['review']='末章已撤去产业成长必然限制皇权的单向表述，补受保护企业、国家订单与分散债权人的反向利益；仍待具体税债冲突、地主与军官站队以及威权工业化/有限立宪的对称比较。'
  r['revision_evidence']='M002_谁能推动皇帝接受约束/本项正文落点.csv；本项补订说明.md'
if not any(r['id']=='SRC001' for r in master):
 r={k:'' for k in master[0]}
 r.update(id='SRC001',category='来源内部差异',state='待考：已在正文注释披露，未影响所用分期稿件算式',title='Coffin原刊周报总份数159与158不合',location='Coffin1917，第289页注1与注2；书稿终9注',problem='原刊注1记周报159份，表中各年15、48、41、51、3合158且合计印158。属于原刊内部差异，非本次网页漏字；目前没有认定缺失或重复的是哪一份。',repair='如需按周报份数计算比率或重建收集范围，回查AF IV原件/清单，说明多出的一份；本次只用逐年稿件及纠正/禁止数，不以158或159推导新结论。',review='原刊第289页图像已核，差异已在终9注如实列明；L004正文吸收不以消除此差异为前提。',evidence='第289页注1：there are 159 in all；同页表：15+48+41+51+3=158。',position_basis='本轮原刊图像定位',revision_evidence='M002_谁能推动皇帝接受约束/回源校勘记录.md；回源材料/Coffin_第289页.png')
 master.append(r)
wc(E/'当前缺陷工作账.csv',master)
progress=json.loads((E/'逐项进度.json').read_text())
entry=dict(id='M002',state='已订正并复核：论证缺口关闭',implemented=['区分1807行为默认与长期存续路径，分别给三种结局排序','补入大臣、军队、债权人与商人、皇室的利益与阻力','补交易顺序、组织和法律保证，以及排序反转条件','纳入莱内报告和1815具体法条、税种/解散例外','联动补齐L004，回源原刊校正1812后段禁稿1为11'],related_partial=['M035：反向利益已写入，税债冲突与政治联盟的对称比较待独立补订'],new_source_issue='SRC001：原刊周报总数159/158差异，已披露且不用于计算',not_claimed=['未将反事实行为排序包装成实证概率','未宣称所有引注或全部材料已完成','书稿未作本轮逐屏视觉验收'],next_id='M003',next_topic='1803决策关口与1807整固路径的行动、代价及失败退路比较')
progress['items']=[z for z in progress['items'] if z['id']!='M002']+[entry]
progress['whole_book_accepted']=False
progress['conclusion_defects']={'original_active':39,'closed':1,'partially_repaired':2,'not_yet_repaired':36}
progress['material_groups']={'original':10,'closed':1,'remaining':9}
dump(E/'逐项进度.json',progress)
print(json.dumps({k:v for k,v in verification.items() if k!='current_hashes'},ensure_ascii=False,indent=2))
print('M002 and L004 updated; M001/M035 partial; SRC001 disclosed; next M003.')
