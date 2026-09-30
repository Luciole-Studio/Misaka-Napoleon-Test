#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Q1 事后描述层：政策束×结局、异常案例、比利时不可判定的来源。
纪律：本文件全部为 post-hoc 描述，不参与 Q1_codebook.md 冻结的反证检验；
样本小且非随机，比例只是本表内的计数，不是发生概率。
"""
import csv, os, json
from collections import defaultdict
from q1_analysis import load, COND

HERE = os.path.dirname(os.path.abspath(__file__))
rows = load()

def rate(grp, key):
    return (len(grp), sum(r[key] for r in grp), round(sum(r[key] for r in grp) / len(grp), 2)) if grp else (0, 0, None)

out = {"note": "post-hoc descriptive; small non-random sample; counts not probabilities"}

# 1. 政策束：S 主权破坏 / R 宗教政策冲突 / D 征兵冲击 / E 精英吸纳
bundles = defaultdict(list)
for r in rows:
    bundles[(r["S"], r["R"], r["D"], r["E"])].append(r)
tbl = []
for k in sorted(bundles):
    g = bundles[k]
    n, m, mr = rate(g, "mass_lo")
    _, s, sr = rate(g, "sustained_lo")
    tbl.append({"S": k[0], "R": k[1], "D": k[2], "E": k[3], "n": n,
                "mass_lo": m, "mass_rate": mr, "sustained_lo": s, "sustained_rate": sr,
                "cases": [x["case_id"] for x in g]})
out["policy_bundles"] = tbl

# 2. 政策条件数（S+R+D 的"挑衅计数"）与外援机会的交互
grid = {}
for prov in (0, 1, 2, 3):
    for o in (0, 1):
        g = [r for r in rows if (r["S"] + r["R"] + r["D"]) == prov and r["O"] == o]
        if g:
            n, m, mr = rate(g, "mass_lo")
            _, s, sr = rate(g, "sustained_lo")
            grid[f"provocations={prov},O={o}"] = {"n": n, "mass_rate": mr, "sustained_rate": sr,
                                                  "cases": [x["case_id"] for x in g]}
out["provocation_x_opportunity"] = grid

# 3. 异常案例：高风险配置却无大起义 / 低风险配置却有
hi_cfg, lo_cfg = "1101", "1010"
out["deviant_high_risk_quiet"] = [{"case_id": r["case_id"], "config": r["config"],
                                   "covariate_basis": r["covariate_basis"]}
                                  for r in rows if r["config"] == hi_cfg and r["mass_lo"] == 0]
out["deviant_low_risk_revolt"] = [{"case_id": r["case_id"], "config": r["config"],
                                   "covariate_basis": r["covariate_basis"]}
                                  for r in rows if r["config"] == lo_cfg and r["mass_lo"] == 1]

# 4. 比利时为何不可判定
be = {}
for cid in ("BE1798", "BE1802"):
    r = [x for x in rows if x["case_id"] == cid][0]
    same = [x for x in rows if x["config"] == r["config"] and x["case_id"] != cid]
    be[cid] = {"config": r["config"],
               "other_cases_in_cell": [x["case_id"] for x in same],
               "their_mass_lo": [x["mass_lo"] for x in same]}
out["belgium_indeterminacy"] = be

# 5. 单结局分布
out["outcome_distribution"] = {
    "mass_lo": sum(r["mass_lo"] for r in rows), "mass_hi": sum(r["mass_hi"] for r in rows),
    "sustained_lo": sum(r["sustained_lo"] for r in rows), "sustained_hi": sum(r["sustained_hi"] for r in rows),
    "exit_context": sum(r["exit_context"] for r in rows), "n": len(rows)}

# 6. 持续抵抗的必要条件检查（本样本内，非全域）
sus = [r for r in rows if r["sustained_lo"] == 1]
out["sustained_cases"] = [{"case_id": r["case_id"], "config": r["config"], "scale": r["scale"]} for r in sus]
out["sustained_necessity_within_sample"] = {c: sum(r[c] for r in sus) for c in COND + ["S", "D", "coast_access", "dynasty_exile", "brigand_tradition"]}
out["sustained_n"] = len(sus)

with open(os.path.join(HERE, "Q1_policy_profiles.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)

print(json.dumps(out["provocation_x_opportunity"], ensure_ascii=False, indent=1))
print("deviant quiet:", out["deviant_high_risk_quiet"])
print("deviant revolt:", out["deviant_low_risk_revolt"])
print("belgium:", json.dumps(out["belgium_indeterminacy"], ensure_ascii=False))
print("sustained necessity:", out["sustained_necessity_within_sample"], "of", out["sustained_n"])
print("dist:", out["outcome_distribution"])
