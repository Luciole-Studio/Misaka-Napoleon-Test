from pathlib import Path
import re,json,subprocess,hashlib,collections
B=Path(__file__).resolve().parents[1]
chapters=sorted((B/'chapters').glob('*.md'))
nums=['一','二','三','四','五','六','七','八','九','十']
parts=[]
for i,p in enumerate(chapters):
 s=p.read_text()
 if i==0:
  s=re.sub(r'^# 胜利之后的欧洲\s+## 拿破仑的另一条道路，1803—1848\s+### 引言：征服一片大陆，然后呢？', '# 引言　征服一片大陆，然后呢？',s)
  s=re.sub(r'^### (?!引言注释)', '## ',s,flags=re.M)
 elif i<=10:
  s=re.sub(r'^# 第[一二三四五六七八九十]+[章编]　',f'# 第{nums[i-1]}章　',s)
  # Keep source chapters consistently numbered, without changing their audit record.
  raw=p.read_text();new=re.sub(r'^# 第[一二三四五六七八九十]+[章编]　',f'# 第{nums[i-1]}章　',raw)
  if new!=raw:p.write_text(new)
 s=s.replace('第一编注释','本章注释').replace('上一编 [','上一章 [').replace('下一编设定','下一章设定')
 if p.name.startswith(('03_','04_')):
  pref='欧' if p.name.startswith('03_') else '南'
  s=re.sub(r'^\[(\d+)\]\s+',lambda m:f'[^{pref}{m[1]}]: ',s,flags=re.M)
  s=re.sub(r'\[(\d+)\](?!\()',lambda m:f'[^{pref}{m[1]}]',s)
 # Chinese-labelled source lists and references.
 s=re.sub(r'^- \*\*\[([\u4e00-\u9fff]+\d+)\]\*\*\s*',lambda m:f'[^{m[1]}]: ',s,flags=re.M)
 s=re.sub(r'\[([\u4e00-\u9fff]+\d+)\](?!\()',lambda m:f'[^{m[1]}]',s)
 s=re.sub(r'^〔([\u4e00-\u9fff]+\d+)〕\s*',lambda m:f'[^{m[1]}]: ',s,flags=re.M)
 s=re.sub(r'〔([\u4e00-\u9fff]+\d+(?:、[\u4e00-\u9fff]+\d+)*)〕',lambda m:''.join('[^'+v+']' for v in m[1].split('、')),s)
 s=re.sub(r'^#{2,3} (?:引言注释|本章注释|本编引文与资料|本编引文与数据出处|本章文献说明|资料附编注释)\s*\n','',s,flags=re.M)
 parts.append(s.strip())
text='\n\n'.join(parts)+'\n'
defs=re.findall(r'^\[\^([^\]]+)\]:',text,re.M)
refs=re.findall(r'\[\^([^\]]+)\](?!:)',text)
missing=sorted(set(refs)-set(defs));dups=[k for k,v in collections.Counter(defs).items() if v>1]
assert not missing,("missing footnotes",missing)
assert not dups,("duplicate footnotes",dups)
assert '<!-- TRADE_TABLES -->' not in text
assert '/Users/' not in text
md=B/'胜利之后的欧洲_完整修订稿.md'
meta='''---
title: "胜利之后的欧洲"
subtitle: "拿破仑的另一条道路，1803—1848"
lang: zh-CN
date: "2026年9月修订本"
---

'''
md.write_text(meta+text)
subprocess.run(['/opt/homebrew/bin/pandoc',str(md),'--standalone','--toc','--toc-depth=2','--section-divs','--metadata','toc-title=全书目录','--include-in-header',str(B/'audit/book_style.html'),'--include-after-body',str(B/'audit/book_interactions.html'),'-o',str(B/'胜利之后的欧洲_阅读版.html')],check=True)
# Permit wide tables to scroll without widening the entire book.
h=B/'胜利之后的欧洲_阅读版.html';html=h.read_text();html=re.sub(r'<table\b([^>]*)>',r'<div class="table-scroll" tabindex="0" role="region" aria-label="数据表，可横向滚动"><table\1>',html).replace('</table>','</table></div>');html=html.replace('<section id="footnotes"','<h1 id="全书注释">全书注释与文献</h1>\n<section id="footnotes"');# Pandoc repeats the full text for repeated note calls; keep one note with return links.
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'html.parser'); seen={}; remap={}
for li in list(soup.select('section.footnotes > ol > li')):
    backs=li.select('a.footnote-back')
    for back in backs: back.extract()
    key=re.sub(r'\s+',' ',str(li.decode_contents())).strip()
    if key in seen:
        survivor,number=seen[key]
        for back in backs: survivor.append(' '); survivor.append(back)
        remap[li['id']]=(survivor['id'],number);li.decompose()
    else:
        number=len(seen)+1;seen[key]=(li,number);remap[li['id']]=(li['id'],number)
        for back in backs: li.append(' ');li.append(back)
for a in soup.select('a.footnote-ref'):
    target,number=remap[a['href'][1:]];a['href']='#'+target
    if a.sup:a.sup.string=str(number)
for li in soup.select('section.footnotes > ol > li'):
    backs=li.select('a.footnote-back')
    for i,a in enumerate(backs,1):
        if len(backs)>1:a.string='↩'+str(i)
        a['aria-label']='返回正文引用'+str(i)
html=str(soup);h.write_text(html)
# Column count check for all markdown tables.
errors=[];inside=False;columns=None
for n,line in enumerate(text.splitlines(),1):
 if line.startswith('|'):
  count=len(re.split(r'(?<!\\)\|',line))-2
  if not inside:columns=count
  elif count!=columns:errors.append([n,columns,count])
  inside=True
 else:inside=False
assert not errors,errors
root=B.parents[1]
ledger=list(__import__('csv').DictReader((B/'audit/材料文件总账.csv').open()))
original=[]
for r in ledger:
 if r['path'].startswith('final/r_5b1357a9c6-report/'):
  p=root/r['path'];actual=hashlib.sha256(p.read_bytes()).hexdigest();original.append({'path':r['path'],'unchanged':actual==r['sha256'],'sha256':actual})
assert len(original)==23 and all(r['unchanged'] for r in original)
qa={'characters_without_metadata':len(text),'han_characters':len(re.findall(r'[\u4e00-\u9fff]',text)),'chapters_including_introduction_appendix':len(chapters),'tables':len(re.findall(r'^\|[-: ]+\|',text,re.M)),'source_note_definitions':len(defs),'source_note_calls':len(refs),'missing_notes':missing,'duplicate_note_definitions':dups,'unused_note_definitions':sorted(set(defs)-set(refs)),'table_column_errors':errors,'original_report_files':original,'original_report_unchanged':True,'html_sha256':hashlib.sha256(html.encode()).hexdigest(),'markdown_sha256':hashlib.sha256(md.read_bytes()).hexdigest(),'limits':'Counts and static checks are not a claim of exhaustive archive reading, causal model validation, or whole-book PDF visual proof.'}
(B/'audit/verification.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in qa.items() if k!='original_report_files'},ensure_ascii=False,indent=2))
