from pathlib import Path
import csv,json,re,hashlib,collections,datetime
R=Path('/Users/makiko/Documents/exam');B=R/'final/r_5b1357a9c6-revised';A=B/'audit/20260924_出版验收复核';C=B/'chapters'
files=sorted(C.glob('*.md'));manifest=[];notes=[];paras=[];heads=[];stats=[];candidates=[];numrows=[];quote_candidates=[]
note_re=re.compile(r'^(?:〔([^〕]+)〕|\[(\d+)\]|- \*\*\[([^\]]+)\]\*\*)\s*(.*)$')
for p in files:
 s=p.read_text();lines=s.splitlines();manifest.append({'file':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
 h='';ns=[];ps=[]
 for i,line in enumerate(lines,1):
  if line.startswith('#'):h=line;heads.append({'file':p.name,'line':i,'heading':line})
  m=note_re.match(line)
  if m:
   label=next(x for x in m.groups()[:3] if x);pref='欧' if p.name.startswith('03_') else '南' if p.name.startswith('04_') else '';label=pref+label if label.isdigit() else label
   row={'file':p.name,'line':i,'label':label,'text':m[4],'locator_signal':bool(re.search(r'页|pp?\.|栏|第.{1,6}条|附录|\d{4}年\d+月\d+日|卷|表\d|第\s*\d',m[4])),'url_signal':'http' in m[4]};notes.append(row);ns.append(row);continue
  if not line.strip() or line.startswith(('#','|','>')):continue
  row={'file':p.name,'line':i,'section':h,'text':line};paras.append(row);ps.append(row)
  formal=bool(re.search(r'〔[^〕]+\d[^〕]*〕|\[(?:[^\]]*\d[^\]]*)\](?!\()|https?://',line))
  if re.search(r'（[^）]*(?:资料|相关|见|研究|文书|通信|表|章|史|Milburn|Wilson|Dutt|Marichal|[A-Z][a-z]{2,})[^）]*）',line) and not formal:candidates.append({**row,'reason':'正文括注没有可解析注号或链接；须核是否能由全书唯一题录定位'})
  if re.search(r'\d',line) and not formal:numrows.append({**row,'reason':'数字段未出现形式引注；相邻注释或作者计算可能有效，待人工核定'})
  if re.search(r'“[^”]{10,}”',line) and not formal:quote_candidates.append({**row,'reason':'长引号段未含形式引注；须区分直接引语、术语和作者拟写'})
 stats.append({'file':p.name,'lines':len(lines),'characters':len(s),'han':len(re.findall('[\u4e00-\u9fff]',s)),'formal_notes':len(ns),'body_paragraph_lines':len(ps)})
def csvout(name,rows):
 if not rows:return
 with (A/name).open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for n,rs in [('书稿快照.csv',manifest),('全书注释逐条登记.csv',notes),('全书正文段落登记.csv',paras),('全书层级标题.csv',heads),('模糊括注待核.csv',candidates),('数字段引注待核.csv',numrows),('直接引语待核.csv',quote_candidates),('分章扫描统计.csv',stats)]:csvout(n,rs)
(A/'全部注释供核读.txt').write_text('\n\n'.join(f"{n['file']}:{n['line']} [{n['label']}] {n['text']}" for n in notes))
(A/'扫描说明.json').write_text(json.dumps({'time':datetime.datetime.now().isoformat(),'chapters':len(files),'notes':len(notes),'loose_citation_candidates':len(candidates),'numeric_paragraph_candidates':len(numrows),'quote_candidates':len(quote_candidates),'meaning':'全稿机器定位并非全部缺陷；每条候选需人工判定。此轮审计不改动被审书稿。'},ensure_ascii=False,indent=2))
print(json.dumps({'chapters':stats,'notes':len(notes),'loose_citations':len(candidates),'numeric_paras':len(numrows),'quotes':len(quote_candidates)},ensure_ascii=False))
# Review inventory category/dedup information, but distinguish indexing from actual reading.
f=B/'audit/20260924_地毯式审计/全目录文件快照.csv';inv=list(csv.DictReader(f.open()));cats=collections.defaultdict(list)
for r in inv:cats[r['category']].append(r)
summary={k:{'files':len(v),'unique_hashes_within_category':len(set(x['sha256'] for x in v)),'bytes':sum(int(x['bytes']) for x in v),'not_prior_registered':sum(x['prior_inventory']=='旧两份总账未登记' for x in v)} for k,v in cats.items()}
(A/'目录范围复核.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print('category_stats',json.dumps(summary,ensure_ascii=False))
