from pathlib import Path
from bs4 import BeautifulSoup
import re,csv,json,collections,difflib,hashlib,zipfile
B=Path(__file__).resolve().parents[2];W=Path(__file__).resolve().parent;C=B/'chapters';E=B/'audit/20260924_逐项补订';root=B.parents[1]
q=json.loads((B/'audit/verification.json').read_text());qa={}
soup=BeautifulSoup((B/'胜利之后的欧洲_阅读版.html').read_text(),'html.parser');ids=[x['id'] for x in soup.find_all(id=True)];idset=set(ids)
qa['duplicate_html_ids']=[k for k,v in collections.Counter(ids).items() if v>1];qa['unresolved_internal_hrefs']=sorted({a['href'] for a in soup.select('a[href^="#"]') if a['href'][1:] not in idset});qa['html_notes']=len(soup.select('section.footnotes > ol > li'));qa['html_note_calls']=len(soup.select('a.footnote-ref'));qa['html_tables']=len(soup.find_all('table'));qa['unrendered_note_markers']=re.findall(r'\[\^[^\]]+\]|〔[\u4e00-\u9fff]+\d+〕',soup.get_text());qa['missing_local_reader_links']=[a['href'] for a in soup.select('a[href]') if a['href'] and not a['href'].startswith(('#','http:','https:','mailto:','javascript:','data:')) and not (B/a['href']).exists()]
a=(W/'修改前/胜利之后的欧洲_完整修订稿.md').read_text();b=(B/'胜利之后的欧洲_完整修订稿.md').read_text();notes=lambda s:set(re.findall(r'^\[\^([^\]]+)\]:',s,re.M));qa['old_note_ids_removed']=sorted(notes(a)-notes(b));qa['new_note_ids']=sorted(notes(b)-notes(a));qa['original_report_23_files_unchanged']=q['original_report_unchanged'];qa['markdown_sha256']=q['markdown_sha256'];qa['html_sha256']=q['html_sha256']
for k in ['duplicate_html_ids','unresolved_internal_hrefs','unrendered_note_markers','missing_local_reader_links','old_note_ids_removed']:assert not qa[k],(k,qa[k])
assert qa['html_note_calls']==q['source_note_calls']==454;assert qa['html_notes']==q['source_note_definitions']==238;assert qa['html_tables']==q['tables']==69
stats=[];diff=[];removedrows=[]
for p in sorted(C.glob('*.md')):
 old=(W/'修改前/chapters'/p.name).read_text();new=p.read_text();d=list(difflib.unified_diff(old.splitlines(),new.splitlines(),fromfile=p.name+' before',tofile=p.name+' after',lineterm=''));diff.extend(d)
 stats.append({'chapter':p.name,'chars_before':len(old),'chars_after':len(new),'changed':old!=new,'added_lines':sum(x.startswith('+') and not x.startswith('+++') for x in d),'removed_lines':sum(x.startswith('-') and not x.startswith('---') for x in d),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 oldrows=collections.Counter(x for x in old.splitlines() if x.startswith('|'));newrows=collections.Counter(x for x in new.splitlines() if x.startswith('|'));removedrows.extend({'chapter':p.name,'old_row':x,'status':'地区或政策结论改写；非删除统计表'} for x in (oldrows-newrows).elements())
assert len(stats)==12 and all(r['changed'] for r in stats)
(W/'逐章差异.patch').write_text('\n'.join(diff)+'\n');(W/'逐章变更统计.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2));(W/'被改写的旧表行.json').write_text(json.dumps(removedrows,ensure_ascii=False,indent=2))
removed=[x[1:] for x in diff if x.startswith('-') and not x.startswith('---') and x[1:].strip()];(W/'替换段落核对.md').write_text('# 被替换原段逐项保留\n\n原有历史数据表留存；下列为替换原段的可回溯记录。旧的模糊终局、术语、来源及跨章条件已在对应新段改写。全书逐句编辑及全部原材料覆盖仍未完成。\n\n'+'\n\n'.join(removed))
qa['replaced_nonempty_lines']=len(removed);qa['rewritten_old_table_rows']=len(removedrows);qa['all_12_chapters_changed']=True
rows=list(csv.DictReader((E/'当前缺陷工作账.csv').open(encoding='utf-8-sig')));qa['ledger_rows']=len(rows);qa['conclusion_partials']=[r['id'] for r in rows if re.fullmatch(r'M\d+',r['id']) and r['state'].startswith('部分')];qa['citation_unclosed']=[r['id'] for r in rows if re.fullmatch(r'C\d+',r['id']) and not r['state'].startswith('已订正')];assert len(qa['citation_unclosed'])==90;assert len(qa['conclusion_partials'])==6
qa['coverage_claim']='12章节实质统稿与新增/替换关键段核读，不宣称全本逐句或全量材料读完';qa['whole_book_visual_verified']=False
manifest=json.loads((W/'模型与复算附件/来源清单.json').read_text());qa['copied_model_sources_unchanged']=all(hashlib.sha256((root/r['provenance']).read_bytes()).hexdigest()==r['sha256'] for r in manifest);assert qa['copied_model_sources_unchanged'];qa['model_source_file_count']=len(manifest)
with zipfile.ZipFile(B/'胜利之后的欧洲_模型与复算附件.zip') as z:qa['zip_crc_error']=z.testzip();assert qa['zip_crc_error'] is None
(W/'最终静态核验.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2))
# 将当前待修项单独列出，保留完整工作账，不把剩余边界当成已修。
openrows=[r for r in rows if r['id']!='M011' and (r['state'].startswith(('部分','未','待')) or r['id'] in ['SRC002','SRC005'])]
with (W/'当前未结缺陷.csv').open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(openrows)
print(json.dumps({k:v for k,v in qa.items() if k not in ['citation_unclosed','new_note_ids']},ensure_ascii=False,indent=2))
