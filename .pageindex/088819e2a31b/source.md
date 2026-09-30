# Q1 分析输出（由 q1_analysis.py 生成，勿手改）

案例 N=35；地区簇 16 个：Bavaria, Belgium, Hamburg, Iberia, Illyria, NEItaly, NWItaly, Naples, Netherlands, NorthGermanClients, Rhineland, Rome, Switzerland, Tuscany, Tyrol, Warsaw
主条件 ['T', 'R', 'E', 'O']；正配置阈值≥0.8，负配置≤0.2，最小样本 n≥2。

## main::mass_lo
- 基率 0.629；常数基准准确率 0.629
- 留一行：覆盖 0.543，判定集准确率 0.737，全样本正确率 0.4
- 留一地区簇：覆盖 0.457，判定集准确率 0.75，全样本正确率 0.343
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 8, 'train_consistency': 0.875, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 9, 'train_consistency': 0.889, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.2, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 3, 'train_consistency': 0.333, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True
- 观测配置表 (T,R,E,O)：
  - 0001 n=1 正例=1 一致性=1.0 thin :: HH1813
  - 0010 n=4 正例=1 一致性=0.25 contradictory :: BE1802, NL1811, HH1806, PL1807
  - 0011 n=3 正例=2 一致性=0.667 contradictory :: NL1799, NL1809, NL1813
  - 0100 n=1 正例=1 一致性=1.0 thin :: BE1798
  - 0101 n=1 正例=1 一致性=1.0 thin :: PV1796
  - 0111 n=2 正例=2 一致性=1.0 positive :: VE1809, EM1809
  - 1001 n=1 正例=1 一致性=1.0 thin :: PA1806
  - 1010 n=6 正例=1 一致性=0.167 negative :: RH1802, PI1809, LI1805, TU1808, ZH1804, CH1805
  - 1011 n=3 正例=2 一致性=0.667 contradictory :: WE1809, BG1813, BA1813
  - 1100 n=2 正例=1 一致性=0.5 contradictory :: CH1798, IL1810
  - 1101 n=10 正例=9 一致性=0.9 positive :: RH1796, PI1798, TU1799, NA1799, CA1806, TY1809, CH1802, ES1808, PT1807, IL1813
  - 1110 n=1 正例=0 一致性=0.0 thin :: RM1809

## main::mass_hi
- 基率 0.686；常数基准准确率 0.686
- 留一行：覆盖 0.514，判定集准确率 0.778，全样本正确率 0.4
- 留一地区簇：覆盖 0.429，判定集准确率 0.8，全样本正确率 0.343
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 8, 'train_consistency': 0.875, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 9, 'train_consistency': 0.889, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.2, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 3, 'train_consistency': 0.667, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True
- 观测配置表 (T,R,E,O)：
  - 0001 n=1 正例=1 一致性=1.0 thin :: HH1813
  - 0010 n=4 正例=2 一致性=0.5 contradictory :: BE1802, NL1811, HH1806, PL1807
  - 0011 n=3 正例=2 一致性=0.667 contradictory :: NL1799, NL1809, NL1813
  - 0100 n=1 正例=1 一致性=1.0 thin :: BE1798
  - 0101 n=1 正例=1 一致性=1.0 thin :: PV1796
  - 0111 n=2 正例=2 一致性=1.0 positive :: VE1809, EM1809
  - 1001 n=1 正例=1 一致性=1.0 thin :: PA1806
  - 1010 n=6 正例=1 一致性=0.167 negative :: RH1802, PI1809, LI1805, TU1808, ZH1804, CH1805
  - 1011 n=3 正例=2 一致性=0.667 contradictory :: WE1809, BG1813, BA1813
  - 1100 n=2 正例=2 一致性=1.0 positive :: CH1798, IL1810
  - 1101 n=10 正例=9 一致性=0.9 positive :: RH1796, PI1798, TU1799, NA1799, CA1806, TY1809, CH1802, ES1808, PT1807, IL1813
  - 1110 n=1 正例=0 一致性=0.0 thin :: RM1809

## main::sustained_lo
- 基率 0.143；常数基准准确率 0.857
- 留一行：覆盖 0.457，判定集准确率 1.0，全样本正确率 0.457
- 留一地区簇：覆盖 0.314，判定集准确率 1.0，全样本正确率 0.314
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': None, 'train_n': 8, 'train_consistency': 0.375, 'decided': False, 'passed': False}
  - TY1809: {'coded_truth': 1, 'pred': None, 'train_n': 9, 'train_consistency': 0.333, 'decided': False, 'passed': False}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.0, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': 0, 'train_n': 3, 'train_consistency': 0.0, 'decided': True, 'passed': True}
  - BE1798: {'coded_truth': 0, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True
- 观测配置表 (T,R,E,O)：
  - 0001 n=1 正例=0 一致性=0.0 thin :: HH1813
  - 0010 n=4 正例=0 一致性=0.0 negative :: BE1802, NL1811, HH1806, PL1807
  - 0011 n=3 正例=0 一致性=0.0 negative :: NL1799, NL1809, NL1813
  - 0100 n=1 正例=0 一致性=0.0 thin :: BE1798
  - 0101 n=1 正例=0 一致性=0.0 thin :: PV1796
  - 0111 n=2 正例=1 一致性=0.5 contradictory :: VE1809, EM1809
  - 1001 n=1 正例=0 一致性=0.0 thin :: PA1806
  - 1010 n=6 正例=0 一致性=0.0 negative :: RH1802, PI1809, LI1805, TU1808, ZH1804, CH1805
  - 1011 n=3 正例=0 一致性=0.0 negative :: WE1809, BG1813, BA1813
  - 1100 n=2 正例=0 一致性=0.0 negative :: CH1798, IL1810
  - 1101 n=10 正例=4 一致性=0.4 contradictory :: RH1796, PI1798, TU1799, NA1799, CA1806, TY1809, CH1802, ES1808, PT1807, IL1813
  - 1110 n=1 正例=0 一致性=0.0 thin :: RM1809

## main::sustained_hi
- 基率 0.429；常数基准准确率 0.571
- 留一行：覆盖 0.686，判定集准确率 0.917，全样本正确率 0.629
- 留一地区簇：覆盖 0.6，判定集准确率 0.952，全样本正确率 0.571
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 8, 'train_consistency': 0.875, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 9, 'train_consistency': 0.889, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.0, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': 0, 'train_n': 3, 'train_consistency': 0.0, 'decided': True, 'passed': True}
  - BE1798: {'coded_truth': 0, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True
- 观测配置表 (T,R,E,O)：
  - 0001 n=1 正例=1 一致性=1.0 thin :: HH1813
  - 0010 n=4 正例=0 一致性=0.0 negative :: BE1802, NL1811, HH1806, PL1807
  - 0011 n=3 正例=1 一致性=0.333 contradictory :: NL1799, NL1809, NL1813
  - 0100 n=1 正例=0 一致性=0.0 thin :: BE1798
  - 0101 n=1 正例=0 一致性=0.0 thin :: PV1796
  - 0111 n=2 正例=2 一致性=1.0 positive :: VE1809, EM1809
  - 1001 n=1 正例=0 一致性=0.0 thin :: PA1806
  - 1010 n=6 正例=0 一致性=0.0 negative :: RH1802, PI1809, LI1805, TU1808, ZH1804, CH1805
  - 1011 n=3 正例=0 一致性=0.0 negative :: WE1809, BG1813, BA1813
  - 1100 n=2 正例=1 一致性=0.5 contradictory :: CH1798, IL1810
  - 1101 n=10 正例=9 一致性=0.9 positive :: RH1796, PI1798, TU1799, NA1799, CA1806, TY1809, CH1802, ES1808, PT1807, IL1813
  - 1110 n=1 正例=1 一致性=1.0 thin :: RM1809

## subsample::drop_general_negative (n=31)
- 基率 0.71；常数基准准确率 0.71
- 留一行：覆盖 0.452，判定集准确率 0.643，全样本正确率 0.29
- 留一地区簇：覆盖 0.419，判定集准确率 0.692，全样本正确率 0.29
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 8, 'train_consistency': 0.875, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 9, 'train_consistency': 0.889, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': None, 'train_n': 2, 'train_consistency': 0.5, 'decided': False, 'passed': False}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 3, 'train_consistency': 0.333, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True

## subsample::drop_exit_context (n=30)
- 基率 0.6；常数基准准确率 0.6
- 留一行：覆盖 0.533，判定集准确率 0.812，全样本正确率 0.433
- 留一地区簇：覆盖 0.467，判定集准确率 0.786，全样本正确率 0.367
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 7, 'train_consistency': 0.857, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 8, 'train_consistency': 0.875, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.2, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 3, 'train_consistency': 0.333, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True

## subsample::post1800_only (n=27)
- 基率 0.593；常数基准准确率 0.593
- 留一行：覆盖 0.519，判定集准确率 0.786，全样本正确率 0.407
- 留一地区簇：覆盖 0.444，判定集准确率 0.75，全样本正确率 0.333
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 4, 'train_consistency': 1.0, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 5, 'train_consistency': 1.0, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.2, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 3, 'train_consistency': 0.333, 'decided': False, 'passed': False}
  - BE1798: {'status': 'absent_from_subsample'}
  - _guard_BE1798_mass_coded_1: True

## subsample::drop_ZH1804 (n=34)
- 基率 0.618；常数基准准确率 0.618
- 留一行：覆盖 0.529，判定集准确率 0.778，全样本正确率 0.412
- 留一地区簇：覆盖 0.5，判定集准确率 0.824，全样本正确率 0.412
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 8, 'train_consistency': 0.875, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 9, 'train_consistency': 0.889, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 4, 'train_consistency': 0.0, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 3, 'train_consistency': 0.333, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True

## subsample::drop_uncertain_outcome (n=24)
- 基率 0.583；常数基准准确率 0.583
- 留一行：覆盖 0.375，判定集准确率 0.556，全样本正确率 0.208
- 留一地区簇：覆盖 0.292，判定集准确率 0.429，全样本正确率 0.125
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': None, 'train_n': 4, 'train_consistency': 0.75, 'decided': False, 'passed': False}
  - TY1809: {'coded_truth': 1, 'pred': None, 'train_n': 4, 'train_consistency': 0.75, 'decided': False, 'passed': False}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.2, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 2, 'train_consistency': 0.5, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True

## subsample::narrowest_combo (n=15)
- 基率 0.733；常数基准准确率 0.733
- 留一行：覆盖 0.4，判定集准确率 0.833，全样本正确率 0.333
- 留一地区簇：覆盖 0.4，判定集准确率 0.833，全样本正确率 0.333
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 3, 'train_consistency': 1.0, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 4, 'train_consistency': 1.0, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': None, 'train_n': 1, 'train_consistency': None, 'decided': False, 'passed': False}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 2, 'train_consistency': 0.5, 'decided': False, 'passed': False}
  - BE1798: {'status': 'absent_from_subsample'}
  - _guard_BE1798_mass_coded_1: True

## recode::O_off_for_late_aid
- 基率 0.629；常数基准准确率 0.629
- 留一行：覆盖 0.514，判定集准确率 0.667，全样本正确率 0.343
- 留一地区簇：覆盖 0.429，判定集准确率 0.667，全样本正确率 0.286
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': None, 'train_n': 2, 'train_consistency': 0.5, 'decided': False, 'passed': False}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 7, 'train_consistency': 0.857, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.2, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 3, 'train_consistency': 0.333, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True

## recode::E_on_for_disputed
- 基率 0.629；常数基准准确率 0.629
- 留一行：覆盖 0.514，判定集准确率 0.722，全样本正确率 0.371
- 留一地区簇：覆盖 0.429，判定集准确率 0.733，全样本正确率 0.314
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 7, 'train_consistency': 0.857, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 8, 'train_consistency': 0.875, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': 0, 'train_n': 5, 'train_consistency': 0.2, 'decided': True, 'passed': True}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 3, 'train_consistency': 0.333, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True

## recode::R_on_for_catholic_annex
- 基率 0.629；常数基准准确率 0.629
- 留一行：覆盖 0.4，判定集准确率 0.643，全样本正确率 0.257
- 留一地区簇：覆盖 0.4，判定集准确率 0.714，全样本正确率 0.286
- 指定反证（留一簇）：未通过
  - ES1808: {'coded_truth': 1, 'pred': 1, 'train_n': 8, 'train_consistency': 0.875, 'decided': True, 'passed': True}
  - TY1809: {'coded_truth': 1, 'pred': 1, 'train_n': 9, 'train_consistency': 0.889, 'decided': True, 'passed': True}
  - RH1802: {'coded_truth': 0, 'pred': None, 'train_n': 4, 'train_consistency': 0.25, 'decided': False, 'passed': False}
  - BE1802: {'coded_truth': 0, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - BE1798: {'coded_truth': 1, 'pred': None, 'train_n': 0, 'train_consistency': None, 'decided': False, 'passed': False}
  - _guard_BE1798_mass_coded_1: True

## 单条件边际（描述性，非因果）
- T=0: n=12, mass_lo=0.667, sustained_lo=0.083
- T=1: n=23, mass_lo=0.609, sustained_lo=0.174
- R=0: n=18, mass_lo=0.444, sustained_lo=0.0
- R=1: n=17, mass_lo=0.824, sustained_lo=0.294
- E=0: n=16, mass_lo=0.875, sustained_lo=0.25
- E=1: n=19, mass_lo=0.421, sustained_lo=0.053
- O=0: n=14, mass_lo=0.286, sustained_lo=0.0
- O=1: n=21, mass_lo=0.857, sustained_lo=0.238
- S=0: n=11, mass_lo=0.455, sustained_lo=0.091
- S=1: n=24, mass_lo=0.708, sustained_lo=0.167
- D=0: n=15, mass_lo=0.667, sustained_lo=0.133
- D=1: n=20, mass_lo=0.6, sustained_lo=0.15
- X=1: n=6, mass_lo=0.167, sustained_lo=0.0
- X=2: n=29, mass_lo=0.724, sustained_lo=0.172
- dynasty_exile=0: n=11, mass_lo=0.545, sustained_lo=0.091
- dynasty_exile=1: n=24, mass_lo=0.667, sustained_lo=0.167
- brigand_tradition=0: n=19, mass_lo=0.684, sustained_lo=0.053
- brigand_tradition=1: n=16, mass_lo=0.562, sustained_lo=0.25
- coast_access=0: n=15, mass_lo=0.6, sustained_lo=0.067
- coast_access=1: n=20, mass_lo=0.65, sustained_lo=0.2
