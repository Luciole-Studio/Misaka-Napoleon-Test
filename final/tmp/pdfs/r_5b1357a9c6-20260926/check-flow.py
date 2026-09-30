from pathlib import Path
from pypdf import PdfReader
import json,re,unicodedata,difflib
w=Path(__file__).parent
norm=lambda s:re.sub(r'\s+','',unicodedata.normalize('NFC',s)).replace('\u00ad','')
pages=[p.extract_text() for p in PdfReader(w/'report.pdf').pages]
pages=[re.sub(r'\n\s*'+str(i)+r'\s*$','',t) for i,t in enumerate(pages,1)]
full=norm('\n'.join(pages));full2=norm(re.sub(r'(?<=\w)-\s*\n(?=\w)','','\n'.join(pages)))
miss=json.loads((w/'missing.json').read_text());remaining=[s for s in miss if norm(s) not in full and norm(s) not in full2]
print('Remaining after accounting for page footers and line-break hyphenation:',len(remaining))
for s in remaining:
 n=norm(s); prefix=n[:min(20,len(n))];pos=full.find(prefix)
 print('SOURCE:',s)
 if pos>=0:print('PDF:',full[pos:pos+len(n)+50])
(w/'flow-check.json').write_text(json.dumps({'remaining':remaining,'explained_by_page_footer_or_hyphenation':len(miss)-len(remaining)},ensure_ascii=False,indent=2))
