#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Q1 预测层：把八个假想区×政策档的条件假设映射到样本内可观测的类比配置。
纪律：因关键反证未通过（见 Q1_analysis_output.md），本层不输出模型预测概率。
脚本只做两件事：(1) 计算每个假设条件向量在样本中的类比证据；(2) 原样带出
研究者条件裁量区间（人工填写于 Q1_prediction_assumptions.csv），并标注其非统计性质。
"""
import csv, json, os
from q1_analysis import load, COND

HERE = os.path.dirname(os.path.abspath(__file__))
rows = load()
with open(os.path.join(HERE, "Q1_prediction_assumptions.csv"), encoding="utf-8") as fh:
    preds = list(csv.DictReader(fh))

out = []
for p in preds:
    cfg = "".join(p[c] for c in COND)
    cell = [r for r in rows if r["config"] == cfg]
    n = len(cell)
    bundle = [r for r in rows if (r["S"], r["R"], r["D"], r["E"]) ==
              (int(p["S"]), int(p["R"]), int(p["D"]), int(p["E"]))]
    rec = {
        "region": p["region"], "scenario": p["scenario"],
        "conditions": {c: int(p[c]) for c in COND + ["S", "D"]},
        "analogue_config": cfg,
        "analogue_n": n,
        "analogue_mass_rate": round(sum(r["mass_lo"] for r in cell) / n, 2) if n else None,
        "analogue_sustained_rate": round(sum(r["sustained_lo"] for r in cell) / n, 2) if n else None,
        "analogue_cases": [r["case_id"] for r in cell],
        "policy_bundle_n": len(bundle),
        "policy_bundle_mass_rate": round(sum(r["mass_lo"] for r in bundle) / len(bundle), 2) if bundle else None,
        "policy_bundle_cases": [r["case_id"] for r in bundle],
        "judgement_band_mass": [float(p["mass_band_lo"]), float(p["mass_band_hi"])],
        "judgement_band_sustained": [float(p["sustained_band_lo"]), float(p["sustained_band_hi"])],
        "band_basis": p["band_basis"], "flip_evidence": p["flip_evidence"],
        "band_status": "researcher conditional judgement; NOT an empirical frequency, "
                       "NOT a calibrated probability, NOT a model output",
    }
    out.append(rec)

with open(os.path.join(HERE, "Q1_prediction_output.json"), "w", encoding="utf-8") as fh:
    json.dump({"warning": "key falsifier failed; numerical model prediction withheld by contract",
               "rows": out}, fh, ensure_ascii=False, indent=1)

hdr = f"{'区域':<8}{'档':<12}{'配置':<6}{'n':<3}{'类比mass':<9}{'类比sust':<9}{'裁量mass':<14}{'裁量sust'}"
print(hdr)
for r in out:
    print(f"{r['region']:<8}{r['scenario']:<12}{r['analogue_config']:<6}{r['analogue_n']:<3}"
          f"{str(r['analogue_mass_rate']):<9}{str(r['analogue_sustained_rate']):<9}"
          f"{str(r['judgement_band_mass']):<14}{r['judgement_band_sustained']}")
