#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
X2 · 大陆体系执行机器：可复算模型
卡片 t_6f3beb / Sister 10038

本脚本只做四件事，每个输入都注出处（见 SOURCES.md 与 notes_*.md）：
  A. 执行密度（douanier / 公里、/ 十万人）与"同时在岗哨兵"折算
  B. 殖民品价格楔子分解（伦敦价 + 特里亚农税 vs 巴黎/莱比锡实价）→ 执行租金残差
  C. 走私保费序列 → 有效关税等价物 (AVE) 与"竞争力阈值"判定
  D. S3严格版 vs 许可证版 的财政/福利对弈账（区间，非点估计）

所有"模型"行在输出中以 MODEL 标注；OBS 为文献观测值。
"""

import csv, json, os

OUT = os.path.dirname(os.path.abspath(__file__))
rows = []

def add(block, item, value, unit, kind, source, note=""):
    rows.append(dict(block=block, item=item, value=value, unit=unit,
                     kind=kind, source=source, note=note))

# ---------------------------------------------------------------- A 执行密度
# OBS: Rowe (in Aaslestad&Joor 2015) p.187: 1812 峰值 ~35,000 海关人员
#      = 4,000 agents de bureaux + 30,750 brigades(边境巡逻)
TOTAL_AGENTS_1812 = 35000
BUREAU_1812 = 4000
BRIGADE_1812 = 30750
RHINE_BRIGADE = 3200          # OBS Rowe p.187, départements réunis 莱茵段
RHINE_DENSITY_PER_100K = 241  # OBS Rowe p.187

add("A", "customs_agents_total_1812", TOTAL_AGENTS_1812, "men", "OBS", "Rowe2015 p.187")
add("A", "customs_bureau_1812", BUREAU_1812, "men", "OBS", "Rowe2015 p.187")
add("A", "customs_brigades_1812", BRIGADE_1812, "men", "OBS", "Rowe2015 p.187")
add("A", "rhine_brigade_men", RHINE_BRIGADE, "men", "OBS", "Rowe2015 p.187")
add("A", "rhine_density_per_100k_pop", RHINE_DENSITY_PER_100K, "men/100k", "OBS", "Rowe2015 p.187")

# MODEL: 需守线长度。低/中/高三档（海岸线量测尺度敏感，故给区间）
FRONTIER_KM = {"low": 8000, "mid": 10000, "high": 13000}
# 构成（中档）：北海-波罗的海岸1000 + 荷比法大西洋-海峡2500 + 法意地中海1800
#              + 伊利里亚亚得里亚1000 + 莱茵线700 + 瑞士400 + 意王国界600
#              + 汉萨/威斯特法利亚/贝格东界600 + 伊利里亚陆界800 + 西班牙/加泰400
for k, v in FRONTIER_KM.items():
    add("A", f"frontier_km_{k}", v, "km", "MODEL", "本卡构造",
        "按1812年疆界分段估计；海岸线长度随量尺变化，故给三档")
    add("A", f"brigade_men_per_km_{k}", round(BRIGADE_1812 / v, 2), "men/km", "MODEL",
        "= 30750 / frontier_km", "在册人，非同时在岗")

# MODEL: 同时在岗折算。三班轮值 + 病假/休假/押解/法庭出庭
ON_POST_SHARE = {"low": 0.20, "mid": 0.28, "high": 0.35}
for fk, fv in FRONTIER_KM.items():
    for sk, sv in ON_POST_SHARE.items():
        men_km = BRIGADE_1812 * sv / fv
        add("A", f"sentries_per_km_frontier{fk}_share{sk}", round(men_km, 3), "men/km", "MODEL",
            "= 30750 * on_post_share / frontier_km",
            f"每名哨兵负责 {round(1/men_km,2)} 公里")
# 莱茵线自校验
RHINE_LINE_KM = 700   # MODEL: 荷兰边界—巴塞尔沿河守线
add("A", "rhine_line_km", RHINE_LINE_KM, "km", "MODEL", "本卡构造")
add("A", "rhine_men_per_km", round(RHINE_BRIGADE / RHINE_LINE_KM, 2), "men/km", "MODEL",
    "= 3200/700", "优先线密度约为帝国平均的1.5–2倍，与Rowe定性叙述一致")

# ---------------------------------------------------------------- B 价格楔子
# OBS: Heckscher 印p.292：巴黎糖价 1810 = 4 法郎/livre，(晚些) = 6 法郎/livre
#      作者自己折为 ≈8 与 ≈12 法郎/kg；伦敦1812最优质糖 1.35–2 法郎/kg
#      → 法国价为伦敦价的 4–9 倍
PARIS_SUGAR = {"1810": 8.0, "late": 12.0}       # 法郎/kg, OBS Heckscher p.292
LONDON_SUGAR_1812 = (1.35, 2.00)                # 法郎/kg, OBS Heckscher p.292
TRIANON_SUGAR_RAW = 300.0 / 100.0               # 法郎/kg, OBS Heckscher 附录II(页图) 原糖300/100kg
TRIANON_SUGAR_CLAY = 400.0 / 100.0

add("B", "paris_sugar_1810", PARIS_SUGAR["1810"], "fr/kg", "OBS", "Heckscher p.292")
add("B", "paris_sugar_late", PARIS_SUGAR["late"], "fr/kg", "OBS", "Heckscher p.292")
add("B", "london_sugar_1812_low", LONDON_SUGAR_1812[0], "fr/kg", "OBS", "Heckscher p.292")
add("B", "london_sugar_1812_high", LONDON_SUGAR_1812[1], "fr/kg", "OBS", "Heckscher p.292")
add("B", "trianon_duty_sugar_raw", TRIANON_SUGAR_RAW, "fr/kg", "OBS", "Heckscher App.II 页图")
add("B", "trianon_duty_sugar_clay", TRIANON_SUGAR_CLAY, "fr/kg", "OBS", "Heckscher App.II 页图")

for label, p in PARIS_SUGAR.items():
    for lo_hi, lp in zip(("lowLondon", "highLondon"), LONDON_SUGAR_1812):
        legal_cost = lp + TRIANON_SUGAR_RAW       # 伦敦离岸价 + 特里亚农税（未含运费保险）
        residual = p - legal_cost
        add("B", f"residual_rent_{label}_{lo_hi}", round(residual, 2), "fr/kg", "MODEL",
            "= 巴黎价 − (伦敦价 + 特里亚农原糖税)",
            f"占巴黎价 {round(100*residual/p,1)}%；含运费、保险(走私保费)、许可证费、"
            "中间商垄断租与库存投机；不等于净走私利润")
        add("B", f"residual_share_{label}_{lo_hi}", round(100*residual/p, 1), "%", "MODEL",
            "residual / paris_price", "")

# OBS: 莱比锡糖价 1813 ≈ 七年前(1806)的3.5倍；靛蓝通常2倍、有时3–5倍
add("B", "leipzig_sugar_1813_over_1806", 3.5, "ratio", "OBS", "Heckscher p.292")
add("B", "leipzig_indigo_typical", 2.0, "ratio", "OBS", "Heckscher pp.289–290 (转引König)")
add("B", "leipzig_indigo_max", 5.0, "ratio", "OBS", "Heckscher pp.289–290 (转引König)")
# 反向：出口作物崩盘
add("B", "memel_corn_fall_1806_1810_low", -60.0, "%", "OBS", "Heckscher p.319 (转引Hoeniger)")
add("B", "memel_corn_fall_1806_1810_high", -80.0, "%", "OBS", "Heckscher p.319")
add("B", "bremen_wheat_fall_1806_1811", -62.0, "%", "OBS", "Heckscher p.319 (转引Schäfer表IX)")
# MODEL: 双向贸易条件冲击（殖民品↑×口粮↓）
add("B", "tot_shock_colonial_over_grain_low", round(3.5/ (1-0.62), 2), "ratio", "MODEL",
    "= 莱比锡糖涨幅 / (1 - 不来梅麦跌幅)",
    "以糖换麦的实物贸易条件恶化约9倍（同一大陆内部，非跨境）")
add("B", "tot_shock_colonial_over_grain_high", round(3.5/(1-0.80), 2), "ratio", "MODEL",
    "= 3.5 / (1-0.80)", "梅梅尔口径")

# ---------------------------------------------------------------- C 保费→AVE
# OBS: Rowe p.195 注27 + p.189 注5–6；Heckscher p.194
PREMIA = [
    ("Rhine 1798-12", 6.0,  "Rowe2015 p.189 n.6 (Wirion)"),
    ("Rhine 1800",    6.0,  "Rowe2015 p.195 n.27"),
    ("Rhine 1801-02", 10.0, "Rowe2015 p.195 n.27"),
    ("Rhine Consulate(Eichhoff)", 15.0, "Rowe2015 pp.188-189 n.5 (10/15/20区间中值)"),
    ("Rhine 1806-10→1808-06", 26.0, "Rowe2015 p.195 n.27"),
    ("Rhine 1809-07", 30.0, "Rowe2015 p.195 n.27"),
    ("Rhine 1809末→1811", 50.0, "Rowe2015 p.195 n.27"),
    ("France frontier 1809 (general)", 30.0, "Heckscher p.194"),
    ("Strasbourg top-grade insurer 1809", 45.0, "Heckscher p.194 (40–50中值)"),
    ("Rees–Bremen line 1809", 7.0, "Rowe2015 p.195 n.26 / Heckscher p.194 (6–8中值)"),
    ("Coast→Düsseldorf/Mainz/Frankfurt 1810-09 (保险+运输)", 50.0,
     "Rowe2015 pp.197-198 n.34"),
]
for name, pct, src in PREMIA:
    add("C", f"smuggling_premium::{name}", pct, "% of value", "OBS", src)

# MODEL: 走私渠道的"有效关税等价物" AVE = 保费 + 额外运输绕道成本
DETOUR = {"low": 5.0, "mid": 12.0, "high": 25.0}   # MODEL: 绕道运输附加，%
for name, pct, src in PREMIA:
    for dk, dv in DETOUR.items():
        add("C", f"AVE_{dk}::{name}", round(pct + dv, 1), "% ad valorem", "MODEL",
            "= 保费 + 绕道运输附加", "与合法渠道的特里亚农税率比较")

# 合法渠道的从价等价（以糖为例，用伦敦价当计税基准）
for lp in LONDON_SUGAR_1812:
    add("C", f"trianon_AVE_sugar_londonbase_{lp}", round(100*TRIANON_SUGAR_RAW/lp, 0),
        "% ad valorem", "MODEL", "= 300fr/100kg ÷ 伦敦价",
        "特里亚农原糖税的从价等价 150%–222%，远高于任何观测到的走私保费"
        "→ 合法渠道在价格上始终劣于走私渠道，除非走私被物理封死")

# 阈值判据（Rowe）：保费推到使非法货物"不具竞争力"
# MODEL: 若大陆内部替代品与本地成本使英货在 AVE > X 时退出，X 的区间
add("C", "uncompetitive_threshold_low", 35.0, "% ad valorem", "MODEL",
    "本卡构造", "低阈值：与萨克森/瑞士/阿尔萨斯同类品成本差约三成")
add("C", "uncompetitive_threshold_high", 60.0, "% ad valorem", "MODEL",
    "本卡构造", "高阈值：英国纱线成本优势较大的品类")

# ---------------------------------------------------------------- D 财政对弈
# OBS 财政：Heckscher p.197 法国关税净收（百万法郎）
CUSTOMS = {"1806": 51.2, "1807": 60.6, "1808": 18.6, "1809": 11.6}
for y, v in CUSTOMS.items():
    add("D", f"french_customs_net_{y}", v, "m fr", "OBS", "Heckscher p.197")
# OBS: 特里亚农起至1811年底海关收入 105.9m（Heckscher p.221）；
#      Marion IV p.306 记 1810-08→1812-01 非常关税累计 105.927667m（F4卡）
add("D", "customs_trianon_to_end1811", 105.9, "m fr", "OBS", "Heckscher p.221")
add("D", "marion_extraordinary_0810_0112", 105.927667, "m fr", "OBS", "Marion IV p.306 via F4卡")
# OBS: 1810残余月份没收品拍卖现金 ≈150m（Thiers 转引，Heckscher p.222）
add("D", "auction_cash_1810_rest", 150.0, "m fr", "OBS", "Heckscher p.222 (转引Thiers)")
# OBS: 荷尔斯泰因存货入汉堡：实物缴税19.7m，合计42.5m（Heckscher p.226）
add("D", "holstein_inkind", 19.7, "m fr", "OBS", "Heckscher p.226")
add("D", "holstein_total", 42.5, "m fr", "OBS", "Heckscher p.226")
add("D", "frankfurt_oct1810_yield", 9.0, "m fr", "OBS", "Heckscher p.226 (转引Darmstädter)")
# OBS: 焚货（汉萨+不来梅可稽）总值 ≈4.5m；意大利王国1811初焚 230,109 fr
add("D", "burnt_goods_hanse_bremen", 4.5, "m fr", "OBS", "Heckscher p.229 (Servières/Schäfer)")
add("D", "burnt_goods_italy_1811", 0.230109, "m fr", "OBS", "Grab2015 p.106 (Prina)")

# MODEL: S3严格版（取消许可证与特里亚农）财政后果
# F4卡已给：严格版非常关税→0–15m/年，总关税→15–35m/年（对照1810≈97m）
add("D", "S3strict_total_customs_low", 15.0, "m fr/yr", "OBS", "F4卡 t_9f10b6 补订②")
add("D", "S3strict_total_customs_high", 35.0, "m fr/yr", "OBS", "F4卡 t_9f10b6 补订②")
add("D", "S0_1810_total_customs", 97.0, "m fr", "OBS", "F4卡（普通35.881+非常61.046）")
for lo_hi, v in (("low", 15.0), ("high", 35.0)):
    add("D", f"S3strict_customs_loss_vs1810_{lo_hi}", round(97.0 - v, 1), "m fr/yr", "MODEL",
        "= 97 − 严格版关税", "仅关税项，不含税基损伤（F4另给−60至−110m/年）")

# MODEL: 执行机器的直接运行成本
SALARY_PREPOSE = 500.0   # OBS Rowe p.191：préposé 年薪500法郎
add("D", "prepose_annual_salary", SALARY_PREPOSE, "fr", "OBS", "Rowe2015 p.191")
for k, mult in (("wage_only", 1.0), ("with_overhead_1_6", 1.6), ("with_overhead_2_2", 2.2)):
    cost = TOTAL_AGENTS_1812 * SALARY_PREPOSE * mult / 1e6
    add("D", f"customs_payroll_cost_{k}", round(cost, 1), "m fr/yr", "MODEL",
        "= 35,000 × 500 fr × 乘数",
        "乘数含军官/总监薪级、兵站、船只、武器、诉讼与监狱成本；下界为纯普通员薪")
# 与收入对比
add("D", "cost_to_revenue_1809_wageonly", round(100*(TOTAL_AGENTS_1812*SALARY_PREPOSE/1e6)/CUSTOMS["1809"], 0),
    "%", "MODEL", "= 纯薪成本 / 1809年关税净收",
    "1809年是体系最严格、收入最低的年份：光工资就吃掉关税收入的百倍量级以上"
    "（注：1809年编制为27,200非35,000，见下行敏感性）")
AG_1809 = 27200   # OBS AHAD
add("D", "customs_agents_1809", AG_1809, "men", "OBS", "AHAD/Cahiers n°24 (二手)")
add("D", "cost_to_revenue_1809_agents27200",
    round(100*(AG_1809*SALARY_PREPOSE/1e6)/CUSTOMS["1809"], 0), "%", "MODEL",
    "= 27,200×500fr / 11.6m", "纯普通员工资即为当年关税净收的1.17倍")

# MODEL: 许可证收入量级
LICENCE_FEE = {"low": 600.0, "mid": 800.0, "colonial_import": 6000.0}
for k, v in LICENCE_FEE.items():
    add("D", f"licence_fee_{k}", v, "fr", "OBS", "Heckscher p.216 / AHAD")
for n in (500, 1000, 2000, 4000):
    for k, v in LICENCE_FEE.items():
        add("D", f"licence_revenue_{n}licences_{k}", round(n*v/1e6, 2), "m fr", "MODEL",
            "= 张数 × 费率", "张数为情景假设，非观测；用以给许可证财政的量级上下界")

# ---------------------------------------------------------------- 输出
with open(os.path.join(OUT, "X2_enforcement_model.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["block", "item", "value", "unit", "kind", "source", "note"])
    w.writeheader()
    for r in rows:
        w.writerow(r)

print(f"rows={len(rows)}")
for r in rows:
    if r["block"] in ("A", "B") or r["item"].startswith(("AVE_mid", "trianon_AVE", "cost_to_revenue",
                                                         "S3strict", "customs_payroll")):
        print(f"[{r['block']}|{r['kind']}] {r['item']} = {r['value']} {r['unit']}  ({r['source']})")
