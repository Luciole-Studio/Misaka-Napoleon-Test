"""Deterministic submission checks; not historical-causal validation or red-team approval."""
from pathlib import Path
from collections import defaultdict
import csv, json, re, hashlib
P=Path(__file__).resolve().parent
ROOT=P.parents[3]
log=[]
def record(s):
    log.append(s);print(s)
h={int(r['year']):r for r in csv.DictReader((P/'B2_series.csv').open())}
assert sorted(h)==list(range(1793,1849))
for r in h.values():
    R,E,I=map(float,[r['revenue_gbp_m'],r['expenditure_gbp_m'],r['interest_gbp_m']])
    assert abs(E-R-float(r['cash_deficit_gbp_m']))<1e-8
    assert abs(R-E+I-float(r['primary_surplus_gbp_m']))<1e-8
    assert abs(100*I/R-float(r['interest_revenue_pct']))<1e-8
record('Annual: 56 unique years, fiscal identities and interest ratios PASS')
monthly=list(csv.DictReader((P/'B2_consol_monthly_1809_1812.csv').open()))
assert len(monthly)==48 and len({(r['year'],r['month']) for r in monthly})==48
record('Monthly: 48 unique observations PASS; no claim of causal identification')
summary=json.loads((P/'B2_model_assumptions.json').read_text())
paths=defaultdict(list)
for r in csv.DictReader((P/'B2_model_paths.csv').open()):paths[r['scenario']].append(r)
assert len(summary)==40 and len(paths)==40
for s in summary:
    rs=paths[s['name']]
    assert [int(r['year']) for r in rs]==list(range(s['start']+1,1849))
    B=float(h[s['start']]['debt_total_calendar_gbp_m'])
    I=float(h[s['start']]['interest_gbp_m'])+s['interest_adjust']
    for r in rs:
        R,G,N,dB,B1,I1=map(float,[r['revenue'],r['primary_spending'],r['cash_deficit'],r['nominal_face_increase'],r['end_debt_face_proxy'],r['next_year_interest']])
        assert abs(float(r['interest_paid'])-I)<1e-7
        assert abs(R+N-G-I)<1e-7
        assert abs(B1-B-dB)<1e-7
        assert abs(dB-N-float(r['issue_discount_adjustment']))<1e-7
        assert abs(I1-I-.03*dB)<1e-7
        assert abs(float(r['interest_revenue_pct'])-I/R*100)<1e-7
        B,I=B1,I1
    for field,threshold,key in [('interest_revenue_pct',60,'first_interest_share_60'),('interest_revenue_pct',70,'first_interest_share_70'),('cash_deficit',30,'first_cash_deficit_30')]:
        crossing=next((int(r['year']) for r in rs if float(r[field])>=threshold),None)
        assert crossing==s[key]
    for year,vals in s['checkpoints_debt_nextinterest_share_deficit'].items():
        r=next(r for r in rs if int(r['year'])==int(year))
        expected=[round(float(r[k]),1) for k in ['end_debt_face_proxy','next_year_interest','interest_revenue_pct','cash_deficit']]
        assert vals==expected
record('Model: 40 paths; cash, face, coupon timing, thresholds, JSON checkpoints PASS')
report=(P/'B2_britain_fiscal.md').read_text()
policy=report.split('## ⑬')[1].split('## ⑭')[0]
timeline=report.split('## ⑭')[1].split('## ⑮')[0]
assert len(re.findall(r'^\|B[1-8]',policy,re.M))==8
assert len(re.findall(r'^\|18\d',timeline,re.M))==32
record('Template: 8 policy rows and 32 timeline rows PASS')
# Literal excerpts only: exact occurrence is not proof of historical interpretation.
checks=[
('Q1','bff7e2ccf088.md','subject to the approbation of parliament'),
('Q2','bff7e2ccf088.md','Last year the interest was 4l. 4s. 2d. per cent.; this year it was 4l. 14s. 11d.'),
('Q3a','bff7e2ccf088.md','For each hundred pounds subscribed'),
('Q3b','bff7e2ccf088.md','100l. in the 3 per cents, reduced, 20l. in the consols, 20l. in the 4 per cents, and 6s. 11d. in the long annuities.'),
('Q4','bff7e2ccf088.md','4,864,267l. had been received'),
('Q5','156d03703582.md','that expense now incurred for our armies would cease, and the supplies at present demanded for them could be applied to the service of our navy'),
('Q6','156d03703582.md','the numbers of persons returning from long voyages and claiming the arrears due to them, had made larger disbursements necessary'),
('Q7','3b8b8e348c6d.md','to grant relief to the extent of six millions, not with the supposition that that sum would be required'),
('Q8','3b8b8e348c6d.md','The Bank of England had now to complain, not that they had no funds with which to discount, but of a deficiency of good paper to discount.'),
('Q9','995bd30de2bb.md','should the state of Europe continue to require it'),
('Q10','1170b6cb87a9.md','if it was to be done at all, it must be done with the consent of parliament'),
('Q11','523f4560156c.md','cannot safely be removed at an earlier period than two years'),
('Q12a','de17c8036944.md','Ayes 75—Noes 151'),
('Q12b','de17c8036944.md','Ayes 45, Noes 180'),
('Q13','2f4fc6ec5d53.md','not to enable Houses who have failed to compromise or settle with their creditors'),
('Q14','523f4560156c.md','£.3.17.10½. per ounce of standard fineness')]
fail=[]
for name,file,quote in checks:
    text=(ROOT/'downloads/pages'/file).read_text()
    normalized=' '.join(text.split())
    ok=quote in normalized
    record(name+' literal '+('PASS' if ok else 'CHECK')+' '+file)
    if not ok:fail.append(name)
record('Quote checks needing manual resolution: '+str(fail))
for file,expected in [
('B2_BoE_millennium_v31.xlsx','4c23dd392a498691eac92659aec283fb43f28118bd80511dc87fc595974195eb'),
('B2_BoE_balance_sheet.xlsx','86121aeb2c91bcf8f6b277f1c80b1d6ffb7b5947b353d9a8b467dd435dc50589'),
('B2_Bordo_White_WP3517.pdf','ed2c1913a953d70e4ac436da4aea5a895a7c80fc0aaa0d714d12b086920d2800')]:
    assert hashlib.sha256((ROOT/'downloads'/file).read_bytes()).hexdigest()==expected
record('Retained originals: three SHA256s PASS')
record('Limits: selected source passages read, not all originals independently audited; quotes checked after whitespace normalization; no visual/layout certification of Markdown required.')
(P/'B2_validation.txt').write_text('\n'.join(log)+'\n')
