"""P2-D v3 变体实验：去掉一个条件、换统治方法、英法战争延续等。条件算例。
运行：python3 variants.py  → 输出 out_variants.csv 与屏幕摘要。"""
import csv
from pathlib import Path
import p2d_model as m

ROOT = Path(__file__).resolve().parent
Y = m.YEARS

def hist_methods(ext_after_1813=0.3):
    """同一地图改用拿破仑1809—1813年的史实方法：教会冲突、市场排斥、荷兰削债、重征兵、低收编、无联邦化。"""
    return {
        "church": {y: 1.0 for y in range(1809, 1849)},
        "market": {**{y: 0.6 for y in range(1806, 1810)}, **{y: 1.0 for y in range(1810, 1849)}},
        "consc": {**{y: 1.0 for y in range(1803, 1808)}, **{y: 1.3 for y in range(1808, 1849)}},
        "coopt": 0.30, "coopt_after": {}, "federal": {}, "debt_cut": {"holland": 1810}, "market_access": [],
        "ext": {**{y: 1.0 for y in range(1803, 1813)}, **{y: ext_after_1813 for y in range(1813, 1849)}},
    }

VARIANTS = [
    ("trackA", "base", {}),
    ("trackA", "英国不议和", {"ext": {y: 1.0 for y in Y}}),
    ("trackB", "base", {}),
    ("trackB", "英国不议和（去掉L3）", {"ext": {y: 1.0 for y in Y}}),
    ("trackB", "去掉储备", {"reserve": 0.0}),
    ("trackB", "英国不议和且去掉储备", {"ext": {y: 1.0 for y in Y}, "reserve": 0.0}),
    ("trackC", "base（摄政期联邦化）", {}),
    ("trackC", "奇迹M1：健康到1836，1825联邦化",
     {"succession_year": 1836, "coopt_after": {1825: 1.0}, "federal": {y: 1.0 for y in range(1825, 1849)}}),
    ("trackC", "摄政拒绝联邦化", {"coopt_after": {}, "federal": {}}),
    ("trackC", "联邦化照做，英法战争延续", {"ext": {y: 1.0 for y in Y}}),
    ("trackC", "摄政拒绝联邦化＋英法战争延续", {"coopt_after": {}, "federal": {}, "ext": {y: 1.0 for y in Y}}),
    ("trackC", "不含伊利里亚（乙层地基：1809年奥地利不开战）",
     {"layers": {**{k: v for k, v in m.TRACKS["trackC"]["layers"].items() if k != "illyria"}}}),
    ("trackC", "同一地图改用史实方法（1813年后对英和平）", hist_methods(0.3)),
    ("trackC", "同一地图改用史实方法＋英法战争延续", hist_methods(1.0)),
    ("flash", "base", {}),
    ("flash", "1814年放弃西班牙",
     {"layers": {**m.TRACKS["flash"]["layers"],
                 "catalonia": m.sched((1808, "W"), (1812, "A"), (1814, "X")),
                 "spain_ebro": m.sched((1808, "W"), (1813, "A"), (1814, "X")),
                 "spain_rest": m.sched((1808, "W"), (1814, "X"))}}),
    ("flash", "永不放弃西班牙",
     {"layers": {**m.TRACKS["flash"]["layers"],
                 "catalonia": m.sched((1808, "W"), (1812, "A")),
                 "spain_ebro": m.sched((1808, "W"), (1813, "A")),
                 "spain_rest": m.sched((1808, "W"))}}),
    ("flash", "1812年后与教廷和解", {"church": {**{y: 1.0 for y in range(1809, 1813)}, **{y: 0.0 for y in range(1813, 1849)}}}),
]

def run():
    regions = m.load_regions()
    rows, summary = [], []
    for key, name, ov in VARIANTS:
        T = dict(m.TRACKS[key]); T.update(ov)
        saved = m.TRACKS[key]
        m.TRACKS[key] = T
        try:
            yearly, events = m.simulate(key, P=m.PARAMS, regions=regions)
        finally:
            m.TRACKS[key] = saved
        d = {r["year"]: r for r in yearly}
        pick = [yr for yr in (1812, 1815, 1816, 1817, 1821, 1823, 1825, 1830, 1840, 1848) if yr in d]
        for yr in pick:
            rows.append(dict(track=key, variant=name, year=yr, pop_A=round(d[yr]["pop_A"], 2),
                             balance_present=round(d[yr]["balance_present"]), budget_gap_Mfr=round(d[yr]["budget_gap_Mfr"], 1)))
        ev = [f"{a[1]}{a[2]}{a[3][:4]}" for a in events if ("脱离" in a[3] or "改换" in a[3] or "放弃" in a[3])]
        summary.append((key, name, {yr: round(d[yr]["balance_present"] / 1e4, 1) for yr in pick}, ev))
    with (ROOT / "out_variants.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    for key, name, bal, ev in summary:
        print(key, name, bal)
        if ev: print("   ", "；".join(ev))

if __name__ == "__main__":
    run()
