#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P2笔记05：P2-D模型逐地区拆账（只读 models/p2d，不改任何参数与公式）。适用于模型v3（01:28版，含外部军事机会O与被动抵抗passive_w）。

第十一章各地区小节引用的"驻军需求、新兵存量、净税、B层法军、盟军在场"逐地区数字由本脚本得出。
做法：读取 models/p2d/p2d_model.py 源码，只在地区循环末尾插入一行日志（记录该地区当年的层级、
阶段、抵抗指数与各分项），其余代码原样执行；各分项按年加总与官方输出 out_<轨道>_yearly.csv 一致
（脚本末尾自动核对）。

用法：python3 P2_notes_05_逐地区拆账.py [输出CSV路径]
      缺省输出到当前目录 p2d_region_log.csv（请勿指向 models/p2d）。
"""
import csv
import sys
import types
from pathlib import Path

MODEL = Path('/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised/models/p2d/p2d_model.py')
src = MODEL.read_text(encoding='utf-8')
src = src.replace('    yearly, events = [], []\n', '    yearly, events = [], []\n    reglog = []\n', 1)
anchor = '            elif lay == "X":\n                agg["pop_lost"] += pop\n'
assert anchor in src, '模型源码结构已变，请更新插入点'
assert 'O_eff' in src and 'passive' in src, '本脚本按v3公式拆账；模型版本不符'
patch = '''            _dens = P["g_base"] + P["g_k"] * st["R"] * st["R"] * (0.35 + 0.65 * O_eff) + d["frontier_per1000"]
            _inner = r in ("old_france", "d1_inner")
            _gar = pop * 1000 * _dens if (lay in ("A", "W") and not _inner) else 0.0
            _rec = sum(v * 0.9 ** i for i, v in enumerate(reversed(st["recruit_hist"][-5:]))) if (lay == "A" and not _inner) else 0.0
            if lay == "A" and not _inner:
                _cut = r in T["debt_cut"] and year >= T["debt_cut"][r]
                _ds = (d["debt_service_cut_Mfr"] if _cut else d["debt_service_Mfr"]) * 1e6
                _tax = pop * 1e6 * d["tax_gross_pc_fr"] * P["realization"](min(1.0, st["R"] + passive)) * d["net_ratio"] - _ds
            else:
                _tax = 0.0
            _le = "X" if st["lost"] else lay
            _frB = d["fr_present_as_B"] * (0.5 + st["R"]) if _le == "B" else 0.0
            _ally = (d["ally_roster"] * max(0.0, 1 - st["R"]) * P["presence"] if _le == "B"
                     else (d["ally_roster"] * max(0.0, 1 - 1.2 * st["R"]) * P["presence"] if _le == "C" else 0.0))
            reglog.append(dict(track=track_key, year=year, region=r, layer=_le, R=round(st["R"], 3), S=st["S"], O=O_eff,
                               garrison=round(_gar), recruits_stock=round(_rec), net_tax_M=round(_tax / 1e6, 2),
                               fr_in_B=round(_frB), ally_present=round(_ally)))
'''
src = src.replace(anchor, anchor + patch, 1)
src = src.replace('    return yearly, events\n', '    return yearly, events, reglog\n', 1)
src = src.replace('if __name__ == "__main__":\n    main()', '')
mod = types.ModuleType('p2d_readonly')
mod.__file__ = str(MODEL)          # 让模型用 ROOT 读取 models/p2d/regions.csv
exec(compile(src, str(MODEL), 'exec'), mod.__dict__)

out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('p2d_region_log.csv')
assert 'models/p2d' not in str(out.resolve()), '不得写入 models/p2d'
regions = mod.load_regions()
rows = []
for key in mod.TRACKS:
    yearly, events, log = mod.simulate(key, regions=regions)
    rows += log
    by_year = {}
    for r in log:
        a = by_year.setdefault(r['year'], [0.0, 0.0, 0.0, 0.0])
        a[0] += r['garrison']; a[1] += r['net_tax_M']; a[2] += r['fr_in_B']; a[3] += r['ally_present']
    for y in yearly:
        a = by_year[y['year']]
        assert abs(a[0] - y['garrison_A']) < 5 and abs(a[1] - y['net_tax_new'] / 1e6) < 0.1 \
            and abs(a[2] - y['fr_in_B']) < 5 and abs(a[3] - y['ally_present']) < 5, (key, y['year'])
with out.open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
print('ok', len(rows), 'rows ->', out)
