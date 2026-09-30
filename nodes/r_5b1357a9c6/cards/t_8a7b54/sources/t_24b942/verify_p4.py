#!/usr/bin/env python3
"""Independent arithmetic audit of P4 CSV against F3/B3 frozen inputs; not empirical calibration."""
import csv
from pathlib import Path
p=Path(__file__).resolve().parent
root=p.parents[1]/'cards'
def load(path):
    with path.open(newline='') as f:return list(csv.DictReader(f))
r=load(p/'P4_annual.csv'); four=load(p/'P4_four_snapshots.csv'); sens=load(p/'P4_sensitivity.csv')
f3=load(root/'t_b1a536/F3_capacity.csv'); b3=load(root/'t_998052/B3_response.csv')
assert len(r)==96 and len(four)==24 and len(sens)==18
index={(x['branch'],x['bound'],int(x['year'])):x for x in r}
assert len(index)==len(r)
for x in r:
    s,b,y=x['branch'],x['bound'],int(x['year'])
    ff=next(v for v in f3 if (v['scenario'],v['bound'],int(v['year']))==(s,b,y))
    assert abs(float(x['france_line_hulls'])-float(ff['hulls']))<.00051
    assert int(x['france_A12'])==int(ff['mobilizable_integer'])
    t=float(x['france_line_displacement_tonnes_ASSUMED'])/float(x['britain_line_displacement_tonnes_ASSUMED'])
    e=float(x['france_effective_A12_tonnes_ASSUMED'])/float(x['britain_effective_A12_tonnes_ASSUMED'])
    assert abs(t-float(x['tonnage_ratio_FR_over_UK']))<.000051
    assert abs(e-float(x['effectiveness_ratio_FR_over_UK']))<.000051
    assert float(x['britain_A12'])<=float(x['britain_line_hulls'])
    assert float(x['france_A12'])<=float(x['france_line_hulls'])
    if y in (1815,1820,1825,1830) and b!='base':
        uk_s='W' if y==1815 else s
        bb=next(v for v in b3 if (v['scenario'],v['bound'],int(v['year']))==(uk_s,b,y))
        assert abs(float(x['britain_A12'])-float(bb['mobilizable_within_12months']))<.00051
        assert abs(float(x['britain_line_hulls'])-float(bb['sea_line_hulls']))<.00051
    if y in (1815,1820,1825,1830):
        snap=next(v for v in four if (v['branch'],v['bound'],int(v['year']))==(s,b,y))
        assert all(snap[k]==x[k] for k in snap)
    if y>1815:
        old=index[(s,b,y-1)]
        for stem,launch,exits in (
           ('france_line_hulls','france_line_launches',('france_line_natural_exit','france_line_war_loss')),
           ('france_frst','france_fr_launches',('france_fr_exit',)),
           ('france_smst','france_sm_launches',('france_sm_exit',)),
           ('britain_line_hulls','britain_line_launches',('britain_line_exit_implied',)),
           ('britain_frst','britain_fr_launches',('britain_fr_exit_implied',)),
           ('britain_smst','britain_sm_launches',('britain_sm_exit_implied',))):
            resid=float(x[stem])-float(old[stem])-float(x[launch])+sum(float(x[k]) for k in exits)
            assert abs(resid)<.002,(s,b,y,stem,resid)
for bound in ('low','base','high'):
    w=index[('W',bound,1815)]; q=index[('P',bound,1815)]
    for col in ('france_line_hulls','france_A12','france_fr_commissioned','france_sm_commissioned','britain_line_hulls','britain_A12','britain_commissioned_line','tonnage_ratio_FR_over_UK','effectiveness_ratio_FR_over_UK'):
        assert w[col]==q[col],(bound,col)
for x in sens[-2:]:
    assert x['test']=='UK_holds_W_instead_of_P_in_1830'
    uk=index[(x['uk_branch'],'base',1830)]
    fr=index[('P','base',1830)]
    v=float(fr['france_effective_A12_tonnes_ASSUMED'])/float(uk['britain_effective_A12_tonnes_ASSUMED'])
    assert abs(v-float(x['effectiveness_ratio_FR_over_UK']))<.000051
print('independent CSV/F3/B3 arithmetic verification: 96 annual, 24 snapshot, 18 stress rows PASS; no historical calibration performed')
