from pathlib import Path
import json,re,hashlib,unicodedata,collections
from pypdf import PdfReader
import pdfplumber
w=Path(__file__).parent; r=PdfReader(w/'report.pdf');texts=[p.extract_text() for p in r.pages];text='\n'.join(texts);(w/'extracted.txt').write_text(text)
norm=lambda s:re.sub(r'\s+','',unicodedata.normalize('NFC',s)).replace('\u00ad','')
full=norm(text);strings=[]
def walk(x):
 if isinstance(x,dict):
  if x.get('t')=='Str':strings.append(x['c'])
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(json.loads((w/'source-ast.json').read_text()));miss=[s for s in strings if norm(s) not in full];(w/'missing.json').write_text(json.dumps(miss,ensure_ascii=False,indent=2))
charsource=collections.Counter(''.join(norm(s) for s in strings));charpdf=collections.Counter(full);missingchars=dict(charsource-charpdf)
bounds=[];stats=[]
with pdfplumber.open(w/'report.pdf') as doc:
 for n,p in enumerate(doc.pages,1):
  chars=[c for c in p.chars if c['text'].strip()]
  bad=[(c['text'],round(c['x0'],2),round(c['x1'],2),round(c['top'],2),round(c['bottom'],2)) for c in chars if c['x0']<40 or c['x1']>p.width-40 or c['top']<35 or c['bottom']>p.height-15]
  if bad:bounds.append([n,bad[:8]])
  stats.append({'page':n,'characters':len(chars),'xmin':min(c['x0'] for c in chars),'xmax':max(c['x1'] for c in chars),'ymin':min(c['top'] for c in chars),'ymax':max(c['bottom'] for c in chars)})
source=w.parents[2]/'r_5b1357a9c6-final-report.md';result={'pages':len(r.pages),'ast_string_nodes':len(strings),'missing_strings':len(miss),'missing_character_counts':missingchars,'source_unchanged':source.read_bytes()==(w/'source.md').read_bytes(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'bounds_errors':bounds,'stats':stats};(w/'qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='stats'},ensure_ascii=False,indent=2));print('missing examples',miss[:16])
