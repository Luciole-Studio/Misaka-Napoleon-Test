from pathlib import Path
import re,csv,json
B=Path('/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised'); A=B/'audit/20260924_出版验收复核'; rows=[]
pat=re.compile(r'结论|判断|最可能|更可能|较可能|最有可能|主线|退路|取决于|有条件|未必|可能.*也可能|是否.*尚|尚未|悬而未决|有望|更有希望|不确定|需要进一步|缺少.*资料|缺乏.*数据|既不|既无|不能.*也不能|无法.*也无法')
for f in sorted((B/'chapters').glob('*.md')):
 lines=f.read_text().splitlines(); heading=''
 for n,l in enumerate(lines,1):
  if l.startswith('#'): heading=l;continue
  if not l.strip() or re.match(r'^(?:〔[^〕]+〕|\[\d+\]|- \*\*\[)',l):continue
  if pat.search(l):rows.append({'id':f'V{len(rows)+1:03}', 'file':f.name,'line':n,'section':heading,'text':l,'cues':'、'.join(dict.fromkeys(pat.findall(l)))})
with (A/'结论与含混论证全稿候选.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
for start in range(0,len(rows),45):
 (A/f'含混核读_{start+1:03}_{min(start+45,len(rows)):03}.txt').write_text('\n\n'.join(f"{r['id']} {r['file']}:{r['line']} {r['section']}\n{r['text']}" for r in rows[start:start+45]))
print(len(rows));print([(f.name,len(f.read_text())) for f in A.glob('含混核读*')])
