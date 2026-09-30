#!/usr/bin/env python3
"""Assemble staged Markdown; validate deliverables and retain a manifest.
No history data are generated here. This does not authenticate historical assumptions.
"""
from pathlib import Path
import csv,hashlib,json
R=Path(__file__).resolve().parent
text='\n'.join((R/p).read_text() for p in ['report_part1.md','report_part2.md'])
(R/'Q2_integration_panel.md').write_text(text)
expected=['Q2_integration_panel.md','Q2_panel.csv','Q2_published_estimates.csv','Q2_calculations.csv','Q2_assumptions.csv','Q2_model_paths.csv','Q2_model_summary.csv','Q2_stock_sensitivity.csv','Q2_fiscal_thresholds.csv','Q2_target_regions.csv','Q2_leave_one_audit.csv','Q2_validation.json','Q2_run_log.txt','SOURCES.md','quote_audit.md','notes_final_validation.md','report_part1.md','report_part2.md','build_panel.py','analyze_q2.py','finalize_q2.py']
manifest=[]
for name in expected:
    p=R/name;assert p.is_file() and p.stat().st_size>0,name
    b=p.read_bytes();entry={'file':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
    if p.suffix=='.csv':
        with p.open(encoding='utf-8-sig') as f:rr=list(csv.DictReader(f))
        entry['data_rows']=len(rr)
        assert all(None not in r for r in rr),name
    manifest.append(entry)
# Final model must have total five-year term INCLUDING training.
with (R/'Q2_model_summary.csv').open(encoding='utf-8-sig') as f:ss=list(csv.DictReader(f))
a=next(r for r in ss if r['profile']=='L' and r['year_since_annexation']=='10')
assert float(a['net_stock_min'])==-38.3 and float(a['net_stock_max'])==5318.2
for s in ss:
    lo=f"{float(s['net_stock_min'])/1000:+.2f}".replace('-','−')
    hi=f"{float(s['net_stock_max'])/1000:+.2f}".replace('-','−')
    assert f'{lo}至{hi}' in text,(s['profile'],s['year_since_annexation'])
counts={e['file']:e.get('data_rows') for e in manifest}
for name,n in [('Q2_panel.csv',116),('Q2_published_estimates.csv',8),('Q2_calculations.csv',46),('Q2_model_paths.csv',3840),('Q2_stock_sensitivity.csv',108),('Q2_target_regions.csv',8),('Q2_leave_one_audit.csv',6)]:
    assert counts[name]==n,(name,counts[name])
with (R/'Q2_panel.csv').open(encoding='utf-8-sig') as f:panel=list(csv.DictReader(f))
sources=(R/'SOURCES.md').read_text()
assert all(f"|{r['source_id']}|" in sources for r in panel)
assert sum(r['value']=='' for r in panel)==13
assert '−0.04至+5.32' in text
assert '未运行新回归或统计留一预测' in text
assert '预算不是实收' in text
assert text.count('## ')>=11
(R/'Q2_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'files_checked':len(expected),'report_lines':len(text.splitlines()),'report_characters':len(text),'checks':'PASS: presence, CSV structure/counts, source-ID crosswalk, all nine model-summary net ranges and caveats only; not historical or causal validation'},ensure_ascii=False,indent=2))
