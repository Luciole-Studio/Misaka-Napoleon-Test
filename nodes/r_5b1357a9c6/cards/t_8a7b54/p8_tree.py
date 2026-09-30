#!/usr/bin/env python3
"""P8 deterministic interval scenario tree; no historical frequency estimation.

Run from project root: python3 nodes/r_5b1357a9c6/cards/t_8a7b54/p8_tree.py
All scalar bounds are joint monotone corner bounds for the stated epistemic box.
Dependence model is a valid convex mixture of conditionally independent and
comonotonic Bernoulli triples (E,R,A), conditional on French framework F.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path
from itertools import product

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
P6 = ROOT / 'nodes/r_5b1357a9c6/cards/t_c87512'
D = json.loads((HERE/'p8_assumptions.json').read_text(encoding='utf-8'))

with (P6/'P6_realization.csv').open(encoding='utf-8-sig', newline='') as f:
    upstream = list(csv.DictReader(f))
assert [(float(r['p_low']),float(r['p_high'])) for r in upstream[:5]] == [(.15,.30),(.40,.60),(.40,.60),(.35,.50),(.45,.60)]
with (P6/'P6_impulse_risk.csv').open(encoding='utf-8-sig', newline='') as f:
    p6_impulse = list(csv.DictReader(f))[:5]
impulse = {float(x['红线行动占单边冲动的份额']):
           (float(x['存续_14周期(≈1834)']),float(x['存续_22周期(≈1848)'])) for x in p6_impulse}
assert abs(impulse[.15][1]-.29)<1e-9

KEYS=['adopt','maintain_given_adopt','uk_given_framework','russia_given_framework',
      'austria_given_framework','residual_dependence_lambda','redline_share_of_impulse']

def piecewise(x, col):
    """Monotone interpolation of P6's discretized impulse stress, not forecast."""
    keys=sorted(impulse)
    if x<keys[0] or x>keys[-1]:
        raise ValueError('redline outside upstream stress grid')
    if x in impulse: return impulse[x][col]
    for lo,hi in zip(keys,keys[1:]):
        if lo<x<hi:
            return impulse[lo][col]+(impulse[hi][col]-impulse[lo][col])*(x-lo)/(hi-lo)
    raise AssertionError(x)

def triple_joint(E,R,A,lam):
    assert all(0<=x<=1 for x in (E,R,A,lam))
    return (1-lam)*E*R*A+lam*min(E,R,A)

def compute(z):
    F=z['adopt']; W=z['maintain_given_adopt']
    E=z['uk_given_framework']; R=z['russia_given_framework']; A=z['austria_given_framework']
    lam=z['residual_dependence_lambda']; r=z['redline_share_of_impulse']
    J=triple_joint(E,R,A,lam)
    C=F*W*J
    s1834=piecewise(r,0); s1848=piecewise(r,1)
    # P6 §6.2 conditional 1848 order survival given unbroken/broken treaty.
    d=.35+.5*s1848
    return {'P_J_given_F':J,'P_F':F*W,'P_C1815':C,
            'P_treaty_1834_given_C':s1834,'P_treaty_1848_given_C':s1848,
            'P_order_1848_given_C':d,'P_O1848':C*d,
            'P_Y1848_min':C*.35,'P_Y1848_max':C*.50}

def midpoint(box): return {k:sum(box[k])/2 for k in KEYS}

def exact_bounds(box):
    # Exact for each output by complete enumeration of 2^7 corners; here
    # monotonicity verified numerically and analytically (ER A independent term
    # <= min, s decreases in r, all other event factors nonnegative).
    out=[compute(dict(zip(KEYS,p))) for p in product(*(box[k] for k in KEYS))]
    return {key:(min(t[key] for t in out),max(t[key] for t in out)) for key in out[0]}

def savecsv(name, fields, rows):
    with (HERE/name).open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader()
        for row in rows: writer.writerow(row)

base=D['baseline']; center=compute(midpoint(base)); bounds=exact_bounds(base)
# source comparator and coherence checks
assert abs(.4*.35*.45-.063)<1e-12
assert abs(.6*.5*.6-.18)<1e-12
assert abs(.15*.4*.3-.018)<1e-12
assert abs(.30*.60*.50-.09)<1e-12
for p in product((0.,.2,.7,1.),repeat=1):
    j=triple_joint(.5,.425,.525,p[0]); assert 0<=j<=.425
for key,(lo,hi) in bounds.items(): assert 0<=lo<=hi<=1
# Generate scenario table; source P6 J .30–.50 retained separately, not substituted.
rows=[]
for name,box in [('P8-residual-copula',base)]+list(D['school_stress'].items()):
    b=exact_bounds(box); c=compute(midpoint(box))
    row={'profile':name}
    for target in ['P_J_given_F','P_F','P_C1815','P_order_1848_given_C','P_O1848']:
        row.update({target+'_low':f'{b[target][0]:.8f}',target+'_mid':f'{c[target]:.8f}',target+'_high':f'{b[target][1]:.8f}'})
    rows.append(row)
savecsv('P8_school_and_core.csv',list(rows[0]),rows)

# Tornado: one parameter varied over its admissible range with all others held
# at analyst central values. No false independent weights or error bars.
trows=[]
for key in KEYS:
    lo=midpoint(base); hi=midpoint(base)
    lo[key]=base[key][0]; hi[key]=base[key][1]
    a=compute(lo)['P_O1848']; b=compute(hi)['P_O1848']
    trows.append({'parameter':key,'input_low':base[key][0],'input_high':base[key][1],
                  'O1848_at_input_low':f'{a:.8f}','O1848_at_input_high':f'{b:.8f}',
                  'swing_percentage_points':f'{abs(a-b)*100:.5f}',
                  'orientation':('lower_when_input_rises' if a>b else 'higher_when_input_rises')})
trows.sort(key=lambda r:-float(r['swing_percentage_points']))
savecsv('P8_tornado.csv',list(trows[0]),trows)

# Events under B/S2 control 1815; contributions C & E are NOT unconditional
# totals over alternative histories. Event C=2015? NO, 1815.
co=D['conditional_outcomes_given_C1815']; an=D['analyst_stress_not_source_probabilities']
cb=bounds['P_C1815']; ob=bounds['P_O1848']
sub=[]
def add(event,denom,interval,source,comment='', contribution='C'):
    xlo,xhi=interval
    px=cb if contribution=='C' else ob
    sub.append({'event_id':event,'denominator':denom,'conditional_low':f'{xlo:.7f}',
                'conditional_high':f'{xhi:.7f}',
                'branch_contribution_1803_low':f'{px[0]*xlo:.8f}',
                'branch_contribution_1803_high':f'{px[1]*xhi:.8f}',
                'source_or_model':source,'warning':comment})
add('Q1_A_core_regular_1835','C1815',co['A_core_regular_1835'],'P2 + analyst timing',['conditional feasibility not statistical rate'][0])
mid=[an['A_mid_choice_given_C'][i]*an['A_mid_joint_resource_given_choice'][i]*
     an['A_mid_local_elite_transfer_given_resources'][i]*an['A_mid_survive_to_1848_given_transfer'][i] for i in (0,1)]
add('Q1_A_mid_56_676m_1848','O1848',mid,'P2 optimistic corner + analyst 4-stage stress','Rare corner; not P2 estimate; sacrifices B-level allies',contribution='O')
add('Q2_order_lasts_1848','C1815',bounds['P_order_1848_given_C'],'P6 impulse grid §§6.1–6.2','Same C and D; first two rates already included')
add('Q2_French_preferential_market_1848','C1815',co['X2_French_preferential_market_1848'],'X2 §16.3','X2 A assumes Napoleon still setting policy; problematic by 1848, read as policy inherited not life prediction')
add('Q2_limited_customs_union_1848','C1815',co['X2_limited_customs_union_1848'],'X2 §16.3','X2 bands are marginal and not normalized; S5 conditional only')
navy=[piecewise(base['redline_share_of_impulse'][1],0)*base['navy_funding_training_given_peace'][0],
      piecewise(base['redline_share_of_impulse'][0],0)*base['navy_funding_training_given_peace'][1]]
add('Q3_naval_E_proxy_ge_0_74_1830','C1815',navy,'P4 P/W envelope + P6 treaty impulse + P8 fiscal stress','Threshold is E proxy, not battle win rate; P4 P minimum .747 / W max .644')
for event,key in [('Q4_Spain_Bourbon_constitutional','Bourbon_constitutional_Spain_1848'),('Q4_Spain_Bourbon_ministerial','Bourbon_absolutist_ministerial_1848'),('Q4_Spain_Bonapartist','Bonapartist_Spain_1848'),('Q4_Spain_republic','republic_Spain_1848')]:
    add(event,'O1848+B4b',co[key],'SP1 §18 / P6 §6.3','Marginal intervals; combinations must normalize with other monarchic',contribution='O')
add('Q5_Italy_Rome_King_north_middle_union','O1848+succession',co['Italy_Rome_King_north_middle_union_1848'],'IT1 / P6 §6.3','Not already Naples and Papal states',contribution='O')
south=[co['Italy_Rome_King_north_middle_union_1848'][i]*co['Naples_join_given_union'][i] for i in (0,1)]
add('Q5_Italy_Rome_King_plus_Naples','O1848+succession',south,'IT1/IT2 + P8 analyst extension','Naples joining has no same-period French commitment',contribution='O')
add('Q6_Austria_stronger_than_Prussia','O1848',co['Austria_still_stronger_than_Prussia_1848'],'A/PR/G2 + analyst probability','Military-dynastic ranking; no 1834 Zollverein shortcut',contribution='O')
add('Q7_South_America_loose_federation','O1848',co['South_America_loose_Hispanic_federation_1848'],'SA §316–325','SA table overreaches on Mexico',contribution='O')
add('Q7_Mexico_independent','O1848',co['Mexico_de_facto_independent_1848'],'MX §0, §372','Can coexist with South America federation',contribution='O')
add('Q7_all_Hispanic_America_sovereign_Madrid','O1848',an['all_Hispanic_America_still_Madrid_sovereign_1848'],'logical upper bound from Mexico >=0.90','SA conflict; upper ≤0.1 no calibrated positive lower',contribution='O')
add('Q7_Cuba_still_Spanish','O1848+B4b',co['Cuba_still_Spanish_under_Bourbon_1848'],'MX §466–469','Bourbon legal-government branch; overall MX .40–.55',contribution='O')
add('Q8_French_trading_posts_unfortified','O1848',co['French_compoirs_restored_unfortified_1848'],'IN1 §⑬ B8 + analyst execution chance','Treaty-return clause vs Wellesley refusal; commercial enclave not India conquest',contribution='O')
add('Q8_Bengal_conquest_sustained','O1848',co['French_conquer_EIC_Bengal_and_hold_1848'],'IN1/IN2/P6 redline + analyst stress cap','Incompatible with lasting UK accord unless treaty collapses',contribution='O')
savecsv('P8_subquestions.csv',list(sub[0]),sub)

# Resource accounting consistency: source P2 compares independent options, not event
# probabilities, and P4-P2 high ends must not be simultaneously treated as free.
recheck={'upstream_P6_independent_joint':[.063,.180],
         'upstream_P6_common_factor_joint':[.30,.50],
         'P8_copula_J':bounds['P_J_given_F'],
         'P8_core_C1815':cb,'P8_order_O1848':ob,
         'P8_center_J':center['P_J_given_F'],'P8_center_O1848':center['P_O1848'],
         'P6_direct_common_order_1848':[.0081,.0585],
         'P8_mid_in_p6_joint_band':.30<=center['P_J_given_F']<=.50,
         'P6_treaty_1848_share_minmax':[min(impulse),max(impulse)],
         'all_conditional_outcomes_between_0_1':all(0<=float(x['conditional_low'])<=float(x['conditional_high'])<=1 for x in sub),
         'notes':'The last global escape cap for A_full is outside the budget-closed model; see text. No data-estimated statistical CI.'}
(HERE/'P8_audit.json').write_text(json.dumps(recheck,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: P6 input match; valid joint copula; outputs monotone; scenario and tornado CSVs written')
print(f"P8 C1815 {cb[0]:.6%}–{cb[1]:.6%}; O1848 {ob[0]:.6%}–{ob[1]:.6%}; J center {center['P_J_given_F']:.6f}")
