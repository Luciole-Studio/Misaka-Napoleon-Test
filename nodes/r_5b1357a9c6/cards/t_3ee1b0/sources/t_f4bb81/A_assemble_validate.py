"""Mechanical assembly and bounded source-locator checks; not independent review.
Run from project root. Does not establish historical truth or source independence.
"""
from pathlib import Path
import re
import json

ROOT = Path.cwd()
HERE = ROOT / 'nodes/r_5b1357a9c6/cards/t_f4bb81'
parts = [HERE / f for f in ('part_01_core.md', 'part_02_policy.md', 'part_03_timeline.md')]
text = '\n\n'.join(p.read_text(encoding='utf-8').rstrip() for p in parts) + '\n'
(HERE / 'A_austria.md').write_text(text, encoding='utf-8')
sources = (HERE / 'SOURCES.md').read_text(encoding='utf-8')
paths = sorted(set(re.findall(r'`(downloads/[^`]+)`', sources)))
missing = [x for x in paths if not (ROOT / x).exists()]
heading_symbols = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯'
headings = {s: bool(re.search(r'^## '+s, text, re.M)) for s in heading_symbols}
timeline = re.findall(r'^\|([0-9]{1,2}) [^|]+\|', text, re.M)
policies = re.findall(r'^\|B([1-8]) ', text, re.M)
quotes = [
 ('T09-army','downloads/pages/603b19b5b0f9.md','150 000 hommes pendant la durée de la guerre maritime'),
 ('T09-payment','downloads/pages/603b19b5b0f9.md','85 millions de francs'),
 ('T12-corps','downloads/pages/0cb883e1dd4e.md','Il ne pourra toutefois être divisé'),
 ('T12-Porte','downloads/pages/0cb883e1dd4e.md','garantissent l’intégrité du territoire do la Porte Ottomane en Europe'),
 ('N0904','downloads/pages/064046ec6241.md','En demandant la Bohême'),
 ('N0515','downloads/pages/a947acecb6dc.md','Ayez un roi de votre choix'),
 ('H09','downloads/pages/ef06d5628e76.md','no permanent officer staff, no magazines'),
 ('M13-rolls','downloads/pages/848ad5b3b9ea.md','259,000 men remained on the army’s rolls'),
 ('M13-mobilized','downloads/pages/848ad5b3b9ea.md','298,000 men in fully mobilized formations'),
 ('CB16','downloads/pages/15d715a151a0.md','942 Millionen'),
 ('HU11','downloads/pages/9a8e1d55620d.md','törvénytelennek nyilvánítván'),
 ('AB','downloads/pages/7378b53aa48e.md','Jeder Mensch hat angeborne'),
 ('FR13','downloads/pages/9f08012c5301.md','la régence de l’Empire'),
 ('Z08','downloads/pages/25101e384c5e.md','l’attribution de la régence à une femme'),
 ('NII','downloads/pages/6c50590d5ddd.md','22 juillet 1832'),
]
def normalize(x):
    return re.sub(r'\s+', ' ', x.replace('’', "'").replace('\u00a0',' '))
quote_results=[]
for label,path,quote in quotes:
    original=(ROOT/path).read_text(encoding='utf-8')
    quote_results.append({'label':label,'path':path,'quote':quote,
                          'literal':quote in original,
                          'whitespace_apostrophe_normalized':normalize(quote) in normalize(original)})
report={'scope':'MECHANICAL_SELF_CHECK_NOT_REDTEAM',
        'assembled_chars':len(text),'all_sixteen_headings':all(headings.values()),
        'timeline_rows':len(timeline),'policy_rows':len(policies),
        'source_paths_checked':len(paths),'missing_source_paths':missing,
        'quote_checks':quote_results,
        'notes':['Normalization affects whitespace and apostrophe glyph only',
                 'Financial tables separately visually checked on PDF262/265/267',
                 'Quotes locate text, not prove causal claims',
                 'No independent review asserted']}
(HERE/'A_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
assert all(headings.values()) and len(timeline)==31 and len(policies)==8
assert not missing
