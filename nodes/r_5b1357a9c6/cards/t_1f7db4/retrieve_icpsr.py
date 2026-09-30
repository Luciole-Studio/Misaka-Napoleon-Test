"""Public ICPSR page/API discovery; no authentication or access controls bypassed."""
from pathlib import Path
from urllib.request import Request,urlopen
import re,json,hashlib,datetime
ROOT=Path(__file__).resolve().parent
out=ROOT/'raw';out.mkdir(exist_ok=True)
u='https://www.icpsr.umich.edu/sites/jeh/view/studies/175583/versions/V1.0'
r=urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=35)
b=r.read(); (out/'icpsr_landing.html').write_bytes(b)
print('final_url',r.url,'size',len(b))
s=b.decode();print('\n'.join(re.findall(r'<script[^>]+src="([^"]+)"',s)))
(out/'icpsr_landing_provenance.json').write_text(json.dumps({'source_url':u,'final_url':r.url,'sha256':hashlib.sha256(b).hexdigest(),'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2))
