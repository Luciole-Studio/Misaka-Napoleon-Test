#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P2笔记07：第十一章在P2-D模型v3上的补充实验（只读 models/p2d，不写任何文件）。

官方变体见 models/p2d/variants.py 与 out_variants.csv。本脚本只补一组官方表里没有的组合：
①"同一地图改用史实方法"再加"皇帝健康到1836年"（只改继承年份，其余沿用 variants.hist_methods），注〔区144〕引用；
②托斯卡纳"并入支"（v3.1的甲、乙、丙三层不并托斯卡纳，这里改回1808年并入），注〔区c18〕引用；
③丙层"联邦化照做、英法战争延续"（只去掉奇迹M2），第七节运气表引用。

用法：python3 P2_notes_07_v3补充实验.py
"""
import sys

sys.dont_write_bytecode = True          # 不在 models/p2d 里生成 __pycache__
MODEL_DIR = '/Users/makiko/Documents/exam/final/r_5b1357a9c6-revised/models/p2d'
sys.path.insert(0, MODEL_DIR)
import p2d_model as m                    # noqa: E402
from variants import hist_methods        # noqa: E402

assert 'O_events' in m.TRACKS['hist'], '本脚本按v3编写；模型版本不符'
REGIONS = m.load_regions()


def run(key, override, label, years=range(1810, 1849)):
    T = dict(m.TRACKS[key]); T.update(override)
    saved = m.TRACKS[key]; m.TRACKS[key] = T
    try:
        yearly, events = m.simulate(key, P=m.PARAMS, regions=REGIONS)
    finally:
        m.TRACKS[key] = saved
    print('===', label)
    print(' | '.join(f"{r['year']}:直辖{r['pop_A']:.2f}百万 余缺{r['balance_present'] / 1e4:+.1f}万 缺钱{r['budget_gap_Mfr']:+.0f}百万"
                     for r in yearly if r['year'] in years))
    print('   事件：', '；'.join(f"{a[1]} {a[2]} {a[3]}" for a in events
                              if ('脱离' in a[3] or '改换' in a[3] or '放弃' in a[3])))


def tuscany_annexed(key):
    """托斯卡纳"并入支"：v3.1三层不并托斯卡纳；这里只把它改回1808年并入，读托斯卡纳自身的逐年数字。"""
    layers = dict(m.TRACKS[key]['layers']); layers['tuscany'] = m.sched((1808, 'A'))
    T = dict(m.TRACKS[key]); T['layers'] = layers
    saved = m.TRACKS[key]; m.TRACKS[key] = T
    m.REGION_LOG.clear()
    try:
        yearly, events = m.simulate(key, P=m.PARAMS, regions=REGIONS)
    finally:
        m.TRACKS[key] = saved
    d = REGIONS['tuscany']
    print('=== 托斯卡纳并入支（%s）：' % key, '；'.join(f"{a[1]}{a[3]}" for a in events if a[2] == 'tuscany'))
    rows = [r for r in m.REGION_LOG if r['region'] == 'tuscany' and r['layer'] == 'A']
    for r in rows:
        tax = d['pop_m'] * 1e6 * d['tax_gross_pc_fr'] * m.PARAMS['realization'](min(1.0, r['R'] + d['passive_w'])) * d['net_ratio'] / 1e6
        r['net_tax_M'] = round(tax, 2)
    for k in ('R', 'garrison_need', 'net_tax_M'):
        v = [r[k] for r in rows]
        print(f"   {k}: {min(v)}—{max(v)}")
    print('   全国余缺（万）：', {r['year']: round(r['balance_present'] / 1e4, 1) for r in yearly if r['year'] in (1812, 1815, 1830, 1848)})
    m.REGION_LOG.clear()


if __name__ == '__main__':
    tuscany_annexed('trackA')
    tuscany_annexed('trackC')
    run('trackC', {'ext': {y: 1.0 for y in m.YEARS}}, '联邦化照做，英法战争延续（只去掉奇迹M2；README变体表有此行，variants.py无）')
    run('trackC', hist_methods(0.3), '史实方法（1813年后对英和平），1821年继承（=官方变体，作核对）')
    hm = hist_methods(0.3); hm['succession_year'] = 1836
    run('trackC', hm, '史实方法（1813年后对英和平），皇帝健康到1836年')
    hm2 = hist_methods(1.0); hm2['succession_year'] = 1836
    run('trackC', hm2, '史实方法＋英法战争延续，皇帝健康到1836年')
