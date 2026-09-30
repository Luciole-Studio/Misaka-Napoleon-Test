#!/usr/bin/env python3
"""M1 reproducible monthly transcriptions, broad windows, placebo, state-gap sensitivity.

Run from project root: python3 nodes/r_5b1357a9c6/cards/t_0a8308/build_m1.py
Only openpyxl required. No daily quotes or outcome probabilities are imputed.
"""
from __future__ import annotations
import csv
import calendar
from collections import defaultdict
from pathlib import Path
from statistics import median
import openpyxl

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
UK = ROOT / 'downloads/B2_BoE_millennium_v31.xlsx'
FR = ROOT / 'downloads/M1_tauxFrance1800_2015.xlsx'

# Event month is an approximation, NOT necessarily first observation after news.
# 'Antipa' news dates are reported by Antipa (2016), pp. 1069-71;
# other dates require independent transmission verification and are marked unverified.
EVENTS = [
 ('war_resumption','1803-05','1803-05-17','not_verified','war resumption; May event month'),
 ('invasion_scare','1803-08', '', 'not_verified','invasion scare; month chosen as descriptive, no isolated news date'),
 ('trafalgar','1805-11','1805-11-06','Antipa_2016_p1071','21 October naval battle; London news 6 November'),
 ('austerlitz','1805-12','','not_verified','December battle; London market arrival not verified; window overlaps Trafalgar'),
 ('tilsit','1807-07','', 'not_verified','Treaty of Tilsit, July; London arrival not established'),
 ('erfurt','1808-10','', 'not_verified','Erfurt meeting, autumn; London arrival not established'),
 ('wagram','1809-07','', 'not_verified','July campaign; London arrival not established'),
 ('commercial_crisis','1810-11','', 'not_verified','1810-11 crisis is a long episode; November arbitrary pivot'),
 ('gebora_badajoz','1811-03','1811-03-12','Antipa_2016_p1064','London Times Badajoz fall announcement 12 March; drawn from Antipa'),
 ('america_war','1812-08','', 'Antipa_2016_p1065','American war continuation reached London late August; exact day not pinned'),
 ('russian_invasion','1812-06','','not_verified','French entry into Russia; London market arrival not verified'),
 ('russia_retreat','1812-12','', 'not_verified','winter retreat news arrival not established'),
 ('leipzig','1813-10','', 'not_verified','battle month; London arrival not established'),
 ('paris_abdication','1814-04','', 'not_verified','Paris capitulation/abdication composite, arrival not established'),
 ('paris_treaty','1814-06','1814-06-02','Antipa_2016_p1065','London Gazette treaty 2 June, ratification 18 June'),
 ('elba_return','1815-03','','not_verified','Napoleon re-entry, March; first London news date not verified'),
 ('waterloo','1815-06','', 'not_verified','battle 18 June; London news to be independently pinned'),
]

def dump(name, rows, header):
    with (OUT / name).open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header, extrasaction='ignore')
        writer.writeheader(); writer.writerows(rows)

def ym(year, month): return f'{year:04d}-{month:02d}'
def ym_shift(x, n):
    y,m=map(int,x.split('-')); t=y*12+m-1+n
    return ym(t//12,(t%12)+1)

def load_uk():
    w = openpyxl.load_workbook(UK, data_only=True, read_only=True)
    s = w['M10. Mthly long-term rates']
    assert s['C4'].value == 'Yield on 3% consols 1753-1823'
    assert s['C5'].value == 'Neal (1990)'
    assert s['C6'].value == 'End month data'
    months={v.lower():i for i,v in enumerate(calendar.month_abbr) if v}
    out={}
    for r, (year,month,yield_pct) in enumerate(s.iter_rows(min_row=7,max_col=3,values_only=True),7):
        if not isinstance(year,int) or not (1802<=year<=1815): continue
        if isinstance(yield_pct,(float,int)):
            out[ym(year, months[str(month).strip().lower()])] = (yield_pct,r)
    w.close()
    return out

def load_fr():
    w=openpyxl.load_workbook(FR, data_only=True, read_only=True)
    s=w['mensuel']
    assert s['C2'].value == 'TXLONG (long-term interest rates)'
    out={}
    for r,(month,_,rate) in enumerate(s.iter_rows(min_row=3,max_col=3,values_only=True),3):
        if not isinstance(month,str) or not month.startswith(('1802M','1803M','1804M','1805M','1806M','1807M','1808M','1809M','1810M','1811M','1812M','1813M','1814M','1815M')): continue
        if rate is not None:
            try: y=float(rate)
            except (ValueError,TypeError): continue
            out[month.replace('M','-')] = (y,r)
    w.close(); return out

def main():
    uk=load_uk(); fr=load_fr()
    assert len(uk)==len(fr)==168, (len(uk),len(fr))
    assert abs(uk['1803-05'][0]-5)<1e-10
    assert abs(fr['1803-05'][0]-9.53418737367533)<1e-10
    values={'UK_consol_3pct':uk,'FR_rente_5pct':fr}
    sources={'UK_consol_3pct':('downloads/B2_BoE_millennium_v31.xlsx','M10. Mthly long-term rates','Neal (1990); BoE v3.1','end_month'),
            'FR_rente_5pct':('downloads/M1_tauxFrance1800_2015.xlsx','mensuel','Vaslin/Courtois/Le Bris via Levy-Garboua and Monnet (2016)','month_unspecified_aggregation')}
    series=[]
    for key,dat in values.items():
        file,sheet,reference,frequency=sources[key]
        coupon=3 if key.startswith('UK') else 5
        for month,(y,r) in sorted(dat.items()):
            series.append(dict(month=month,market=key,yield_pct=f'{y:.10f}',price_per_100_proxy=f'{100*coupon/y:.10f}',
                               coupon_per_100=coupon,source_file=file,source_sheet=sheet,source_cell=f'C{r}',
                               source_lineage=reference,aggregation=frequency,
                               price_note='perpetuity coupon/yield; not original quoted price; ignores accrued coupon'))
    dump('M1_series.csv',series,list(series[0]))
    events=[]; sensitivity=[]
    # Common broader window: previous month -> month after event; disaggregated adjacent-month legs.
    # The monthly quote cannot generally isolate news-day or causality.
    for eid,em,news,status,description in EVENTS:
        for key,dat in values.items():
            cup=3 if key.startswith('UK') else 5
            for a,b,label in [(-1,0,'month_before_to_event'),(0,1,'event_to_month_after'),(-1,1,'bracketing_two_months'),(-2,2,'bracketing_four_months')]:
                m0=ym_shift(em,a); m1=ym_shift(em,b)
                y0,y1=dat[m0][0],dat[m1][0]
                p0,p1=100*cup/y0,100*cup/y1
                dy=100*(y1-y0)
                ret=100*(p1/p0-1)
                row=dict(event_id=eid,event_month=em,news_date_london=news,news_status=status,
                         description=description,market=key,window=label,start_month=m0,end_month=m1,
                         start_yield_pct=f'{y0:.8f}',end_yield_pct=f'{y1:.8f}',yield_change_bp=f'{dy:.4f}',
                         start_price_proxy=f'{p0:.8f}',end_price_proxy=f'{p1:.8f}',price_proxy_return_pct=f'{ret:.4f}',
                         attribution='not_identified',source_rows=f'{sources[key][1]}!C{dat[m0][1]};C{dat[m1][1]}')
                events.append(row)
                if label=='bracketing_two_months':
                    for gap in (.20,.40,.60):
                        for attributable in (.25,.50,1.0):
                            # Illustrative two-state payoff-gap model. Not a probability level, not a CI.
                            delta_pp=100*(ret/100)*attributable/gap
                            sensitivity.append(dict(event_id=eid,market=key,start_month=m0,end_month=m1,
                                proxy_price_return_pct=f'{ret:.4f}',assumed_good_bad_price_gap_pct=f'{100*gap:.0f}',
                                assumed_event_attributable_fraction=attributable,
                                implied_change_in_good_state_probability_pp=f'{delta_pp:.2f}',
                                note='scenario-only state gap; unconstrained probability change may be outside [-100,100]'))
    dump('M1_event_windows.csv',events,list(events[0]))
    dump('M1_sensitivity.csv',sensitivity,list(sensitivity[0]))
    # Placebo: empirical all-window magnitude, leave target event months +/- 1 month out
    by_market=defaultdict(dict)
    for market,dat in values.items():
        cup=3 if market.startswith('UK') else 5
        for m in sorted(dat):
            m2=ym_shift(m,2)
            if m2 in dat:
                by_market[market][m]=100*((dat[m][0]/dat[m2][0])-1)
    target={e[1] for e in EVENTS}
    control={ym_shift(e,d) for e in target for d in [-1,0,1]}
    plc=[]
    for r in events:
        if r['window']!='bracketing_two_months': continue
        market=r['market']; own_start=r['start_month']; x=abs(float(r['price_proxy_return_pct']))
        arr=[abs(v) for m,v in by_market[market].items() if m not in control and ym_shift(m,1) not in control and ym_shift(m,2) not in control]
        pct=100*sum(v<=x for v in arr)/len(arr)
        plc.append(dict(event_id=r['event_id'],market=market,absolute_proxy_return_pct=f'{x:.4f}',
                        placebo_windows=len(arr),placebo_median_absolute_return_pct=f'{median(arr):.4f}',
                        empirical_percentile_among_placebo=f'{pct:.1f}',
                        placebo_definition='all 2-month ends 1802-1815, exclude months within one of any named event; descriptive not randomization'))
    dump('M1_placebos.csv',plc,list(plc[0]))
    # Severe-assumption posterior stress, NOT an identified market probability.
    # Analyst-supplied prior 10-30% and binary bond value gap 20-60% are not sourced estimates.
    posterior=[]
    for r in sensitivity:
        for prior in (.10,.20,.30):
            shift_bad=-float(r['implied_change_in_good_state_probability_pp'])/100
            post=prior+shift_bad
            posterior.append(dict(event_id=r['event_id'],market=r['market'],
                 bad_event_name='British_defeat_stylized' if r['market'].startswith('UK') else 'French_debt_impairment_not_Napoleon_collapse',
                 assumed_prior_bad_probability=prior,
                 assumed_good_bad_price_gap_pct=r['assumed_good_bad_price_gap_pct'],
                 assumed_event_attributable_fraction=r['assumed_event_attributable_fraction'],
                 implied_posterior_bad_probability=f'{post:.6f}',
                 feasible_0_to_1='yes' if 0<=post<=1 else 'no',
                 note='binary-state stress only; unmatched war finance/inflation/credit risk; posterior not data-identified'))
    dump('M1_conditional_probability_stress.csv',posterior,list(posterior[0]))
    policy=[]
    for load in (0,.01,.02,.0315):
        for haircut in (0,.10,.20):
            recover=1-haircut
            p=(.0315-load)/recover
            policy.append(dict(contract='Napoleon_death_or_capture_1813-05-21_to_1813-06-21',
                 gross_premium_per_100=.0315,assumed_loading_fraction_of_limit=load,
                 assumed_net_claim_payout_fraction=recover,
                 implied_death_OR_capture_probability=f'{p:.6f}',
                 implied_no_death_AND_no_capture_probability=f'{1-p:.6f}',
                 note='illustrative actuary no discount; not political survival nor Lloyds maritime premium'))
    dump('M1_policy_probability_sensitivity.csv',policy,list(policy[0]))
    print('UK monthly observations',len(uk),'FR',len(fr),'series',len(series),'events',len(events),'sensitivity',len(sensitivity),'posterior_stress',len(posterior),'policy',len(policy))
    for e in events:
        if e['window']=='bracketing_two_months':
            print(e['event_id'],e['market'],e['start_month'],e['end_month'],e['yield_change_bp'],e['price_proxy_return_pct'])

if __name__=='__main__': main()
