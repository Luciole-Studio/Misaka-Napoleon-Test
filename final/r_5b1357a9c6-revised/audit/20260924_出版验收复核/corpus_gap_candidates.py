from pathlib import Path
import re,csv,json,collections,hashlib
R=Path('/Users/makiko/Documents/exam');B=R/'final/r_5b1357a9c6-revised';A=B/'audit/20260924_出版验收复核';book=(B/'胜利之后的欧洲_完整修订稿.md').read_text();norm=lambda s: re.sub(r'[,，\s]','',s)
booknums=set(re.findall(r'\d+(?:\.\d+)?',norm(book)))
rows=[];todo=[];seen=set();files=[]
for base in [R/'nodes/r_5b1357a9c6/cards',R/'nodes/r_b55f2c1cf5/cards']:
 if not base.exists():continue
 for d in sorted(base.iterdir()):
  if not d.is_dir():continue
  for p in sorted(d.glob('*.md')):
   if p.name=='SOURCES.md':continue
   s=p.read_text(errors='replace');sha=hashlib.sha256(s.encode()).hexdigest()
   if sha in seen:continue
   seen.add(sha);files.append(str(p.relative_to(R)));heading=''
   for i,line in enumerate(s.splitlines(),1):
    if line.startswith('#'):heading=line
    if len(line)>1200 or len(line)<35:continue
    if re.search(r'未完成|未获得|未取得|未读取|未读|未转录|未做|未抓到|尚缺|待补|待查|待核|工具.*(?:失败|限制)|工具.*(?:不能|无法)',line):todo.append({'file':str(p.relative_to(R)),'line':i,'heading':heading,'text':line,'status':'原研究的未完成记录；须与后续补订及正文逐条核销'})
    if not re.search(r'法郎|英镑|卢比|比索|先令|杜卡特|银|艘|人|磅|吨|公里|万|million|率|%',line):continue
    nums=[n for n in re.findall(r'\d+(?:\.\d+)?',norm(line)) if float(n)>=30 and not (1700<=float(n)<=2100 and '.' not in n)]
    absent=sorted(set(nums)-booknums)
    if len(absent)>=2:rows.append({'file':str(p.relative_to(R)),'line':i,'heading':heading,'absent_numeric_tokens':'|'.join(absent),'text':line,'status':'仅候选：可能单位换算、概括、纠错或真正遗漏；不能以字符串未命中判漏'})
def out(name,rs):
 with (A/name).open('w') as f:w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
out('研究数字入文待核.csv',rows);out('原研究未完事项待核.csv',todo)
# One representative per latest topic; no claim that this is exhaustive semantic reading.
groups=collections.defaultdict(list)
for r in rows:groups['/'.join(r['file'].split('/')[:4])].append(r)
selected=[]
for g,rr in groups.items():
 rr.sort(key=lambda x:(' 2.' in x['file'] or ' 3.' in x['file'],'notes' in x['file'], -len(x['absent_numeric_tokens'].split('|'))))
 selected.extend(rr[:2])
(A/'数字候选重点核读.txt').write_text('\n\n'.join(f"{r['file']}:{r['line']} {r['heading']}\n{r['text']}" for r in selected))
(A/'研究卡机器筛查范围.json').write_text(json.dumps({'distinct_text_files_scanned':len(files),'files':files,'numeric_candidates':len(rows),'unfinished_record_candidates':len(todo),'selected_for_manual_review':len(selected),'limits':'机器读取不是人文全文核读，历史未完事项不是当前未完认证，数字未命中不是缺漏认证'},ensure_ascii=False,indent=2))
print(json.dumps({'files':len(files),'numeric_candidates':len(rows),'unfinished_candidates':len(todo),'selected':len(selected),'selected_text_chars':(A/'数字候选重点核读.txt').stat().st_size},ensure_ascii=False))
