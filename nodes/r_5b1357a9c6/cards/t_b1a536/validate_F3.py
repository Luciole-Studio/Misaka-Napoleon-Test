#!/usr/bin/env python3
"""Deliverable arithmetic/structure and quotation-location checks, not historical validation."""
from pathlib import Path
import csv,json,math,re,hashlib
from collections import Counter
ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parents[3]
def csvread(name):return list(csv.DictReader((ROOT/name).open()))
a=csvread('F3_capacity.csv');assert len(a)==156
ix={(r['scenario'],r['bound'],int(r['year'])):r for r in a};assert len(ix)==156
parameters=json.loads((ROOT/'F3_model_parameters.json').read_text())
max_stock_residual=0
for r in a:
 s,b,y=r['scenario'],r['bound'],int(r['year'])
 H=float(r['hulls']);M=float(r['personnel_total_1000']);Q=float(r['qualified_personnel_1000'])
 A=int(r['mobilizable_integer']);I=int(r['commissioned_model_I'])
 R=float(r['nonline_personnel_reserved_1000']);RQ=float(r['nonline_qualified_reserved_1000']);ready=float(r['ready_fraction'])
 assert 0<=I<=A<=H and 0<=Q<=M
 assert A*.8+R<=M+1e-5 and A*.45+RQ<=Q+1e-5 and A<=ready*H+1e-5
 calc=max(0,min(ready*H,(M-R)/.8,(Q-RQ)/.45))
 assert abs(calc-float(r['mobilizable_continuous']))<2e-6
 assert A==math.floor(calc+1e-6)
 assert A-I==int(r['reserve_ready_within_12m'])
 assert abs(H-A-float(r['hulls_not_mobilizable_within12m']))<1e-6
 if y>1810:
  previous=ix[s,b,y-1]
  residual=abs(H-(float(previous['hulls'])+float(r['launches'])-float(r['natural_retirement'])-float(r['war_loss'])))
  max_stock_residual=max(max_stock_residual,residual)
  assert residual<2e-6
 if y<=1815:
  other=ix['P' if s=='W' else 'W',b,y]
  assert all(r[k]==other[k] for k in r if k!='scenario')
assert int(ix['W','base',1830]['mobilizable_integer'])==84
assert int(ix['P','base',1830]['mobilizable_integer'])==111
sens=csvread('F3_sensitivity.csv');assert len(sens)==80
assert len({(r['scenario'],r['test'],r['year']) for r in sens})==80
for r in sens:
 if r['test']=='base':assert int(r['A12'])==int(ix[r['scenario'],'base',int(r['year'])]['mobilizable_integer'])
mat=csvread('F3_material_requirements.csv');assert len(mat)==24
for r in mat:assert abs(sum(float(r[k]) for k in ['line_new_required','line_repair_required','nonline_assumed_required'])-float(r['total_required_not_actual_transport']))<.011
yards=csvread('yards_launches_1807_1813.csv');assert len(yards)==52 and len({r['ship_identity'] for r in yards})==52
assert sum(r['scope']=='requested_seven' for r in yards)==50
hist=csvread('F3_historical_anchors.csv');assert len({r['id'] for r in hist})==len(hist)
assert all(r['record_type']=='model_not_observation' for r in a)
report=(ROOT/'F3_french_navy_capacity.md').read_text()
for marker in '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯':assert f'## {marker}' in report
section=report.split('## ⑭',1)[1].split('## ⑮',1)[0]
nodes=[ln for ln in section.splitlines() if re.match(r'^\|18\d\d｜',ln)]
assert len(nodes)==38
policy=report.split('## ⑬',1)[1].split('## ⑭',1)[0]
assert len([ln for ln in policy.splitlines() if re.match(r'^\|B[1-8] ',ln)])==8
# Local quotations: matching normalized whitespace only; source context already read.
quotes=[
 ('S02','downloads/pages/171e7ef70128.md','La construction d’un vaisseau de 80 canons exige l’emploi de 3737 stères de bois','源单位，不自动换实方'),
 ('S03','downloads/pages/21ae17eda88c.md','les ports et arsenaux comptaient 104 vaisseaux, à flot ou en chantier.','在建和浮存混合，非可战104'),
 ('S04','downloads/pages/f042c1f13d31.md','Je ne veux pas que mes escadres sortent','有条件指挥命令，不等舰队从未出海'),
 ('S05','downloads/pages/82a063e7e022.md','un corps de 66,000 matelots','规划而非到员'),
 ('S06','downloads/pages/550652301685.md','construire chaque année huit vaisseaux au lieu de six','仅Anvers的目标，不是全国实绩'),
 ('S07','downloads/pages/f9f391a5effc.md','En 1825, l’inscription maritime comptait 94 611 inscrits dont 73 053 officiers mariniers, matelots novices et mousses.','职业登记不等军舰可用熟练人数'),
 ('S08','downloads/pages/b63d35ce3cb6.md','dont 52 à flot, portés comme disponibles sur les états de la marine','1814和约后口径；转录未阅原刊'),
 ('S09','downloads/pages/78508d75464b.md','5314 navires ennemis sont pris de 1803 à 1814','累计俘获，非英国商船存量净减'),
 ('S12','downloads/pages/04c2ed9cef98.md','sa machine à vapeur fut construite par une entreprise de Liverpool, W. Fawcett','Sphinx160hp的英国机器，不是所有法国机器皆英国进口')
]
normalize=lambda s:re.sub(r'\s+',' ',s).strip()
quote_receipts=[]
for source,path,quote,limit in quotes:
 text=(PROJECT/path).read_text();matches=[i for i,line in enumerate(text.splitlines(),1) if normalize(quote) in normalize(line)]
 assert matches,(source,quote)
 quote_receipts.append(dict(source=source,path=path,line=matches[0],quote=quote,method='whitespace_normalized_substring',limit=limit))
pdf_quotes=[
 dict(source='S01',doc_id='0fd6bd047f2a',page=16,character=2399,hash='cd8349ec598890dbd82e132eb1dd26c369f714fb6ac3076d435f8ec8ed420fa1',quote="Le vice-amiral Ganteaume, chargé au printemps 1810 par Napoléon de s'occuper du recrutement et de la formation des marins pour la nouvelle marine de 100 vaisseaux, estime le nombre de marins français à 30000.",limit='Ganteaume估计，不是普查'),
 dict(source='S01',doc_id='0fd6bd047f2a',page=24,character=4245,hash='f0fc3593e11b95fc7a409e5ecf3cedb3ae1d73d34dcc8e62c666a3bb1cdc14d5',quote="223404900 fr en 1812, 255746100 en 1813, 145919400 pour l'entretien en 1814",limit='计划/估算，非决算'),
 dict(source='S01',doc_id='0fd6bd047f2a',page=17,character=2510,hash='2465fdd5ae4c971ed6651dec96598620d0fd216b213c21f42332863b364dddd9',quote="Dans l'immédiat, le Danemark n'est en mesure de fournir que 200 matelots pour compléter les équipages des deux vaisseaux de l'Escaut.",limit='即时可拨，非总登记'),
 dict(source='S01',doc_id='0fd6bd047f2a',page=18,character=650,hash='a1e90f4c3b11d4bbd79912fb004fc3dad4d3c18df5f79e060f6736c4f4d8a89e',quote="70% des conscrits de 1811 viennent de départements qui ne sont pas français aujourd'hui.",limit='今日边界、征额类别，不是全部舰员占比')
]
audit=json.loads((ROOT/'F3_model_audit.json').read_text());assert len(audit)==6
assert all(x['backend_output']['ok'] and x['backend_output']['feasible'] for x in audit)
receipt=dict(status='arithmetic_structure_and_locator_checks_passed',not_validated=['historical_parameter_truth','joint_fiscal_material_feasibility','battle_win_probability','rendered_layout'],capacity_rows=len(a),sensitivity_rows=len(sens),material_rows=len(mat),historical_anchor_rows=len(hist),unique_yard_hulls=len(yards),timeline_nodes=len(nodes),policy_choices=8,unit_dimensions=16,max_csv_stock_residual=max_stock_residual,max_backend_residual=max(x['max_abs_replay_residual'] for x in audit),local_quote_checks=quote_receipts,pdf_doc_verify_receipts=pdf_quotes,report_sha256=hashlib.sha256(report.encode()).hexdigest())
(ROOT/'F3_validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
md=['# F3引文定位账','只证明已读版本存在所引文字；支持范围和限制另列。9项网页按空白规范化查字串，4项PDF由doc_verify返回定位；不能替代独立史源验证。','']
for n,r in enumerate(pdf_quotes+quote_receipts,1):
 locator=f"doc {r['doc_id']} p{r['page']}，字符{r['character']}，claim_hash `{r['hash']}`" if 'doc_id' in r else f"`{r['path']}` 第{r['line']}行"
 md += [f"## Q{n:02d}｜{r['source']}",f"> {r['quote']}",f"定位：{locator}。限制：{r['limit']}。",'']
(ROOT/'F3_quote_ledger.md').write_text('\n'.join(md)+'\n')
validation=f'''# F3交付自检

- 全量报告：16项模板，8项政策反应，38个带锚点/机制/推演的年表节点；涵盖S1/S2/S3/S5/S6及1848终局。
- 数量：156行能力曲线、80行敏感性、24行材料需求、{len(hist)}行史实/计划锚点、52个不同下水舰体（七组50）。模型和观察分表。
- 约束：所有年0≤I≤A12≤H、Q≤M、总员和合格员配额守恒；W/P至1815相同。CSV舍入后最大存量残差{max_stock_residual:.3g}舰；独立后端最大残差{receipt['max_backend_residual']:.3g}舰。
- 1830定稿A12主84(W)/111(P)，I主73/61；原81/108草算被替代。R代表非战列任务预留，Q为合格人员子集，非额外人口。
- 13项短引定位在F3_quote_ledger.md：4项PDF定位、9项网页空白规范化定位；Glover与Winfield–Roberts原书未读明确标注。
- F4已实读联合预算：陆300+海195只在较高收入/盟约现金案闭合；不能把本卡数量主线和最大陆军叠加。
- 未验证：参数的统计识别、完整材种与财政的联合可行性、海战胜率、Markdown渲染视觉布局。工具运算通过不是历史结论被机器证明。
- 重跑：python3 nodes/r_5b1357a9c6/cards/t_b1a536/validate_F3.py（先用build_F3_model.py与build_F3_sensitivity.py生成CSV）。
- 报告sha256：{receipt['report_sha256']}
'''
(ROOT/'VALIDATION.md').write_text(validation)
print(json.dumps({k:v for k,v in receipt.items() if k not in ['local_quote_checks','pdf_doc_verify_receipts']},ensure_ascii=False,indent=2))
