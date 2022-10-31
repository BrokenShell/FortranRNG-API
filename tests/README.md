## FortranRNG Test Suite
### Boolean Generator Tests
```
Output Analysis: FortranRNG.percent_true(33.333) => bool[True, False] : True ~= 33.333%
Typical Timing: 98 ± 7 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 0
 Maximum: 1
 Mean: 0.341
 Std Deviation: 0.4742825570732535
bool distribution of 100000:
 False: 66.521%
 True: 33.479%

```
### Integer Generator Tests
```
Output Analysis: FortranRNG.random_below(10) => [0, 10)
Typical Timing: 100 ± 7 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 4
 Maximum: 9
 Mean: 4.405
 Std Deviation: 2.8515094434537835
Distribution of 100000 samples:
 0: 9.987%
 1: 10.156%
 2: 9.865%
 3: 9.958%
 4: 9.839%
 5: 9.961%
 6: 9.917%
 7: 10.045%
 8: 10.216%
 9: 10.056%

Output Analysis: FortranRNG.random_int(1, 10) => [1, 10]
Typical Timing: 123 ± 15 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 5
 Maximum: 10
 Mean: 5.417
 Std Deviation: 2.937301267956479
Distribution of 100000 samples:
 1: 10.044%
 2: 9.967%
 3: 9.988%
 4: 10.034%
 5: 10.054%
 6: 9.937%
 7: 9.907%
 8: 10.084%
 9: 9.952%
 10: 10.033%

Output Analysis: FortranRNG.random_range(2, 11, 2) => [2, 10] by 2
Typical Timing: 140 ± 29 ns
Statistics of 1000 samples:
 Minimum: 2
 Median: 6
 Maximum: 10
 Mean: 6.294
 Std Deviation: 2.7461072639474784
Distribution of 100000 samples:
 2: 20.042%
 4: 20.271%
 6: 20.075%
 8: 19.655%
 10: 19.957%

Output Analysis: FortranRNG.d(10) => [1, 10]
Typical Timing: 106 ± 21 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 6
 Maximum: 10
 Mean: 5.522
 Std Deviation: 2.8526572969169735
Distribution of 100000 samples:
 1: 10.085%
 2: 9.877%
 3: 10.066%
 4: 10.073%
 5: 10.037%
 6: 10.004%
 7: 9.823%
 8: 10.052%
 9: 10.06%
 10: 9.923%

Output Analysis: FortranRNG.dice(3, 6) => [3, 18] ~= 10.5
Typical Timing: 126 ± 10 ns
Statistics of 1000 samples:
 Minimum: 3
 Median: 11
 Maximum: 18
 Mean: 10.492
 Std Deviation: 2.9887905361314413
Distribution of 100000 samples:
 3: 0.453%
 4: 1.427%
 5: 2.843%
 6: 4.601%
 7: 6.818%
 8: 9.695%
 9: 11.639%
 10: 12.495%
 11: 12.428%
 12: 11.565%
 13: 9.777%
 14: 6.868%
 15: 4.681%
 16: 2.795%
 17: 1.414%
 18: 0.501%

Output Analysis: FortranRNG.plus_or_minus(3) => [-3, 3]
Typical Timing: 119 ± 35 ns
Statistics of 1000 samples:
 Minimum: -3
 Median: 0
 Maximum: 3
 Mean: -0.053
 Std Deviation: 2.051438373288215
Distribution of 100000 samples:
 -3: 14.315%
 -2: 14.099%
 -1: 14.31%
 0: 14.459%
 1: 14.327%
 2: 14.119%
 3: 14.371%

Output Analysis: FortranRNG.plus_or_minus_linear(3) => [-3, 3] ~= 0
Typical Timing: 119 ± 27 ns
Statistics of 1000 samples:
 Minimum: -3
 Median: 0
 Maximum: 3
 Mean: -0.035
 Std Deviation: 1.6230863838408014
Distribution of 100000 samples:
 -3: 6.264%
 -2: 12.296%
 -1: 18.638%
 0: 25.099%
 1: 18.689%
 2: 12.728%
 3: 6.286%

```
### Float Generator Tests
```
Output Analysis: FortranRNG.canonical() => int(10x)[0, 10)
Typical Timing: 82 ± 7 ns
Statistics of 1000 samples:
 Minimum: 0.0008658834023806961
 Median: (0.5233929062468657, 0.5238370162694735)
 Maximum: 0.9998730732899659
 Mean: 0.5169573087349707
 Std Deviation: 0.29113941678527466
<lambda> distribution of 100000:
 0: 9.9%
 1: 9.782%
 2: 10.015%
 3: 10.086%
 4: 9.981%
 5: 9.954%
 6: 10.052%
 7: 10.005%
 8: 10.137%
 9: 10.088%

Output Analysis: FortranRNG.random_float(1, 10) => int[1, 10)
Typical Timing: 148 ± 19 ns
Statistics of 1000 samples:
 Minimum: 1.004526029715023
 Median: (5.241083195628559, 5.242394316716904)
 Maximum: 9.994248126227511
 Mean: 5.38383129513744
 Std Deviation: 2.6528892871774983
int distribution of 100000:
 1: 11.246%
 2: 10.974%
 3: 11.089%
 4: 11.109%
 5: 11.087%
 6: 11.275%
 7: 11.054%
 8: 11.084%
 9: 11.082%

Output Analysis: FortranRNG.triangular(0.0, 10.0, 5.0) => round[0, 10] ~= 5.0
Typical Timing: 138 ± 25 ns
Statistics of 1000 samples:
 Minimum: 0.31020819989934423
 Median: (4.957463919530078, 4.960905803124106)
 Maximum: 9.899365809712503
 Mean: 5.030130094786555
 Std Deviation: 2.068757305951089
round distribution of 100000:
 0: 0.53%
 1: 3.988%
 2: 7.964%
 3: 11.998%
 4: 16.072%
 5: 19.067%
 6: 16.119%
 7: 11.799%
 8: 7.924%
 9: 4.023%
 10: 0.516%

```
