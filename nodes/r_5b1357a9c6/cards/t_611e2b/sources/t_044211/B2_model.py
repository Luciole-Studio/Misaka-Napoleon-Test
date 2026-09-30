"""B2 conditional fiscal arithmetic, not estimated history or fitted probabilities.
GBP million current-account arithmetic; no GDP forecast. Par debt and cash differ.
Inherited coupons fixed; new loans issued as 3% perpetuities at price c/y.
N_t = G_t + I_(t-1) - T_t. B_t = B_(t-1) + N_t*y/c.
I_t = I_(t-1) + y*N_t. New coupons first paid next year.
A cash surplus buys stock at the same price. Debt includes baseline annuity PV;
old annuity expiry is not simulated (conservative). No monetization revenue,
redemption fund fiction, tax base elasticity or automatic sovereign default.
After a stress probe is crossed, numbers are no-policy-change counterfactuals,
NOT financeable forecasts. Thresholds are diagnostic, not historical laws.
"""
from pathlib import Path
import csv,json,itertools
P=Path(__file__).resolve().parent
history={int(r['year']):r for r in csv.DictReader((P/'B2_series.csv').open())}
def scenario(name,start,R,G,y,g=0,cap=None,interest_adjust=0,transition_years=0):
 return dict(name=name,start=start,R=R,G=G,y=y,g=g,surplus_cap=cap,coupon=.03,interest_adjust=interest_adjust,transition_years=transition_years)
scenarios=[
 scenario('S1_early_peace_1805',1805,48,24,.0425,.0125,2),
 scenario('S2_armed_coexistence_disciplined',1810,66,42,.05,.01,1.5),
 scenario('S2_armed_coexistence_costly',1810,64,43,.055,.01,1),
 scenario('S3_adaptive_blockade',1810,60,39,.055,.005,1),
 scenario('S3_stubborn_lower_stress',1810,60,48,.06,0),
 scenario('S3_stubborn_upper_stress',1810,55,50,.07,0),
 scenario('no_allies_no_spending_cut',1810,66,57,.055,.01),
 scenario('S3_cumulative_catastrophe',1810,50,55,.08,0)]
for R,G,y,ia in itertools.product([55,60],[48,50],[.06,.07],[-2,0,2]):
 scenarios.append(scenario(f'grid_R{R}_G{G}_y{y}_Iadjust{ia}',1810,R,G,y,interest_adjust=ia))
# A bounded transition sensitivity, not a calibrated demobilization estimate:
# first model year retains the historical primary-spending scale; over 1 or 2
# further annual steps its excess over target G is removed. Historical arrears
# are not added again; unobserved new compensation/credit losses remain excluded.
for base in scenarios[:4]:
 for lag in [1,2]:
  scenarios.append(dict(base,name=f"{base['name']}_transition{lag}",transition_years=lag))
rows=[];summary=[]
for s in scenarios:
 h=history[s['start']];B=float(h['debt_total_calendar_gbp_m']);I=float(h['interest_gbp_m'])+s['interest_adjust']
 historical_G=float(h['primary_expenditure_gbp_m'])
 first60=first70=first30=None;points={}
 for year in range(s['start']+1,1849):
  n=year-s['start']-1;R=s['R']*(1+s['g'])**n;G=s['G']*(1+s['g'])**n
  transition_extra=(historical_G-s['G'])*max(0,1-n/s['transition_years'])*(1+s['g'])**n if s['transition_years'] else 0
  G+=transition_extra
  N=G+I-R
  tax_cut=0
  if s['surplus_cap'] is not None and N < -s['surplus_cap']:
   tax_cut=-N-s['surplus_cap'];R-=tax_cut;N=-s['surplus_cap']
  share=I/R*100
  if share>=60 and first60 is None:first60=year
  if share>=70 and first70 is None:first70=year
  if N>=30 and first30 is None:first30=year
  dB=N*s['y']/s['coupon'];Bnew=B+dB;Inew=I+s['y']*N
  assert abs((R+N)-(G+I))<1e-8
  assert abs((Bnew-B)-N-(dB-N))<1e-8
  assert abs((Inew-I)-s['coupon']*dB)<1e-8
  row=dict(scenario=s['name'],year=year,revenue=R,primary_spending=G,interest_paid=I,cash_deficit=N,new_issue_running_cost_pct=100*s['y'],assumed_new_coupon_pct=100*s['coupon'],nominal_face_increase=dB,issue_discount_adjustment=dB-N,end_debt_face_proxy=Bnew,next_year_interest=Inew,interest_revenue_pct=share,automatic_tax_cut=tax_cut,transition_extra_primary_spending=transition_extra,stress60_year=first60,stress70_year=first70,financing30_year=first30,label='MODEL_NOT_OBSERVATION')
  rows.append(row);B=Bnew;I=Inew
  if year in [1815,1820,1830,1840,1848]:points[year]=[round(B,1),round(I,1),round(share,1),round(N,1)]
 summary.append(dict(**s,first_interest_share_60=first60,first_interest_share_70=first70,first_cash_deficit_30=first30,checkpoints_debt_nextinterest_share_deficit=points))
with (P/'B2_model_paths.csv').open('w',newline='') as out:
 cw=csv.DictWriter(out,fieldnames=list(rows[0]));cw.writeheader();cw.writerows(rows)
(P/'B2_model_assumptions.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
for r in summary[:8]:print(r)
grid=[x for x in summary if x['name'].startswith('grid_')]
grid_base=[x for x in grid if x['interest_adjust']==0]
print('Base grid crossing 60:',min(x['first_interest_share_60'] for x in grid_base),max(x['first_interest_share_60'] for x in grid_base))
print('Base grid crossing 70:',min(x['first_interest_share_70'] for x in grid_base),max(x['first_interest_share_70'] for x in grid_base))
print('Widened grid crossing 60:',min(x['first_interest_share_60'] for x in grid),max(x['first_interest_share_60'] for x in grid))
print('Widened grid crossing 70:',min(x['first_interest_share_70'] for x in grid),max(x['first_interest_share_70'] for x in grid))
for r in summary:
 if r['transition_years']:print('TRANSITION',r)
