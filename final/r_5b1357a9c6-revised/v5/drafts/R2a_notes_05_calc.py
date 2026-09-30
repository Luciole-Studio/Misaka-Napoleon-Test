"""R2a 条件算例：三条轨道下英国财政路径（1811—1848）与工业相对规模。

性质：条件会计算术，沿用研究卡B2（nodes/r_5b1357a9c6/cards/t_044211/B2_model.py）的方程，
不是历史估计，也不是预测。金额为百万名义英镑。起点取B2_series.csv的1810年
（债务面额代理值688.47、当年利息24.4）。

方程（与B2相同）：
  N_t = G_t + I_{t-1} - R_t          当年现金缺口（负为盈余）
  D_t = D_{t-1} + N_t * y / 0.03     新债按3%永续券面额计
  I_t = I_{t-1} + y * N_t            新增票息次年起付
  盈余超过cap时视为减税（R下调），与B2的surplus_cap相同。

各轨道的G（非息支出）与R（收入）按时段给出低、高两档，理由写在PATHS的注释里。
运行：python3 R2a_notes_05_calc.py  → 输出同目录 R2a_notes_05_calc_output.csv
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
D0, I0 = 688.4651446811936, 24.4   # B2_series.csv 1810行
COUPON = 0.03

def seg(years, G, R):
    return [(y, G, R) for y in years]

# 每条路径：name, y(新借成本), cap(盈余上限), g(和平期年增长), 分段(年, G, R)
# G、R为该年水平；和平期从指定年起按g复合增长（G与R同率）。
PATHS = []

def build(name, y, cap, g, war, peace_start, G_peace, R_peace, y_peace=None):
    rows = [(yr, G, R, y) for yr, G, R in war]
    yp = y if y_peace is None else y_peace
    for yr in range(peace_start, 1849):
        n = yr - peace_start
        rows.append((yr, G_peace * (1 + g) ** n, R_peace * (1 + g) ** n, yp))
    PATHS.append(dict(name=name, y=y, cap=cap, rows=rows))

# ---------- 甲　最可能（1807年后不入伊比利亚；1812—13海上停战，1814全面和约） ----------
# 1811—13：史实非息支出减去半岛相关净支出5—10（Sherwig p.255：1811年半岛战费近1,100万镑；
# 葡萄牙补贴约200万、西班牙60万—100万），另无1813年大陆补贴；收入与史实接近。
# 1814—15过渡；1816起武装和平包38—45、收入67—69，均按年增1%（与B2的S2_armed_coexistence两档同口径：
# B2以1811年R64—66、G42—43起按1%增长，推到1816年约为R67—69、G44—45）。
build('甲_低成本', 0.050, 1.5, 0.010,
      seg([1811], 52.7, 71.0) + seg([1812], 52.0, 70.5) + seg([1813], 50.0, 72.0) +
      seg([1814], 46.0, 70.0) + seg([1815], 42.0, 66.0),
      1816, 38.0, 69.0)
build('甲_高成本', 0.055, 1.0, 0.010,
      seg([1811], 57.7, 70.5) + seg([1812], 58.0, 70.0) + seg([1813], 56.0, 71.0) +
      seg([1814], 52.0, 69.0) + seg([1815], 47.0, 66.0),
      1816, 45.0, 67.0)

# ---------- 昙花一现（1803—11史实；1812法俄妥协；英法战争延续至1821—25崩解） ----------
# 1811—12史实；1813—14拿破仑主力转向半岛、英美战争至1814年底：非息支出72—80
# （史实1813—14为83.8、82.9，内含750万—1,000万大陆补贴，此处扣除，另加半岛增量0—5）。
# 1815—21低强度续战55—62；1816—17饥荒收入下调；1822—24联军与登陆62—72；1825起和平；
# 和平后保留部分战时税（收入64—68，而非史实废所得税后的约58），债务转换使新借成本降至4.5%。
war_flash_low = (seg([1811], 62.7, 71.0) + seg([1812], 68.4, 70.3) + seg([1813], 72.0, 74.0) +
                 seg([1814], 72.0, 76.0) + seg(range(1815, 1816), 60.0, 74.0) +
                 seg(range(1816, 1818), 55.0, 69.0) + seg(range(1818, 1822), 55.0, 71.0) +
                 seg(range(1822, 1825), 62.0, 71.0) + seg([1825], 42.0, 64.0))
war_flash_high = (seg([1811], 62.7, 71.0) + seg([1812], 68.4, 70.3) + seg([1813], 80.0, 73.0) +
                  seg([1814], 80.0, 75.0) + seg(range(1815, 1816), 65.0, 72.0) +
                  seg(range(1816, 1818), 62.0, 66.0) + seg(range(1818, 1822), 60.0, 69.0) +
                  seg(range(1822, 1825), 72.0, 70.0) + seg([1825], 48.0, 62.0))
build('昙花一现_低成本', 0.055, 1.5, 0.010, war_flash_low, 1826, 28.0, 68.0, y_peace=0.045)
build('昙花一现_高成本', 0.060, 1.0, 0.005, war_flash_high, 1826, 34.0, 64.0, y_peace=0.045)

# ---------- 强行成功（乙：1810关税改造、不并荷汉；1812—13停战，1813—14和约） ----------
build('乙_低成本', 0.050, 1.5, 0.010,
      seg([1811], 50.0, 72.0) + seg([1812], 50.0, 72.0) + seg([1813], 46.0, 70.0) +
      seg([1814], 42.0, 68.0), 1815, 38.0, 68.5)
build('乙_高成本', 0.055, 1.0, 0.010,
      seg([1811], 55.0, 71.0) + seg([1812], 55.0, 71.0) + seg([1813], 50.0, 69.0) +
      seg([1814], 46.0, 67.0), 1815, 44.5, 66.5)
# 丙：同乙，但法国直辖安特卫普—易北海岸，英国维持更高海军戒备（非息支出+4）
build('丙_高戒备', 0.055, 1.0, 0.010,
      seg([1811], 55.0, 71.0) + seg([1812], 56.0, 70.0) + seg([1813], 52.0, 69.0) +
      seg([1814], 49.0, 67.0), 1815, 48.5, 66.5)

def run(p):
    D, I = D0, I0
    out = []
    for yr, G, R, yy in p['rows']:
        N = G + I - R
        cut = 0.0
        if N < -p['cap']:
            cut = -N - p['cap']; R -= cut; N = -p['cap']
        share = I / R * 100
        dD = N * yy / COUPON
        D, I_next = D + dD, I + yy * N
        out.append(dict(path=p['name'], year=yr, revenue=round(R, 2), primary=round(G, 2),
                        interest=round(I, 2), deficit=round(N, 2), debt_face_proxy=round(D, 1),
                        interest_revenue_pct=round(share, 1), tax_cut=round(cut, 2),
                        label='CONDITIONAL_ARITHMETIC_NOT_FORECAST'))
        I = I_next
    return out

rows = []
for p in PATHS:
    rows += run(p)
with (HERE / 'R2a_notes_05_calc_output.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

for p in PATHS:
    pts = {r['year']: r for r in rows if r['path'] == p['name']}
    s = ' | '.join(f"{y}: 债{pts[y]['debt_face_proxy']} 息/收{pts[y]['interest_revenue_pct']}%"
                   for y in (1815, 1820, 1825, 1830, 1848))
    print(p['name'], '|', s)

# ---------- 工业相对规模（B5卡B5_growth_paths.csv的参数） ----------
# 昙花一现：1815起用S3楔子（-1.1至-0.4个百分点/年），到1822年止，此后楔子归零；
# 另给一个"战后追赶"上沿（1823—48年+0.2个百分点/年，取自B5的S5高档楔子）。
import math
for lo_hi, start, wedge in (('低', 0.78, -0.011), ('高', 0.90, -0.004)):
    rel_1822 = start * math.exp(wedge * 7)
    catch = rel_1822 * math.exp(0.002 * 26)
    print(f'昙花一现工业相对史实（{lo_hi}）：1822={rel_1822:.3f}，1848无追赶={rel_1822:.3f}，1848有追赶={catch:.3f}')
