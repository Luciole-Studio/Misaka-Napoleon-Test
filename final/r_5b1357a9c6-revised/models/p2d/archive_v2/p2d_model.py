#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P2-D 动态行省化模型（条件算例，不是历史预测，不产生概率）。

用法：python3 p2d_model.py            # 跑全部轨道，输出CSV
      python3 p2d_model.py --sens     # 另跑参数敏感性

只用Python标准库。参数来自 regions.csv（地区）与本文件 TRACKS（轨道政策与冲击）。
设计说明见 README.md。所有函数形式与系数都是可替换的假设，已在 PARAMS 中集中列出。
"""
from __future__ import annotations

import csv
import itertools
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
YEARS = list(range(1803, 1849))

# ------------------------------------------------------------------ 可替换的全局假设
PARAMS = {
    # 抵抗向均衡值调整的速度（按Q2三剖面：低摩擦3—6年、中6—12年、高压单靠时间不回落）
    "adj_speed": {"L": 0.40, "M": 0.25, "H": 0.15},
    # 并合后适应（抵抗随年数下降）的上限与时间常数
    "adapt_max": {"L": 0.12, "M": 0.10, "H": 0.04},
    "adapt_tau": {"L": 3.0, "M": 6.0, "H": 12.0},
    # 征兵超过可承受水平时的抵抗增量系数
    "consc_w": 0.15,
    # 收编（本地精英任官、双语司法、代表权）对均衡抵抗的压低系数
    "coopt_w": 0.12,
    # 驻军密度：每千人 = base + k * R^2（按P2中档密度校准：R≈0.2→约2.5，R≈0.45→约6.6，R≈0.7→约13.8，R≈0.9→约21.8）
    "g_base": 1.5, "g_k": 25.0,
    # 逃役率与实收率
    "evasion": lambda R: min(0.85, 0.05 + 0.60 * R),
    "realization": lambda R: max(0.10, 1.0 - 0.80 * R),
    # 阶段升级门槛：R低于门槛且持续年数
    "stage2_R": 0.30, "stage2_years": 3,
    "stage3_R": 0.20, "stage3_years": 5,
    # 阶段倒退与脱离
    "regress_R": 0.60, "breakaway_R": 0.80, "breakaway_years": 2,
    # 兵均年费（法郎），在场率
    "unit_cost": 700.0, "presence": 0.85,
    # 法国本土安全与野战预备的基础需求（在场人数），不含新省驻军
    "base_demand": 330000.0,
    # 旧法国与内圈的常态驻防（在场），计入 base_demand 以外的地区驻军时不重复
    "old_france_garrison": 70000.0,
    # 干部：每省高级职位与带薪文官
    "senior_per_dept": 10, "civil_per_dept": 160,
    # 1815年以后民族意识上升（每年，乘以地区nat_w；联邦化改革可抵消一部分）
    "nat_rate": 0.004,
    # 皇帝在世且强制力完整时的脱离门槛，与继承危机期间的门槛
    "breakaway_R_strong": 0.90, "breakaway_R_weak": 0.78,
    # 藩属（B层）受民族意识影响的折扣
    "nat_B_factor": 0.5,
}


def load_regions():
    rows = {}
    with (ROOT / "regions.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            for k in ("pop_m", "departments", "R0", "church_w", "market_w", "consc_tol_per1000",
                      "ext_w", "sovereign_w", "nat_w", "frontier_per1000", "call_per1000", "reliable", "tax_gross_pc_fr",
                      "net_ratio", "debt_service_Mfr", "debt_service_cut_Mfr", "official_local0", "official_local_growth", "ally_roster",
                      "fr_present_as_B"):
                r[k] = float(r[k])
            rows[r["region"]] = r
    return rows


# ------------------------------------------------------------------ 轨道：控制层日程、政策与冲击
# layer: 'A' 并合省, 'B' 法典化藩属, 'C' 同盟, 'W' 战争占领（A或B名义下的战争状态）, 'N' 不在体系内, 'X' 已脱离
def sched(*pairs):
    return list(pairs)

BASE_LAYERS_1803 = {
    "old_france": "A", "d1_inner": "A", "parma": "B", "tuscany": "C", "valais": "C",
    "berg": "N", "westphalia": "N", "west_rest": "N", "holland": "B", "hanseatic": "N",
    "rome": "N", "illyria": "N", "catalonia": "C", "spain_ebro": "C", "north_italy": "B",
    "south_germany": "N", "naples": "N", "spain_rest": "C", "switzerland": "C",
    "warsaw": "N", "saxony": "N",
}

TRACKS = {
    # 史实日程作校验：1812年后不再推演（仅用于检查模型能否在1811—1813年显示压力）
    "hist": {
        "label": "史实（校验用，截至1813）",
        "end": 1813,
        "layers": {
            "parma": sched((1805, "A")), "tuscany": sched((1808, "A")), "valais": sched((1810, "A")),
            "berg": sched((1806, "B")), "westphalia": sched((1807, "B")), "west_rest": sched((1806, "C")),
            "holland": sched((1810, "A")), "hanseatic": sched((1811, "A")), "rome": sched((1809, "A")),
            "illyria": sched((1809, "A")), "catalonia": sched((1808, "W"), (1812, "A")),
            "spain_ebro": sched((1808, "W")), "south_germany": sched((1805, "C")), "naples": sched((1806, "B")),
            "spain_rest": sched((1808, "W")), "warsaw": sched((1807, "B")), "saxony": sched((1806, "C")),
        },
        "church": {y: 1.0 for y in range(1809, 1815)},
        "market": {**{y: 0.6 for y in range(1806, 1810)}, **{y: 1.0 for y in range(1810, 1815)}},
        "consc": {**{y: 1.0 for y in range(1803, 1808)}, **{y: 1.3 for y in range(1808, 1812)}, 1812: 1.8, 1813: 2.5},
        "ext": {y: 1.0 for y in range(1803, 1815)},
        "coopt": 0.30, "debt_cut": {"holland": 1810},
        "shocks": {1812: 0.03},
        "reserve": 0.0, "succession_year": None, "succession_shock": 0.0,
        # 战时陆军开支：以拿破仑1808—1813年战争预算量级为条件设定（待按F4卡与马里翁核定）
        "army_budget": {**{y: 300e6 for y in range(1803, 1808)}, **{y: 450e6 for y in range(1808, 1812)},
                        1812: 550e6, 1813: 550e6},
    },
    # 昙花一现：史实扩张逻辑照走；1812年与俄国在4月条件基础上妥协（决定D-F1），此后继续并合；
    # 西班牙战争、英法战争延续；1816年饥荒；皇帝死亡窗口1821（健康设定H）→继承危机
    "flash": {
        "label": "昙花一现",
        "end": 1848,
        "layers": {
            "parma": sched((1805, "A")), "tuscany": sched((1808, "A")), "valais": sched((1810, "A")),
            "berg": sched((1806, "B"), (1813, "A")), "westphalia": sched((1807, "B"), (1814, "A")),
            "west_rest": sched((1806, "C")), "holland": sched((1810, "A")), "hanseatic": sched((1811, "A")),
            "rome": sched((1809, "A")), "illyria": sched((1809, "A")),
            "catalonia": sched((1808, "W"), (1812, "A"), (1822, "X")), "spain_ebro": sched((1808, "W"), (1813, "A"), (1822, "X")),
            "south_germany": sched((1805, "C")), "naples": sched((1806, "B")), "spain_rest": sched((1808, "W"), (1822, "X")),
            "warsaw": sched((1807, "B")), "saxony": sched((1806, "C")), "switzerland": sched((1803, "C")),
        },
        "church": {**{y: 1.0 for y in range(1809, 1822)}, **{y: 0.5 for y in range(1822, 1849)}},
        "market": {**{y: 0.6 for y in range(1806, 1810)}, **{y: 1.0 for y in range(1810, 1849)}},
        "consc": {**{y: 1.0 for y in range(1803, 1808)}, **{y: 1.3 for y in range(1808, 1812)},
                  1812: 1.6, 1813: 1.6, 1814: 1.5, **{y: 1.4 for y in range(1815, 1849)}},
        "ext": {y: 1.0 for y in range(1803, 1849)},
        "coopt": 0.30, "debt_cut": {"holland": 1810},
        "shocks": {1812: 0.03, 1816: 0.06, 1817: 0.03, 1820: 0.03, 1830: 0.06, 1848: 0.08},
        "reserve": 0.0, "succession_year": 1821, "succession_shock": 0.10,
        "army_budget": {**{y: 300e6 for y in range(1803, 1808)}, **{y: 450e6 for y in range(1808, 1812)},
                        **{y: 550e6 for y in range(1812, 1816)}, **{y: 450e6 for y in range(1816, 1821)},
                        **{y: 380e6 for y in range(1821, 1849)}},
    },
    # 最可能（甲层）：1807年后停止扩张；帕尔马、托斯卡纳、瓦莱有条件并合；
    # 宗教不再冲突；封锁转为有限经济战；皇帝死亡窗口取1821—1830中段（1825），继承有预备
    "trackA": {
        "label": "最可能（甲层）",
        "end": 1848,
        "layers": {
            "parma": sched((1805, "A")), "tuscany": sched((1808, "A")), "valais": sched((1810, "A")),
            "berg": sched((1806, "B")), "westphalia": sched((1807, "B")), "west_rest": sched((1806, "C")),
            "holland": sched((1806, "B")), "hanseatic": sched((1806, "C")), "rome": sched((1808, "C")),
            "south_germany": sched((1805, "C")), "naples": sched((1806, "B")), "warsaw": sched((1807, "B")),
            "saxony": sched((1806, "C")), "switzerland": sched((1803, "C")),
        },
        "church": {},
        "market": {**{y: 0.6 for y in range(1806, 1808)}, **{y: 0.4 for y in range(1808, 1815)},
                   **{y: 0.25 for y in range(1815, 1849)}},
        "consc": {**{y: 1.0 for y in range(1803, 1808)}, **{y: 0.8 for y in range(1808, 1849)}},
        "ext": {**{y: 1.0 for y in range(1803, 1813)}, **{y: 0.3 for y in range(1813, 1849)}},
        "coopt": 0.50, "debt_cut": {},
        "shocks": {1812: 0.03, 1816: 0.06, 1817: 0.03, 1820: 0.02, 1830: 0.05, 1848: 0.07},
        "reserve": 0.4, "succession_year": 1821, "succession_shock": 0.05,
        "army_budget": {y: 300e6 for y in YEARS},
    },
    # 乙层主线（上帝视角）：每个节点采纳当时最好的方案；直辖只扩到帕尔马、托斯卡纳、瓦莱与（经请求的）贝格；
    # 封锁1810年起改造为关税同盟；宗教不冲突；荷兰、汉萨保留地位；1830年后对新省实行部分联邦化
    "trackB": {
        "label": "上帝视角主线（乙层）",
        "end": 1848,
        "layers": {
            "parma": sched((1805, "A")), "tuscany": sched((1808, "A")), "valais": sched((1810, "A")),
            "berg": sched((1806, "B"), (1812, "A")), "westphalia": sched((1807, "B")),
            "west_rest": sched((1806, "C")), "holland": sched((1806, "B")), "hanseatic": sched((1806, "C")),
            "rome": sched((1808, "C")), "south_germany": sched((1805, "C")), "naples": sched((1806, "B")),
            "warsaw": sched((1807, "B")), "saxony": sched((1806, "C")), "switzerland": sched((1803, "C")),
        },
        "church": {},
        "market": {**{y: 0.6 for y in range(1806, 1808)}, **{y: 0.3 for y in range(1808, 1810)},
                   **{y: 0.1 for y in range(1810, 1849)}},
        "consc": {**{y: 1.0 for y in range(1803, 1808)}, **{y: 0.8 for y in range(1808, 1849)}},
        "ext": {**{y: 1.0 for y in range(1803, 1813)}, **{y: 0.3 for y in range(1813, 1849)}},
        "coopt": 0.80, "debt_cut": {}, "federal": {y: 0.5 for y in range(1830, 1849)},
        "shocks": {1812: 0.03, 1816: 0.06, 1817: 0.03, 1820: 0.02, 1830: 0.05, 1848: 0.07},
        "reserve": 0.6, "succession_year": 1821, "succession_shock": 0.04,
        "army_budget": {y: 300e6 for y in YEARS},
    },
    # 强行成功（乙层＋丙层）：当时最好的方案组合＋登记运气；直辖范围扩大到约6000万人口；
    # 1825年前后"联邦化改革"（地方议会、双语、低征兵）——作为检验对象，而非预设成功
    "trackC": {
        "label": "强行成功（乙＋丙层；摄政期联邦化）",
        "end": 1848,
        "layers": {
            "parma": sched((1805, "A")), "tuscany": sched((1808, "A")), "valais": sched((1810, "A")),
            "berg": sched((1806, "B"), (1811, "A")), "westphalia": sched((1807, "B"), (1813, "A")),
            "west_rest": sched((1806, "C"), (1815, "A")), "holland": sched((1806, "B"), (1810, "A")),
            "hanseatic": sched((1806, "C"), (1811, "A")), "rome": sched((1808, "C")),
            "illyria": sched((1810, "A")), "north_italy": sched((1805, "B"), (1815, "A")),
            "south_germany": sched((1805, "C")), "naples": sched((1806, "B")), "warsaw": sched((1807, "B")),
            "saxony": sched((1806, "C")), "switzerland": sched((1803, "C"), (1815, "A")),
        },
        "church": {},
        "market": {**{y: 0.6 for y in range(1806, 1808)}, **{y: 0.3 for y in range(1808, 1811)},
                   **{y: 0.1 for y in range(1811, 1849)}},
        "consc": {**{y: 1.0 for y in range(1803, 1808)}, **{y: 0.9 for y in range(1808, 1825)},
                  **{y: 0.7 for y in range(1825, 1849)}},
        "ext": {**{y: 1.0 for y in range(1803, 1813)}, **{y: 0.3 for y in range(1813, 1849)}},
        "coopt": 0.80, "coopt_after": {1823: 1.0}, "debt_cut": {},
        # 联邦化改革放在摄政期（研究卡F1：最大行省化的真实窗口是摄政期而非皇帝在世期，α路径）
        "federal": {y: 1.0 for y in range(1823, 1849)},
        "shocks": {1812: 0.02, 1816: 0.06, 1817: 0.03, 1820: 0.02, 1830: 0.05, 1848: 0.07},
        # 健康设定H：1821年皇帝死亡；摄政有预备，冲击0.06。另设变体"奇迹M1"（健康到1836年）
        "reserve": 0.6, "succession_year": 1821, "succession_shock": 0.06,
        "army_budget": {**{y: 300e6 for y in range(1803, 1815)}, **{y: 330e6 for y in range(1815, 1849)}},
    },
}


def layer_at(track, region, year):
    lay = BASE_LAYERS_1803[region]
    for y, l in track["layers"].get(region, []):
        if year >= y:
            lay = l
    return lay


def simulate(track_key, P=PARAMS, regions=None, override=None):
    regions = regions or load_regions()
    T = json.loads(json.dumps({k: v for k, v in TRACKS[track_key].items() if k not in ("layers",)},
                              default=str))
    T = TRACKS[track_key]
    if override:
        T = {**T, **override}
    state = {}
    for r, d in regions.items():
        state[r] = {"R": d["R0"], "S": 3 if r == "old_france" else (2 if r == "d1_inner" else 0),
                    "years_A": 0 if r not in ("old_france", "d1_inner") else 10,
                    "low2": 0, "low3": 0, "high": 0, "lost": False, "recruit_hist": [],
                    "local_share": d["official_local0"]}
    yearly, events = [], []
    prev_balance = 0.0  # 上一年全国在场兵力余缺，用于判断镇压能力是否足以压住叛离
    for year in YEARS:
        if year > T["end"]:
            break
        church = T["church"].get(year, 0.0)
        market = T["market"].get(year, 0.0)
        consc = T["consc"].get(year, 1.0)
        ext = T["ext"].get(year, 0.0)
        coopt = T["coopt"]
        for y, v in sorted(T.get("coopt_after", {}).items()):
            if year >= y:
                coopt = v
        shock = T["shocks"].get(year, 0.0)
        if year in (1816, 1817):
            shock *= (1.0 - T["reserve"])  # 储备只能出于1811—12年粮荒后的当时理由；见README
        succ = T["succession_year"]
        agg = dict(track=track_key, year=year, pop_A=0.0, pop_B=0.0, pop_C=0.0, pop_W=0.0, pop_lost=0.0,
                   garrison_A=0.0, fr_in_B=0.0, ally_present=0.0, new_recruits=0.0, net_tax_new=0.0,
                   cadre_need_ext=0.0, stage0=0, stage1=0, stage2=0, stage3=0, meanR_outerA=0.0)
        outerA_R = []
        for r, d in regions.items():
            st = state[r]
            lay = "X" if st["lost"] else layer_at(T, r, year)
            if lay == "X" and not st["lost"]:
                st["lost"] = True; events.append((track_key, year, r, "放弃（按轨道日程撤出）"))
            prof = d["profile"]
            # 均衡抵抗
            debt = 0.15 if (r in T["debt_cut"] and year >= T["debt_cut"][r]) else 0.0
            call = d["call_per1000"] * consc
            consc_term = P["consc_w"] * max(0.0, call / max(0.1, d["consc_tol_per1000"]) - 1.0) if lay == "A" else 0.0
            adapt = P["adapt_max"][prof] * (1 - math.exp(-st["years_A"] / P["adapt_tau"][prof])) if lay == "A" else 0.0
            war = 0.35 if lay == "W" else 0.0
            sov = d["sovereign_w"] if lay == "A" and r not in ("old_france", "d1_inner") else 0.0
            fed = T.get("federal", {}).get(year, 0.0)
            nat = P["nat_rate"] * max(0, year - 1815) * d["nat_w"] * (1.0 - fed)
            if lay == "B":
                nat *= P["nat_B_factor"]
            elif lay not in ("A", "W"):
                nat = 0.0
            R_star = (d["R0"] + d["church_w"] * church + d["market_w"] * market + consc_term
                      + d["ext_w"] * ext + debt + war + sov * (1.0 - 0.5 * fed) + nat
                      - P["coopt_w"] * (coopt - 0.5) - adapt)
            if succ and year >= succ and year <= succ + 3 and r not in ("old_france",):
                R_star += T["succession_shock"] * (1.0 if r != "d1_inner" else 0.5)
            R_star = min(1.0, max(0.0, R_star))
            st["R"] = min(1.0, max(0.0, st["R"] + P["adj_speed"][prof] * (R_star - st["R"]) + shock))
            R = st["R"]
            if lay in ("A", "W") and r not in ("old_france", "d1_inner"):
                st["years_A"] += 1 if lay == "A" else 0
                if st["S"] == 0 and lay == "A":
                    st["S"] = 1
                st["low2"] = st["low2"] + 1 if R < P["stage2_R"] else 0
                st["low3"] = st["low3"] + 1 if R < P["stage3_R"] else 0
                if st["S"] == 1 and st["low2"] >= P["stage2_years"]:
                    st["S"] = 2; events.append((track_key, year, r, "进入阶段2（功能整合）"))
                if st["S"] == 2 and st["low3"] >= P["stage3_years"]:
                    st["S"] = 3; events.append((track_key, year, r, "进入阶段3（政治整合）"))
                if R > P["regress_R"] and st["S"] >= 2:
                    st["S"] -= 1; events.append((track_key, year, r, "阶段倒退"))
                weak = bool(succ and year >= succ) or T.get("weak_from", 9999) <= year
                thr = P["breakaway_R_weak"] if weak else P["breakaway_R_strong"]
                st["high"] = st["high"] + 1 if R > thr else 0
                # 叛离需要三件事同时成立：地方抵抗持续越过门槛；中央上一年已无余力（强势期要求缺兵逾10万，
                # 继承后只要有缺口）；外敌能够介入（强势期外援系数≥0.5，继承后≥0.3）或正逢冲击
                overstretched = prev_balance < (-100000.0 if not weak else 0.0)
                reachable = ext >= (0.5 if not weak else 0.3) or lay == "W"
                crisis = (succ and succ <= year <= succ + 4) or shock >= 0.05
                # 战争占领区（W）不因抵抗而"脱离"：只要法军仍在，就持续消耗驻军；放弃战区须由轨道日程决定（层级改为X）
                if lay == "A" and st["high"] >= P["breakaway_years"] and overstretched and (reachable or crisis):
                    st["lost"] = True; events.append((track_key, year, r, "脱离（叛离或被外敌夺取）"))
                    lay = "X"
            pop = d["pop_m"]
            if lay == "A":
                agg["pop_A"] += pop
                if r not in ("old_france", "d1_inner"):
                    dens = P["g_base"] + P["g_k"] * R * R + d["frontier_per1000"]
                    agg["garrison_A"] += pop * 1000 * dens
                    arrived = pop * 1e6 * call / 1000 * (1 - P["evasion"](R))
                    st["recruit_hist"].append(arrived * d["reliable"])
                    agg["new_recruits"] += sum(v * 0.9 ** i for i, v in enumerate(reversed(st["recruit_hist"][-5:])))
                    # 并合后由巴黎承接的旧债年息：若史实式削债则按削后额，并在抵抗项中另计削债惩罚
                    cut = r in T["debt_cut"] and year >= T["debt_cut"][r]
                    debt_srv = (d["debt_service_cut_Mfr"] if cut else d["debt_service_Mfr"]) * 1e6
                    agg["net_tax_new"] += pop * 1e6 * d["tax_gross_pc_fr"] * P["realization"](R) * d["net_ratio"] - debt_srv
                    st["local_share"] = min(0.95, st["local_share"] + d["official_local_growth"] * (1 + coopt))
                    ext_share = 1 - st["local_share"]
                    agg["cadre_need_ext"] += d["departments"] * (P["senior_per_dept"] + P["civil_per_dept"]) * ext_share
                    outerA_R.append((R, pop))
                    agg[f"stage{st['S']}"] += 1
            elif lay in ("B", "C") and bool(succ and year >= succ) and prev_balance < -50000.0 \
                    and R > (0.65 if lay == "B" else 0.60):
                # 继承后中央无力时，藩属与同盟改换保证人（里德条约式转向）
                st["lost"] = True; events.append((track_key, year, r, "藩属或同盟改换保护人"))
                agg["pop_lost"] += pop
            elif lay == "B":
                agg["pop_B"] += pop
                agg["fr_in_B"] += d["fr_present_as_B"] * (0.5 + R)  # 抵抗高时法国驻军须加
                agg["ally_present"] += d["ally_roster"] * max(0.0, 1 - R) * P["presence"]
            elif lay == "C":
                agg["pop_C"] += pop
                agg["ally_present"] += d["ally_roster"] * max(0.0, 1 - 1.2 * R) * P["presence"]
            elif lay == "W":
                agg["pop_W"] += pop
                agg["garrison_A"] += pop * 1000 * (P["g_base"] + P["g_k"] * R * R + d["frontier_per1000"])
            elif lay == "X":
                agg["pop_lost"] += pop
        if outerA_R:
            agg["meanR_outerA"] = sum(R * p for R, p in outerA_R) / sum(p for _, p in outerA_R)
        demand = P["base_demand"] + agg["garrison_A"] + agg["fr_in_B"]
        budget = T["army_budget"][year] + 0.5 * agg["net_tax_new"]
        fr_roster_paid = budget / P["unit_cost"]
        supply = fr_roster_paid * P["presence"] + agg["ally_present"]
        agg.update(demand_present=demand, budget_Mfr=budget / 1e6, fr_roster_paid=fr_roster_paid,
                   supply_present=supply, balance_present=supply - demand,
                   budget_needed_Mfr=max(0.0, (demand - agg["ally_present"]) / P["presence"]) * P["unit_cost"] / 1e6)
        agg["budget_gap_Mfr"] = agg["budget_needed_Mfr"] - agg["budget_Mfr"]
        prev_balance = agg["balance_present"]
        yearly.append(agg)
    return yearly, events


def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)


def main():
    regions = load_regions()
    all_events = []
    for key in TRACKS:
        yearly, events = simulate(key, regions=regions)
        for row in yearly:
            for k, v in list(row.items()):
                if isinstance(v, float):
                    row[k] = round(v, 3)
        write_csv(ROOT / f"out_{key}_yearly.csv", yearly)
        all_events += events
    write_csv(ROOT / "out_events.csv", [dict(track=a, year=b, region=c, event=d) for a, b, c, d in all_events])
    if "--sens" in sys.argv:
        sens = []
        for key, gk, adj, coopt in itertools.product(("flash", "trackA", "trackC"), (18.0, 25.0, 32.0),
                                                     (0.8, 1.0, 1.25), (-0.1, 0.0, 0.1)):
            P = {**PARAMS, "g_k": gk, "adj_speed": {k: v * adj for k, v in PARAMS["adj_speed"].items()}}
            T = TRACKS[key]
            yearly, events = simulate(key, P=P, regions=regions, override={"coopt": T["coopt"] + coopt})
            for yr in (1815, 1830, 1848):
                row = next((x for x in yearly if x["year"] == yr), None)
                if row:
                    sens.append(dict(track=key, g_k=gk, adj_mult=adj, coopt_shift=coopt, year=yr,
                                     pop_A=round(row["pop_A"], 2), pop_lost=round(row["pop_lost"], 2),
                                     balance_present=round(row["balance_present"]),
                                     budget_gap_Mfr=round(row["budget_gap_Mfr"], 1),
                                     meanR_outerA=round(row["meanR_outerA"], 3),
                                     breakaways=sum(1 for e in events if e[3].startswith("脱离") and e[1] <= yr)))
        write_csv(ROOT / "out_sensitivity.csv", sens)
    print("ok")


if __name__ == "__main__":
    main()
