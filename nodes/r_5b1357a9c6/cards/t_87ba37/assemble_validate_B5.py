"""Assemble already-written sections and audit bounded claims. Not a truth gate."""
from pathlib import Path
import json,csv,re,hashlib
P=Path(__file__).resolve().parent
root=P.parents[3]
pieces=['report_01_capacity.md','report_02_reactions.md','report_03_model_conclusion.md']
text='\n\n'.join((P/x).read_text() for x in pieces)
sources=(P/'SOURCES.md').read_text()
(P/'B5_british_industry_trade.md').write_text(text+'\n\n---\n\n'+sources)
# Literal quotes from saved original captures; no semantics are certified.
queries=[
 ('downloads/pages/3b8b8e348c6d.md','Exports were not trade'),
 ('downloads/pages/3b8b8e348c6d.md','we ought to have returns'),
 ('downloads/pages/0cf6ab7705f7.md','they would willingly bear the pressure without a murmur'),
 ('downloads/pages/ba2ab29e8259.md','counterbalance, in some measure'),
 ('downloads/pages/92274137edfc.md','invaluable constitution'),
 ('downloads/pages/e5b32951df65.md','ce véritable ouragan qui secoua toute l’économie britannique'),
 ('downloads/pages/ead7fbfac794.md','interina e provisoriamente'),
 ('downloads/pages/cd205de92b28.md','the anticipated unrest did not happen'),
 ('downloads/pages/98f3132e9a36.md','widely evaded')]
def norm(s):
 return re.sub(r'\s+',' ',s).replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').strip().lower()
qc=[]
for path,q in queries:
 s=(root/path).read_text();qc.append(dict(source=path,quote=q,normalized_literal_match=norm(q) in norm(s)))
chron=[l for l in (P/'report_02_reactions.md').read_text().splitlines() if re.match(r'\|18\d\d',l)]
policy=[l for l in (P/'report_02_reactions.md').read_text().splitlines() if re.match(r'\|B[1-8] ',l)]
needed=list('①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯')
assert all('## '+x in text for x in needed)
assert len(chron)>=25 and len(policy)==8
annual=list(csv.DictReader((P/'B5_annual_exports_1803_1815.csv').open()))
a11=next(r for r in annual if r['year']=='1811')
assert abs(float(a11['usa_raw'])-float(a11['usa_corrected'])-10)<1e-8
assert abs(float(a11['total_corrected'])-27.459)<1e-8
assert next(r for r in annual if r['year']=='1813')['total_corrected']==''
markets=list(csv.DictReader((P/'B5_market_scenarios.csv').open()))
for r in markets:
 assert abs(float(r['total_after'])-(float(r['base_total'])-float(r['europe_loss'])+float(r['effective_extra'])))<1e-8
assert len(markets)==12
# Section excerpt ownership / lineage kept in notes. Do not overwrite source materials.
result={'report_bytes':len((text+'\n\n---\n\n'+sources).encode()),'chronology_nodes':len(chron),'policy_menu_rows':len(policy),'all_16_sections_present':True,'literal_quote_checks':qc,'all_literal_checks_pass':all(r['normalized_literal_match'] for r in qc),'market_identity_rows_checked':len(markets),'annual_missing_1813_retained':True,'BoE1811_raw_and_corrected_retained':True,'bounds_are_subjective_not_CI':True,'visual_verification':'Heckscher p175/242/245 and Marshall p74 image checks; Markdown layout not rendered','limitations':['Literal matching is not contextual support','No pure Latin America domestic cash series','No general-equilibrium or regression identification','Book and official-series copying share source lineages']}
(P/'B5_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
manifest={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in P.iterdir() if x.is_file() and x.suffix in ['.md','.csv','.json','.py','.xlsx'] and x.name!='B5_delivery_manifest.json'}
(P/'B5_delivery_manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
