from pathlib import Path
import shutil, csv, json, hashlib, subprocess, zipfile
R=Path('/Users/makiko/Documents/exam'); B=R/'final/r_5b1357a9c6-revised';W=B/'audit/20260924_整书统稿'; D=W/'模型与复算附件'; D.mkdir(exist_ok=True)
sets={
 't_c98c24':['*.csv','p2_joint_model.py','notes_model_audit.md','phase_design.md'],
 't_1f7db4':['Q2_*.csv','analyze_q2.py','notes_method.md'],
 't_c87512':['P6_*.csv','p6_wargame.py','p6_endgame.py'],
 't_24b942':['P4_*.csv','build_p4.py','verify_p4.py'],
 't_b1a536':['F3_capacity.csv','F3_sensitivity.csv','F3_material_requirements.csv','F3_model_parameters.json','F3_historical_anchors.csv'],
 't_998052':['B3_response.csv','B3_capacity.csv','model_assumptions.md'],
}
manifest=[]
for folder,pats in sets.items():
 src=R/'nodes/r_5b1357a9c6/cards'/folder;dst=D/'历史模型/cards'/folder;dst.mkdir(parents=True,exist_ok=True)
 for p in sorted({p for pat in pats for p in src.glob(pat)}):
  target=dst/p.name;shutil.copy2(p,target)
  manifest.append({'file':str(target.relative_to(D)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'provenance':str(p.relative_to(R)),'status':'历史条件模型；不等于本书选定主线'})
current=D/'本次预算与约束';current.mkdir(exist_ok=True)
(current/'预算.csv').write_text('revenue,civil_debt_court,army,navy,new_obligations,transport_capital,reserve\n650,280,245,90,15,0,20\n750,280,280,145,25,0,20\n850,300,300,165,25,40,20\n')
(current/'复算.py').write_text('''from pathlib import Path
import csv,json
P=Path(__file__).resolve().parent
rows=[]
for r in csv.DictReader((P/'预算.csv').open()):
 r={k:float(v) for k,v in r.items()}
 used=sum(v for k,v in r.items() if k!='revenue')
 assert used==r['revenue']
 r['balance']=r['revenue']-used
 r['army_roster_at_700']=r['army']*1000000/700
 r['army_roster_at_900']=r['army']*1000000/900
 rows.append(r)
out={'unit':'million francs; army cost francs per person-year; author scenarios, not historical revenue observations','budgets':rows,'province_example_gross':{'retained':83+37.5+33+16,'excluded':66.5+38.791+22.5+16.5,'unallocated':342.260044-(83+37.5+33+16+66.5+38.791+22.5+16.5)},'common_fund_spendable':{'base_5m_5pct':5-20*.05-1,'5m_7pct':5-20*.07-1,'3m_7pct':3-20*.07-1},'rail_1500km_cost_mfr':[1500*.25,1500*.40],'annual_rail_15years_mfr':[1500*.25/15,1500*.40/15],'navy_extra_195_vs_165':195-165,'navy_extra_share_rail_40':(195-165)/40,'rouanet_piano_source_mismatch':{'2812_over_10499':2812/10499,'3256_over_10499':3256/10499},'annualized_3144_nine_month_letters':3144*12/9}
(P/'复算结果.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
''')
r=subprocess.run(['python3',str(current/'复算.py')],text=True,capture_output=True,check=True)
# 旧模型在隔离副本重跑，只核输出复现，不把运行成功当历史成立。
T=W/'历史模型隔离复算';shutil.copytree(D/'历史模型',T,dirs_exist_ok=True)
runs=[]
for folder,script in [('t_c98c24','p2_joint_model.py'),('t_1f7db4','analyze_q2.py'),('t_24b942','build_p4.py'),('t_c87512','p6_wargame.py'),('t_c87512','p6_endgame.py')]:
 d=T/'cards'/folder;before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in d.glob('*.csv')}
 r=subprocess.run(['python3',str(d/script)],text=True,capture_output=True,timeout=60)
 after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in d.glob('*.csv')}
 runs.append({'script':f'{folder}/{script}','exit_code':r.returncode,'changed_existing_csv':[k for k in before if before[k]!=after.get(k)],'new_csv':[k for k in after if k not in before],'stdout':r.stdout[-1500:],'stderr':r.stderr[-1500:]})
(D/'历史模型复现检查.json').write_text(json.dumps(runs,ensure_ascii=False,indent=2))
(D/'说明.md').write_text('''# 《胜利之后的欧洲》模型与复算附件

版本：2026-09-24整书统稿。与同名完整修订稿及阅读版配套；附件是算式与证据追踪，不替代正文的论证和数据表。

## 先区分两类东西

- **本次预算与约束**：正文采用的650／750／850百万法郎收入门槛、用途分配、700／900法郎兵均成本敏感性、共同基金、铁路及源内差额复算。数字是明确的规划假设，不是已经查得的同一疆域年度国库实收。运行其中“复算.py”只需Python 3标准库。
- **历史模型**：保留前期研究的P2省化、Q2征兵、P4海军竞赛、P6对弈，以及F3法国海军与B3英国反应输入结果。正文保留它们作为条件比较，并未采纳全部地域、舰数或概率为当前主线。

## 定位

P2对应资料附编的省化与队列讨论；Q2对应行省化章的兵额转换；P4对应海军章1815—1830年的较高投入对照；P6对应资料附编的历史路径比较。其文件名只是复算入口，正文已另行写明论点。

各目录保持原有相对布局。P2、Q2、P4、P6的五项脚本已在隔离副本执行，退出码、既有CSV是否复现见“历史模型复现检查.json”。原始文件未被运行修改。运行成功仅表示给定参数下的算术可复现，不证明参数、因果关系、政治概率或1848年的结果。

F3只附参数、输入锚点和既有结果，其原引擎依赖未随书打包，也未在本轮重新执行。因此，P4成功读取F3既有输出不等于F3从最上游完整重算。对于同年疆域实收、逐国盟约承诺和低预算主线舰队，正文仍保留联合核算缺口。

本包不包含第三方专著和扫描全文。“来源清单.json”记录研究文件相对来源及SHA-256；“附件指纹.json”记录本包文件版本。源表中的MODEL及缺失值保持原意。历史模型中的条件概率和路径分值均属作者设值，不是统计识别。
''')
(D/'来源清单.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
files=[p for p in D.rglob('*') if p.is_file() and p.name!='附件指纹.json'];(D/'附件指纹.json').write_text(json.dumps({str(p.relative_to(D)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},ensure_ascii=False,indent=2))
zipout=B/'胜利之后的欧洲_模型与复算附件.zip'
with zipfile.ZipFile(zipout,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(D.rglob('*')):
  if p.is_file():z.write(p,str(p.relative_to(D)))
p=B/'chapters/10_资料附编.md';s=p.read_text();old=next(l for l in s.splitlines() if l.startswith('〔资6〕'));new='〔资6〕本书作者编制的[模型与复算附件](胜利之后的欧洲_模型与复算附件.zip)，2026年9月24日版，包括各情景输入、源代码、生成表、版本指纹与复现记录。P2省化、Q2征兵、P4海军竞赛及P6对弈的五项脚本在隔离副本执行；F3上游容量引擎未重跑，海军竞赛使用其已保存输出。新增现金预算、共同基金和铁路试算另列输入与算式。这里证明的是给定输入下的算术和部分输出复现，不是同一疆域全部年度实收、盟约履行或政治概率已经验证。';s=s.replace(old,new);p.write_text(s)
print(json.dumps({'archived_files':len(manifest),'zip_bytes':zipout.stat().st_size,'runs':runs},ensure_ascii=False,indent=2))
