from urllib.request import urlopen,Request
from pathlib import Path
import re,json,hashlib
u='https://www.cambridge.org/core/journals/journal-of-economic-history/article/drafting-the-great-army-the-political-economy-of-conscription-in-napoleonic-france/FDBA5D70BC85C24186EF7C9767D249BF'
p=Path(__file__).resolve().parent/'raw'
b=urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
(p/'cambridge.html').write_bytes(b)
s=b.decode('utf8')
urls=set(re.findall(r'''(?:https?[^\s"'<>]+|/core/services/[^\s"'<>]+)''',s))
print('\n'.join(x for x in sorted(urls) if any(y in x.lower() for y in ['suppl','sup0','mmc','s0022050723000360sup'])))
(p/'cambridge_html_provenance.json').write_text(json.dumps({'url':u,'sha256':hashlib.sha256(b).hexdigest(),'purpose':'public supplementary file links not preserved by page reader'},indent=2))
