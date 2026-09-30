#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Q1 反抗决定因素：配置比较 + 留一行/留一地区簇检验 + 敏感性。
输入 Q1_cases_frozen.csv（人工编码，逐行带出处）。
输出 Q1_dataset.csv（分析用派生列）、Q1_analysis_output.json、Q1_analysis_output.md。
纪律：算法与阈值在 Q1_codebook.md 中先行冻结；本脚本不做阈值搜索、不做显著性检验。
"""
import csv, json, itertools, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "Q1_cases_frozen.csv")
COND = ["T", "R", "E", "O"]          # 主四条件：地形庇护/宗教政策冲突/精英吸纳/外援机会
POS_HI, NEG_LO = 0.8, 0.2            # 冻结阈值
MIN_N = 2                            # 配置最小训练样本

KEY_POS = ["ES1808", "TY1809"]       # 用户指定反证：正例
KEY_NEG = ["RH1802", "BE1802"]       # 用户指定反证：负例
KEY_EXTRA_POS = ["BE1798"]           # 比利时1798必须仍为正例


def load(path=SRC):
    with open(path, encoding="utf-8") as fh:
        rows = [ {k: (v.strip() if isinstance(v, str) else v) for k, v in r.items()}
                 for r in csv.DictReader(fh) ]
    for r in rows:
        for k in ("mass_lo", "mass_hi", "sustained_lo", "sustained_hi",
                  "exit_context", "anti_french_explicit", "T", "R", "E", "O",
                  "S", "D", "X", "dynasty_exile", "brigand_tradition", "coast_access"):
            r[k] = int(r[k])
        r["start_year"] = int(r["start_year"]); r["end_year"] = int(r["end_year"])
        r["scale"] = None if r["scale"] == "NA" else int(r["scale"])
        r["config"] = "".join(str(r[c]) for c in COND)
    return rows


def outcome(row, which, bound):
    return row[f"{which}_{bound}"]


def truth_table(rows, which, bound):
    """观测配置表：只报有样本的行，不填逻辑余项。"""
    cells = defaultdict(list)
    for r in rows:
        cells[r["config"]].append(r)
    out = []
    for cfg in sorted(cells):
        grp = cells[cfg]
        n = len(grp)
        k = sum(outcome(r, which, bound) for r in grp)
        cons = k / n
        verdict = ("positive" if (n >= MIN_N and cons >= POS_HI) else
                   "negative" if (n >= MIN_N and cons <= NEG_LO) else
                   "contradictory" if n >= MIN_N else "thin")
        out.append({"config": cfg,
                    "conditions": dict(zip(COND, [int(x) for x in cfg])),
                    "n": n, "positives": k, "consistency": round(cons, 3),
                    "verdict": verdict,
                    "cases": [r["case_id"] for r in grp]})
    return out


def predict(train, cfg, which, bound):
    grp = [r for r in train if r["config"] == cfg]
    n = len(grp)
    if n < MIN_N:
        return None, n, None
    cons = sum(outcome(r, which, bound) for r in grp) / n
    if cons >= POS_HI:
        return 1, n, round(cons, 3)
    if cons <= NEG_LO:
        return 0, n, round(cons, 3)
    return None, n, round(cons, 3)


def loo(rows, which, bound, by_cluster=False):
    preds = []
    for r in rows:
        if by_cluster:
            train = [x for x in rows if x["cluster"] != r["cluster"]]
        else:
            train = [x for x in rows if x["case_id"] != r["case_id"]]
        p, n, cons = predict(train, r["config"], which, bound)
        preds.append({"case_id": r["case_id"], "cluster": r["cluster"],
                      "config": r["config"], "truth": outcome(r, which, bound),
                      "pred": p, "train_n": n, "train_consistency": cons,
                      "correct": None if p is None else int(p == outcome(r, which, bound))})
    decided = [p for p in preds if p["pred"] is not None]
    base = sum(outcome(r, which, bound) for r in rows) / len(rows)
    const_pred = 1 if base >= 0.5 else 0
    summary = {
        "n_cases": len(rows),
        "base_rate": round(base, 3),
        "constant_baseline_accuracy": round(
            sum(int(outcome(r, which, bound) == const_pred) for r in rows) / len(rows), 3),
        "coverage": round(len(decided) / len(rows), 3),
        "accuracy_on_decided": round(sum(p["correct"] for p in decided) / len(decided), 3) if decided else None,
        "correct_over_all_cases": round(sum(p["correct"] for p in decided) / len(rows), 3),
    }
    return preds, summary


def key_test(preds, rows, which, bound):
    """用户指定的反证门槛：模型须对西班牙/蒂罗尔/莱茵1802/比利时1802 全部作出判定，
    且判定与各案按来源编码的结局一致（want = 该案的编码真值，而不是预设方向）。
    另设防作弊断言：BE1798 的 mass 必须仍编码为 1，不得为通过检验而抹平比利时1798。
    注：BE1798 在 sustained 结局上按来源编码为 0（约两个月即被镇压），
    因此对该结局不要求方向为 1；早先版本在此处设了错误期望值，本版已修正。"""
    idx = {p["case_id"]: p for p in preds}
    detail, ok = {}, True
    for cid in KEY_POS + KEY_NEG + KEY_EXTRA_POS:
        p = idx.get(cid)
        if p is None:
            detail[cid] = {"status": "absent_from_subsample"}
            continue
        want = p["truth"]                       # 以来源编码为准
        passed = (p["pred"] is not None and p["pred"] == want)
        detail[cid] = {"coded_truth": want, "pred": p["pred"],
                       "train_n": p["train_n"], "train_consistency": p["train_consistency"],
                       "decided": p["pred"] is not None, "passed": passed}
        ok = ok and passed
    guard = [r for r in rows if r["case_id"] == "BE1798"]
    guard_ok = (not guard) or guard[0]["mass_lo"] == 1
    detail["_guard_BE1798_mass_coded_1"] = guard_ok
    return {"passed": bool(ok and guard_ok), "detail": detail}


def subsample(rows, name):
    if name == "main":
        return rows
    if name == "drop_general_negative":
        return [r for r in rows if r["negative_strength"] != "general"]
    if name == "drop_exit_context":
        return [r for r in rows if r["exit_context"] == 0]
    if name == "post1800_only":
        return [r for r in rows if r["start_year"] >= 1800]
    if name == "drop_ZH1804":
        return [r for r in rows if r["case_id"] != "ZH1804"]
    if name == "drop_uncertain_outcome":
        return [r for r in rows if r["mass_lo"] == r["mass_hi"] and r["sustained_lo"] == r["sustained_hi"]]
    if name == "narrowest_combo":
        return [r for r in rows if r["negative_strength"] != "general" and r["exit_context"] == 0
                and r["start_year"] >= 1800 and r["case_id"] != "ZH1804"
                and r["mass_lo"] == r["mass_hi"]]
    raise KeyError(name)


def recode(rows, name):
    """编码敏感性：对易内生/争议项整行翻转，不挑个案优化。"""
    out = [dict(r) for r in rows]
    if name == "none":
        return out
    for r in out:
        if name == "O_off_for_late_aid" and r["case_id"] in ("ES1808", "PT1807", "PA1806"):
            r["O"] = 0
        if name == "E_on_for_disputed" and r["case_id"] in ("CA1806", "HH1813", "RM1809", "NL1811"):
            r["E"] = 1
        if name == "R_on_for_catholic_annex" and r["case_id"] in ("BE1802", "TU1808", "EM1809", "VE1809"):
            r["R"] = 1
        r["config"] = "".join(str(r[c]) for c in COND)
    return out


def run_block(rows, which, bound, tag):
    preds_loo, sum_loo = loo(rows, which, bound, by_cluster=False)
    preds_log, sum_log = loo(rows, which, bound, by_cluster=True)
    return {"tag": tag, "outcome": which, "bound": bound,
            "truth_table": truth_table(rows, which, bound),
            "loo_row": {"summary": sum_loo, "key_test": key_test(preds_loo, rows, which, bound)},
            "logo_cluster": {"summary": sum_log, "key_test": key_test(preds_log, rows, which, bound),
                             "predictions": preds_log}}


def main():
    rows = load()
    results = {"n_total": len(rows),
               "clusters": sorted({r["cluster"] for r in rows}),
               "conditions": COND, "thresholds": {"positive": POS_HI, "negative": NEG_LO,
                                                  "min_cell_n": MIN_N},
               "blocks": []}

    # 主分析：mass 下界/上界；sustained 下界/上界
    for which in ("mass", "sustained"):
        for bound in ("lo", "hi"):
            results["blocks"].append(run_block(rows, which, bound, f"main::{which}_{bound}"))

    # 子样本敏感性（mass 下界）
    for sub in ("drop_general_negative", "drop_exit_context", "post1800_only",
                "drop_ZH1804", "drop_uncertain_outcome", "narrowest_combo"):
        sr = subsample(rows, sub)
        results["blocks"].append(run_block(sr, "mass", "lo", f"subsample::{sub} (n={len(sr)})"))

    # 编码敏感性（mass 下界）
    for rc in ("O_off_for_late_aid", "E_on_for_disputed", "R_on_for_catholic_annex"):
        results["blocks"].append(run_block(recode(rows, rc), "mass", "lo", f"recode::{rc}"))

    # 单条件的边际描述（非因果）
    marg = {}
    for c in COND + ["S", "D", "X", "dynasty_exile", "brigand_tradition", "coast_access"]:
        for v in (0, 1, 2):
            grp = [r for r in rows if r[c] == v]
            if grp:
                marg[f"{c}={v}"] = {"n": len(grp),
                                    "mass_lo_rate": round(sum(r["mass_lo"] for r in grp) / len(grp), 3),
                                    "sustained_lo_rate": round(sum(r["sustained_lo"] for r in grp) / len(grp), 3)}
    results["marginals"] = marg

    # 派生数据集
    with open(os.path.join(HERE, "Q1_dataset.csv"), "w", encoding="utf-8", newline="") as fh:
        cols = list(load()[0].keys())
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("NA" if r[k] is None else r[k]) for k in cols})

    with open(os.path.join(HERE, "Q1_analysis_output.json"), "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=1)

    # Markdown 汇总
    L = ["# Q1 分析输出（由 q1_analysis.py 生成，勿手改）", ""]
    L.append(f"案例 N={results['n_total']}；地区簇 {len(results['clusters'])} 个：{', '.join(results['clusters'])}")
    L.append(f"主条件 {COND}；正配置阈值≥{POS_HI}，负配置≤{NEG_LO}，最小样本 n≥{MIN_N}。")
    L.append("")
    for b in results["blocks"]:
        L.append(f"## {b['tag']}")
        s1, s2 = b["loo_row"]["summary"], b["logo_cluster"]["summary"]
        L.append(f"- 基率 {s1['base_rate']}；常数基准准确率 {s1['constant_baseline_accuracy']}")
        L.append(f"- 留一行：覆盖 {s1['coverage']}，判定集准确率 {s1['accuracy_on_decided']}，全样本正确率 {s1['correct_over_all_cases']}")
        L.append(f"- 留一地区簇：覆盖 {s2['coverage']}，判定集准确率 {s2['accuracy_on_decided']}，全样本正确率 {s2['correct_over_all_cases']}")
        kt = b["logo_cluster"]["key_test"]
        L.append(f"- 指定反证（留一簇）：{'通过' if kt['passed'] else '未通过'}")
        for cid, d in kt["detail"].items():
            L.append(f"  - {cid}: {d}")
        if b["tag"].startswith("main::"):
            L.append("- 观测配置表 (T,R,E,O)：")
            for c in b["truth_table"]:
                L.append(f"  - {c['config']} n={c['n']} 正例={c['positives']} 一致性={c['consistency']} {c['verdict']} :: {', '.join(c['cases'])}")
        L.append("")
    L.append("## 单条件边际（描述性，非因果）")
    for k, v in results["marginals"].items():
        L.append(f"- {k}: n={v['n']}, mass_lo={v['mass_lo_rate']}, sustained_lo={v['sustained_lo_rate']}")
    with open(os.path.join(HERE, "Q1_analysis_output.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")

    print("N =", results["n_total"])
    for b in results["blocks"]:
        kt = b["logo_cluster"]["key_test"]["passed"]
        print(f"{b['tag']:<46} LOGO cov={b['logo_cluster']['summary']['coverage']:<5} "
              f"acc={b['logo_cluster']['summary']['accuracy_on_decided']} keytest={'PASS' if kt else 'FAIL'}")


if __name__ == "__main__":
    main()
