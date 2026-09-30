# P7 SOURCES ｜ 来源分层申明

本卡是总装卡：**第一层来源是本轮44张单位卡与4张总装卡的定稿产物**，第二层是它们所亲读的一手/二手文献（P7经卡转引，未重复亲验），第三层是明标的通识/权重知识填充项。红队抽核任一锚点请先回源卡，再沿源卡SOURCES回一手。

## A. 亲读并直接承重（本卡逐文件读取）

### A1 骨架
- `nodes/r_5b1357a9c6/cards/t_c87512/P6_victory_paths_wargame.md` §5（1803–15逐年）、§6（1816–48分段+八分问对弈版）、§0–§3（定理与开关）——年表骨架与1848终局的第一来源
- `nodes/r_5b1357a9c6/cards/t_c87512/P6_paths_annual.csv` 路径B年度状态行（britain/blockade/russia/spain/manpower/fiscal六列）——每年封锁态与两账结算的机读来源
- 协调台账 `nodes/r_5b1357a9c6/coordination_ledger.md` 全文（188行）——各卡验收记录、口径冲突表、接口待办；P7口径纪律（P6验收条⑪）出处

### A2 血肉（44单位卡年表，经 extract_yeartables.py 批量抽取1,494行原料后逐段亲读）
F1 t_08b9e7 / F2 t_0e763d（含annual_levies、hardware）/ F3 t_b1a536（含model_keypoints）/ F4 t_9f10b6 / F5 t_7c3954 / B1 t_c69786（B1a/B1b/B1c）/ B2 t_044211（含evidence_bank）/ B3 t_998052（含table_historical）/ B4 t_b9e29c（含transport supplement）/ B5 t_87ba37（含export_substitution、三报告）/ B6 t_0fed70 / IE t_c8b161 / R1 t_91cbee / R2 t_29957a（含三报告）/ R3 t_2c3192 / PL t_b5dab4 / A t_f4bb81 / PR t_3ee1b0 / G1 t_f55d87 / G2 t_cbaee3 / NL t_ccdcc8 / SC t_8b4a3e（part5/6+主文）/ IT1 t_be9258 / IT2 t_8f2668 / IT3 t_5b1d64 / SP1 t_3282da / SP2 t_27c409（part2/3+主文）/ PT t_219822 / OT t_66ee8d / EG t_ca3e8d / PS t_611e2b（含sec4）/ IN1 t_0bb54c / IN2 t_05cc22（三版本）/ US t_b0f045 / HT t_68821f（三版本）/ MX t_9bd988 / SA t_f314c4 / X1 t_656a10 / X2 t_6f3beb / X3 t_86b684 / X4 t_b702da / E1 t_02f417（partA/C）/ D1 t_40198e / D2 t_e0038f
- 各卡交接摘要（Handoff）与台账验收条目作为定稿结论的第二读法来源

### A3 总装姊妹卡（数字直接引用）
- P2 `t_c98c24/P2_provincialization_verdict.md` 结论与 `P2_budget.csv`/`P2_policy_closure.csv`（39.5–40.5m、57.57万/55.86万、330m/165m变体）
- P4 `t_24b942/P4_four_snapshots.csv`（0.742/0.902/0.449/0.876/0.731）、P4_sensitivity（无安特卫普0.444）
- P5 `t_ec2248/P5_continental_economy_1815_1848.md`（分层准入、Chaptal账、货币三形态、莱茵河制度、1.37–1.51倍带）

### A4 工具起点（上一轮）
- `nodes/r_b55f2c1cf5/cards/t_a8401d/build_timeline.py` 与 `c17_timeline.csv`——结构参照（path/period/source-key设计）；其季度NA记账格式按本轮契约弃用；其已核锚点经本轮B1/PR/OT重核后引用；"未识别"未继承

## B. 经单位卡转引的关键一手/二手文献（标注：P7未亲验，回源卡核）
- Oman《Peninsular War》III/IV附录法军返表（F2亲读）；Marion《Histoire financière》IV 1925（F4亲读，pp.304–325诸表）；Buist《At Spes non Fracta》1974（X1亲读，pp.285–331白银合约与tiercering）；Heckscher《The Continental System》1922（X2/X3/G2/IT1亲读，pp.178–306）；Ellis《Napoleon's Continental Blockade: Alsace》1981（X2/P5亲读，附录D/G/I首转录）；Lieven/Riehn/Keep（R3亲读）；Vandal I–III（R1/PR/OT亲读）；Czartoryski回忆录（R1/PL亲读）；Barton《Scandinavia in the Revolutionary Era》（SC亲读）；Grab 2003（IT1/D2/G2/NL亲读）；La Parra两传（SP1亲读）；Esdaile/Tone/Fraser/Fontana/Lawrence/Callahan（SP2亲读）；Shaw/Aksan/Yaycioglu/Puryear/Driault（OT/EG亲读）；Aitchison条约集VII/IX、Driault 1904、Kaye、Prinsep（PS亲读）；Milburn/Minto/Wilson III/Dutt 1906（IN1亲读）；Sen/Parkinson/Gordon/Prentout经Kaeppelin（IN2亲读）；Perkins/Pitkin（US亲读）；Geggus/Mackenzie/Girard IJNH/Slave Voyages（HT亲读）；Marichal/Humboldt（MX亲读）；Castlereagh Correspondence VII/Torrente/Moreno/Hamnett（SA亲读）；Ziegler/Ferguson/Ullmann/Gartenlaube 1875（X1亲读）；Chaptal 1819（P5/E1亲读）；Kanefsky-Robey/Fremdling/Alder/Paixhans 1822（X3/P4亲读）；Fortescue 1909/Chilcott/Desbrière（B4亲读）；James舰表经Benyon（B3亲读）；BoE千年数据库v3.1（B2亲读）；Planert书评/Fichte印数/Carbonari回忆录（X4亲读）；Joor/调停法/军事协约1803（NL亲读）；Tokarz/Rychel-Mantur（PL亲读）；Axtmann转Beer表（A亲读）；Rouanet–Piano JEH 2023+附录（Q2亲读）；黑海历史统计项目敖德萨序列/Multhauf硝石/Dawson马匹/Albion 1926（E1亲读）。

## C. 明标"通识/权重知识"的填充条目（不承重，仅年表连续性；共约20处，条目内已标）
1818英美公约、1819新加坡、1829萨蒂废除、1834 Napier事件、1816 Exmouth轰阿尔及尔（对照）、1829 Barradas远征（对照）、1838法墨糕点战争（对照）、1834叙利亚起义、1843塞尔维亚轮替、1846–48驻扎官期、1832跨大西洋霍乱（E1机制内）、1837美国恐慌（周期内生）、1842 Webster–Ashburton等。凡"（对照）"者为史实事件在本线的**不发生**申明。

## D. 本卡生成物
- `P7_chronicle.csv`（338条，8字段+id）；`P7_consistency.csv`（54行四账+冲突）；`P7_world_chronicle_1803_1848.md`（1,383行）
- 脚本：`extract_yeartables.py`（原料抽取）、`build_p7.py`（合并/校验/覆盖检查）、`gen_consistency.py`、`gen_md.py`；fragment源文件 `frag_*.py` 9个（含逐条锚点，即本卡的notes层）
- 复算：`python3 build_p7.py && python3 gen_consistency.py && python3 gen_md.py` 确定性重建全部交付物

## E. 缺口（对应正文§5）
- 英国对保护性关税的反应函数无卡检验（全项目最大单点，B1-sup/X2-sup候选）
- 1806法方书面条款、俄方关税容忍档案、Danson 1894保费、1812文官宪兵实员表、F1红线份额独立估计
- OT/EG/PS/IN的S5年表为分段非逐年，东方/亚洲栏1816–48分辨率低于欧洲栏
- P2乙层分叉（联合乐观反例）未展开为备选年表
