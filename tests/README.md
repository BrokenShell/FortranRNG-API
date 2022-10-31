## FortranRNG Test Suite

### Boolean Generator Tests
    Output Analysis: FortranRNG.percent_true(33.333) => bool[True, False] : True ~= 33.333%
    Typical Timing: 101 ± 11 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 0
     Maximum: 1
     Mean: 0.323
     Std Deviation: 0.4678566980282423
    bool distribution of 100000:
     False: 66.771%
     True: 33.229%

### Integer Generator Tests
    Output Analysis: FortranRNG.random_below(10) => [0, 10)
    Typical Timing: 104 ± 12 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 4
     Maximum: 9
     Mean: 4.491
     Std Deviation: 2.8312426485440865
    Distribution of 100000 samples:
     0: 9.984%
     1: 10.0%
     2: 9.93%
     3: 10.052%
     4: 10.21%
     5: 9.976%
     6: 9.853%
     7: 10.117%
     8: 10.002%
     9: 9.876%
    
    Output Analysis: FortranRNG.random_int(1, 10) => [1, 10]
    Typical Timing: 118 ± 16 ns
    Statistics of 1000 samples:
     Minimum: 1
     Median: 5
     Maximum: 10
     Mean: 5.468
     Std Deviation: 2.921559773735857
    Distribution of 100000 samples:
     1: 10.028%
     2: 9.989%
     3: 10.17%
     4: 9.968%
     5: 9.983%
     6: 9.887%
     7: 10.02%
     8: 9.985%
     9: 9.95%
     10: 10.02%
    
    Output Analysis: FortranRNG.random_range(2, 11, 2) => [2, 10] by 2
    Typical Timing: 130 ± 20 ns
    Statistics of 1000 samples:
     Minimum: 2
     Median: 6
     Maximum: 10
     Mean: 5.99
     Std Deviation: 2.9045371983048067
    Distribution of 100000 samples:
     2: 19.981%
     4: 19.762%
     6: 20.184%
     8: 19.9%
     10: 20.173%
    
    Output Analysis: FortranRNG.d(10) => [1, 10]
    Typical Timing: 101 ± 16 ns
    Statistics of 1000 samples:
     Minimum: 1
     Median: 5
     Maximum: 10
     Mean: 5.453
     Std Deviation: 2.8266200276621514
    Distribution of 100000 samples:
     1: 10.024%
     2: 10.094%
     3: 9.953%
     4: 9.937%
     5: 9.892%
     6: 9.92%
     7: 10.083%
     8: 9.993%
     9: 10.152%
     10: 9.952%
    
    Output Analysis: FortranRNG.dice(3, 6) => [3, 18] ~= 10.5
    Typical Timing: 143 ± 27 ns
    Statistics of 1000 samples:
     Minimum: 3
     Median: 10
     Maximum: 18
     Mean: 10.402
     Std Deviation: 2.9180320270536635
    Distribution of 100000 samples:
     3: 0.435%
     4: 1.35%
     5: 2.836%
     6: 4.741%
     7: 6.956%
     8: 9.582%
     9: 11.592%
     10: 12.629%
     11: 12.35%
     12: 11.555%
     13: 9.799%
     14: 6.893%
     15: 4.645%
     16: 2.797%
     17: 1.36%
     18: 0.48%
    
    Output Analysis: FortranRNG.plus_or_minus(3) => [-3, 3]
    Typical Timing: 110 ± 23 ns
    Statistics of 1000 samples:
     Minimum: -3
     Median: 0
     Maximum: 3
     Mean: -0.024
     Std Deviation: 1.9963490199385001
    Distribution of 100000 samples:
     -3: 14.251%
     -2: 14.467%
     -1: 14.171%
     0: 14.271%
     1: 14.307%
     2: 14.336%
     3: 14.197%
    
    Output Analysis: FortranRNG.plus_or_minus_linear(3) => [-3, 3] ~= 0
    Typical Timing: 117 ± 22 ns
    Statistics of 1000 samples:
     Minimum: -3
     Median: 0
     Maximum: 3
     Mean: 0.031
     Std Deviation: 1.6001873639044897
    Distribution of 100000 samples:
     -3: 6.298%
     -2: 12.476%
     -1: 18.94%
     0: 24.943%
     1: 18.683%
     2: 12.36%
     3: 6.3%

### Float Generator Tests
    Output Analysis: FortranRNG.canonical() => int(10x)[0, 10)
    Typical Timing: 87 ± 15 ns
    Statistics of 1000 samples:
     Minimum: 0.0034464484139629104
     Median: (0.5231857781223649, 0.5239468488405762)
     Maximum: 0.9968710627092774
     Mean: 0.5148848758658147
     Std Deviation: 0.28776735700470873
    <lambda> distribution of 100000:
     0: 9.98%
     1: 10.136%
     2: 9.969%
     3: 10.01%
     4: 10.011%
     5: 10.023%
     6: 9.913%
     7: 9.937%
     8: 10.024%
     9: 9.997%
    
    Output Analysis: FortranRNG.random_float(1, 10) => int[1, 10)
    Typical Timing: 157 ± 32 ns
    Statistics of 1000 samples:
     Minimum: 1.0052348192611125
     Median: (5.501368877363047, 5.513415363499294)
     Maximum: 9.991516015397192
     Mean: 5.439190196671824
     Std Deviation: 2.602347462267085
    int distribution of 100000:
     1: 11.208%
     2: 11.143%
     3: 11.089%
     4: 11.124%
     5: 11.114%
     6: 11.007%
     7: 11.079%
     8: 11.148%
     9: 11.088%
    
    Output Analysis: FortranRNG.triangular(0.0, 10.0, 5.0) => round[0, 10] ~= 5.0
    Typical Timing: 129 ± 17 ns
    Statistics of 1000 samples:
     Minimum: 0.19968260417503564
     Median: (4.90347886015103, 4.909571274372774)
     Maximum: 9.79201743712531
     Mean: 4.9673089985487815
     Std Deviation: 2.0230588419563698
    round distribution of 100000:
     0: 0.507%
     1: 3.993%
     2: 7.966%
     3: 11.936%
     4: 16.125%
     5: 18.996%
     6: 15.936%
     7: 12.047%
     8: 8.012%
     9: 3.968%
     10: 0.514%

### ZeroCool Index Generator Tests
    Output Analysis: FortranRNG.random_index(10) => [0, 9]
    Typical Timing: 103 ± 16 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 4
     Maximum: 9
     Mean: 4.403
     Std Deviation: 2.844764258015712
    Distribution of 100000 samples:
     0: 10.169%
     1: 9.945%
     2: 9.969%
     3: 9.824%
     4: 10.054%
     5: 10.023%
     6: 10.034%
     7: 9.965%
     8: 9.938%
     9: 10.079%
    
    Output Analysis: FortranRNG.random_index(-10) => [-10, -1]
    Typical Timing: 116 ± 24 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -6
     Maximum: -1
     Mean: -5.659
     Std Deviation: 2.832444481669807
    Distribution of 100000 samples:
     -10: 10.108%
     -9: 10.055%
     -8: 10.165%
     -7: 10.105%
     -6: 10.059%
     -5: 9.903%
     -4: 9.816%
     -3: 9.906%
     -2: 9.932%
     -1: 9.951%
    
    Output Analysis: FortranRNG.front_linear(10) => [0, 9] ~= 0
    Typical Timing: 106 ± 16 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 2
     Maximum: 9
     Mean: 2.819
     Std Deviation: 2.3477118116904276
    Distribution of 100000 samples:
     0: 18.945%
     1: 16.95%
     2: 15.07%
     3: 12.877%
     4: 10.946%
     5: 9.01%
     6: 7.169%
     7: 5.073%
     8: 2.974%
     9: 0.986%
    
    Output Analysis: FortranRNG.front_linear(-10) => [-10, -1] ~= -10
    Typical Timing: 117 ± 15 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -8
     Maximum: -1
     Mean: -7.206
     Std Deviation: 2.3990246600065035
    Distribution of 100000 samples:
     -10: 18.877%
     -9: 16.982%
     -8: 14.986%
     -7: 13.267%
     -6: 11.047%
     -5: 8.931%
     -4: 6.986%
     -3: 4.991%
     -2: 2.954%
     -1: 0.979%
    
    Output Analysis: FortranRNG.middle_linear(10) => [0, 9] ~= 4.5
    Typical Timing: 109 ± 17 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 5
     Maximum: 9
     Mean: 4.569
     Std Deviation: 2.0384784508045195
    Distribution of 100000 samples:
     0: 1.997%
     1: 5.938%
     2: 10.214%
     3: 13.88%
     4: 18.026%
     5: 18.067%
     6: 13.973%
     7: 10.016%
     8: 5.944%
     9: 1.945%
    
    Output Analysis: FortranRNG.middle_linear(-10) => [-10, -1] ~= -5.5
    Typical Timing: 113 ± 17 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -5
     Maximum: -1
     Mean: -5.515
     Std Deviation: 2.066408731361016
    Distribution of 100000 samples:
     -10: 2.095%
     -9: 6.051%
     -8: 9.943%
     -7: 13.978%
     -6: 18.03%
     -5: 17.985%
     -4: 13.974%
     -3: 9.833%
     -2: 6.014%
     -1: 2.097%

    Output Analysis: FortranRNG.back_linear(10) => [0, 9] ~= 9
    Typical Timing: 98 ± 7 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 7
     Maximum: 9
     Mean: 6.163
     Std Deviation: 2.3929390207769936
    Distribution of 100000 samples:
     0: 1.038%
     1: 3.035%
     2: 5.01%
     3: 7.007%
     4: 8.878%
     5: 10.907%
     6: 13.118%
     7: 14.83%
     8: 17.093%
     9: 19.084%
    
    Output Analysis: FortranRNG.back_linear(-10) => [-10, -1] ~= -1
    Typical Timing: 107 ± 10 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -3
     Maximum: -1
     Mean: -3.733
     Std Deviation: 2.317559509933258
    Distribution of 100000 samples:
     -10: 1.004%
     -9: 3.01%
     -8: 5.012%
     -7: 6.927%
     -6: 9.053%
     -5: 11.116%
     -4: 13.087%
     -3: 14.827%
     -2: 17.051%
     -1: 18.913%
    
    Output Analysis: FortranRNG.quantum_linear(10) => [0, 9] ~= 4.5
    Typical Timing: 127 ± 22 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 4
     Maximum: 9
     Mean: 4.368
     Std Deviation: 2.6434000006740495
    Distribution of 100000 samples:
     0: 7.389%
     1: 8.732%
     2: 9.937%
     3: 11.395%
     4: 12.56%
     5: 12.668%
     6: 11.463%
     7: 9.926%
     8: 8.56%
     9: 7.37%
    
    Output Analysis: FortranRNG.quantum_linear(-10) => [-10, -1] ~= -5.5
    Typical Timing: 141 ± 29 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -6
     Maximum: -1
     Mean: -5.492
     Std Deviation: 2.6961463619776294
    Distribution of 100000 samples:
     -10: 7.264%
     -9: 8.806%
     -8: 10.207%
     -7: 11.288%
     -6: 12.573%
     -5: 12.634%
     -4: 11.288%
     -3: 9.91%
     -2: 8.616%
     -1: 7.414%
