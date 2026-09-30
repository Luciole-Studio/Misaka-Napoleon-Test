# D2 笔记09：本章算术（假设算术，非观测）

```
== 1. Abolition of Prussia: task buckets (persons) ==
rump_control(S2/S5) 15,000–30,000
low_friction_initial3y 25,000–45,000
medium_friction_initial3y 45,000–75,000
high_friction_initial3y 80,000–120,000
cooperative_settled_5_15y 20,000–30,000

== increments over rump control (low=scen_low-rump_high, high=scen_high-rump_low; floor 0) ==
low_friction_initial3y 0–30,000
medium_friction_initial3y 15,000–60,000
high_friction_initial3y 50,000–105,000
cooperative_settled_5_15y 0–15,000

== annual cost at 600-900 francs per soldier-year (million francs) ==
rump_control(S2/S5) 9.0–27.0
low_friction_initial3y 15.0–40.5
medium_friction_initial3y 27.0–67.5
high_friction_initial3y 48.0–108.0
cooperative_settled_5_15y 12.0–27.0
incr low_friction_initial3y 0.0–27.0
incr medium_friction_initial3y 9.0–54.0
incr high_friction_initial3y 30.0–94.5
incr cooperative_settled_5_15y 0.0–13.5

== old P6 parameter error check ==
old: lo+=6.0, hi+=12.0 (thousand) -> 6,000-12,000 persons
if only parameter corrected to 60: lo+=60, hi+=120 -> 60,000-120,000
card intended medium friction total: 45,000-75,000; increment over rump: 15,000-60,000

== 2. Population arithmetic ==
Austria A-route 1848 (22-23m base, 0.5-1.0%, 40y): 2,686–3,424 万
Austria B-route 1810 rough: 1,850–1,950 万; 1848 x1.21-1.46: 2,238–2,847 万
Prussia rump 1848: 619–806 万
Prussia complete (no Jena) 1848: 1,311–1,788 万
ratio Austria A / Prussia rump 1848: 3.3–5.5
ratio Austria B / Prussia rump 1848: 2.8–4.6
ratio Austria A / Prussia complete 1848: 1.5–2.6
ratio Austria 1808 / Prussia rump 1808: 4.4–5.1
HGIS growth 1818-1852: 1.569 annual 1.3328%

== 3. Army ratios ==
Austria standing 1835-48 16-23万 vs Prussia rump 5.6-9.7万 ratio: 1.6–4.1
Austria standing 1815-30 14-20万 vs Prussia rump 1820s 4-6万 ratio: 2.3–5.0
Austria vs complete unreformed Prussia 8-12万 (orig report): 1.3–2.9 ; vs 12-18万 (P7): 0.89–1.9

== 4. Austria 1809 military/revenue, 1805 ==
1809 mil/rev: 2.148 1805 mil/rev 0.830 1803 0.472 1808 0.676
Revenue decline 1804->1810: 0.679

== 5. Prussia indemnity pacing ==
140m francs: half cash at 6m/month -> 11.666666666666666 months; 120m after Erfurt
Prussian 1820 debt 217.2m = 4.25 years revenue -> revenue approx 51.1 m thaler
1806 military/revenue 16-17/27: 0.59–0.63
```

脚本：scratchpad/d2_calc.py（内容照录如下）
```python
# D2 chapter 5 arithmetic (assumption arithmetic, not observation)
def rng(a,b): return f"{a:,.0f}–{b:,.0f}"
print("== 1. Abolition of Prussia: task buckets (persons) ==")
buckets = {
 'rump_control(S2/S5)': ((10000,10000),(0,0),(5000,20000)),
 'low_friction_initial3y': ((10000,15000),(5000,10000),(10000,20000)),
 'medium_friction_initial3y': ((15000,20000),(10000,15000),(20000,40000)),
 'high_friction_initial3y': ((20000,25000),(15000,25000),(45000,70000)),
 'cooperative_settled_5_15y': ((10000,10000),(0,5000),(10000,15000)),
}
tot={}
for k,(f,n,m) in buckets.items():
    lo=f[0]+n[0]+m[0]; hi=f[1]+n[1]+m[1]; tot[k]=(lo,hi)
    print(k, rng(lo,hi))
rl,rh=tot['rump_control(S2/S5)']
print("\n== increments over rump control (low=scen_low-rump_high, high=scen_high-rump_low; floor 0) ==")
for k in ['low_friction_initial3y','medium_friction_initial3y','high_friction_initial3y','cooperative_settled_5_15y']:
    lo=max(0,tot[k][0]-rh); hi=tot[k][1]-rl
    print(k, rng(lo,hi))
print("\n== annual cost at 600-900 francs per soldier-year (million francs) ==")
for k,(lo,hi) in tot.items():
    print(k, f"{lo*600/1e6:.1f}–{hi*900/1e6:.1f}")
for k in ['low_friction_initial3y','medium_friction_initial3y','high_friction_initial3y','cooperative_settled_5_15y']:
    lo=max(0,tot[k][0]-rh); hi=tot[k][1]-rl
    print('incr',k, f"{lo*600/1e6:.1f}–{hi*900/1e6:.1f}")
print("\n== old P6 parameter error check ==")
print("old: lo+=6.0, hi+=12.0 (thousand) -> 6,000-12,000 persons")
print("if only parameter corrected to 60: lo+=60, hi+=120 -> 60,000-120,000")
print("card intended medium friction total: 45,000-75,000; increment over rump: 15,000-60,000")
print("\n== 2. Population arithmetic ==")
def grow(b0,b1,g0,g1,y): return b0*(1+g0)**y, b1*(1+g1)**y
# Austria Track A (no 1809 cession): 1808 contemporary estimate 22-23m, 40 yrs 0.5-1.0%
a=grow(22e6,23e6,0.005,0.010,40); print("Austria A-route 1848 (22-23m base, 0.5-1.0%, 40y):", rng(a[0]/1e4,a[1]/1e4),"万")
# Austria B-route: 22-23m minus 3.5m (rough, mixed sources) -> 18.5-19.5m in 1810; index 121-146 by 1848
b0,b1=22e6-3.5e6,23e6-3.5e6
print("Austria B-route 1810 rough:", rng(b0/1e4,b1/1e4),"万; 1848 x1.21-1.46:", rng(b0*1.21/1e4,b1*1.46/1e4),"万")
p=grow(4.5e6,5.0e6,0.008,0.012,40); print("Prussia rump 1848:", rng(p[0]/1e4,p[1]/1e4),"万")
pB=grow(9.0e6,10.7e6,0.009,0.0123,42); print("Prussia complete (no Jena) 1848:", rng(pB[0]/1e4,pB[1]/1e4),"万")
print("ratio Austria A / Prussia rump 1848:", f"{a[0]/p[1]:.1f}–{a[1]/p[0]:.1f}")
print("ratio Austria B / Prussia rump 1848:", f"{b0*1.21/p[1]:.1f}–{b1*1.46/p[0]:.1f}")
print("ratio Austria A / Prussia complete 1848:", f"{a[0]/pB[1]:.1f}–{a[1]/pB[0]:.1f}")
print("ratio Austria 1808 / Prussia rump 1808:", f"{22/5:.1f}–{23/4.5:.1f}")
# HGIS historical Prussia 1818 10,796,874 -> 1852 16,935,420
print("HGIS growth 1818-1852:", f"{16935420/10796874:.3f}", "annual", f"{(16935420/10796874)**(1/34)-1:.4%}")
print("\n== 3. Army ratios ==")
print("Austria standing 1835-48 16-23万 vs Prussia rump 5.6-9.7万 ratio:", f"{16/9.7:.1f}–{23/5.6:.1f}")
print("Austria standing 1815-30 14-20万 vs Prussia rump 1820s 4-6万 ratio:", f"{14/6:.1f}–{20/4:.1f}")
print("Austria vs complete unreformed Prussia 8-12万 (orig report):", f"{16/12:.1f}–{23/8:.1f}", "; vs 12-18万 (P7):", f"{16/18:.2f}–{23/12:.1f}")
print("\n== 4. Austria 1809 military/revenue, 1805 ==")
print("1809 mil/rev:", f"{66.8/31.1:.3f}", "1805 mil/rev", f"{64.8/78.1:.3f}", "1803", f"{35.9/76.1:.3f}", "1808", f"{45.2/66.9:.3f}")
print("Revenue decline 1804->1810:", f"{(78.0-25.0)/78.0:.3f}")
print("\n== 5. Prussia indemnity pacing ==")
print("140m francs: half cash at 6m/month ->", 70/6, "months; 120m after Erfurt")
print("Prussian 1820 debt 217.2m = 4.25 years revenue -> revenue approx", f"{217.2/4.25:.1f}", "m thaler")
print("1806 military/revenue 16-17/27:", f"{16/27:.2f}–{17/27:.2f}")
```
