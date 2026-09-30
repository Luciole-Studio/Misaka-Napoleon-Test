#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P5 大陆经济秩序 1815-1848 可复算模型
卡：t_ec2248（Sister 10038）
输出：P5_growth.csv（增长与分配区间）、P5_trade.csv（贸易结构）、控制台自检

方法声明
--------
本脚本不做统计估计。它做三件事：
(1) 冻结已核观测（Bairoch 人均工业化指数、Maddison 人均GDP与人口、Ellis 附录G/I 贸易官方值、
    Chaptal 1819 制造业价值分解）；
(2) 把各情景的差异表述为**对年增长率的加法分量**（单位：百分点/年），每个分量都必须写出锚点来源；
(3) 复利到 1848 年并输出区间。所得区间是**条件包络（condition envelope）**，不是统计置信区间，
    不可相乘、不可当概率。
"""
import csv, os, math

OUT = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# 一、观测底表（事实层）
# ============================================================

# Bairoch 1982, Table 9「人均工业化水平，UK 1900 = 100」
# 本卡未取 Bairoch 原刊；数值转录自 NBER WP6904 Table 2（该表自注 Source: Table 9, Bairoch (1982)）。
# 标为二手转录，红队须核 Bairoch 原表。
BAIROCH = {   # 1750, 1800, 1830, 1860, 1880, 1900, 1913
    "UK":          [10, 16, 25, 64, 87, 100, 115],
    "France":      [ 9,  9, 12, 20, 28,  39,  59],
    "Belgium":     [ 9, 10, 14, 28, 43,  56,  88],
    "Germany":     [ 8,  8,  9, 15, 25,  52,  85],
    "Italy":       [ 8,  8,  8, 10, 12,  17,  26],
    "Switzerland": [ 7, 10, 16, 26, 39,  67,  87],
    "Spain":       [ 7,  7,  8, 11, 14,  19,  22],
    "Austria-Hungary":[7, 7, 8, 11, 15,  23,  32],
    "Russia":      [ 6,  6,  7,  8, 10,  15,  20],
    "Sweden":      [ 7,  8,  9, 15, 24,  41,  67],
    "Europe-exUK": [ 7,  8,  9, 14, 21,  36,  57],
}
BY = [1750, 1800, 1830, 1860, 1880, 1900, 1913]

def bairoch_interp(country, year):
    """线性内插 Bairoch 指数。1815 与 1848 为内插值，非 Bairoch 报告年。"""
    v = BAIROCH[country]
    for i in range(len(BY) - 1):
        if BY[i] <= year <= BY[i + 1]:
            f = (year - BY[i]) / (BY[i + 1] - BY[i])
            return v[i] + f * (v[i + 1] - v[i])
    raise ValueError(year)

# Maddison Project 2020（downloads/E1_MaddisonProject_2020.xlsx，本卡已抽取 P5_maddison_extract.csv）
# 人均GDP（2011年国际元）与人口（千人）
MADDISON_GDPPC = {  # 1820, 1830, 1840, 1850
    "France": [1809, 1898, 2276, 2546],
    "UK":     [3306, 3550, 4018, 4332],
    "Belgium":[2358, None, None, 2944],
    "Netherlands":[3006, 3038, 3623, 3779],
    "Germany":[1572, None, None, 2276],
    "Italy":  [2665, 2657, 2711, 2611],
    "Spain":  [1600, None, None, 1706],
    "Austria":[1941, 2230, 2415, 2630],
}
MADDISON_POP = {    # 千人，1820,1830,1840,1850
    "France": [31250, 33300, 34900, 36350],
    "UK":     [21239, 24139, 26745, 27181],
    "Belgium":[3434, 3750, 4080, 4449],
    "Netherlands":[2333, 2633, 2886, 3098],
    "Germany":[24905, 28045, 31126, 33746],
    "Italy":  [20176, 21513, 22939, 24460],
    "Spain":  [12203, 13041, 13937, 14894],
    "Switzerland":[1986, 2100, 2220, 2379],
    "Austria":[3369, 3538, 3716, 3950],
}

def pop_1848(c):
    """1840-1850 线性内插到 1848。"""
    p = MADDISON_POP[c]
    return p[2] + 0.8 * (p[3] - p[2])

# Ellis 1981 附录G（印 pp.285-286）法国对外贸易官方值（百万法郎）——本卡亲读并按合计复原
TRADE_G = [
    (1787, 551, 440, 991), (1788, 517, 466, 983), (1789, 576, 441, 1017),
    (1806, 477, 455, 932), (1807, 393, 376, 769), (1808, 320, 331, 651),
    (1809, 288, 332, 620), (1810, 339, 365, 704), (1811, 299, 328, 627),
    (1812, 308, 419, 727), (1813, 251, 354, 605), (1814, 239, 346, 585),
    (1815, 199, 422, 621), (1816, 242, 547, 789), (1817, 332, 464, 796),
    (1818, 335, 502, 837), (1819, 294, 460, 754), (1820, 335, 543, 878),
    (1821, 355, 450, 805), (1822, 368, 427, 795), (1823, 317, 427, 744),
    (1824, 401, 505, 906),
]
# Ellis 1981 附录I（印 pp.288-289，源 A.N. F12 251）法国出口目的地（百万法郎）
TRADE_I = {
    # year: dict
    1806: {"USA":45.923,"UK":0.0,"Holland":56.546,"Hanse":24.119,"Denmark":30.806,
           "Germany":126.132,"Prussia":10.718,"Russia":1.558,"Switzerland":26.673,
           "Austria":1.436,"Italy_K":40.059,"Italy_other":20.517,"Spain":65.311,
           "Portugal":9.280,"Ottoman":5.826},
    1810: {"USA":4.411,"UK":38.918,"Holland":44.574,"Hanse":1.967,"Denmark":0.779,
           "Germany":143.391,"Prussia":0.728,"Russia":0.817,"Switzerland":21.217,
           "Austria":3.441,"Italy_K":51.646,"Italy_other":20.505,"Spain":38.343,
           "Portugal":0.0,"Ottoman":5.367},
    1813: {"USA":31.622,"UK":114.632,"Holland":0.0,"Hanse":9.564,"Denmark":9.349,
           "Germany":72.514,"Prussia":0.859,"Russia":0.0,"Switzerland":22.829,
           "Austria":0.281,"Italy_K":47.944,"Italy_other":16.262,"Spain":22.168,
           "Portugal":0.0,"Ottoman":5.624},
    1817: {"USA":41.783,"UK":41.562,"Holland":48.259,"Hanse":2.423,"Denmark":3.729,
           "Germany":56.211,"Prussia":10.027,"Russia":5.790,"Switzerland":19.158,
           "Austria":0.544,"Italy_K":15.103,"Italy_other":17.958,"Spain":50.094,
           "Portugal":6.789,"Ottoman":2.934},
}
# Chaptal 1819 印 pp.203-204 制造业价值分解（法郎）
CHAPTAL = {"total":1820102409, "raw_dom":416000000, "raw_imp":186000000,
           "labour":844000000, "overhead":192000000, "profit":182005221}

# ============================================================
# 二、情景的年增长率加法分量（本卡裁量；每项注明锚点）
# ============================================================
# 单位：百分点/年，作用于 1815→1848 的人均工业化指数增长率。
# 键：(scenario, region) -> list of (component, low, high, anchor)
#
# 区域组：FR=旧法国核心；INNER=内圈并合省（比利时/莱茵左岸/皮埃蒙特，用 Bairoch Belgium 代理）；
#        DE=德意志（邦联诸邦，用 Bairoch Germany 代理）；IT=意大利；CH=瑞士；ES=西班牙。
COMPONENTS = {
 ("S2","FR"): [("市场准入：保住德意志+意大利市场（Ellis 附录I：1810 德143.4+意51.6 vs 1817 德56.2+意15.1，年差≈124m官方值≈1806年出口总额27%）", +0.25, +0.60, "Ellis App.I"),
               ("投入端：许可证常态化+对英通商和平→原棉与机器可得（Chaptal：进口原料占制造业毛产值10.2%）", +0.10, +0.35, "Chaptal 1819 / X2 保护版"),
               ("基建：莱茵自由航行+斯海尔德无税+安特卫普续建提前", +0.05, +0.20, "notes_infrastructure §1-2"),
               ("避免 1812-14 灾难与 1815 疆界收缩（起点效应另计）", +0.05, +0.15, "F2/F5")],
 ("S2","INNER"):[("并入法国大市场且无关税墙内歧视（D1：整合7-12年完成）", +0.15, +0.45, "D1"),
               ("煤铁区位与安特卫普港口（X3：帝国内唯一英式煤铁区位）", +0.10, +0.30, "X3"),
               ("征兵与直接税负担（D1：1812 比利时人均毛负担24.8法郎=旧法国水准）", -0.15, -0.05, "D1")],
 ("S2","DE"): [("被法国关税墙排除在外（贝格出口6,000万→1,100万法郎）", -0.35, -0.10, "Grab p.98 / X3"),
               ("无 1834 关税同盟（Keller-Shiue：同盟使城市对小麦价差 -5.5%）", -0.20, -0.05, "Keller-Shiue 2014"),
               ("和平+法国市场的农产品与原料需求", +0.10, +0.30, "Ellis App.I 德意志诸邦栏"),
               ("萨克森作为体系内最大工业赢家的外溢", +0.05, +0.20, "Heckscher pp.230-232 / G2")],
 ("S2","IT"): [("生丝只准输里昂、纺织品被排斥（Heckscher p.298；1810-08-23「la France avant tout」）", -0.30, -0.10, "Heckscher p.297-298"),
               ("统一税收-征兵国家+法典（IT1：岁入近翻倍）", +0.10, +0.30, "IT1"),
               ("和平与内部关税统一", +0.05, +0.20, "IT1/X2")],
 ("S2","CH"): [("调停模式：零驻军、低撷取、走私通道租金", +0.05, +0.25, "NL/CH 卡"),
               ("对意纺织销路被打击", -0.20, -0.05, "Heckscher p.298")],
 ("S2","ES"): [("不打半岛战争：保住1806年65.3m对法出口市场与美洲白银管道", +0.20, +0.50, "Ellis App.I / SP1 / MX"),
               ("旧制财政死锁与美洲危机不因此消失", -0.15, 0.00, "SP2")],

 ("S3","FR"): [("投入端：原棉与殖民品相对价格冲击长期化（O'Rourke 表3 法国原棉/纺织品 +78.81%、糖/纺织品 +125.59%）", -0.45, -0.15, "O'Rourke 2005 Tab.3"),
               ("执行机器财政自毁（X2：关税15-35m−执行28-38.5m−税基损伤60-110m）", -0.30, -0.10, "X2 / F4 补订"),
               ("受保护部门的幼稚工业租金（Juhász：保护促进已就绪部门的技术采用）", +0.15, +0.45, "Juhász 2018"),
               ("载体型技术被冻结（X3：蒸汽/动力织机/焦炭冶铁的载体被切断）", -0.25, -0.10, "X3")],
 ("S3","INNER"):[("同 FR 的投入端冲击，且海港区受损更重", -0.50, -0.20, "X2/D2"),
               ("走私与转口租金（可守性三判据）", +0.05, +0.20, "X2")],
 ("S3","DE"): [("海岸带兼并与封锁摧毁税基（汉堡435家糖厂剩40家、失业4.5万+）", -0.45, -0.15, "D2"),
               ("萨克森式受保护内陆工业扩张", +0.15, +0.40, "Heckscher pp.302-306")],
 ("S3","IT"): [("的里雅斯特-阜姆腹地断裂、海运停摆", -0.35, -0.10, "Grab pp.194-195"),
               ("受保护内陆工业", +0.05, +0.20, "Heckscher")],
 ("S3","CH"): [("对外销路双向受阻", -0.25, -0.05, "Heckscher p.298")],
 ("S3","ES"): [("半岛战争或长期动员+美洲丧失", -0.40, -0.10, "SP2/SA")],

 ("S5","FR"): [("S2 的全部市场准入收益，并延续到继承之后", +0.30, +0.70, "Ellis App.I"),
               ("铁路与河流瓶颈解除（X3：1848 帝国 2,500-5,000km，中 3,500）", +0.10, +0.30, "X3 / notes_infrastructure"),
               ("和平期财政再配置：削军后可腾挪 5,800-9,300 万/年给下部工程", +0.05, +0.25, "F4 / notes_infrastructure §4"),
               ("制度红利在 1848 前尚不可观测（ACJR 1850 系数 -.160(SE .250) 不显著）", 0.00, +0.10, "ACJR 2011 Tab.3"),
               ("保护主义自身成为天花板（无 1817 式被迫升级）", -0.20, -0.05, "X3")],
 ("S5","INNER"):[("内圈为增量资产：根特/列日/蒙斯-亚琛煤铁带+安特卫普", +0.20, +0.55, "X3/D1"),
               ("资本与技术仍须外购", -0.10, 0.00, "X3")],
 ("S5","DE"): [("关税同盟化分支 B（X2 概率带 1848 视点 0.25-0.35）的期望收益", +0.05, +0.30, "X2 §8"),
               ("否则维持分层准入的次级地位", -0.25, -0.05, "X2 §8 分支A")],
 ("S5","IT"): [("罗马王/欧仁统一北中意→内部关税统一与米兰-都灵-热那亚三角", +0.10, +0.35, "IT1"),
               ("里昂优先的原料束缚若延续", -0.25, -0.05, "Heckscher p.298")],
 ("S5","CH"): [("和平期过境与机械化外溢", +0.10, +0.30, "Bairoch 观测：瑞士1800-1830 10→16 为大陆最快")],
 ("S5","ES"): [("波旁立宪+保美洲→白银与市场", +0.15, +0.45, "SP1/MX"),
               ("内战与财政死锁风险", -0.25, -0.05, "SP2")],

 ("S6","FR"): [("行省化吞噬资本、技工、和平与税基（每延长1,000km边境线需增2,370-3,840边境旅）", -0.40, -0.15, "X2 §7 / F4 对冲曲线"),
               ("外圈净财政贡献 [-10,+40]m/年（中心 +10~20m）远低于纸面144m", -0.20, 0.00, "D2/F4"),
               ("统一市场的名义扩大", +0.05, +0.25, "D1")],
 ("S6","INNER"):[("内圈本身仍受益，但被中央预算挤出", -0.10, +0.20, "X3/F4")],
 ("S6","DE"): [("海岸带并入即财政自败；南德吞并使盟军变驻军需求", -0.50, -0.20, "G1/G2/D2")],
 ("S6","IT"): [("旧教皇领与外圈并合的反复叛乱与驻军成本", -0.40, -0.10, "D2/IT2")],
 ("S6","CH"): [("兼并即销毁产出并激活山地起义链", -0.45, -0.15, "NL/CH 卡")],
 ("S6","ES"): [("全西班牙A层省化任何版本不可行（高）", -0.60, -0.20, "D2/SP2")],
}

# 情景对 1815 年起点水平的乘数（避免 1812-15 破坏 / 额外破坏）
START_1815 = {
    "S0": (1.00, 1.00),
    "S2": (1.02, 1.10),   # 无1812俄征、无1813-14入侵、无疆界崩解
    "S3": (0.95, 1.03),   # 封锁延续但无大陆战败
    "S5": (1.02, 1.10),   # 与S2同前史
    "S6": (0.95, 1.05),   # 强制整合期的破坏与镇压
}

REGION_PROXY = {"FR":"France","INNER":"Belgium","DE":"Germany","IT":"Italy",
                "CH":"Switzerland","ES":"Spain"}
REGION_POP = {"FR":"France","INNER":"Belgium","DE":"Germany","IT":"Italy",
              "CH":"Switzerland","ES":"Spain"}

SCENARIOS = ["S0","S2","S3","S5","S6"]

def run():
    rows = []
    idx1815, idx1848_s0, g0 = {}, {}, {}
    for r, c in REGION_PROXY.items():
        idx1815[r] = bairoch_interp(c, 1815)
        idx1848_s0[r] = bairoch_interp(c, 1848)
        g0[r] = (idx1848_s0[r] / idx1815[r]) ** (1 / 33) - 1
    uk1815, uk1848 = bairoch_interp("UK", 1815), bairoch_interp("UK", 1848)
    g0_uk = (uk1848 / uk1815) ** (1 / 33) - 1

    results = {}
    for s in SCENARIOS:
        for r in REGION_PROXY:
            lo_add = hi_add = 0.0
            comps = COMPONENTS.get((s, r), [])
            for (_n, lo, hi, _a) in comps:
                lo_add += lo / 100.0
                hi_add += hi / 100.0
            s_lo, s_hi = START_1815[s]
            base = idx1815[r]
            lo = base * s_lo * (1 + g0[r] + lo_add) ** 33
            hi = base * s_hi * (1 + g0[r] + hi_add) ** 33
            mid = (lo + hi) / 2
            results[(s, r)] = (lo, mid, hi)
            rows.append({
                "block": "A_industrial_index_1848",
                "scenario": s, "region": r, "proxy_country": REGION_PROXY[r],
                "index_1815": round(base, 2),
                "S0_index_1848": round(idx1848_s0[r], 2),
                "g0_annual_pct": round(g0[r] * 100, 3),
                "add_low_pp": round(lo_add * 100, 3),
                "add_high_pp": round(hi_add * 100, 3),
                "low": round(lo, 2), "mid": round(mid, 2), "high": round(hi, 2),
                "pct_of_S0_low": round(100 * lo / idx1848_s0[r], 1),
                "pct_of_S0_high": round(100 * hi / idx1848_s0[r], 1),
                "note": "Bairoch UK1900=100 指数；1815/1848 为线性内插；区间=条件包络非CI",
            })

    # 英国（承 B5 已验收包络：S2 79-100%、S3 54-79%、S5 88-109% of actual 1848）
    UK_ENV = {"S0": (100, 100), "S2": (79, 100), "S3": (54, 79), "S5": (88, 109), "S6": (75, 100)}
    for s, (a, b) in UK_ENV.items():
        rows.append({"block": "A_industrial_index_1848", "scenario": s, "region": "UK",
                     "proxy_country": "UK", "index_1815": round(uk1815, 2),
                     "S0_index_1848": round(uk1848, 2), "g0_annual_pct": round(g0_uk * 100, 3),
                     "add_low_pp": "", "add_high_pp": "",
                     "low": round(uk1848 * a / 100, 2), "mid": round(uk1848 * (a + b) / 200, 2),
                     "high": round(uk1848 * b / 100, 2),
                     "pct_of_S0_low": a, "pct_of_S0_high": b,
                     "note": "承 B5 t_87ba37 已验收包络；S6 为本卡按 S2/S5 中位外推，置信低"})

    # B：大陆工业总量 vs 英国（指数×人口）
    for s in SCENARIOS:
        for tag, f in (("low", 0), ("mid", 1), ("high", 2)):
            cont = sum(results[(s, r)][f] * pop_1848(REGION_POP[r]) for r in REGION_PROXY)
            ukv = uk1848 * (UK_ENV[s][0] if tag == "low" else UK_ENV[s][1] if tag == "high"
                            else (UK_ENV[s][0] + UK_ENV[s][1]) / 2) / 100
            ukt = ukv * pop_1848("UK")
            rows.append({"block": "B_continental_vs_UK_1848", "scenario": s, "region": "CONT/UK",
                         "proxy_country": tag, "index_1815": "", "S0_index_1848": "",
                         "g0_annual_pct": "", "add_low_pp": "", "add_high_pp": "",
                         "low": round(cont / 1000, 1), "mid": round(ukt / 1000, 1),
                         "high": round(cont / ukt, 2), "pct_of_S0_low": "", "pct_of_S0_high": "",
                         "note": "low列=大陆六区工业总量(指数×千人/1000)；mid列=英国同口径；high列=倍数"})

    # C：分配 —— 要素份额（Chaptal 1819 基线 + 情景保护租金）
    base_profit = CHAPTAL["profit"] / CHAPTAL["total"] * 100
    base_wage = CHAPTAL["labour"] / CHAPTAL["total"] * 100
    RENT = {"S0": (0.0, 0.0), "S2": (0.5, 2.0), "S3": (2.0, 5.0), "S5": (1.0, 3.0), "S6": (0.0, 2.0)}
    for s in SCENARIOS:
        lo, hi = RENT[s]
        rows.append({"block": "C_factor_shares_pct_of_gross_manuf_output", "scenario": s,
                     "region": "FR+INNER", "proxy_country": "Chaptal1819",
                     "index_1815": round(base_profit, 2), "S0_index_1848": round(base_wage, 2),
                     "g0_annual_pct": "", "add_low_pp": lo, "add_high_pp": hi,
                     "low": round(base_profit + lo, 2), "mid": round(base_profit + (lo + hi) / 2, 2),
                     "high": round(base_profit + hi, 2), "pct_of_S0_low": "", "pct_of_S0_high": "",
                     "note": "利润份额；基线10.00%（Chaptal 印pp.203-204）；租金增量为本卡裁量，"
                             "上限由 X2 走私保费 AVE 55±8% 与替代品成本劣势 35-60% 约束"})

    # D：区域离散度（最高/最低区域指数比）
    for s in SCENARIOS:
        mids = {r: results[(s, r)][1] for r in REGION_PROXY}
        hi_r = max(mids, key=mids.get); lo_r = min(mids, key=mids.get)
        rows.append({"block": "D_regional_dispersion_1848", "scenario": s,
                     "region": f"{hi_r}/{lo_r}", "proxy_country": "",
                     "index_1815": "", "S0_index_1848": "", "g0_annual_pct": "",
                     "add_low_pp": "", "add_high_pp": "",
                     "low": round(mids[lo_r], 2), "mid": round(mids[hi_r], 2),
                     "high": round(mids[hi_r] / mids[lo_r], 2), "pct_of_S0_low": "",
                     "pct_of_S0_high": "", "note": "low=最低区中值；mid=最高区中值；high=比值"})

    with open(os.path.join(OUT, "P5_growth.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    # ---- 分量明细表（可审计） ----
    crows = []
    for (s, r), comps in sorted(COMPONENTS.items()):
        for (n, lo, hi, a) in comps:
            crows.append({"scenario": s, "region": r, "component": n,
                          "low_pp_per_year": lo, "high_pp_per_year": hi, "anchor": a})
    with open(os.path.join(OUT, "P5_components.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(crows[0].keys()))
        w.writeheader(); w.writerows(crows)

    # ---- 贸易表 ----
    trows = []
    for (y, imp, exp, tot) in TRADE_G:
        trows.append({"block": "G_french_trade_official_values_mfr", "year": y,
                      "imports": imp, "exports": exp, "total": tot,
                      "check_sum_equals_total": "OK" if imp + exp == tot else f"DIFF {imp+exp-tot}",
                      "pct_of_1789_total": round(100 * tot / 1017, 1)})
    GTOT = {1806: 465, 1810: 377, 1813: 354, 1817: 464}   # Ellis 附录G 同年出口总额
    for y, d in sorted(TRADE_I.items()):
        tot = sum(d.values())
        sysmkt = d["Germany"] + d["Italy_K"] + d["Italy_other"] + d["Switzerland"] + d["Holland"]
        trows.append({"block": "I_export_destinations_mfr", "year": y,
                      "imports": round(sysmkt, 3), "exports": round(tot, 3),
                      "total": GTOT[y],
                      "check_sum_equals_total":
                          f"附录I十五目的地合计占附录G出口总额 {100*tot/GTOT[y]:.1f}%；"
                          f"体系内大陆市场占G总额 {100*sysmkt/GTOT[y]:.1f}%",
                      "pct_of_1789_total": round(100 * sysmkt / GTOT[y], 1)})
    with open(os.path.join(OUT, "P5_trade.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(trows[0].keys()))
        w.writeheader(); w.writerows(trows)

    # ---- 控制台自检 ----
    print("=== 自检 1：Chaptal 分解加总 ===")
    ssum = sum(CHAPTAL[k] for k in ("raw_dom", "raw_imp", "labour", "overhead", "profit"))
    print(f"  分项和 {ssum:,} vs 原文总额 {CHAPTAL['total']:,} 差 {CHAPTAL['total']-ssum:,}（四舍五入）")
    print(f"  利润份额 {100*CHAPTAL['profit']/CHAPTAL['total']:.2f}%  工资份额 "
          f"{100*CHAPTAL['labour']/CHAPTAL['total']:.2f}%  进口原料 "
          f"{100*CHAPTAL['raw_imp']/CHAPTAL['total']:.2f}%")
    c = CHAPTAL["raw_dom"] + CHAPTAL["raw_imp"] + CHAPTAL["overhead"]
    print(f"  s/v={CHAPTAL['profit']/CHAPTAL['labour']:.3f}  "
          f"s/(c+v)={CHAPTAL['profit']/(c+CHAPTAL['labour']):.3f}  c/v={c/CHAPTAL['labour']:.3f}")
    print("=== 自检 2：Ellis 附录G 合计一致性 ===")
    bad = [r for r in trows if r["block"].startswith("G_") and r["check_sum_equals_total"] != "OK"]
    print(f"  {len(TRADE_G)} 行中不自洽 {len(bad)} 行")
    print("=== 自检 3：1824 vs 1789 ===")
    print(f"  1824 总额 906 = 1789 年 1017 的 {906/1017*100:.1f}%；"
          f"出口 505/441={505/441*100:.1f}%；进口 401/576={401/576*100:.1f}%")
    print("=== 自检 4：体系内大陆市场占法国出口比重（分母=附录G出口总额）===")
    GT = {1806: 465, 1810: 377, 1813: 354, 1817: 464}
    for y in sorted(TRADE_I):
        d = TRADE_I[y]; tot = sum(d.values())
        sysmkt = d["Germany"] + d["Italy_K"] + d["Italy_other"] + d["Switzerland"] + d["Holland"]
        print(f"  {y}: 体系市场 {sysmkt:6.1f} / G总额 {GT[y]:3d} = {100*sysmkt/GT[y]:4.1f}%   "
              f"（附录I十五地合计 {tot:6.1f} = G总额的 {100*tot/GT[y]:5.1f}%）")
    print("=== 自检 5：Bairoch 内插 ===")
    for c_ in ("UK", "France", "Belgium", "Germany", "Italy", "Switzerland", "Spain"):
        print(f"  {c_:12s} 1815={bairoch_interp(c_,1815):5.2f}  1848={bairoch_interp(c_,1848):5.2f}")
    print("=== 主结果：1848 人均工业化指数（UK1900=100） ===")
    for s in SCENARIOS:
        line = f"  {s}: "
        for r in REGION_PROXY:
            lo, mid, hi = results[(s, r)]
            line += f"{r}={lo:.1f}-{hi:.1f} "
        print(line)
    print(f"写出：P5_growth.csv({len(rows)}行) P5_components.csv({len(crows)}行) "
          f"P5_trade.csv({len(trows)}行)")

if __name__ == "__main__":
    run()
