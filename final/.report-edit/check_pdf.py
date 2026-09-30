from pathlib import Path
from pypdf import PdfReader
import pdfplumber, re, json, hashlib
p=Path('/Users/makiko/Documents/exam/final'); f=p/'output/pdf/拿破仑反事实研究报告-学术润色版.pdf'; r=PdfReader(f)
assert hashlib.sha256((p/'r_b55f2c1cf5-report.md').read_bytes()).hexdigest()=='492b6b6790169ce9c8141c4ef1c50b91e69ae31e0b5509a55c5bedae0e0f3749'
for name in ('r_b55f2c1cf5-material-index.csv','r_b55f2c1cf5-report-polished.md'):
 assert r.attachments[name][0]==(p/name).read_bytes()
text='\n'.join(x.extract_text() for x in r.pages)
(p/'.report-edit/extracted-text.txt').write_text(text)
norm=re.sub(r'\s+','',text);s=(p/'r_b55f2c1cf5-report-polished.md').read_text()
urls=set(re.findall(r'https?://[^\s）]+',s));codes=set(re.findall(r'`([^`]+)`',s))
missing_codes=[v for v in codes if re.sub(r'\s+','',v) not in norm]
missing_urls=[v for v in urls if re.sub(r'\s+','',v) not in norm]
assert not missing_codes and not missing_urls,(missing_codes,missing_urls)
assert '\ufffd' not in text and '\u25a0' not in text
bad=[];stats=[]
with pdfplumber.open(f) as pdf:
 for i,page in enumerate(pdf.pages,1):
  chars=[c for c in page.chars if c['text'].strip()]
  # CJK line breaking deliberately permits a final punctuation glyph to hang.
  for c in chars:
   if c['x0']<55 or c['x1']>page.width-47 or c['top']<15 or c['bottom']>page.height-15:
    bad.append([i,c['text'],c['x0'],c['x1'],c['top'],c['bottom']])
   elif c['x1']>page.width-58 and c['text'] not in '、。，；：！？）】》」』”’.,;:!?)]':
    bad.append([i,'nonpunctuation outside frame',c['text'],c['x1']])
  body=[c for c in chars if 50<c['top']<790]
  stats.append([i,len(body),round(max((c['bottom'] for c in body),default=0),1)])
assert not bad,bad[:20]
links=[]
for page in r.pages:
 for ref in page.get('/Annots',[]):
  a=ref.get_object()
  if a.get('/A',{}).get('/URI'):links.append(str(a['/A']['/URI']))
assert len(links)>=16
result={'pages':len(r.pages),'attachments':list(r.attachments.keys()),'missing_code':missing_codes,'missing_url':missing_urls,'out_of_bounds':bad,'page_body_stats':stats,'uri_links':len(links),'original_unchanged':True}
(p/'.report-edit/pdf-qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print('PASS:',len(r.pages),'pages;',len(codes),'unique code locators;',len(urls),'URLs;',len(links),'PDF URI links; embedded attachments exact; original unchanged')
print('Sparse body pages',[s for s in stats if s[1]<180])
