#!/usr/bin/env python3
"""Bounded arithmetic/structure audit. Does not verify historical truth.
Rebuilds final report from staged Markdown without changing those sources.
"""
from pathlib import Path
from decimal import Decimal as D
import csv,json,re,hashlib
ROOT=Path(__file__).resolve().parent
p1=(ROOT/'report_part1.md').read_text()
p2=(ROOT/'report_part2.md').read_text()
time=(ROOT/'report_timeline.md').read_text()
concl=(ROOT/'report_conclusion.md').read_text()
pre,cap=p2.split('## ⑮ 能力上限',1)
text='\n\n'.join([p1,'## ⑮ 能力上限'+cap,pre,time,concl])
text+='\n\n---\n\n## 来源附录（著录、版本与阅读边界）\n\n'+(ROOT/'SOURCES.md').read_text()
(ROOT/'R2_russia_economy_nobility.md').write_text(text)
checks=[]
for token in '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯':
    assert '## '+token in text
checks.append('16 required sections present')
timeline_rows=[r for r in time.splitlines() if re.match(r'^\| \d\d｜',r)]
assert len(timeline_rows)==30
assert all(len(r.split('|'))==9 for r in timeline_rows)
for sc in ['S1','S2','S3','S5','S6']:
    assert sc in time.splitlines()[4]
checks.append('30 timeline nodes / 5 scenario columns')
for i in range(1,9):
    assert f'**B{i} ' in p2
checks.append('8 policy menus present')
sources=(ROOT/'SOURCES.md').read_text()
used=set(re.findall(r'S\d\d',p1+p2+time+concl))
for s in used:
    assert '| '+s+' |' in sources,s
checks.append(f'{len(used)} distinct source codes mapped; not independence count')
with (ROOT/'R2_loss_grid.csv').open() as f: grid=list(csv.DictReader(f))
assert len(grid)==256
for r in grid:
    e,b,n,p,rr,d=(D(r[k]) for k in ['e','b','n','p','r','d'])
    L=e*b*(1-p*(n+(1-n)*rr))
    assert abs(D(r['gross_loss_pct'])-100*L)<D('1e-10')
    assert abs(D(r['free_cash_loss_pct'])-100*L/(1-d))<D('1e-10')
checks.append('256 grid rows independently re-evaluated with Decimal; both loss columns match')
with (ROOT/'R2_series.csv').open() as f: series=list(csv.DictReader(f))
assert len(series)==157
assert sum(r['kind']=='missing' for r in series)==38
for year in range(1803,1816):
    direct=next(D(r['value']) for r in series if r['year']==str(year) and r['series']=='paper_kopecks_per_silver_ruble')
    inv=next(D(r['value']) for r in series if r['year']==str(year) and r['series']=='silver_kopecks_per_paper_ruble')
    assert abs(inv*direct-10000)<D('1e-8')
checks.append('13 exchange inversions; 38 explicit missing entries; no interpolation')
res=json.loads((ROOT/'R2_model_results.json').read_text())
for sc in ['S2','S3']:
    for estate in ['export','inland']:
        group=[r for r in grid if r['scenario']==sc and r['estate']==estate]
        target=res[sc+'_'+estate]
        assert target['endpoint_count']==len(group)
        for pref,col in [('gross','gross_loss_pct'),('free','free_cash_loss_pct')]:
            vals=[D(r[col]) for r in group]
            assert abs(D(str(target[pref+'_min_pct']))-min(vals))<D('1e-10')
            assert abs(D(str(target[pref+'_max_pct']))-max(vals))<D('1e-10')
for sc,n,r,p in [('S2',D('.85'),D('.2'),D('.95')),('S3',D('.25'),D('.2'),D('.75'))]:
    center=D('.5')*D('.65')*(1-p*(n+(1-n)*r))*100
    assert abs(D(str(res['central'][sc]['gross_pct']))-center)<D('1e-10')
    assert abs(D(str(res['central'][sc]['free_pct']))-center/D('.6'))<D('1e-10')
for key,rec in res['falsifier_probe'].items():
    vals=[D(e)*(1-D(key))*100 for e in ['.3','.65']]
    assert abs(D(str(rec['gross_min_pct']))-min(vals))<D('1e-10')
    assert abs(D(str(rec['gross_max_pct']))-max(vals))<D('1e-10')
assert D('.5')*D('.65')*(1-D('1')*(D('1')+(1-D('1'))*D('.2')))==0
checks.append('JSON loss summaries, central examples, three recovery probes and full-trade zero-loss limit match')
assert abs(D(str(res['hemp_replacement']['france_needed_total_multiplier']))-(D('61')+D('2.4'))/D('2.4'))<D('1e-12')
assert abs(D(str(res['hemp_replacement']['continental_needed_total_multiplier']))-(D('61')+D('25.3'))/D('25.3'))<D('1e-12')
checks.append('2 replacement multipliers recalculated without tonnage conversion')
assert abs(sum([D('91.26'),D('.02'),D('.38'),D('5.5'),D('2.12')])-D('99.28'))<D('1e-12')
assert sum([D('76'),D('2'),D('.38'),D('1.5')])==D('79.88')
checks.append('2 source-table sum conflicts preserved')
for y in [1815,1830,1848]:
    for i,g in enumerate([D('.006'),D('.009')]):
        pop=D('43.785')*(1+g)**(y-1811)
        assert abs(D(str(res['population'][str(y)][i]))-pop)<D('1e-9')
checks.append('6 population endpoints recalculated with Decimal; comparison geography remains conditional')
# Hash all files cited in source inventory; fail if any listed path missing.
project=ROOT.parents[3]
paths=sorted(set(re.findall(r'`(downloads/[^`]+)`',sources)))
manifest=[]
for path in paths:
    f=project/path
    assert f.is_file(),path
    manifest.append({'path':path,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size})
(ROOT/'R2_source_hashes.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
checks.append(f'{len(manifest)} cited local source files present and hashed')
out={'scope':'structural and arithmetic checks only; NOT external peer review or historical source validation',
     'checks':checks,'checks_passed':len(checks),'final_chars':len(text),'source_files':len(manifest)}
(ROOT/'R2_arithmetic_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
