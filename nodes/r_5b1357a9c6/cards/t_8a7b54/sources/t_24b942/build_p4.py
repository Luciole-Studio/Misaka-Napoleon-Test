#!/usr/bin/env python3
"""Transparent conditional coupled naval inventory, NOT a calibrated historical estimate.
Inputs F3, B3 are existing research-card scenario assumptions. Python stdlib only.
"""
import csv, json
from pathlib import Path
P=Path(__file__).resolve().parent
R=P.parents[1]
F3=R/'cards/t_b1a536/F3_capacity.csv'
B3=R/'cards/t_998052/B3_response.csv'
SENS=R/'cards/t_b1a536/F3_sensitivity.csv'
with F3.open() as f:
    fs={(r['scenario'],r['bound'],int(r['year'])):r for r in csv.DictReader(f)}
with B3.open() as f:
    bs={(r['scenario'],r['bound'],int(r['year'])):r for r in csv.DictReader(f)}
with SENS.open() as f:
    sens={(r['scenario'],r['test'],int(r['year'])):r for r in csv.DictReader(f)}
yrs=(1815,1820,1825,1830)
B=('low','base','high')
F_T={'low':3200,'base':3500,'high':3800}
U_T={'low':3400,'base':3600,'high':3900}

def interp(y, knots):
    if y in knots:return float(knots[y])
    low=max(k for k in knots if k<y); high=min(k for k in knots if k>y)
    return float(knots[low])+(float(knots[high])-float(knots[low]))*(y-low)/(high-low)

def uk(s,b,y,col):
    if b=='base':return (uk(s,'low',y,col)+uk(s,'high',y,col))/2
    vals={yr:bs[(s,b,yr)][col] for yr in yrs}
    return interp(y,vals)

def fq(s,b,y):
    return float(fs[(s,b,y)]['fleet_training_factor_assumed'])

# Offshore cruiser stocks are additional transparent sensitivity assumptions.
# "small" means task-capable small cruiser, NOT Napoleon's 400 coastal boats.
def f_cruisers(s,b):
    ix=B.index(b)
    f= [35.,40.,45.][ix]; c=[45.,55.,65.][ix]
    out={1810:(f,c,0.,0.,0.,0.)}
    for y in range(1811,1831):
        if y<=1815:
            lfr=[4.,5.,6.][ix]; lsm=[4.,5.,6.][ix]
            exf=[.045,.04,.035][ix]; exc=[.09,.08,.07][ix]
            wf=[.3,.2,.1][ix]; wc=[.3,.2,.1][ix]
        elif s=='W':
            lfr=[2.,2.5,3.5][ix]; lsm=[4.,5.,6.][ix]
            exf=[.05,.045,.04][ix]; exc=[.09,.08,.07][ix]
            wf=[.3,.2,.1][ix]; wc=[.3,.2,.1][ix]
        else:
            lfr=[3.,3.5,4.][ix]; lsm=[6.,7.,8.][ix]
            exf=[.045,.04,.035][ix]; exc=[.07,.06,.05][ix]
            wf=[.05,.03,0.][ix]; wc=[.05,.03,0.][ix]
        ef=exf*f+wf; ec=exc*c+wc
        f += lfr-ef; c += lsm-ec
        out[y]=(f,c,lfr,lsm,ef,ec)
    return out

# B3 provides no cruiser-stock path, only frigate/small commissioned count and
# all line-ship stocks. We register UK cruiser stocks and completions separately.
UFR={
  'low': {1810:110,1815:120,1820:125,1825:130,1830:132},
  'high':{1810:120,1815:135,1820:145,1825:150,1830:155}}
USM={
  'low': {1810:215,1815:220,1820:225,1825:230,1830:235},
  'high':{1810:245,1815:255,1820:265,1825:275,1830:285}}

def uc(s,b,y):
    if b=='base':
        a=uc(s,'low',y); d=uc(s,'high',y)
        return tuple((v+w)/2 for v,w in zip(a,d))
    F=interp(y,UFR[b]); C=interp(y,USM[b])
    if y<=1810: return F,C,0,0,0,0
    LFR={'low':5,'high':8}[b]; LSM={'low':16,'high':22}[b]
    prevF=interp(y-1,UFR[b]); prevC=interp(y-1,USM[b])
    ef=prevF+LFR-F; ec=prevC+LSM-C
    return F,C,LFR,LSM,ef,ec

def u_line(s,b,y):
    if y==1810:return 124.,0.,0.
    H=uk(s,b,y,'sea_line_hulls') if y>=1815 else interp(y,{1810:124,1815:uk(s,b,1815,'sea_line_hulls')})
    prev=uk(s,b,y-1,'sea_line_hulls') if y>1815 else interp(y-1,{1810:124,1815:uk(s,b,1815,'sea_line_hulls')})
    # interpolation across 5y blocks, six/eight gross completions each year
    L={'low':6,'base':7,'high':8}[b]
    return H,L,prev+L-H

def uk_q(s,b,y):
    first={'low':.95,'base':1.00,'high':1.05}[b]
    last=({'W':{'low':1.00,'base':1.05,'high':1.10},
            'P':{'low':.90,'base':.95,'high':1.00}}[s][b])
    return first+(last-first)*(y-1815)/15

def officer_fr(s,b,y):
    first={'low':.35,'base':.45,'high':.55}[b]
    last=({'W':{'low':.58,'base':.67,'high':.76},
            'P':{'low':.65,'base':.75,'high':.85}}[s][b])
    return first+(last-first)*(y-1815)/15

def officer_uk(s,b,y):
    first={'low':.78,'base':.83,'high':.88}[b]
    last=({'W':{'low':.83,'base':.88,'high':.93},
            'P':{'low':.72,'base':.78,'high':.84}}[s][b])
    return first+(last-first)*(y-1815)/15

rows=[]; snaps=[]
for s in ('W','P'):
    for b in B:
        fc=f_cruisers(s,b)
        for y in range(1815,1831):
            # 1815 is common pre-settlement snapshot. For P, use W British
            # in the four-section ratio; report P-post-truce as a non-synchronous note.
            bsame = 'W' if (s=='P' and y==1815) else s
            f=fs[(s,b,y)]; H=float(f['hulls']); A=int(f['mobilizable_integer'])
            FFR,FSM,LFR,LSM,EFR,ESM=fc[y]
            UFR_,USM_,ULFR,ULSM,UEFR,UESM=uc(bsame,b,y)
            UH,UL,UE=u_line(bsame,b,y)
            UA=uk(bsame,b,y,'mobilizable_within_12months')
            UI=uk(bsame,b,y,'commissioned_line')
            URI=uk(bsame,b,y,'standing_frigates')
            USI=uk(bsame,b,y,'standing_small_cruisers')
            UM=uk(bsame,b,y,'standing_total_personnel')
            UBS=uk(bsame,b,y,'standing_cost_low')/1e6
            UBE=uk(bsame,b,y,'standing_cost_high')/1e6
            FOther=float(f['nonline_personnel_reserved_1000'])*1000
            # French cruiser active subset limited by nonline pool with shore min 5k.
            desired={'W':{'low':.7,'base':.75,'high':.8},
                     'P':{'low':.35,'base':.45,'high':.55}}[bsame][b]
            crewdemand=(FFR*300+FSM*110)*desired
            active_factor=min(desired,max(0,(FOther-5000)/(FFR*300+FSM*110)))
            fri=FFR*active_factor; smi=FSM*active_factor
            frac_f= float(f['sea_training_days_assumed'])
            ukdays={'W':{'low':140,'base':175,'high':210},
                    'P':{'low':100,'base':135,'high':170}}[bsame][b]
            # assumption: representative line training, not logged fleet average.
            qt=uk_q(bsame,b,y)
            FT=H*F_T[b]; UT=UH*U_T[b]
            EA=A*F_T[b]*fq(s,b,y)
            EU=UA*U_T[b]*qt
            officerF=officer_fr(s,b,y); officerU=officer_uk(bsame,b,y)
            row=dict(record_type='CONDITIONAL_MODEL_NOT_OBSERVATION', branch=s,
                mapped_S='S2/S3' if s=='W' else 'S1/S2-truce/S5', bound=b, year=y,
                time_note='common_pre_truce_1815' if y==1815 else 'annual_planning_year',
                france_line_hulls=round(H,3), france_line_launches=float(f['launches']),
                france_line_natural_exit=float(f['natural_retirement']),
                france_line_war_loss=float(f['war_loss']), france_A12=A,
                france_commissioned_line=int(f['commissioned_model_I']),
                france_frst=round(FFR,3), france_smst=round(FSM,3),
                france_fr_launches=LFR, france_sm_launches=LSM,
                france_fr_exit=round(EFR,3), france_sm_exit=round(ESM,3),
                france_fr_commissioned=round(fri,2),france_sm_commissioned=round(smi,2),
                france_total_personnel=round(float(f['personnel_total_1000'])*1000),
                france_qualified_personnel=round(float(f['qualified_personnel_1000'])*1000),
                france_sea_training_days_assumed=frac_f,
                france_officers_8yr_share_ASSUMED=round(officerF,3),
                france_budget_planning_floor_million_francs_ASSUMED={'low':165,'base':195,'high':245}[b],
                britain_line_hulls=round(UH,3), britain_line_launches=UL,
                britain_line_exit_implied=round(UE,3),britain_A12=round(UA,3),
                britain_commissioned_line=round(UI,3),
                britain_frst=round(UFR_,3),britain_smst=round(USM_,3),
                britain_fr_launches=ULFR,britain_sm_launches=ULSM,
                britain_fr_exit_implied=round(UEFR,3),britain_sm_exit_implied=round(UESM,3),
                britain_fr_commissioned=round(URI,3),britain_sm_commissioned=round(USI,3),
                britain_total_personnel=round(UM),britain_sea_training_days_ASSUMED=ukdays,
                britain_officers_8yr_share_ASSUMED=round(officerU,3),
                britain_budget_min_million_GBP_at_1812_level=round(UBS,3),
                britain_budget_max_million_GBP_at_1812_level=round(UBE,3),
                france_line_displacement_tonnes_ASSUMED=round(FT,3),
                britain_line_displacement_tonnes_ASSUMED=round(UT,3),
                tonnage_ratio_FR_over_UK=round(FT/UT,4),
                france_effective_A12_tonnes_ASSUMED=round(EA,3),
                britain_effective_A12_tonnes_ASSUMED=round(EU,3),
                effectiveness_ratio_FR_over_UK=round(EA/EU,4),
                uk_skill_factor_ASSUMED=round(qt,4),
                fr_skill_factor_ASSUMED=fq(s,b,y))
            assert 0 <= int(f['commissioned_model_I']) <= A <= H+1e-8
            assert 0 <= UI <= UA <= UH+1e-8
            assert URI<=UFR_ and USI<=USM_ and fri<=FFR and smi<=FSM
            assert fri*300+smi*110 <= FOther-4999.99
            assert UE>=0 and UEFR>=0 and UESM>=0 and UE <= UL+124
            rows.append(row)
            if y in yrs:
                snaps.append({k:row[k] for k in ('branch','bound','year','time_note',
                    'france_line_hulls','britain_line_hulls','france_A12','britain_A12',
                    'france_line_displacement_tonnes_ASSUMED','britain_line_displacement_tonnes_ASSUMED',
                    'tonnage_ratio_FR_over_UK','effectiveness_ratio_FR_over_UK',
                    'fr_skill_factor_ASSUMED','uk_skill_factor_ASSUMED')})

# Stress: W only; one-at-a-time changes use F3 sensitivity, not summation.
stress=[]
for y in yrs:
    r=next(r for r in rows if r['branch']=='W' and r['bound']=='base' and r['year']==y)
    for test in ('lower_launches_30pct','lower_recruitment_30pct',
                 'ready_minus_10pp','no_Antwerp_initial12_and_launch3'):
        ff=sens[('W',test,y)]
        A=int(ff['A12']); FH=float(ff['hulls'])
        stress.append(dict(test=test,year=y,
            france_A12=A,france_hulls=round(FH,3),
            baseline_UK_A12=r['britain_A12'],
            tonnage_ratio_FR_over_UK=round(FH*F_T['base']/r['britain_line_displacement_tonnes_ASSUMED'],4),
            effectiveness_ratio_FR_over_UK=round(A*F_T['base']*r['fr_skill_factor_ASSUMED']/r['britain_effective_A12_tonnes_ASSUMED'],4),
            warning='single shock only; UK response held at W base'))
# UK peace-vs-war cut response sensitivity; same French P BASE in 1830.
pu=next(r for r in rows if r['branch']=='P' and r['bound']=='base' and r['year']==1830)
for scenario in ('P','W'):
    uk_a=uk(scenario,'base',1830,'mobilizable_within_12months')
    q=uk_q(scenario,'base',1830)
    stress.append(dict(test='UK_holds_W_instead_of_P_in_1830',year=1830,
        uk_branch=scenario,france_A12=pu['france_A12'],baseline_UK_A12=uk_a,
        tonnage_ratio_FR_over_UK=pu['tonnage_ratio_FR_over_UK'],
        effectiveness_ratio_FR_over_UK=round(pu['france_A12']*F_T['base']*pu['fr_skill_factor_ASSUMED']/(uk_a*U_T['base']*q),4),
        warning='cross-policy stress; French P unchanged but UK choice endogenous to threat'))

def savecsv(name,data):
    with (P/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
savecsv('P4_annual.csv',rows)
savecsv('P4_four_snapshots.csv',snaps)
# heterogenous fields in stress
keys=list(dict.fromkeys(k for r in stress for k in r))
with (P/'P4_sensitivity.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(stress)
# Validation independent identity checks from rounded output (tolerance <= .0001)
for r in rows:
    y=r['year']; b=r['bound']; s=r['branch']; UKs='W' if y==1815 else s
    assert abs(r['tonnage_ratio_FR_over_UK']-r['france_line_displacement_tonnes_ASSUMED']/r['britain_line_displacement_tonnes_ASSUMED'])<=.000051
    assert abs(r['effectiveness_ratio_FR_over_UK']-r['france_effective_A12_tonnes_ASSUMED']/r['britain_effective_A12_tonnes_ASSUMED'])<=.000051
    if y>1815:
        p=next(t for t in rows if t['year']==y-1 and t['bound']==b and t['branch']==s)
        assert abs(r['france_line_hulls']-p['france_line_hulls']-r['france_line_launches']+r['france_line_natural_exit']+r['france_line_war_loss'])<.002
        assert abs(r['britain_line_hulls']-p['britain_line_hulls']-r['britain_line_launches']+r['britain_line_exit_implied'])<.002
        assert abs(r['france_frst']-p['france_frst']-r['france_fr_launches']+r['france_fr_exit'])<.002
        assert abs(r['france_smst']-p['france_smst']-r['france_sm_launches']+r['france_sm_exit'])<.002
        assert abs(r['britain_frst']-p['britain_frst']-r['britain_fr_launches']+r['britain_fr_exit_implied'])<.002
        assert abs(r['britain_smst']-p['britain_smst']-r['britain_sm_launches']+r['britain_sm_exit_implied'])<.002
print('annual rows',len(rows),'snapshots',len(snaps),'stress',len(stress),'all identity checks pass')
for s in ('W','P'):
 for y in yrs:
  r=next(r for r in rows if r['year']==y and r['branch']==s and r['bound']=='base')
  print(s,y,'H',r['france_line_hulls'],r['britain_line_hulls'],
    'A12',r['france_A12'],r['britain_A12'],
    'T',r['tonnage_ratio_FR_over_UK'],'E',r['effectiveness_ratio_FR_over_UK'])
