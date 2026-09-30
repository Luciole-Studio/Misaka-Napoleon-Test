#!/usr/bin/env python3
"""Builds out_summary.md from out_snapshots.csv and out_sensitivity.csv (run navy_model.py first)."""
import csv
from pathlib import Path
HERE = Path(__file__).resolve().parent
LAB = {'jia': '最可能（甲）', 'flash': '昙花一现', 'yi': '强行成功·乙层', 'bing': '强行成功·丙层'}
snap = list(csv.DictReader((HERE / 'out_snapshots.csv').open()))
sens = list(csv.DictReader((HERE / 'out_sensitivity.csv').open()))
def g(tr, env, y, k):
    r = next(r for r in snap if r['track'] == tr and r['envelope'] == env and int(r['year']) == y)
    return float(r[k])
ONE = ('British strong response only (France base)', 'British weak response only (France base)',
       'French unfavourable only (Britain base)', 'French favourable only (Britain base)')
def one(tr, y, k):
    v = [float(r[k]) for r in sens if r['track'] == tr and int(r['year']) == y and r['test'] in ONE]
    return min(v), max(v)
L = ['# 海军模型结果摘要（条件算例，不是预测或置信区间）', '',
     '单位：H＝战列舰舰体（年中存量）；A12＝一年内可动员整舰；T＝舰体排水吨位比（法÷英）；TA＝可动员舰吨位比（法÷英）。',
     '"单因素区间"＝只换英国反应强弱或只换法国参数高低时的最小—最大；"外包络"＝法国不利参数配英国强反应、法国有利参数配英国弱反应。', '',
     '|轨道|年|法H|法A12|英H|英A12|T 基准（外包络）|TA 基准|TA 单因素区间|TA 外包络|英国海军费用£m（1812价）|',
     '|---|---:|---:|---:|---:|---:|---|---:|---|---|---:|']
for tr in ('jia', 'flash', 'yi', 'bing'):
    for y in (1815, 1830, 1848):
        T0, Tl, Tu = g(tr, 'base', y, 'T_hull_tonnage'), g(tr, 'lower', y, 'T_hull_tonnage'), g(tr, 'upper', y, 'T_hull_tonnage')
        A0, Al, Au = g(tr, 'base', y, 'T_A12_tonnage'), g(tr, 'lower', y, 'T_A12_tonnage'), g(tr, 'upper', y, 'T_A12_tonnage')
        o1, o2 = one(tr, y, 'T_A12')
        L.append(f"|{LAB[tr]}|{y}|{g(tr,'base',y,'fr_H'):.0f}|{g(tr,'base',y,'fr_A12'):.0f}|{g(tr,'base',y,'uk_H'):.0f}|{g(tr,'base',y,'uk_A12'):.0f}|"
                 f"{T0:.2f}（{min(Tl,Tu):.2f}—{max(Tl,Tu):.2f}）|{A0:.2f}|{o1:.2f}—{o2:.2f}|{min(Al,Au):.2f}—{max(Al,Au):.2f}|{g(tr,'base',y,'uk_cost_GBPm'):.1f}|")
L += ['', '## 敏感性（基准参数，一次改一项）', '', '|轨道|检验|年|法H|法A12|英H|英A12|T|TA|英国费用£m|', '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for r in sens:
    L.append(f"|{LAB[r['track']]}|{r['test']}|{r['year']}|{float(r['fr_H']):.0f}|{float(r['fr_A12']):.0f}|{float(r['uk_H']):.0f}|{float(r['uk_A12']):.0f}|{float(r['T_hull']):.2f}|{float(r['T_A12']):.2f}|{float(r['uk_cost']):.1f}|")
(HERE / 'out_summary.md').write_text('\n'.join(L) + '\n')
print('\n'.join(L[:20]))
