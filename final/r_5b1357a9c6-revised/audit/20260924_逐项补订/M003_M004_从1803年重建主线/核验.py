from pathlib import Path
from collections import Counter
from urllib.parse import unquote
from bs4 import BeautifulSoup
import csv,json,re,hashlib,shutil,difflib
B=Path('/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised');E=B/'audit/20260924_逐项补订';W=E/'M003_M004_从1803年重建主线';R=W/'回源材料';root=B.parents[1]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def csvout(p,rows):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
copy={
'm003_amiens.pdf':'亚眠和约_1802_Fairburn印本.pdf',
'm003_1806_papers.md':'1806英法谈判_英国议会文书转录.md',
'm003_george.md':'乔治三世_18030518宣言_网页转录.md',
'm003_wilberforce.md':'Wilberforce_18030523发言_网页转录.md',
'm003_hicks.md':'Hicks_2006_为何发生耶拿战役.md',
'm003_tilsit_russia.md':'法俄提尔西特条约_法文转录.md',
'm003_tilsit_prussia.md':'法普提尔西特条约_法文转录.md'}
for a,b in copy.items():
 if (Path('/tmp')/a).exists():shutil.copy2(Path('/tmp')/a,R/b)
 else:assert (R/b).is_file()
for n in [1,8,11,12,13,14]:
 src=Path(f'/tmp/m003_amiens-{n:02d}.png');dst=R/f'亚眠和约_PDF第{n:02d}页.png'
 if src.exists():shutil.copy2(src,dst)
 else:assert dst.is_file()
manifest=json.loads((W/'修改前指纹.json').read_text());changed=[]
for r in manifest:
 p=Path(r['path'])
 if p.parent.name=='chapters' and h(p)!=r['sha256']:changed.append(p.name)
assert set(changed)=={'00_导论.md','01_法国的能力与代价.md','02a_英国海权与和平_国家财政与社会.md','06_东方与印度.md','07_行省化的边界.md','09_另一条十九世纪.md'}
old=(W/'修改前/胜利之后的欧洲_完整修订稿.md').read_text();new=(B/'胜利之后的欧洲_完整修订稿.md').read_text()
notes=lambda s:dict(re.findall(r'^\[\^([^\]]+)\]: (.*)$',s,re.M));a,b=notes(old),notes(new)
assert len(a)==213 and len(b)==220;assert set(a)<=set(b)
assert set(b)-set(a)=={f'导{i}' for i in range(2,9)}
changed_notes=[k for k in a if a[k]!=b[k]];assert changed_notes==['终1']
refs=lambda s:Counter(re.findall(r'\[\^([^\]]+)\](?!:)',s));x,y=refs(old),refs(new);assert not x-y
old_tables=re.findall(r'^\|.*(?:\n\|.*)*',old,re.M);new_tables=re.findall(r'^\|.*(?:\n\|.*)*',new,re.M)
assert len(old_tables)==62 and len(new_tables)==63
assert not Counter(old_tables)-Counter(new_tables)
old_fin=(W/'修改前/chapters/01_法国的能力与代价.md').read_text();new_fin=(B/'chapters/01_法国的能力与代价.md').read_text()
nums=lambda s:set(re.findall(r'\d+(?:[,，.]\d+)*(?:%|亿|万)?',s))
assert not nums(old_fin)-nums(new_fin),nums(old_fin)-nums(new_fin)
assert new_fin.count('172,763,591')==1 and new_fin.count('149,627,795')==1
assert new_fin.count('1811年4月30日')==1 and '戈丹' not in new_fin
assert round(149627795/172763591*100,2)==86.61
assert 55+7+20+10+12.5==104.5
qa=json.loads((B/'audit/verification.json').read_text());assert all(q['unchanged'] for q in qa['original_report_files']) and len(qa['original_report_files'])==23
soup=BeautifulSoup((B/'胜利之后的欧洲_阅读版.html').read_text(),'html.parser');ids=[v['id'] for v in soup.select('[id]')]
assert len(ids)==len(set(ids)); missing={unquote(z['href'][1:]) for z in soup.select('a[href^="#"]')}-set(ids);assert not missing
assert len(soup.select('section.footnotes > ol > li'))==220
assert len(soup.select('.table-scroll > table'))==63
intro=soup.find('section',id='引言-征服一片大陆然后呢')
# Locate using visible heading instead of depending on punctuation transliteration.
hd=next(z for z in soup.find_all('h1') if '引言' in z.get_text());intro=hd.parent
headings=[(int(z.name[1]),z.get_text()) for z in intro.find_all(re.compile(r'^h[1-6]$'))]
assert not [z for z in headings if z[0]==4],headings
p=B/'chapters/09_另一条十九世纪.md';s=p.read_text()
assert s.index('## 五、')<s.index('### 6．从行政让步')<s.index('## 六、')
assert '另一条历史确实存在于当时的能力和选择之中' not in s
assert '不是后来网页转录的1' not in s
assert '网页转录' in b['终9']
assert 'une réciprocité et d’une égalité parfaites' not in b['导8']
assert 'réciprocité et d’une' not in new
assert 'réciprocité et d\'une égalité parfaites' in (R/'法俄提尔西特条约_法文转录.md').read_text()
for name in changed+['build_book.py']:
 p=B/'chapters'/name if name.endswith('.md') else B/'audit'/name
 bef=W/'修改前/chapters'/name if name.endswith('.md') else W/'修改前'/name
 (W/name.replace('.md','.diff').replace('.py','.diff')).write_text(''.join(difflib.unified_diff(bef.read_text().splitlines(True),p.read_text().splitlines(True),fromfile='修改前/'+name,tofile='修改后/'+name)))
loc=[]
anchors={
'00_导论.md':['本书的核心判断是','### 从1803年','#### 1．','#### 2．','#### 3．','#### 4．','#### 5．','### 什么才算赢'],
'01_法国的能力与代价.md':['1811年4月30日，高丹','财政账自身还有时间差','新省带来的收入'],
'02a_英国海权与和平_国家财政与社会.md':['把公开交涉与私人盘算','**较早议和最值得'],
'06_东方与印度.md':['拿破仑的排序也会','这一交换把本章'],
'07_行省化的边界.md':['依导论所定尺度'],
'09_另一条十九世纪.md':['## 一、','### 6．从行政让步','拿破仑并非从不纠正','**本书最终选择','它最稳妥的对英底线']}
for name,starts in anchors.items():
 lines=(B/'chapters'/name).read_text().splitlines()
 for st in starts:
  found=[(n+1,line) for n,line in enumerate(lines) if line.startswith(st)];assert len(found)==1,(name,st)
  loc.append(dict(file=name,line=found[0][0],anchor=st,text=found[0][1]))
csvout(W/'正文落点与修订证据.csv',loc)
verification=dict(changed_chapters=changed,unchanged_other_chapters=6,chapter_count=12,old_note_identifiers_retained=213,old_note_texts_unchanged=212,expanded_old_note='终1：保留原说明，增加具体导2—导8回指',new_notes=[f'导{i}' for i in range(2,9)],old_note_calls_retained=394,current_note_calls=411,added_calls=dict(y-x),old_tables_preserved_exactly=62,new_criteria_tables=1,current_tables=63,first_chapter_unique_numeric_tokens_preserved=True,duplicate_finance_cases_consolidated=True,original_report_files_unchanged=23,missing_internal_anchors=[],duplicate_html_ids=[],intro_heading_levels=[v[0] for v in headings],book_visual_verified=False,source_images_read=['封面','印页9','印页12','印页13','印页14','印页15'],new_chinese_characters=qa['han_characters']-json.loads((W/'修改前/verification.json').read_text())['han_characters'],scope='六章相关段落联动修订；定向来源核读，不代表exam全材料已读或全书学术引用已验收。原有62表不变，新加1张判准表。',current_hashes={str(p.relative_to(B)):h(p) for p in list((B/'chapters').glob('*.md'))+[B/'audit/build_book.py',B/'胜利之后的欧洲_完整修订稿.md',B/'胜利之后的欧洲_阅读版.html']})
dump(W/'补订核验.json',verification)
dump(W/'回源材料指纹.json',[dict(path=str(p.relative_to(W)),sha256=h(p),bytes=p.stat().st_size) for p in sorted(R.iterdir())])
print(json.dumps(verification,ensure_ascii=False,indent=2))
