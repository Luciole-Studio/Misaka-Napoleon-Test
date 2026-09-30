"""C17 bookkeeping generator. No probabilities estimated, no historical values interpolated.
All uncalibrated money and manpower remain NA; source keys resolve in c17_sources.md.
"""
from pathlib import Path
import csv, json
from datetime import date
P=Path(__file__).resolve().parent
# Explicit observed nodes; omitted quarters are not assertions that nothing happened.
events={
'1803Q1':('窗口前背景；不允许干预','BOUND'),
'1803Q2':('5月起允许分岔；未核双方可接受的续约套餐','C1:01'),
'1803Q3':('8月22日外锚地通信；出港流程成为承重问题','C1:02'),
'1803Q4':('12月1/12日Ganteaume意见：先掩护而非小艇独渡','C1:02'),
'1804Q3':('7月2日Rochefort集中提案；9月27/29日爱尔兰协同提案','C1:03-04'),
'1805Q1':('3月2日舰队会合命令及备选；收讫执行不全','C1:06'),
'1805Q2':('4月11日英俄签约；不能等同同步批准或联合作战','CAL:1'),
'1805Q3':('8月9日奥加入；22-26日东调各层命令；9月1日Cadiz确讯抵达','CAL:1'),
'1805Q4':('10月7日多瑙河节点；20日乌尔姆投降；12月26日普雷斯堡条约','CAL:1;C13:2'),
'1806Q3':('9月25日拿破仑离巴黎；28日到Mainz；同年英法交涉仍受多方权限限制','CAL:2;C13:3'),
'1806Q4':('10月14日Jena/Auerstedt；11月16日停战未获普王批准；21日柏林敕令','CAL:2;C1:09-10'),
'1807Q1':('2月7-8日Eylau；冬季道路妨碍迅速行动','CAL:2'),
'1807Q2':('6月14日Friedland；和谈尚跨季','CAL:2'),
'1807Q3':('7月7日法俄、9日法普提尔西特；条约不等于自动稳定均衡','CAL:2;C13:2'),
'1807Q4':('10月27日枫丹白露合作条约；不是不换朝的内心承诺','C1:12;SPAIN'),
'1808Q1':('3月23日致Murat暂缓扰宫；27日向Louis提王位为转引锚','C1:12-13;SPAIN'),
'1808Q2':('4月16日刊本条件承认Ferdinand信；诚意与日期异文需保留','SPAIN'),
'1808Q3':('9月8日法普协定正文赔款1.4亿；42,000法定兵额自次年起','C13:2'),
'1808Q4':('10月埃尔福特与英方复文：西班牙代表资格阻谈；不能在不废王情景照搬','C13:3-4;C16:3'),
'1809Q4':('奥国和约减让；法方对波兰保证与俄婚试探分别存在','C1:15-17'),
'1810Q1':('反波兰公约已签未获拿破仑批准；2月反提案义务不同','C12:4;C1:18'),
'1811Q1':('法方贸易通融指示；英议会讨论商业信用救助','C12:D4;H1811M'),
'1811Q2':('法方降军备与补偿讨论；英6月5日促和与继续信用拨款并存','C1:19;C16:2'),
'1811Q4':('Nesselrode十月备忘录：前沿安全、贸易及普鲁士与奥方担保','R1811'),
'1812Q2':('4月8日俄先撤军后谈判条件；6月23日英对美Orders撤销为史实对照','C12:4;C16:3'),
'1812Q3':('有限停线主要来自回溯记述；不作为本三线已批准备份作战案','C12:4D'),
'1812Q4':('11月英国反对派分裂发生于俄战消息语境；不倒填S2','C16:2.4'),
}
fiscal={
1803:'普通税及商业信用存在；无同口径季度国库账',
1804:'C2战税子集仅年度截至4月5日；不是英国总收入',
1805:'8月24日必要时暂停军饷保银行为表态；非实际停饷或国家破产',
1806:'C2英国战税子集；法国现金和跨战区支付缺口未量化',
1807:'C2英国战税分项/合计冲突；不以修补值填账',
1808:'C2英国战税子集及棉品官方固定价；非现金余额',
1809:'C2英国战税合计冲突；棉品出口不等于可征税回款',
1810:'特别领地贷国库4500万名义法郎结清旧预算拖欠；季度未知',
1811:'巴黎头两月122件破产；英3月议600万信用额度与5月贷款合同；均非季度现金实发总额',
1812:'英贸易松绑有条件；无可信财政破产年份',
1813:'国库现金NA；不得把史实战败财政压力直接搬入已分岔路线',
1814:'国库现金NA；征服收入减少须与军事开支减少同时核算',
1815:'国库现金NA；1816-02-01债务存量不能倒填1815季度余额',
}
def stage(k):
 if k<'1803Q2':return 'PRE_WINDOW'
 if k<='1805Q3':return '海峡准备与大陆威胁并存；无新逐季观测不等于无活动'
 if k<='1807Q3':return '大陆作战与和谈；继承史实仅作对照基线'
 if k<='1810Q3':return '条件性大陆整固；保西王、撤军及盟友信用须兑现'
 if k<='1811Q4':return '贸易—军備—联盟交换窗口；对手条件不可删除'
 return '长期承诺维持压力测试；没有新增成功事件或稳定年数观测'

def row(s,y,q):
 k=f'{y}Q{q}'
 ev,es=events.get(k,('本季未新增已核事件；承接阶段任务，不声称历史无事','C1;CAL'))
 d=dict(path=s,quarter=k,epistemic_label='事实对照+模型推演',observed_anchor=ev,calendar_source=es,
 military_action=stage(k),military_source='C11;C12;C14',
 treasury_FRF='NA',treasury_GBP='NA',fiscal_anchor_S0=fiscal[y],fiscal_source='C2;C4F;C4U;C9',
 available_effectives='NA',manpower_state='驻防/野战/沿海/补充另账；征额不等于完训可用；盟军不保证续供',manpower_source='C14',
 diplomatic_precondition='不把敌手反应固定；选项存在不等于批准与接受',diplomacy_source='C1;C13',
 timing_check='UNKNOWN：无逐部出发到达/逐港日表；冬季不是绝对禁航或停战季',timing_source='CAL;C11;C14',
 pod='NONE_NEW',conditional_probability='未定级；不得视为通过',probability_source='C11:8;C12:4.2;C13:7',
 status='BASELINE_CONTEXT_NOT_CAPACITY_TEST',conflict='现金/实兵缺口未闭合',
 interpretation_limit='财政锚为S0史实背景，非反事实预测；来源键见c17_sources.md；NA不等于0；C12概率仅原情景条件裁量，S2避免西班牙消耗会改变让步激励，整线不继承原概率')
 if y==1811:
  d['fiscal_source']+=';H1811M;H1811B'
 if s=='S1':
  if k=='1804Q3':
   d.update(military_action='比较集中与爱尔兰协同，不新增双线舰队；本主线不采用Latouche存活改写',pod='C1:03-04菜单；非独立成功事件')
  if k=='1805Q3':
   d.update(military_action='选择Villeneuve坚持北上与集中掩护分支；达到渡海条件才准主力上船',pod='D1-S1;C1:06',conditional_probability='低：1805集中掩护支线整体；四门槛不可连乘',probability_source='C11:8',status='LOW_BRANCH_UNVERIFIED',conflict='同一布洛涅主力不可同时登英和复制8月东调；A/B窗口未闭合',timing_check='22-26日命令层有差异；英8月16/17日分兵不作法8月15日已知信息')
  elif k>='1805Q4':
   d.update(military_action='仅条件延续：先核登陆后供给、终战与再部署；不指定新的征服结果',diplomatic_precondition='英国合法政府和舰队分别接受/执行；大陆联军自主行动',diplomacy_source='C11:7-8;C16:1,6',pod='M1-S1至M5-S1条件持续',conditional_probability='快速迫和不高于低概率登陆支线；其后未定级',probability_source='C11:8;C16',status='UNRESOLVED_AFTER_DIVERGENCE',conflict='不继承史实乌尔姆/提尔西特战果、法军财政入账或英舰缴械',timing_check='史实8月26日至10月7日42天/至20日55天不是登陆后可复制的返回工期')
 else:
  if k>='1807Q4':
   d.update(status='CONDITIONAL_NOT_CLOSED',military_action='保留西班牙盟友而非换朝；不把避免半岛战争折算成同量自由机动兵',diplomatic_precondition='西班牙保实权；葡萄牙/殖民地/封锁争端仍须单独处理',diplomacy_source='SPAIN;C5;C13:7C',pod='D1-S2;M1-S2',military_source='C5;C14')
  if k=='1808Q2':
   d.update(military_action='兑现4月条件承认姿态为晚分岔替代；主路径采用1807Q4开始不升级换朝',conflict='晚分岔仍须核退位自愿性、撤占与信誉修复；不使用3月29日伪信')
  if k>='1808Q3':
   d['diplomatic_precondition']+='；普鲁士赔款与撤军不可同时无限加码'
  if k>='1810Q1':
   d.update(military_action='按地区评估可核缩编与防卫；不将缩军命令当全国稳态实力',military_source='C14;C12',pod='D1-S2持续;D2-S2;D3-S2;M2-S2',diplomatic_precondition='可执行普鲁士撤军终点；俄贸易与前沿安全；奥地利同意不得预支',diplomacy_source='C12:4;C13:7C',conflict='俄奥也能恢复财政军力；和平红利不只归法国')
  if k=='1811Q4':
   d.update(pod='D3-S2;D4-S2;D5-S2;D6-S2;M2-S2;M3-S2',military_action='把法国贸易/降军备提议与俄备忘录放入谈判；整个交换包尚未共同批准',diplomatic_precondition='贸易空间+前沿限兵+普鲁士安全+补偿+担保；不可只摘取避战收益',conditional_probability='原卡条件评级中：避免1812式全面入侵；本组合因前置西班牙改写未定级，不保证更长和平',probability_source='C12:4.2A',status='CONDITIONAL_AVOIDANCE_ONLY')
  if k>='1812Q1':
   d.update(military_action='不发动1812式全面入侵；留足防御、驻防、训练与财政负担；无需复制史实1813/14溃退',diplomatic_precondition='各方继续履约；英方接受特定大陆安排而非永久服从；俄奥独立军力获容忍',diplomacy_source='C12:7;C13:7C;C16',pod='D1-S2至D6-S2持续;M1-S2至M5-S2',conditional_probability='原卡条件评级：避免1812中、英接受有限大陆优势中低、长期排他霸权低；本组合未定级，整线不可定量',probability_source='C12:4.2A,7;C13:7C',status='MAINTENANCE_UNVERIFIED',conflict='避免灾难不等于已证1815和平稳态；不能调用不存在的永久征服收益')
  if s=='S3' and k>='1810Q4':
   d.update(military_action='强化封锁以求迫和；军警/舰队/盟国执行投入须另付成本',military_source='C1:10;C4F;C16',diplomatic_precondition='A严格俄贸易封闭：放弃S2贸易通融收益；B俄国豁免：不再声称完全封锁',diplomacy_source='R1811;C12:4;C16:3',pod='D1-S3;M1-S3至M4-S3',conditional_probability='未定级：依赖未给更强封锁迫和成功率；不能转用史实危机强度',probability_source='C16:1-3;C12:4',status='POLICY_CONFLICT_REQUIRES_FORK',conflict='最大化版本互斥；折中可行性待核，不宣称所有有限封锁都不可能',timing_check='经济痛→贸易松绑→谈判→战略承认各有时滞；没有破产倒计时')
 if k=='1803Q1':
  d.update(status='PRE_WINDOW',military_action='不安排任何改写',pod='OUTSIDE_POD',conditional_probability='不适用',conflict='无；仅满足完整历年账格',timing_check='项目干预下限为1803年5月')
 elif k=='1803Q2':
  d['timing_check']='本季1/3以上在PoD下限之前；不得把5月前事件改写'
 return d
rows=[row(s,y,q) for s in ('S1','S2','S3') for y in range(1803,1816) for q in range(1,5)]
with (P/'c17_timeline.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
assert len(rows)==156 and len({(r['path'],r['quarter']) for r in rows})==156
assert all(r[x]=='NA' for r in rows for x in ['treasury_FRF','treasury_GBP','available_effectives'])
assert all(r['status']=='UNRESOLVED_AFTER_DIVERGENCE' for r in rows if r['path']=='S1' and r['quarter']>='1805Q4')
assert all(r['status']=='POLICY_CONFLICT_REQUIRES_FORK' for r in rows if r['path']=='S3' and r['quarter']>='1810Q4')
assert all(all(str(v) for v in r.values()) for r in rows)
diffs={'1805-08-26_to_1805-10-07':(date(1805,10,7)-date(1805,8,26)).days,'1805-08-26_to_1805-10-20':(date(1805,10,20)-date(1805,8,26)).days,'1805-08-22_to_1805-10-07':(date(1805,10,7)-date(1805,8,22)).days,'1805-08-22_to_1805-10-20':(date(1805,10,20)-date(1805,8,22)).days,'1806-09-25_to_1806-10-14':(date(1806,10,14)-date(1806,9,25)).days,'1807-06-14_to_1807-07-07':(date(1807,7,7)-date(1807,6,14)).days}
(P/'c17_checks.json').write_text(json.dumps({'rows':len(rows),'rows_each':{s:sum(r['path']==s for r in rows) for s in ('S1','S2','S3')},'numeric_cash_and_effectives':'ALL_NA','status_counts':{st:sum(r['status']==st for r in rows) for st in sorted({r['status'] for r in rows})},'date_differences_exclude_start':diffs,'validation_scope':'Schema, complete grid, NA discipline, branch invalidation and calendar subtraction only; NOT historical feasibility certification.'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Wrote 156 rows; bookkeeping assertions passed. No capacity model fitted.')
