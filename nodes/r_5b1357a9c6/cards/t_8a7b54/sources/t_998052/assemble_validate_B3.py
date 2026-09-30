#!/usr/bin/env python3
"""Assemble segmented manuscript and bounded checks. Not a source-support validator."""
from pathlib import Path
import csv,json,re,hashlib,subprocess,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[3]
build=subprocess.run([sys.executable,str(P/'build_B3.py')],check=True,capture_output=True,text=True)
(P/'build_receipt.json').write_text(build.stdout)
parts=[(P/f).read_text() for f in ['part_01_unit.md','part_02_quant_and_reactions.md','part_03_timeline.md','part_04_capacity_conclusion.md']]
text='\n\n'.join(parts).replace('{{HISTORICAL_TABLE}}',(P/'table_historical.md').read_text().strip())
text+='\n\n## 引用与复核\n\n逐条引文、实际阅读版本、来源URL、缓存和未决冲突详见[SOURCES.md](SOURCES.md)。主报告引用键均在其中展开。可复算但非统计拟合的模型参数见[model_assumptions.md](model_assumptions.md)。表格与分情景端点为配对规划包，不是概率置信带。\n'
(P/'B3_royal_navy.md').write_text(text)
records=list(csv.DictReader((P/'B3_capacity.csv').open()))
response=list(csv.DictReader((P/'B3_response.csv').open()))
calc=json.loads((P/'B3_calculations.json').read_text())
checks=[]
def test(label,condition):
    checks.append({'check':label,'pass':bool(condition)})
    if not condition:print('FAILED',label)
test('16 unit headings',all(f' {x} ' in text for x in '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯'))
timeline=[l for l in parts[2].splitlines() if re.match(r'^\|18\d{2}',l)]
test('29 dated timeline rows with evidence/confidence',len(timeline)==29 and all('[' in l and l.count('|')==5 for l in timeline))
test('8 policy rows',all('|B'+str(i)+' ' in parts[1] for i in range(1,9)))
test('no unresolved template placeholder','{{' not in text)
test('7 complete new annual observations',calc['annual_complete_rows']==7 and calc['annual_source_loaded'])
test('capacity 479 rows',len(records)==479)
test('16 paired responses',len(response)==16)
for r in response:
    test(f"{r['scenario']}/{r['bound']}/{r['year']} I<=A12<=H",0<=int(r['commissioned_line'])<=int(r['mobilizable_within_12months'])<=int(r['sea_line_hulls']))
for r in response:
    m=650*int(r['commissioned_line'])+280*int(r['standing_frigates'])+110*int(r['standing_small_cruisers'])+int(r['standing_other_personnel'])
    test(f"{r['scenario']}/{r['bound']}/{r['year']}:standing package",m==int(r['standing_total_personnel']) and 4_000_000+85*m==int(r['standing_cost_low']) and 6_000_000+105*m==int(r['standing_cost_high']))
for pkg in calc['packages']:
    m=650*pkg['line']+280*pkg['frigates']+110*pkg['small_cruisers']+pkg['other_personnel']
    test(f"package {pkg['package']} arithmetic",m==pkg['total_personnel'] and 4_000_000+85*m==pkg['cost_low'] and 6_000_000+105*m==pkg['cost_high'])
for y in range(1803,1816):
    d={r['metric']:int(r['value_low']) for r in records if r['section']=='observation' and str(r['year'])==str(y) and r['metric'].startswith('line_')}
    test(f'year{y}:line classifications',d['line_sea_commission']+d['line_sea_ordinary']==d['line_sea_total'] and sum(d['line_'+k] for k in ['sea_total','harbour_commission','harbour_ordinary','building_or_ordered'])==d['line_grand_total'])
# Verify exact recoverable strings/whitespace only, not the validity of accompanying claims.
quotes=[
('H13','3b214d7b54fb','If we suddenly disbanded, it would not be so easy a task, on an emergency, to recal our seamen'),
('H15','156d03703582','that expense now incurred for our armies would cease'),
('H17','245fa51bae26','The number of men which he had to propose was 19,000'),
('H20','7aa4f576eb19','23,000 men be employed for the sea service'),
('H21','95e29ff1c015','with the prospect of a long peace'),
('H30','597653e3e3aa','our naval force must partly depend upon that of other powers'),
('RMG-I','1b22dbe49e2a','After 1815, though not abolished, it was not used.'),
('RMG-M','2d8d72a79507','16 ships-of-the-line'),
('A-p356','f9c908249692','exports from British North America jumped from 4,442 to 16,729'),
('A-p368','f9c908249692','only one cargo of teak had reached England'),
('D-n50','b92bac3d423e',"Albion's tendency to exaggerate shortages should be noted however."),
('FR2','6864746209f3','Si les deux vaisseaux restent à Malamocco sans pouvoir sortir'),
('J23','c2105af935e9','The Nelson not having yet been at sea'),
('BJ','71106f9334bc','it will require the whole of the force now with me to equip and navigate them to England'),
]
qout=[]
for key,base,q in quotes:
    p=ROOT/'downloads/pages'/f'{base}.md';t=' '.join(p.read_text().split())
    ok=q in t;qout.append({'key':key,'path':str(p.relative_to(ROOT)),'quote':q,'whitespace_normalized_match':ok})
test('14 bounded quotations located',all(q['whitespace_normalized_match'] for q in qout))
result={'purpose':'Arithmetic, file structure and literal locator checks only; not proof of historical/model validity','checks':checks,'quote_checks':qout,'all_pass':all(x['pass'] for x in checks),'report_bytes':len(text.encode()),'timeline_rows':len(timeline),'model':'No regression, no fitted parameters, no battle simulation','limits':['annual1806-15 not image collated','no complete hemp/copper balance','A12 has no observed recall/repair schedule','budget conflicts preserved']}
(P/'B3_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
# Content hashes establish the exact delivery version and F3 input version.
manifest=[]
for f in ['B3_royal_navy.md','B3_capacity.csv','B3_response.csv','model_assumptions.md','SOURCES.md','build_B3.py','B3_calculations.json','sources/annual/annual_1809_1815.csv']:
    p=P/f;manifest.append({'kind':'B3_deliverable','path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for f in ['F3_capacity.csv','F3_model_parameters.json']:
    p=ROOT/'nodes/r_5b1357a9c6/cards/t_b1a536'/f;manifest.append({'kind':'F3_input_model_not_observation','path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(P/'delivery_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps({'all_pass':result['all_pass'],'checks':len(checks),'quotes_matched':sum(q['whitespace_normalized_match'] for q in qout),'timeline_rows':len(timeline),'report_bytes':result['report_bytes'],'capacity_rows':len(records),'response_rows':len(response)},ensure_ascii=False,indent=2))
if not result['all_pass']:
    print('Failures:',[c['check'] for c in checks if not c['pass']], 'Quote misses:',[q['key'] for q in qout if not q['whitespace_normalized_match']])
    sys.exit(1)
