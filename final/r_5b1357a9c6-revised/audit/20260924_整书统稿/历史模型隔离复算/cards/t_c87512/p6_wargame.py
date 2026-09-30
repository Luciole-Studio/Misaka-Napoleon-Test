#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P6 回合制对弈引擎（t_c87512）
每年一回合：法国行动 → 各单位按反应函数响应 → 军事/外交/财政结算 → 资源冲突检查。

设计声明（必须与报告同读）：
1. 本引擎不是预测器，是**一致性记账器**：它检验一条被脚本化的路径在人力、财政、
   战区占用（同一机动军不得两处）与他国反应函数上是否自洽，并把不自洽处标出来。
2. 所有参数取自本轮单位卡（见 SRC 字段与 notes_inputs_core.md 的锚点编号）。
   凡标 MODEL 的是本卡设定的情景参数，不是史料观测。
3. 概率是各单位卡给出的条件裁量带，禁止相乘当作统计置信区间；本引擎给出的
   joint 区间只是"若视为条件独立"的算术上下界，报告中必须并列给出相关性修正。
"""

import csv, json, os

OUT = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# 0. 参数表（单位：人力=千人在场可用；财政=百万法郎/年）
# ----------------------------------------------------------------------------

P = {
    # F2 人力包络（A1/A2）
    "inreg_low": 400.0, "inreg_high": 550.0, "inreg_center": 450.0,   # 法国在册（千）
    "allied_low": 150.0, "allied_high": 250.0, "allied_center": 200.0, # 盟军在册（千）
    "present_rate": 0.85,          # F2 在场可用率 0.80–0.90 取中
    # F2 姿态锚（千人在场可用需求）
    "need_S2_center": 540.0, "need_S5_center": 490.0,
    "need_S6lite_center": 566.25, "need_S6max_center": 922.25, "need_S6full_center": 1102.25,
    "supply_S2_center": 595.0, "supply_S5_center": 637.5, "supply_S6max_wide": 800.0,
    # 边际增量（千人在场），SP1/F2-Oman、B4、R3、D2、IT2
    "delta_spain_occupation_low": 290.0, "delta_spain_occupation_high": 360.0,
    "delta_britain_landing_low": 80.0, "delta_britain_landing_high": 130.0,
    "delta_russia_campaign_fr": 250.0,      # 法籍主力份额（1812总60万含过半非法籍，F2口径纠错）
    "delta_russia_limited": 180.0,
    "delta_outer_ring_low": 60.0, "delta_outer_ring_high": 100.0,   # D2 外圈治安实测量级
    "delta_calabria": 22.0,                  # IT2 1810年被困卡拉布里亚海岸
    "delta_illyria": 28.5,                   # D2 19‰×150万
    "delta_prussia_takeover_mid": 6.0,       # PR 取消后中摩擦 4.5–7.5万 → 取中（千人=60）
    "delta_orient_expedition": 30.0,         # PS 边缘可行档 2–3万
    # F4 财政（A3）
    "fisc_joint_military_treaty": 495.0,     # 高收入+可兑盟约案：陆海合计
    "fisc_joint_military_noTreaty": 230.0,   # 无盟约中心案：仅陆军余量
    "fisc_army_line": 300.0, "fisc_navy_main": 195.0,
    "cost_per_soldier_fr": 700.0/1000.0,     # 700法郎/兵年 → 百万法郎/千人
    "cost_per_soldier_outer": 900.0/1000.0,  # Marion 那不勒斯脚注 900
    # X2 关税制度（E1）
    "customs_strict": (15.0, 35.0), "customs_protective": (60.0, 90.0),
    "customs_license_1810": 97.0, "customs_enforce_strict": (28.0, 38.5),
    "customs_enforce_protective": (14.0, 24.0),
    "taxbase_damage_strict": (-110.0, -60.0),   # F4 严格封锁税基损伤
    # 海军（A4/A6）
    "navy_A12_1830_W": 84, "navy_A12_1830_P": 111,
    "uk_A12_1830_W": (115, 145), "uk_A12_1830_P": (100, 140),
    "uk_escalation_trigger_sail": (40, 60),   # B3：法国当季可出海压力超此即英方升档
}

SRC = {
    "inreg": "F2 L9/L271–275 (t_0e763d)",
    "need": "F2 L11 表 (t_0e763d)",
    "spain": "SP1 L67 二值函数 / F2-Oman 两切片",
    "landing": "B4 三阈值（台账 B4 条）",
    "outer": "D2 L18/L112 (t_e0038f)",
    "fisc": "F4 §C（台账 F4 提交条）",
    "customs": "X2 §6.3/保护版（t_6f3beb L21–22）+F4 补订②③",
    "navy": "F3 定稿 A12 / B3 response / P4_four_snapshots.csv",
}

# ----------------------------------------------------------------------------
# 1. 单位反应函数（B1–B8 政策 → 立场/贡献/成本）
#    stance: ALLY_ACTIVE(出兵) / ALLY_PASSIVE(不阻) / COMPLIANT(服从需驻军)
#            / NEUTRAL / HOSTILE_ARMED(参战) / INSURGENT(叛乱)
# ----------------------------------------------------------------------------

def react_britain(pol, year, state):
    """B1/B1a/B1b：英国不是'被打服'而是'在六条件下接受'。"""
    if pol["britain"] == "invade":
        # B4：登陆本身是海上事件；B1a：占城不启动投降倒计时
        return ("HOSTILE_ARMED", "登陆战；占城后1–3月为有条件议价窗，前提法方给有限条款且能持续补给")
    if pol["blockade"] == "strict" and pol["britain"] != "settle":
        return ("HOSTILE_ARMED", "S3：1812–16应急改组较可能，不保证签法国条件（B1b L92）")
    if pol["annex_new"] or pol["britain"] == "max_demand":
        return ("HOSTILE_ARMED", "S6式无终点兼并：1807–15难形成接受其永久性的稳定多数（B1b L94）")
    if pol["britain"] == "settle" and state["fr_self_limit_years"] >= 2:
        # B1b L9：有可接受条款时 1806–07 早窗、1811–14 中置信窗
        if year <= 1807:
            return ("NEGOTIATING", "早窗：Talents已实际谈判；写定领土交易且不反复加价即可提前成交（B1b L9）")
        return ("NEGOTIATING", "1811–14中置信窗；法国兑现自限比给秩序取名更重要（B1b L126）")
    return ("HOSTILE_ARMED", "无可接受条款：续战并等待大陆伙伴")

def react_russia(pol, year, state):
    """R1：可达上限=C层被胁迫同盟，半衰期4年；关税容忍是唯一六列同击让步。"""
    if pol["russia"] == "war_full":
        return ("HOSTILE_ARMED", "R3：无焦土无冬季俄军仍保正规野战军≥20万；最优期望仅'一次休战'")
    if pol["russia"] == "war_limited":
        return ("HOSTILE_ARMED", "R1 L188：止于双河线→不签文书→事实性长期武装对峙=东境'第二个西班牙'")
    if pol["blockade"] == "strict":
        # 关税容忍与S3制度互斥
        state["ru_clock"] += 2
        return ("COMPLIANT_DECAYING", "封锁加严=关阀动作；同盟寿命时钟加速（R1 L209/L214）")
    if pol["blockade"] in ("protective", "license") and pol["poland"] != "kingdom":
        return ("NONBELLIGERENT", "关税容忍+不称波兰王国：买到'不战'不是'亲法'（R1 L288）；半衰期可上调8–12年（R1 L26）")
    if pol["poland"] == "kingdom":
        state["ru_clock"] += 2
        return ("HOSTILE_DRIFT", "复国王国名号：俄方耐受为零（PL卡：1810公约'永不重建'）")
    return ("COMPLIANT_DECAYING", "默认C层，四年半衰期")

def react_austria(pol, year, state):
    if pol["austria"] == "partition":
        return ("HOSTILE_ARMED", "A卡：肢解方案无地方合作者与预算；1813证明骨架可复起（29.8万）")
    if pol["austria"] == "humiliate":
        return ("HOSTILE_DRIFT", "割海口+8,500万赔款型和约→1811式破产但不锁死再战能力")
    if pol["austria"] == "partner":
        return ("ALLY_PASSIVE", "A卡主线：保王朝核心/商业海口/明确边界→跨一次继承的不平等合作伙伴")
    return ("NEUTRAL", "")

def react_prussia(pol, year, state):
    if pol["prussia"] == "abolish":
        if state["ru_stance"] in ("NONBELLIGERENT", "COMPLIANT_DECAYING") and pol["poland"] != "kingdom":
            return ("ABOLISHED", "PR：1807夏–1808.2可谈窗；前提不同时大复波兰；接管中摩擦4.5–7.5万")
        return ("HOSTILE_ARMED", "PR：1811-10起俄方把'保证普鲁士存续'写成最本质条款→取消须付更高价")
    if pol["prussia"] == "rump":
        return ("COMPLIANT", "1808巴黎公约限军42,000（十年期）+三要塞法军10,000由普方供宿粮")
    return ("NEUTRAL", "")

def react_spain(pol, year, state):
    if pol["spain"] == "ally_bourbon":
        return ("ALLY_ACTIVE", "SP1 L67：同盟态=25,000远征军+港口+船厂+对葡通道；SP2 L11：不面对1808式总起义")
    if pol["spain"] == "puppet":
        return ("INSURGENT", "SP2：开关三条件全满足→总起义；占领态吞噬29–36万法军")
    if pol["spain"] == "annex_ebro":
        return ("INSURGENT", "SP1 L15：A层南界在比利牛斯；埃布罗兼并=在最贵的地方买最少的服从")
    return ("NEUTRAL", "")

def react_south_germany(pol, year, state):
    if pol["germany"] == "annex":
        return ("HOSTILE_DRIFT", "G1：吞并南德=33k即时盟军换60–90k驻军需求+十年负净供兵")
    if state["blood_tax_over"]:
        return ("DEFECT_RISK", "G1：替代担保人出现∧血税超限→Ried型转向")
    return ("ALLY_ACTIVE", "G1：自带行政/自征税/自供兵，1808邦联承诺126,000人")

def react_papacy(pol, year, state):
    if pol["church"] == "annex_rome":
        return ("VETO_PERMANENT", "IT3：教皇个人可压服、枢机-教会法机构不可压服→永不结案的正统性诉讼")
    return ("ACCOMMODATING", "IT3 7.1：'专约+教皇有限主权'和解均衡，长久判据下性价比最高单项投资")

def react_us(pol, year, state):
    if pol["blockade"] == "strict":
        return ("HOSTILE_DRIFT", "US：P(英美战争)0.55–0.75，但P(美法武装冲突)亦升至0.25–0.40；扣船=自断管道")
    return ("SERVICE_SUPPLIER", "US：价格='不扣美国船'；S2下P(英美战争)0.30–0.45")

def react_scandinavia(pol, year, state):
    if pol["blockade"] == "strict":
        return ("ALLY_BANKRUPT", "SC：S3第一受害者是法国盟友；丹麦财政寿命5–6年；买瑞典必卖丹麦")
    return ("ALLY_PASSIVE", "SC：名义封锁+许可证常态+不惩瑞典→丹麦可维系")

def react_ottoman(pol, year, state):
    if pol["orient"] == "partition":
        return ("HOSTILE_ARMED", "OT：1808瓜分死锁于达达尼尔；每次被出卖即掉头")
    if pol["orient"] == "corridor":
        return ("REFUSES_PASSAGE", "OT：1807连25,000援军过境波斯尼亚都被地方贝伊否决")
    return ("FRIENDLY_AUTONOMOUS", "OT：低成本维持其对俄敌意+不再出卖它")

UNIT_FUNCS = [
    ("英国", react_britain), ("俄国", react_russia), ("奥地利", react_austria),
    ("普鲁士", react_prussia), ("西班牙", react_spain), ("南德", react_south_germany),
    ("教廷", react_papacy), ("美国", react_us), ("北欧", react_scandinavia),
    ("奥斯曼", react_ottoman),
]

# ----------------------------------------------------------------------------
# 2. 结算
# ----------------------------------------------------------------------------

def manpower(pol, state):
    """返回 (需求低, 需求高, 供给低, 供给高)；单位千人在场可用。"""
    base = P["need_S2_center"] if pol["posture"] == "S2" else (
           P["need_S5_center"] if pol["posture"] == "S5" else
           P["need_S6lite_center"] if pol["posture"] == "S6lite" else
           P["need_S6max_center"])
    lo = hi = base
    if pol["spain"] in ("puppet", "annex_ebro"):
        lo += P["delta_spain_occupation_low"]; hi += P["delta_spain_occupation_high"]
    if pol["britain"] == "invade":
        lo += P["delta_britain_landing_low"]; hi += P["delta_britain_landing_high"]
    if pol["russia"] == "war_full":
        lo += P["delta_russia_campaign_fr"]; hi += P["delta_russia_campaign_fr"]
    if pol["russia"] == "war_limited":
        lo += P["delta_russia_limited"]; hi += P["delta_russia_limited"]
    # 防重复计入：S6lite/S6max 锚点内已含外圈（荷兰/汉萨/罗马/伊利里亚），不再叠加
    if pol["outer_ring"] and pol["posture"] not in ("S6lite", "S6max"):
        lo += P["delta_outer_ring_low"]; hi += P["delta_outer_ring_high"]
    if pol["naples_mode"] == "counterinsurgency":
        lo += P["delta_calabria"]; hi += P["delta_calabria"]
    if pol["prussia"] == "abolish":
        lo += P["delta_prussia_takeover_mid"]; hi += P["delta_prussia_takeover_mid"] * 2
    if pol["orient"] == "expedition":
        lo += P["delta_orient_expedition"]; hi += P["delta_orient_expedition"]
    sup_lo = (P["inreg_low"] + P["allied_low"]) * P["present_rate"]
    sup_hi = (P["inreg_high"] + P["allied_high"]) * P["present_rate"]
    if pol["posture"] == "S6max":
        sup_hi = P["supply_S6max_wide"]
    # 盟邦退出（南德/北欧/西班牙敌对）直接扣盟军
    if state["allies_lost"]:
        sup_lo -= 80.0; sup_hi -= 120.0
    return lo, hi, sup_lo, sup_hi

def fiscal(pol, state):
    """返回 (军费可得, 军费需求低, 军费需求高, 关税净, 说明)。单位百万法郎/年。"""
    if pol["treaty_income"]:
        avail = P["fisc_joint_military_treaty"]
    else:
        avail = P["fisc_joint_military_noTreaty"] + 195.0  # 无盟约时海军须自陆军线外另找
    if pol["blockade"] == "strict":
        c_lo, c_hi = P["customs_strict"]; e_lo, e_hi = P["customs_enforce_strict"]
        base_dmg = P["taxbase_damage_strict"]
        customs_net = (c_lo - e_hi + base_dmg[0], c_hi - e_lo + base_dmg[1])
    elif pol["blockade"] == "protective":
        c_lo, c_hi = P["customs_protective"]; e_lo, e_hi = P["customs_enforce_protective"]
        customs_net = (c_lo - e_hi, c_hi - e_lo)
    else:
        customs_net = (30.0, 60.0)
    avail += (customs_net[0] + customs_net[1]) / 2.0
    lo, hi, _, _ = manpower(pol, state)
    need_lo = lo * P["cost_per_soldier_fr"]
    need_hi = hi * P["cost_per_soldier_fr"]
    if pol["outer_ring"] or pol["spain"] in ("puppet", "annex_ebro"):
        need_hi = hi * P["cost_per_soldier_outer"]
    need_lo += pol["navy_budget"]; need_hi += pol["navy_budget"]
    return avail, need_lo, need_hi, customs_net, ""

def theater_conflict(pol):
    """同一机动军不得两处：统计当年需要主力野战军的战区。"""
    active = []
    if pol["britain"] == "invade": active.append("英伦")
    if pol["spain"] in ("puppet", "annex_ebro"): active.append("伊比利亚")
    if pol["russia"] in ("war_full", "war_limited"): active.append("俄境")
    if pol["austria"] in ("partition", "humiliate") and pol.get("austria_war"): active.append("多瑙")
    if pol["prussia"] == "abolish" and pol.get("prussia_war"): active.append("北德")
    if pol["orient"] == "expedition": active.append("东方")
    return active

# ----------------------------------------------------------------------------
# 3. 路径脚本
# ----------------------------------------------------------------------------

def base_policy(**kw):
    pol = dict(posture="S2", britain="blockade_only", blockade="license", russia="neutral",
               austria="neutral", prussia="neutral", spain="ally_bourbon", germany="confed",
               church="concordat", poland="duchy", orient="friendly", naples_mode="satellite",
               outer_ring=False, annex_new=False, treaty_income=True, navy_budget=100.0,
               austria_war=False, prussia_war=False)
    pol.update(kw); return pol

# 路径A：S1 入侵线（1803–1812）
PATH_A = {
 1803: (base_policy(britain="invade_prep", blockade="none", navy_budget=120.0),
        "布洛涅集结；全部资源压海峡；不动西班牙不动意大利"),
 1804: (base_policy(britain="invade_prep", blockade="none", navy_budget=140.0),
        "继续集结；舰队集中计划；奥俄外交安抚（放弃德意志新动作）"),
 1805: (base_policy(britain="invade", blockade="none", navy_budget=140.0),
        "【奇迹节点M-A1】海峡窗口开；8万+炮马D+2上岸"),
 1806: (base_policy(britain="invade", blockade="none", navy_budget=140.0, outer_ring=False),
        "【奇迹节点M-A2】登陆军持续补给；伦敦被占后给有限条款"),
 1807: (base_policy(britain="settle", blockade="none", navy_budget=120.0),
        "英方分裂：伍斯特政府续战 vs 有限媾和；法方不索舰不废王"),
 1808: (base_policy(britain="settle", blockade="license", navy_budget=110.0), "和约执行/撤军"),
 1809: (base_policy(britain="settle", blockade="license", navy_budget=110.0), "秩序建构"),
 1810: (base_policy(britain="settle", blockade="license", navy_budget=110.0), "秩序建构"),
}

# 路径B：S2′ 大陆整固＋英国不败而接受（最优构造线）
PATH_B = {
 1803: (base_policy(britain="blockade_only", blockade="none", navy_budget=90.0),
        "不打亚眠翻盘仗：把马耳他争端交第三方仲裁，换英方承认低地现状（B8只采当时提过的方案）"),
 1804: (base_policy(britain="settle", blockade="none", navy_budget=90.0),
        "称帝；同时对英写定领土交易清单并承诺不再加价（B1b L9的可成交条件）"),
 1805: (base_policy(britain="settle", blockade="none", navy_budget=100.0, austria="partner"),
        "不进德意志；以意大利王冠换奥地利商业海口与边界保证→第三次同盟不成型"),
 1806: (base_policy(britain="settle", blockade="none", navy_budget=110.0, austria="partner"),
        "【早窗】Talents政府谈判：实际占有+等价交换；同时不建大邦联宪法只做仲裁+配额（G2窄版）"),
 1807: (base_policy(britain="settle", blockade="protective", navy_budget=120.0, austria="partner",
                    russia="neutral"),
        "对俄给关税容忍（非封锁），不称波兰王国只保公国；普鲁士维持残普"),
 1808: (base_policy(britain="settle", blockade="protective", navy_budget=130.0, austria="partner",
                    spain="ally_bourbon"),
        "【B4b】不废西王：联姻去条件化，收25,000西班牙远征军与加的斯-费罗尔船厂"),
 1809: (base_policy(britain="settle", blockade="protective", navy_budget=140.0, austria="partner"),
        "教廷和解：专约2.0，教皇保有罗马与授职权→拆除S6第一证伪器"),
 1810: (base_policy(britain="settle", blockade="protective", navy_budget=150.0, austria="partner"),
        "不并荷兰不并汉萨：改为关税同盟式分层准入（X2保护版）"),
 1811: (base_policy(britain="settle", blockade="protective", navy_budget=160.0, austria="partner"),
        "统合公债+法定利息上限（X1 F2条件）；关闭加来金几尼通道"),
 1812: (base_policy(britain="settle", blockade="protective", navy_budget=170.0, austria="partner"),
        "不征俄：以'欧洲总和约'姿态签英法条约（1811–14中置信窗）"),
 1813: (base_policy(britain="settle", blockade="protective", navy_budget=180.0, austria="partner",
                    posture="S5"),
        "和约执行年：降为S5和平姿态（需求540→49万）——引擎强制的取舍：不降姿态就养不起195m海军"),
 1814: (base_policy(britain="settle", blockade="protective", navy_budget=190.0, austria="partner",
                    posture="S5"),
        "【F1 0.7/18月节点】把单边冲动导向非体系方向：印度洋巡航基地与美洲承认外交"),
 1815: (base_policy(britain="settle", blockade="protective", navy_budget=195.0, austria="partner",
                    posture="S5"),
        "秩序固化：帝国法典圈+藩属军自养+海军十年计划"),
}

# 路径C：S3 封锁绞杀变体
PATH_C = {
 1803: (base_policy(blockade="license", navy_budget=90.0), "备战"),
 1806: (base_policy(blockade="strict", navy_budget=90.0, outer_ring=True, annex_new=True),
        "柏林敕令；为执法而并地"),
 1807: (base_policy(blockade="strict", navy_budget=90.0, outer_ring=True, annex_new=True,
                    russia="neutral"), "提尔西特把俄国拖入封锁"),
 1808: (base_policy(blockade="strict", navy_budget=90.0, outer_ring=True, annex_new=True,
                    spain="puppet"), "为闭合伊比利亚海岸废立西班牙"),
 1810: (base_policy(blockade="strict", navy_budget=90.0, outer_ring=True, annex_new=True,
                    spain="puppet"), "特里亚农-枫丹白露；并荷兰汉萨"),
 1812: (base_policy(blockade="strict", navy_budget=90.0, outer_ring=True, annex_new=True,
                    spain="puppet", russia="war_full"), "为封锁闭环征俄（Ellis法则自毁点）"),
}

# 路径D：S4 东方转向变体
PATH_D = {
 1803: (base_policy(blockade="license", navy_budget=100.0), "备战"),
 1807: (base_policy(blockade="license", navy_budget=100.0, orient="corridor", russia="neutral"),
        "提尔西特后转东：芬肯施泰因+Gardane使团"),
 1808: (base_policy(blockade="license", navy_budget=100.0, orient="partition", russia="neutral"),
        "圣彼得堡瓜分谈判（死锁于达达尼尔）"),
 1809: (base_policy(blockade="license", navy_budget=100.0, orient="expedition", russia="neutral",
                    spain="puppet"), "波斯走廊远征＋伊比利亚未了"),
 1810: (base_policy(blockade="license", navy_budget=100.0, orient="expedition", russia="neutral",
                    spain="puppet"), "赫拉特方向；印度洋同时求援"),
}

# 路径S0：史实对照线（负控制组）——引擎若不能在此复现已知的1812资源崩溃，则引擎无效
PATH_S0 = {
 1805: (base_policy(blockade="none", navy_budget=120.0, austria="humiliate", austria_war=True),
        "史实：放弃登陆转身打奥地利（乌尔姆-奥斯特利茨）；同年特拉法加"),
 1807: (base_policy(blockade="strict", navy_budget=60.0, russia="neutral", poland="duchy",
                    prussia="rump", outer_ring=False), "史实：提尔西特+柏林/米兰敕令"),
 1808: (base_policy(blockade="strict", navy_budget=60.0, spain="puppet", outer_ring=False),
        "史实：巴约讷废立"),
 1810: (base_policy(blockade="strict", navy_budget=60.0, spain="puppet", outer_ring=True,
                    annex_new=True, church="annex_rome", naples_mode="counterinsurgency"),
        "史实：并荷兰汉萨罗马；特里亚农-枫丹白露"),
 1812: (base_policy(blockade="strict", navy_budget=60.0, spain="puppet", outer_ring=True,
                    annex_new=True, church="annex_rome", russia="war_full",
                    naples_mode="counterinsurgency", posture="S6lite"),
        "史实：征俄（伊比利亚同时在战）"),
}

PATHS = [("S0_史实对照线", PATH_S0), ("A_S1入侵线", PATH_A), ("B_S2最优构造线", PATH_B),
         ("C_S3封锁绞杀", PATH_C), ("D_S4东方转向", PATH_D)]

# ----------------------------------------------------------------------------
# 4. 奇迹目录（外生、法国不可选择、卡片判定概率≤0.25者计为奇迹）
# ----------------------------------------------------------------------------
MIRACLES = [
  ("M-A1", "海峡窗口：8万+炮马弹药D+2完整上岸且运输队未被截击", 0.10, 0.25,
   "B4：无48h集中4万实绩、无D+2完整卸载校准；马位缺2,436；B3无固定72h预警但责任区编制在位", ["A_S1入侵线"]),
  ("M-A2", "登陆后持续跨海补给（第二、三波与粮弹）", 0.10, 0.20,
   "B4/B3：两潮/六潮为不同时间模型；英舰队未失效即切断", ["A_S1入侵线"]),
  ("M-A3", "伦敦失守后英国在1–3月内签有限和约而非迁政府续战", 0.25, 0.45,
   "B1a L7：两分支并列，续战以基地+可信支付为条件；此项为条件反应非纯外生", ["A_S1入侵线"]),
  ("M-A4", "1805–06奥俄不利用法军渡海组织第三次同盟", 0.15, 0.30,
   "A/R1：史实1805同盟已成型；法军主力离陆是最强诱因", ["A_S1入侵线"]),
  ("M-C1", "俄国自愿长期执行排他封锁而不索关税容忍", 0.05, 0.15,
   "R1 L209/L214：关税容忍是唯一六列同击项，制度上等于放弃S3", ["C_S3封锁绞杀"]),
  ("M-C2", "美国在扣船政策下仍维持中立运输管道", 0.10, 0.20,
   "US：1810朗布依埃敕令扣押一切进法港美船；价格=不扣船", ["C_S3封锁绞杀"]),
  ("M-C3", "英国工业在25年排除下崩解到被迫接受法国最高条件", 0.05, 0.15,
   "B5：S3下1848工业为史实54–79%，不是崩解；B1b L92不保证签法国条件", ["C_S3封锁绞杀"]),
  ("M-C4", "严格封锁与大规模战争同时维持效力", 0.05, 0.15,
   "X2 L21 Ellis法则（印p.202）：两者不相容", ["C_S3封锁绞杀"]),
  ("M-D1", "≥2万法军经波斯走廊在两个战役季内抵赫拉特并保持补给", 0.10, 0.25,
   "PS：单季无预置=关闭；分梯队+四仓+里海航运为'边缘可行（中低）'", ["D_S4东方转向"]),
  ("M-D2", "奥斯曼允许大军过境或合营瓜分不破裂", 0.05, 0.15,
   "OT：1807连25,000援军过境被地方贝伊否决；1808瓜分死锁于达达尼尔", ["D_S4东方转向"]),
  ("M-D3", "法国万人级远征的四闸门同开（欧洲和平×大西洋出港×印度洋中继×季风窗）", 0.05, 0.15,
   "IN2 C4：1803–15从未同开", ["D_S4东方转向"]),
  ("M-B1", "英国在未被击败时签署承认法国大陆优势的条约", 0.40, 0.60,
   "B1b L9：有可接受条款时1806–07早窗与1811–14中置信窗；非奇迹级低概率", ["B_S2最优构造线"]),
  ("M-B2", "俄国十年不战（关税容忍+不称王国+不吞奥尔登堡）", 0.35, 0.50,
   "R1备选一（中）：窗口叠加；X2许可证经济可持续则半衰期上调8–12年", ["B_S2最优构造线"]),
  ("M-B3", "奥地利在无1809式羞辱下不再入场", 0.45, 0.60,
   "A卡S5-A路：保王朝核心+海口+边界→跨一次继承的合作伙伴", ["B_S2最优构造线"]),
]

FATE = [
  ("L1", "拿破仑活到罗马王1829-03-20成年", 0.50, 0.65, "F1 L15"),
  ("L2", "一次继承成功交接（条件于L1或摄政法）", 0.65, 0.80, "F5：1820s死 65–80%"),
  ("L3", "王朝存续至1848（无条件加权）", 0.40, 0.55, "F5；'行政国家存续而王朝更替'≥70%"),
]

# 法国侧选择节点（C类：非外生，按F1先验计价）
CHOICE_NODES = [
 ("C1", "1803不为马耳他重开战/接受第三方仲裁", "工具性（保财政与海军重建期）", 0.45, 0.60),
 ("C2", "1805不进德意志、以王冠换奥地利保证", "工具性（拆同盟=包围收益）", 0.45, 0.65),
 ("C3", "1806–07对英写定领土交易且不再加价", "非工具性（要求承认对等约束）", 0.15, 0.25),
 ("C4", "1807对俄给关税容忍（放弃排他封锁）", "工具性（换东境安全+财政）", 0.35, 0.55),
 ("C5", "1808保留波旁+联姻（B4b）", "工具性（王朝收益+25,000军+白银管道）", 0.35, 0.55),
 ("C6", "1809教廷和解、不并罗马", "工具性（正统性=王朝收益）", 0.40, 0.60),
 ("C7", "1810不并荷兰汉萨，改分层准入", "非工具性（放弃直接支配）", 0.15, 0.25),
 ("C8", "1811建统合公债+法定利率上限", "非工具性（自缚财政）", 0.15, 0.30),
 ("C9", "1812不征俄", "工具性（避免两线+保封锁效力）", 0.35, 0.55),
 ("C10", "胜利后18个月不启动新单边行动（或导向非体系方向）", "F1判0.7反向≈0.3", 0.25, 0.40),
]

# ----------------------------------------------------------------------------
# 5. 运行
# ----------------------------------------------------------------------------

def run():
    rows, conflicts = [], []
    for pname, script in PATHS:
        state = dict(fr_self_limit_years=0, ru_clock=0, allies_lost=False,
                     blood_tax_over=False, ru_stance="NEUTRAL")
        for year in sorted(script):
            pol, decision = script[year]
            if pol["britain"] == "settle" or (not pol["annex_new"] and pol["spain"] == "ally_bourbon"):
                state["fr_self_limit_years"] += 1
            else:
                state["fr_self_limit_years"] = 0
            if pol["russia"] == "war_full" or pol["blockade"] == "strict":
                state["blood_tax_over"] = True
            reacts = []
            for uname, f in UNIT_FUNCS:
                st, why = f(pol, year, state)
                if uname == "俄国": state["ru_stance"] = st
                if uname in ("南德", "北欧") and st in ("DEFECT_RISK", "ALLY_BANKRUPT"):
                    state["allies_lost"] = True
                reacts.append(f"{uname}:{st}")
            nlo, nhi, slo, shi = manpower(pol, state)
            avail, flo, fhi, customs, _ = fiscal(pol, state)
            act = theater_conflict(pol)
            conflict = "同一机动军被要求在%d个战区：%s" % (len(act), "+".join(act)) if len(act) > 1 else ""
            if conflict:
                conflicts.append(dict(path=pname, year=year, theaters="+".join(act),
                                      note="违反'同一军队不能两处'硬约束", decision=decision))
            man_gap_lo = round(slo - nhi, 1); man_gap_hi = round(shi - nlo, 1)
            fis_gap_lo = round(avail - fhi, 1); fis_gap_hi = round(avail - flo, 1)
            rows.append(dict(path=pname, year=year, decision=decision,
                             posture=pol["posture"], britain=pol["britain"], blockade=pol["blockade"],
                             russia=pol["russia"], spain=pol["spain"],
                             manpower_need_k=f"{nlo:.1f}–{nhi:.1f}",
                             manpower_supply_k=f"{slo:.1f}–{shi:.1f}",
                             manpower_balance_k=f"{man_gap_lo}–{man_gap_hi}",
                             manpower_status="NEGATIVE" if man_gap_hi < 0 else ("TIGHT" if man_gap_lo < 0 else "OK"),
                             fiscal_avail_m=round(avail, 1),
                             fiscal_need_m=f"{flo:.1f}–{fhi:.1f}",
                             fiscal_balance_m=f"{fis_gap_lo}–{fis_gap_hi}",
                             fiscal_status="NEGATIVE" if fis_gap_hi < 0 else ("TIGHT" if fis_gap_lo < 0 else "OK"),
                             customs_net_m=f"{customs[0]:.1f}–{customs[1]:.1f}",
                             theater_conflict=conflict, reactions="; ".join(reacts)))
    # 写盘
    with open(os.path.join(OUT, "P6_paths_annual.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    with open(os.path.join(OUT, "P6_resource_conflicts.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["path", "year", "theaters", "note", "decision"])
        w.writeheader(); w.writerows(conflicts)
    # 奇迹表
    mrows = []
    for mid, desc, plo, phi, basis, paths in MIRACLES:
        mrows.append(dict(id=mid, event=desc, p_low=plo, p_high=phi,
                          is_miracle="YES" if phi <= 0.25 else "NO（中概率反应，不计奇迹）",
                          basis=basis, paths="|".join(paths)))
    with open(os.path.join(OUT, "P6_miracles.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(mrows[0].keys())); w.writeheader(); w.writerows(mrows)
    # 路径评分
    scores = []
    for pname, _ in PATHS:
        ms = [m for m in MIRACLES if pname in m[5]]
        strict = [m for m in ms if m[3] <= 0.25]
        wide = [m for m in ms if m[3] <= 0.30]
        jl = 1.0; jh = 1.0
        for m in ms: jl *= m[2]; jh *= m[3]
        verdict = "≥3独立低概率事件→该路径不能作主线" if len(strict) >= 3 else (
                  "奇迹≤1→存在论在该路径上成立" if len(strict) <= 1 else "介于两者之间")
        if len(strict) < 3 <= len(wide):
            verdict += "；宽判据(≤0.30)下达到3件，主线资格在判据敏感区"
        scores.append(dict(path=pname, required_events=len(ms), miracles_le_0_25=len(strict),
                           miracles_le_0_30=len(wide),
                           miracle_ids="|".join(m[0] for m in strict),
                           joint_if_independent=f"{jl:.4f}–{jh:.4f}", falsifier=verdict))
    with open(os.path.join(OUT, "P6_path_scores.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(scores[0].keys())); w.writeheader(); w.writerows(scores)
    # 选择节点（C类）
    crows = [dict(id=c[0], node=c[1], f1_class=c[2], p_low=c[3], p_high=c[4]) for c in CHOICE_NODES]
    jl = 1.0; jh = 1.0
    for c in CHOICE_NODES: jl *= c[3]; jh *= c[4]
    crows.append(dict(id="JOINT_INDEP", node="十节点条件独立乘积（悲观上界，报告须并列相关性修正）",
                      f1_class="—", p_low=round(jl, 6), p_high=round(jh, 6)))
    with open(os.path.join(OUT, "P6_choice_nodes.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "node", "f1_class", "p_low", "p_high"])
        w.writeheader(); w.writerows(crows)
    print(json.dumps(dict(rows=len(rows), conflicts=len(conflicts), miracles=len(mrows),
                          choice_joint_low=jl, choice_joint_high=jh,
                          scores=scores), ensure_ascii=False, indent=1))

if __name__ == "__main__":
    run()
