#!/usr/bin/env python3
"""
navy_model.py  (v5, R2b, 2026-09-26)

Budget-coupled French fleet + endogenous British response, three tracks, 1810-1848.
CONDITIONAL WORKED EXAMPLE, NOT A FORECAST, NOT A CONFIDENCE INTERVAL.
Python standard library only.

Built on (copies in source_copies/, research-card directories untouched):
  F3 (t_b1a536)  build_F3_model.py : hull / personnel stock-flow and the A12 formula
  P4 (t_24b942)  build_p4.py       : tonnage and ratio conventions (d_F, d_UK)
  B3 (t_998052)  model_assumptions : British manning package M=650L+280R+110C+O,
                                     cost C=K+vM, blockade rule H=ceil((rF+g)/a)
Changes (see README.md):
  1. French launches are no longer an exogenous schedule: they are what the navy
     budget (chapter 1: 145m francs in the 750 tier 1815-29, 165m in the 850 tier
     1830-48) can pay for after fixed costs, ships in commission and ships in
     ordinary, capped by yard/timber capacity.
  2. Britain responds by rule (old chapter 3, lines 241-248; B3/P4 section 5):
     war  : ships in commission I_UK >= r*F + g, F = c_F*I_Fr + w*allies
     peace: 12-month mobilizable A12_UK >= r*F + g, F = c_F*A12_Fr + w*allies,
            hulls H_UK >= A12_target / a;  I_UK = max(floor, r_I*I_Fr + g_I)
     subject to build capacity (<=8/yr, <=12/yr when the gap is large) and a
     parliamentary ceiling on cost.
  3. Three tracks (most likely / flash-in-the-pan / forced success) with
     track-specific initial stocks (1805-1810 divergences), budgets, truce dates,
     coastal manpower, events (loss of Dutch, Italian, Belgian ports) and the
     Antwerp branch.
  4. Horizon extended to 1848 (sail battle line; steam handled in the text).
"""
import csv, json, math, argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
YEARS = list(range(1810, 1849))

# ----------------------------------------------------------------------------
# PARAMETERS  (three bundles: 'lo' = unfavourable to France, 'base', 'hi' =
# favourable to France; British 'strong' response pairs with 'lo')
# ----------------------------------------------------------------------------
B = ('lo', 'base', 'hi')
IX = {'lo': 0, 'base': 1, 'hi': 2}

FR = {
    # F3 initial personnel pools (thousand), summer 1810, historical scope
    'M0': [60, 65, 70], 'Q0': [35, 40, 45],
    # F3 war (W) flows
    'W_Min': [8, 10, 12], 'W_Mexit': [.10, .09, .08],
    'W_Qin': [4, 4.5, 5], 'W_Qexit': [.07, .06, .05],
    'W_ready': [.70, .775, .85], 'W_oM': [25, 30, 35], 'W_oQ': [15, 17.5, 20],
    'W_ret': [.06, .05, .04], 'W_loss': [1.5, 1.0, 0.5], 'W_share': [.80, .875, .95],
    # F3 peace (P) flows
    'P_Min': [8, 9, 10], 'P_Mexit': [.06, .055, .05],
    'P_Qin': [5, 5.5, 6], 'P_Qexit': [.04, .035, .03],
    'P_ready': [.80, .85, .90], 'P_ret': [.045, .04, .035], 'P_loss': [.2, .1, 0.0],
    'P_oM_early': 35, 'P_oM_late': 40, 'P_oQ_early': 20, 'P_oQ_late': 23,
    'young_ret': [.035, .025, .015],          # 1811-1815 young fleet (F3)
    'crew': 0.8, 'qcrew': 0.45,               # thousand per line ship (F3)
    # yard + timber capacity, launches per year (F3 schedule used as a CAP)
    'cap_1811_15': [8, 10, 12], 'cap_1816_30': [7, 8.5, 10], 'cap_1831_48': [6, 7, 8],
    # peace commissioning share of A12 (policy); war share = W_share
    'P_share': [.40, .40, .40],
    'P_share_max': .55,          # slack money first buys more ships in commission (training)
    # peace yard capacity: national ceiling incl. Antwerp (F3 yard table: sums of
    # sustainable ranges ~12.5 war, upper ~17.5); grows 0.5/yr from war level when funded
    'P_cap_ceiling': [9.0, 11.0, 13.0], 'P_cap_growth': 0.5,
    # the navy does not launch hulls it cannot man: hull goal = man-limited A12 / ready x (1+reserve)
    'hull_reserve': [.10, .15, .20],
    # inscription maritime cap (peace years): registered seafarers (Villiers & Culerrier 1982 p.52:
    # 1825 94,611; 1845 125,272; Tupinier's 1835 inspection via Hansard 1839: 90,000 registered,
    # 35,000 of them qualified, of age and available = 39%).  Scope factor by track, peace-trade bonus.
    'reg_hist': {1815: 80.0, 1825: 94.6, 1845: 125.3, 1848: 128.0},
    'phi': [.34, .39, .44],          # usable qualified share of registered
    'q_nonline_1815_30': [12.0, 10.0, 8.0], 'q_nonline_1831_48': [14.0, 12.0, 10.0],
    'trade_bonus': [.003, .005, .007],   # extra annual growth of registered seafarers in peace
    # COSTS, million francs per year, c.1810 price scale (see README calibration)
    'c_L': [2.6, 2.3, 2.0],      # one line ship built (hull, masts, rigging, guns)
    'c_o': [.35, .30, .25],      # one line hull kept in ordinary / reserve
    'c_Iw': [1.45, 1.30, 1.15],  # one line ship in commission, war footing
    'c_Ip': [1.00, .90, .80],    # one line ship in commission, peace footing
    'kap_w': [.35, .30, .25],    # cruiser/small-craft add-on, war
    'kap_p': [.50, .40, .30],    # cruiser/small-craft add-on, peace (Portal-style)
    'F0w': [60, 52, 45],         # fixed: admin, arsenals, colonies, coast, flotilla
    'F0p': [46, 40, 34],
    'd_F': [3200, 3500, 3800],   # mean loaded displacement, t (P4 convention)
}

UK = {  # index 0 = strong (unfavourable to France) ... 2 = weak
    'r': [1.20, 1.12, 1.05], 'g': [25, 20, 15], 'a': [.75, .80, .85],
    'cF': [.90, .85, .80], 'w_ally': [.7, .5, .3],
    # Russia: Hansard 1839 (Wood): 43 afloat in 1807 and 1839; in commission 30 (1817), 37 (1823), 36 (1832)
    'russia': {1810: 30, 1830: 35, 1848: 40},
    'wR_fr_dominant': [.3, .2, .1],     # Russia's weight when France dominates Europe
    'wR_after_collapse': [.7, .5, .3],  # Russia's weight once France is cut down (as in 1830s history)
    'A12_floor': [65, 60, 55], 'I_floor': [20, 15, 12],
    'rI': [1.5, 1.35, 1.2], 'gI': [10, 8, 5],
    'I_war_floor': [95, 90, 85], 'I_war_floor_after1815': [80, 75, 70], 'a_war': .87,
    'lookahead_years': 3,        # UK projects visible French net construction (ships on the stocks)
    'g_scheldt': [8, 6, 4],      # extra North-Sea squadron Britain keeps if Antwerp stays a war port
    'dispose_margin': 1.10,      # UK disposes surplus hulls only above 110% of target
    'ret': .045, 'ret_min': .025, 'ret_surplus': .08,
    'L_max': 8, 'L_surge': 12, 'L_min_peace': 2, 'L_min_war': 6,
    'ceiling_peace': [15.0, 12.0, 9.0],   # GBP million per year
    'ceiling_war': 22.0,
    'K0': 1.8, 'k_h': .020, 'v_peace': 80.0, 'v_war': 100.0, 'c_b': .09,
    'd_UK': [3400, 3600, 3900],
    'H1810': 124.0, 'I1810': 108.0,
}


def val(p, b):
    return p[IX[b]] if isinstance(p, list) else p


# ----------------------------------------------------------------------------
# TRACKS
# ----------------------------------------------------------------------------
def lin(y, pts):
    """piecewise-linear interpolation through {year: value}"""
    ks = sorted(pts)
    if y <= ks[0]:
        return pts[ks[0]]
    if y >= ks[-1]:
        return pts[ks[-1]]
    for a, c in zip(ks, ks[1:]):
        if a <= y <= c:
            return pts[a] + (pts[c] - pts[a]) * (y - a) / (c - a)


def antwerp_cut(y, s):
    """capacity lost when Antwerp may no longer build ships of the line"""
    if s['antwerp'] != 'restricted' or y <= s['truce']:
        return 0.0
    return 3.0 if y <= s['truce'] + 5 else 1.5   # other yards expand after five years


def track_defs():
    T = {}
    # ---------------- most likely (layer A) ----------------
    T['jia'] = dict(
        label='最可能（甲层）',
        H0=46.0, dM=-1.0, dQ=-0.5,   # -Dutch 9 hulls/5k/3k, +Rosily's 5 hulls/~4k (no war with Spain)
        truce=1814, antwerp='restricted', dutch_yards=False,
        coast=lambda y, s: 0.85,     # no Holland, no Hanse in the French inscription
        budget=lambda y, s: 110 if y == 1810 else (s.get('war_budget', 160) if y <= s['truce'] else (145 if y < 1830 else 165)),
        F0_scale=lambda y, s: 1.0,
        spain=lambda y: lin(y, {1810: 12, 1830: 8, 1848: 6}),
        dutch=lambda y: lin(y, {1810: 6, 1820: 7, 1830: 8, 1848: 7}),
        events={}, young_extra=0.0, peace_cap_ceiling_mod=0.0,
        scope=lambda y, s: 1.20,     # old France + Belgium + Liguria (+Tuscany)
    )
    # ---------------- forced success, layer B ----------------
    T['yi'] = dict(
        label='强行成功（乙层）',
        H0=56.0, dM=5.0, dQ=3.5,     # jia + Trafalgar/Ortegal hulls and crews saved (luck L1)
        truce=1812, antwerp='restricted', dutch_yards=False,
        coast=lambda y, s: 0.85,
        budget=lambda y, s: 110 if y == 1810 else (160 if y <= s['truce'] else (s.get('peace_budget', 145) if y < 1830 else 165)),
        F0_scale=lambda y, s: 1.0,
        spain=lambda y: lin(y, {1810: 16, 1830: 11, 1848: 8}),
        dutch=lambda y: lin(y, {1810: 6, 1820: 8, 1830: 9, 1848: 8}),
        events={}, young_extra=0.01, peace_cap_ceiling_mod=0.0,
        scope=lambda y, s: 1.22,     # as jia, plus Trafalgar crews kept
    )
    # ---------------- forced success, layer C ----------------
    T['bing'] = dict(
        label='强行成功（丙层）',
        H0=65.0, dM=10.0, dQ=6.5,    # yi + Netherlands annexed 1810 (9 hulls, ~5k men, ~3k qualified)
        truce=1812, antwerp='restricted', dutch_yards=True,
        coast=lambda y, s: 0.90 if y <= 1815 else 1.0,   # Dutch five-year conscription exemption
        budget=lambda y, s: 110 if y == 1810 else (160 if y <= s['truce'] else (s.get('squeeze', 145) if y < 1825 else (145 if y < 1830 else 165))),
        F0_scale=lambda y, s: 1.08,  # longer coast: Dutch ports and Hanse
        spain=lambda y: lin(y, {1810: 16, 1830: 11, 1848: 8}),
        dutch=lambda y: 0.0,
        events={}, young_extra=0.01, peace_cap_ceiling_mod=+1.0,
        scope=lambda y, s: 1.45,     # + Netherlands, Hanse, Oldenburg
    )
    # ---------------- flash in the pan ----------------
    def flash_budget(y, s):
        k = s.get('late_budget_scale', 1.0)
        if y == 1810: return 110
        if y == 1811: return 155
        if y == 1812: return 159
        if y == 1813: return 167
        if y <= 1815: return 170
        if y <= 1820: return 130
        if y <= 1825: return lin(y, {1821: 110, 1825: 70})
        if y <= 1830: return 65 * k
        if y <= 1840: return 70 * k
        return 85 * k
    T['flash'] = dict(
        label='昙花一现',
        H0=50.0, dM=0.0, dQ=0.0,
        truce=1825, antwerp='free', belgium='kept', dutch_yards=True,
        coast=lambda y, s: 1.0 if y <= 1815 else (0.85 if y <= 1821 else (0.70 if y <= 1825 else (0.55 if s.get('belgium') == 'kept' else 0.50))),
        budget=flash_budget,
        F0_scale=lambda y, s: 1.0 if y <= 1825 else 0.72,   # post-collapse France: Restoration-sized coast
        spain=lambda y: 0.0, dutch=lambda y: 0.0,
        # year: (hulls removed, M removed, Q removed); 1826: foreign seamen released at the settlement
        events={1816: (9, 5, 3), 1822: (8, 4, 2.5)},
        release_1826=(0.30, 0.25),
        young_extra=0.0, peace_cap_ceiling_mod=-4.0,
        scope=lambda y, s: 1.35 if y <= 1815 else (1.20 if y <= 1821 else (1.10 if y <= 1825 else (1.05 if s.get('belgium') == 'kept' else 1.0))),
    )
    return T


# ----------------------------------------------------------------------------
# CORE SIMULATION
# ----------------------------------------------------------------------------
def a12(H, M, Q, ready, oM, oQ, idle=0.0, insc=None):
    c = [ready * max(0.0, H - idle), (M - oM) / FR['crew'], (Q - oQ) / FR['qcrew']]
    names = ['hull', 'men', 'qualified']
    if insc is not None:
        c.append(insc); names.append('inscription')
    v = max(0.0, min(c))
    return math.floor(v + 1e-9), names[c.index(min(c))]


def inscription_cap(y, T, s, bfr, truce, peace):
    """A12 ceiling from the inscription maritime (peace years only)"""
    if not peace:
        return None
    reg = lin(y, FR['reg_hist']) * T['scope'](y, s) * (1 + val(FR['trade_bonus'], bfr)) ** max(0, y - truce)
    qn = val(FR['q_nonline_1815_30'], bfr) if y <= 1830 else val(FR['q_nonline_1831_48'], bfr)
    return (val(FR['phi'], bfr) * reg - qn) / FR['qcrew']


def f3_schedule(y, sc, b):
    if y == 1810: return 0.0
    if y <= 1815: return val([8, 10, 12], b)
    if y <= 1820: return val([8, 9, 10], b) if sc == 'P' else val([7, 8.5, 10], b)
    return val([6, 7, 8], b)


def run(track, bfr='base', buk=None, settings=None, validation=None):
    """Run one track.  bfr: French bundle; buk: British bundle ('lo' = strong
    British response, 'hi' = weak).  validation='W'/'P' reproduces F3 exactly."""
    T = track_defs()[track]
    s = dict(truce=T['truce'], antwerp=T.get('antwerp', 'restricted'), belgium=T.get('belgium', 'kept'))
    if settings:
        s.update(settings)
    buk = buk or bfr
    if validation:
        H, M, Q = 50.0, val(FR['M0'], bfr), val(FR['Q0'], bfr)
    else:
        H = T['H0']
        M = val(FR['M0'], bfr) + T['dM']
        Q = val(FR['Q0'], bfr) + T['dQ']
    Hu = UK['H1810']
    rows = []
    prev = dict(A12=None, I=None, net=0.0)
    cap_peace = None
    share_now = None
    for y in YEARS:
        truce = 1815 if validation else s['truce']
        peace = (validation == 'P' and y >= 1816) if validation else (y > truce)
        yp = (y - truce) if peace else 0
        if peace:
            Min, Mex = val(FR['P_Min'], bfr), val(FR['P_Mexit'], bfr)
            Qin, Qex = val(FR['P_Qin'], bfr), val(FR['P_Qexit'], bfr)
            ready = val(FR['P_ready'], bfr)
            oM = FR['P_oM_early'] if yp <= 5 else FR['P_oM_late']
            oQ = FR['P_oQ_early'] if yp <= 5 else FR['P_oQ_late']
            ret, loss = val(FR['P_ret'], bfr), val(FR['P_loss'], bfr)
        else:
            Min, Mex = val(FR['W_Min'], bfr), val(FR['W_Mexit'], bfr)
            Qin, Qex = val(FR['W_Qin'], bfr), val(FR['W_Qexit'], bfr)
            ready = val(FR['W_ready'], bfr)
            oM, oQ = val(FR['W_oM'], bfr), val(FR['W_oQ'], bfr)
            ret, loss = val(FR['W_ret'], bfr), val(FR['W_loss'], bfr)
        if y <= 1815:
            ret = val(FR['young_ret'], bfr) + (0.0 if validation else T['young_extra'])
        coast = (1.0 if validation else T['coast'](y, s)) * s.get('man_scale', 1.0)
        # ---- training link (peace): more ships in commission, more qualified seamen
        if peace and not validation and share_now is not None:
            Qin = Qin * (0.8 + 0.5 * share_now)
        # ---- capacity (launches/yr)
        if validation:
            cap = f3_schedule(y, validation, bfr)
        elif not peace:
            cap = 0.0 if y == 1810 else val(FR['cap_1811_15'], bfr)
            if not T['dutch_yards']: cap -= 0.5
            if track == 'flash':
                if y >= 1816: cap -= 0.5
                if y >= 1822: cap -= 1.5
        else:
            ceiling = val(FR['P_cap_ceiling'], bfr) + T['peace_cap_ceiling_mod']
            if not T['dutch_yards']: ceiling -= 0.5
            ceiling -= antwerp_cut(y, s)
            if track == 'flash' and s.get('belgium') == 'lost' and y >= 1826: ceiling -= 2.0
            if cap_peace is None:
                cap_peace = min(ceiling, val(FR['cap_1811_15'], bfr) - (0 if T['dutch_yards'] else 0.5) - antwerp_cut(y, s))
            cap = min(ceiling, cap_peace)
        # ---- events
        evH = evM = evQ = 0.0
        if not validation and y in T['events']:
            evH, evM, evQ = T['events'][y]
        if not validation and track == 'flash' and s.get('belgium') == 'lost' and y == 1826:
            evH += H * 0.28 / 3.0   # Antwerp ~28% of hulls; one third to the new owner (Paris 1814 art. XV)
        # ---- step 1: retirement, losses, events, personnel
        if y > 1810:
            nat = H * ret
            H_pre = max(0.0, H - nat - loss - evH)
            M = max(0.0, M * (1 - Mex) + Min * coast - evM)
            Q = max(0.0, min(M, Q * (1 - Qex) + Qin * coast - evQ))
        else:
            nat, H_pre = 0.0, H
        if (not validation) and track == 'flash' and y == 1826:
            M *= (1 - T['release_1826'][0]); Q *= (1 - T['release_1826'][1])
        idle = 0.0
        if (not validation) and s['antwerp'] == 'restricted' and truce < y <= truce + 3:
            idle = 0.3 * 0.28 * H_pre    # Antwerp squadron being moved to other bases
        insc = None if validation else inscription_cap(y, T, s, bfr, truce, peace)
        A_pre, _ = a12(H_pre, M, Q, ready, oM, oQ, idle, insc)
        budget = slack = None
        forced = 0.0
        if validation:
            L = cap if y > 1810 else 0.0
            H = H_pre + L
            A, bind = a12(H, M, Q, ready, oM, oQ)
            I = math.floor(A * (val([.45, .55, .65], bfr) if peace else val([.80, .875, .95], bfr)))
            share = None
        else:
            budget = T['budget'](y, s) * s.get('budget_scale', 1.0)
            if s.get('steam_from') and y >= s['steam_from']:
                budget *= 1 - s.get('steam_share', 0.15) * min(1.0, (y - s['steam_from'] + 1) / 8.0)
            F0 = (val(FR['F0p'], bfr) if peace else val(FR['F0w'], bfr)) * T['F0_scale'](y, s)
            kap = val(FR['kap_p'], bfr) if peace else val(FR['kap_w'], bfr)
            cI = val(FR['c_Ip'], bfr) if peace else val(FR['c_Iw'], bfr)
            co, cL = val(FR['c_o'], bfr), val(FR['c_L'], bfr)
            share = s.get('share', val(FR['P_share'], bfr)) if peace else val(FR['W_share'], bfr)
            I_des = share * A_pre
            nonbuild = F0 + (1 + kap) * (cI * I_des + co * (H_pre - I_des))
            if nonbuild <= budget:
                I_aff = I_des
                L = min(cap, (budget - nonbuild) / ((1 + kap) * cL)) if y > 1810 else 0.0
                if peace:
                    menlim = min((M - oM) / FR['crew'], (Q - oQ) / FR['qcrew'], insc if insc is not None else 1e9)
                    H_goal = max(0.0, menlim) / ready * (1 + val(FR['hull_reserve'], bfr))
                    L = max(0.0, min(L, H_goal - H_pre))
                slack = budget - nonbuild - (1 + kap) * cL * L
                if peace and slack > 0 and 'share' not in s:
                    # slack buys more ships in commission (training) up to the cap share
                    extra = min(slack / ((1 + kap) * (cI - co)), max(0.0, (FR['P_share_max'] - share) * A_pre))
                    I_aff += extra
                    slack -= extra * (1 + kap) * (cI - co)
                    share = I_aff / A_pre if A_pre else share
                if peace and slack > (1 + kap) * cL and L >= cap - 1e-9:
                    cap_peace = (cap_peace or cap) + FR['P_cap_growth']      # expand slips / timber stocks
            else:
                I_aff = max(0.0, (budget - F0 - (1 + kap) * co * H_pre) / ((1 + kap) * (cI - co)))
                I_aff = min(I_aff, I_des)
                L = 0.0
                rest = F0 + (1 + kap) * (cI * I_aff + co * (H_pre - I_aff))
                if rest > budget + 1e-9:
                    forced = (rest - budget) / ((1 + kap) * co)
                    H_pre = max(0.0, H_pre - forced)
                slack = 0.0
            H = H_pre + L
            A, bind = a12(H, M, Q, ready, oM, oQ, idle, insc)
            I = min(math.floor(I_aff + 1e-9), A)
            share_now = share if peace else None
        # ---- British response (1-year perception lag; projects visible net construction)
        uk = None
        if not validation:
            ub = buk
            r, g, a = val(UK['r'], ub), val(UK['g'], ub), val(UK['a'], ub)
            cF, w = val(UK['cF'], ub), val(UK['w_ally'], ub)
            Fa = prev['A12'] if prev['A12'] is not None else A
            Fi = prev['I'] if prev['I'] is not None else I
            proj = max(0.0, prev['net']) * UK['lookahead_years'] * ready
            sp, du = T['spain'](y), T['dutch'](y)
            ru = lin(y, UK['russia'])
            wR = val(UK['wR_after_collapse'], ub) if (track == 'flash' and y > 1825) else val(UK['wR_fr_dominant'], ub)
            if s.get('uk_off') and peace:
                Fthreat, proj = 0.0, 0.0
            if peace and s['antwerp'] == 'free' and track != 'flash':
                g = g + val(UK['g_scheldt'], ub)
            if peace:
                if not s.get('uk_off'):
                    Fthreat = cF * (Fa + proj) + w * (sp + du) + wR * ru
                A12_tgt = max(val(UK['A12_floor'], ub), r * Fthreat + g)
                H_tgt = A12_tgt / a
                I_tgt = max(val(UK['I_floor'], ub), val(UK['rI'], ub) * Fi + val(UK['gI'], ub))
                ceiling = val(UK['ceiling_peace'], ub); vcost = UK['v_peace']; a_eff = a
                Lmin = UK['L_min_peace']
            else:
                Fthreat = cF * Fi + w * 0.6 * (sp + du) + wR * 0.6 * ru
                floor_w = val(UK['I_war_floor'], ub) if y <= 1815 else val(UK['I_war_floor_after1815'], ub)
                I_tgt = max(floor_w, r * Fthreat + g)
                H_tgt = I_tgt / UK['a_war']
                A12_tgt = H_tgt * UK['a_war']
                ceiling = UK['ceiling_war']; vcost = UK['v_war']; a_eff = UK['a_war']
                Lmin = UK['L_min_war']
            if Hu > H_tgt * (UK['dispose_margin'] if peace else 1.0):
                retire = (min(UK['ret_surplus'] * Hu, max(UK['ret'] * Hu, Hu - H_tgt * UK['dispose_margin']))
                          if peace else UK['ret'] * Hu)
                Lu = Lmin
            elif Hu > H_tgt:
                retire = UK['ret'] * Hu
                Lu = Lmin
            else:
                retire = UK['ret_min'] * Hu
                gap = H_tgt - (Hu - retire)
                Lu = min(UK['L_surge'] if gap > 20 else UK['L_max'], max(Lmin, gap))
            Hu_new = Hu - retire + Lu
            Iu = min(I_tgt, Hu_new * a_eff)
            def manning(Iu):
                if peace:
                    R_, C_, O_ = 0.6 * Iu + 10, 0.4 * Iu + 35, 5000 + 40 * Iu
                else:
                    R_, C_, O_ = Iu, 2 * Iu, 15000
                return 650 * Iu + 280 * R_ + 110 * C_ + O_
            Mu = manning(Iu)
            cost = UK['K0'] + UK['k_h'] * Hu_new + vcost * Mu / 1e6 + UK['c_b'] * Lu
            ceil_bind = False
            if cost > ceiling:
                ceil_bind = True
                floor_I = val(UK['I_floor'], ub) if peace else 60
                while cost > ceiling and Iu > floor_I:
                    Iu = max(floor_I, Iu - 1); Mu = manning(Iu)
                    cost = UK['K0'] + UK['k_h'] * Hu_new + vcost * Mu / 1e6 + UK['c_b'] * Lu
                while cost > ceiling and Lu > 0:
                    d = min(1.0, Lu); Lu -= d; Hu_new -= d
                    cost = UK['K0'] + UK['k_h'] * Hu_new + vcost * Mu / 1e6 + UK['c_b'] * Lu
            Hu = Hu_new
            uk = dict(H=Hu, I=Iu, A12=Hu * a_eff, L=Lu, retire=retire, M=Mu, cost=cost, ceiling=ceiling,
                      ceil_bind=ceil_bind, A12_tgt=A12_tgt, H_tgt=H_tgt, I_tgt=I_tgt, Fthreat=Fthreat,
                      spain=sp, dutch=du)
        prev = dict(A12=A, I=I, net=(L - nat - loss) if y > 1810 else 0.0)
        row = dict(track=track, fr_bundle=bfr, uk_bundle=buk, year=y, regime='peace' if peace else 'war',
                   fr_H=round(H, 3), fr_L=round(L, 3), fr_retire=round(nat, 3), fr_forced_condemn=round(forced, 3),
                   fr_M_k=round(M, 3), fr_Q_k=round(Q, 3), fr_A12=A, fr_bind=bind, fr_I=I,
                   fr_share=None if share is None else round(share, 3), fr_cap=round(cap, 2),
                   fr_budget=None if budget is None else round(budget, 2),
                   fr_slack_for_cruisers_steam=None if slack is None else round(slack, 2))
        if uk:
            dF, dU = val(FR['d_F'], bfr), val(UK['d_UK'], bfr)
            row.update(uk_H=round(uk['H'], 3), uk_I=round(uk['I'], 3), uk_A12=round(uk['A12'], 3),
                       uk_L=round(uk['L'], 2), uk_M=round(uk['M']), uk_cost_GBPm=round(uk['cost'], 3),
                       uk_ceiling=uk['ceiling'], uk_ceiling_binding=uk['ceil_bind'],
                       uk_A12_target=round(uk['A12_tgt'], 2), uk_H_target=round(uk['H_tgt'], 2),
                       uk_Fthreat=round(uk['Fthreat'], 2), spain_A12=round(uk['spain'], 2),
                       dutch_A12=round(uk['dutch'], 2),
                       T_hull_tonnage=round(H * dF / (uk['H'] * dU), 4),
                       T_A12_tonnage=round(A * dF / (uk['A12'] * dU), 4),
                       ratio_I=round(I / uk['I'], 4) if uk['I'] else None,
                       coalition_A12_ratio=round((A + 0.5 * (uk['spain'] + uk['dutch'])) / uk['A12'], 4))
        rows.append(row)
    return rows


# ----------------------------------------------------------------------------
# VALIDATION against the F3 card output (copied, unchanged)
# ----------------------------------------------------------------------------
def validate():
    src = HERE / 'source_copies' / 'F3_t_b1a536' / 'F3_capacity.csv'
    ref = {}
    with src.open() as f:
        for r in csv.DictReader(f):
            ref[(r['scenario'], r['bound'], int(r['year']))] = r
    out, worst, n = [], 0.0, 0
    for sc in ('W', 'P'):
        for b, lab in zip(B, ('low', 'base', 'high')):
            for r in run('flash', bfr=b, validation=sc):
                k = (sc, lab, r['year'])
                if k not in ref:
                    continue
                n += 1
                dH = abs(r['fr_H'] - float(ref[k]['hulls']))
                dA = abs(r['fr_A12'] - int(ref[k]['mobilizable_integer']))
                worst = max(worst, dH)
                if dA != 0 or dH > 1e-3:
                    out.append(f'MISMATCH {k}: H {r["fr_H"]} vs {ref[k]["hulls"]}; A12 {r["fr_A12"]} vs {ref[k]["mobilizable_integer"]}')
    out.append(f'F3 replication (French stock-flow, exogenous F3 launch schedule, no budget, no UK): '
               f'{n} rows compared, worst |dH|={worst:.1e} (rounding), A12 exact; '
               f'{"PASS" if not any(l.startswith("MISMATCH") for l in out) else "FAIL"}')
    return out


# ----------------------------------------------------------------------------
# DRIVER
# ----------------------------------------------------------------------------
SNAP = (1815, 1830, 1848)


def envelope_runs():
    """base; lower = France 'lo' + British strong; upper = France 'hi' + British weak"""
    res = {}
    for tr in ('jia', 'flash', 'yi', 'bing'):
        res[(tr, 'base')] = run(tr, 'base', 'base')
        res[(tr, 'lower')] = run(tr, 'lo', 'lo', settings=dict(late_budget_scale=0.85) if tr == 'flash' else None)
        res[(tr, 'upper')] = run(tr, 'hi', 'hi', settings=dict(late_budget_scale=1.15) if tr == 'flash' else None)
    return res


def pick(rows, y):
    return next(r for r in rows if r['year'] == y)


def sensitivity():
    out = []
    tests = [
        ('jia', 'Antwerp not restricted', dict(antwerp='free')),
        ('jia', 'truce 1812', dict(truce=1812)),
        ('jia', 'truce 1816', dict(truce=1816)),
        ('jia', 'war budget 120 (1811-truce)', dict(war_budget=120)),
        ('jia', 'war budget 190 (1811-truce)', dict(war_budget=190)),
        ('jia', 'war budget 90 (ch.1 650 tier)', dict(war_budget=90)),
        ('jia', 'peace commission share fixed 0.30', dict(share=0.30)),
        ('jia', 'peace commission share fixed 0.55', dict(share=0.55)),
        ('jia', 'all budgets x0.85', dict(budget_scale=0.85)),
        ('yi', 'peace budget 195 in 1813-29 (army 280->230)', dict(peace_budget=195)),
        ('yi', 'Antwerp not restricted', dict(antwerp='free')),
        ('bing', 'Dutch-debt squeeze: 130 in 1813-24', dict(squeeze=130)),
        ('flash', 'Belgium and Antwerp lost 1826', dict(belgium='lost')),
        ('jia', 'British response switched off (peace floor only)', dict(uk_off=True)),
        ('yi', 'British response switched off (peace floor only)', dict(uk_off=True)),
        ('jia', 'French seamen inflow x0.8', dict(man_scale=0.8)),
        ('jia', 'French seamen inflow x1.2', dict(man_scale=1.2)),
    ]
    runs = [(t, 'reference (base)', {}, 'base', 'base') for t in ('jia', 'yi', 'bing', 'flash')]
    runs += [(t, n, st, 'base', 'base') for t, n, st in tests]
    runs += [(t, 'British strong response only (France base)', {}, 'base', 'lo') for t in ('jia', 'yi', 'bing', 'flash')]
    runs += [(t, 'British weak response only (France base)', {}, 'base', 'hi') for t in ('jia', 'yi', 'bing', 'flash')]
    runs += [(t, 'French unfavourable only (Britain base)', {}, 'lo', 'base') for t in ('jia', 'yi', 'bing', 'flash')]
    runs += [(t, 'French favourable only (Britain base)', {}, 'hi', 'base') for t in ('jia', 'yi', 'bing', 'flash')]
    runs += [(t, 'French budget 15% to steam from 1838', dict(steam_from=1838, steam_share=0.15), 'base', 'base') for t in ('jia', 'yi', 'bing', 'flash')]
    for tr, name, st, bf, bu in runs:
        rows = run(tr, bf, bu, settings=st)
        for y in SNAP:
            r = pick(rows, y)
            out.append(dict(track=tr, test=name, year=y, fr_H=r['fr_H'], fr_A12=r['fr_A12'], fr_I=r['fr_I'],
                            uk_H=r['uk_H'], uk_A12=r['uk_A12'], uk_I=r['uk_I'], T_hull=r['T_hull_tonnage'],
                            T_A12=r['T_A12_tonnage'], uk_cost=r['uk_cost_GBPm']))
    # British rule vs 'no response' (UK held at B3 armed-peace low package, H 125, A12 100)
    return out


def write_csv(path, rows):
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader(); w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--quiet', action='store_true')
    args = ap.parse_args()
    val_lines = validate()
    (HERE / 'out_validation.txt').write_text('\n'.join(val_lines) + '\n')
    res = envelope_runs()
    allrows = []
    for (tr, env), rows in res.items():
        for r in rows:
            rr = dict(envelope=env); rr.update(r); allrows.append(rr)
    write_csv(HERE / 'out_annual.csv', allrows)
    snaps = []
    for (tr, env), rows in res.items():
        for y in SNAP:
            r = pick(rows, y)
            snaps.append(dict(track=tr, envelope=env, year=y, fr_H=r['fr_H'], fr_A12=r['fr_A12'], fr_I=r['fr_I'],
                              fr_bind=r['fr_bind'], fr_budget=r['fr_budget'], fr_L=r['fr_L'], fr_cap=r['fr_cap'],
                              fr_slack=r['fr_slack_for_cruisers_steam'], uk_H=r['uk_H'], uk_A12=r['uk_A12'],
                              uk_I=r['uk_I'], uk_cost_GBPm=r['uk_cost_GBPm'],
                              uk_ceiling_binding=r['uk_ceiling_binding'], T_hull_tonnage=r['T_hull_tonnage'],
                              T_A12_tonnage=r['T_A12_tonnage'], ratio_I=r['ratio_I'],
                              coalition_A12_ratio=r['coalition_A12_ratio']))
    write_csv(HERE / 'out_snapshots.csv', snaps)
    write_csv(HERE / 'out_sensitivity.csv', sensitivity())
    (HERE / 'out_params.json').write_text(json.dumps(dict(FR=FR, UK=UK), ensure_ascii=False, indent=1))
    if not args.quiet:
        print(val_lines[-1])
        for s_ in snaps:
            print(s_['track'], s_['envelope'], s_['year'], 'FR H/A12/I', s_['fr_H'], s_['fr_A12'], s_['fr_I'],
                  'UK H/A12/I', round(s_['uk_H'], 1), round(s_['uk_A12'], 1), round(s_['uk_I'], 1),
                  'T', s_['T_hull_tonnage'], 'TA', s_['T_A12_tonnage'], 'cost', s_['uk_cost_GBPm'],
                  'slack', s_['fr_slack'])


if __name__ == '__main__':
    main()
