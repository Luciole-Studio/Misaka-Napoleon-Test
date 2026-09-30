#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Last Order 终审补算：竞争路径 E「S2本义」= 史实（S0政策向量）打到1807年提尔西特，
自1808年起切换为路径B的两个开关（保护性关税+关税容忍；B4b保波旁）、教廷和解、不并荷汉、不征俄。
只调用 P6 引擎（t_c87512/p6_wargame.py）的参数与函数，不改写该卡任何文件；输出写本目录。
两个变体：E_literal = 引擎原状态机（1807柏林敕令一旦置 blood_tax_over 即永久）；
          E_reset  = 1808切换为保护性关税且无对俄战争后重置 blood_tax_over（依G1：Ried机制=替代担保人∧血税超限(1812灭军)，
                     单凭1807封锁不触发），其余与引擎完全相同。
"""
import sys, os, csv, json
sys.path.insert(0, "/Users/makiko/Documents/exam/nodes/r_5b1357a9c6/cards/t_c87512")
import p6_wargame as W

bp = W.base_policy
PATH_E = {
 1805: (bp(blockade="none", navy_budget=120.0, austria="humiliate", austria_war=True),
        "史实：乌尔姆-奥斯特里茨-普雷斯堡；特拉法加"),
 1806: (bp(blockade="strict", navy_budget=60.0, austria="humiliate"),
        "史实：耶拿-奥尔施泰特；柏林敕令；莱茵邦联"),
 1807: (bp(blockade="strict", navy_budget=60.0, russia="neutral", poland="duchy", prussia="rump",
           austria="humiliate", outer_ring=False),
        "史实：弗里德兰-提尔西特；残普+华沙公国+俄入体系"),
 1808: (bp(britain="settle", blockade="protective", navy_budget=110.0, russia="neutral", poland="duchy",
           prussia="rump", austria="partner", spain="ally_bourbon"),
        "【开关】特里亚农型保护关税提前+对俄关税容忍（不签米兰敕令）；【B4b】不废西王、联姻去条件化；对奥改保证（1805后不再羞辱）"),
 1809: (bp(britain="settle", blockade="protective", navy_budget=120.0, russia="neutral", poland="duchy",
           prussia="rump", austria="partner", spain="ally_bourbon"),
        "教廷和解、不并罗马；无西班牙泥潭→奥地利无1809窗口（A卡S5-A）"),
 1810: (bp(britain="settle", blockade="protective", navy_budget=130.0, russia="neutral", poland="duchy",
           prussia="rump", austria="partner", spain="ally_bourbon"),
        "不并荷兰汉萨，分层准入；奥婚（在普雷斯堡后的奥地利有史实动机）"),
 1811: (bp(britain="settle", blockade="protective", navy_budget=150.0, russia="neutral", poland="duchy",
           prussia="rump", austria="partner", spain="ally_bourbon"),
        "统合公债；接受俄1810关税（B7''v3）；不吞奥尔登堡"),
 1812: (bp(britain="settle", blockade="protective", navy_budget=170.0, russia="neutral", poland="duchy",
           prussia="rump", austria="partner", spain="ally_bourbon"),
        "不征俄；B1b 1811–14窗：欧洲总和约谈判"),
 1813: (bp(britain="settle", blockade="protective", navy_budget=180.0, russia="neutral", poland="duchy",
           prussia="rump", austria="partner", spain="ally_bourbon", posture="S5"),
        "和约执行：降为S5姿态"),
 1814: (bp(britain="settle", blockade="protective", navy_budget=190.0, russia="neutral", poland="duchy",
           prussia="rump", austria="partner", spain="ally_bourbon", posture="S5"), "秩序固化"),
 1815: (bp(britain="settle", blockade="protective", navy_budget=195.0, russia="neutral", poland="duchy",
           prussia="rump", austria="partner", spain="ally_bourbon", posture="S5"), "秩序固化"),
}

def run(variant):
    rows = []
    state = dict(fr_self_limit_years=0, ru_clock=0, allies_lost=False, blood_tax_over=False, ru_stance="NEUTRAL")
    for year in sorted(PATH_E):
        pol, decision = PATH_E[year]
        if pol["britain"] == "settle" or (not pol["annex_new"] and pol["spain"] == "ally_bourbon"):
            state["fr_self_limit_years"] += 1
        else:
            state["fr_self_limit_years"] = 0
        if pol["russia"] == "war_full" or pol["blockade"] == "strict":
            state["blood_tax_over"] = True
        if variant == "E_reset" and pol["blockade"] == "protective" and pol["russia"] not in ("war_full","war_limited"):
            state["blood_tax_over"] = False
            state["allies_lost"] = False
        reacts = []
        for uname, f in W.UNIT_FUNCS:
            st, why = f(pol, year, state)
            if uname == "俄国": state["ru_stance"] = st
            if uname in ("南德", "北欧") and st in ("DEFECT_RISK", "ALLY_BANKRUPT"):
                state["allies_lost"] = True
            reacts.append(f"{uname}:{st}")
        nlo, nhi, slo, shi = W.manpower(pol, state)
        avail, flo, fhi, customs, _ = W.fiscal(pol, state)
        act = W.theater_conflict(pol)
        rows.append(dict(variant=variant, year=year, decision=decision, posture=pol["posture"],
            blockade=pol["blockade"], manpower_need_k=f"{nlo:.1f}–{nhi:.1f}",
            manpower_supply_k=f"{slo:.1f}–{shi:.1f}",
            manpower_balance_k=f"{slo-nhi:.1f}–{shi-nlo:.1f}",
            manpower_status="NEGATIVE" if shi-nlo < 0 else ("TIGHT" if slo-nhi < 0 else "OK"),
            fiscal_avail_m=round(avail,1), fiscal_need_m=f"{flo:.1f}–{fhi:.1f}",
            fiscal_balance_m=f"{avail-fhi:.1f}–{avail-flo:.1f}",
            fiscal_status="NEGATIVE" if avail-flo < 0 else ("TIGHT" if avail-fhi < 0 else "OK"),
            customs_net_m=f"{customs[0]:.1f}–{customs[1]:.1f}",
            theaters="+".join(act), reactions="; ".join(reacts)))
    return rows

allrows = run("E_literal") + run("E_reset")
with open("P6E_paths_annual.csv","w",newline="",encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(allrows[0].keys())); w.writeheader(); w.writerows(allrows)
# 奇迹与选择节点：路径E所需外生事件 = M-B1, M-B2, M-B3（同路径B）；C类节点 = C4–C10（无C1/C2/C3）
C = [c for c in W.CHOICE_NODES if c[0] in ("C4","C5","C6","C7","C8","C9","C10")]
jl = jh = 1.0
for c in C: jl *= c[3]; jh *= c[4]
CB = W.CHOICE_NODES
jbl = jbh = 1.0
for c in CB: jbl *= c[3]; jbh *= c[4]
summary = dict(path_E_choice_nodes=[c[0] for c in C], path_E_joint_indep=(round(jl,6), round(jh,6)),
               path_B_joint_indep=(round(jbl,7), round(jbh,7)),
               ratio_E_over_B_low=round(jl/jbl,2), ratio_E_over_B_high=round(jh/jbh,2),
               miracles_required=["M-B1","M-B2","M-B3"], miracles_le_0_25=0)
json.dump(summary, open("P6E_summary.json","w"), ensure_ascii=False, indent=1)
for r in allrows:
    print(r["variant"], r["year"], r["posture"], r["blockade"], "MAN", r["manpower_need_k"], "vs", r["manpower_supply_k"], r["manpower_status"],
          "| FISC avail", r["fiscal_avail_m"], "need", r["fiscal_need_m"], r["fiscal_status"], "| customs", r["customs_net_m"], "|", r["theaters"])
print(json.dumps(summary, ensure_ascii=False))
