## FortranRNG Test Suite

### Boolean Generator Tests
    Output Analysis: FortranRNG.percent_true(33.333) => bool[True, False] : True ~= 33.333%
    Typical Timing: 96 ± 6 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 0
     Maximum: 1
     Mean: 0.326
     Std Deviation: 0.4689818162188636
    bool distribution of 100000:
     False: 66.565%
     True: 33.435%
    
### Integer Generator Tests
    Output Analysis: FortranRNG.random_below(10) => [0, 10)
    Typical Timing: 96 ± 4 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 4
     Maximum: 9
     Mean: 4.413
     Std Deviation: 2.862625652373294
    Distribution of 100000 samples:
     0: 10.052%
     1: 10.117%
     2: 10.058%
     3: 10.147%
     4: 9.981%
     5: 9.892%
     6: 10.034%
     7: 9.794%
     8: 9.993%
     9: 9.932%
    
    Output Analysis: FortranRNG.random_int(1, 10) => [1, 10]
    Typical Timing: 115 ± 7 ns
    Statistics of 1000 samples:
     Minimum: 1
     Median: (5, 6)
     Maximum: 10
     Mean: 5.548
     Std Deviation: 2.9476065518288537
    Distribution of 100000 samples:
     1: 9.802%
     2: 9.807%
     3: 9.975%
     4: 9.909%
     5: 10.089%
     6: 9.974%
     7: 10.056%
     8: 10.04%
     9: 10.213%
     10: 10.135%
    
    Output Analysis: FortranRNG.random_range(2, 11, 2) => [2, 10] by 2
    Typical Timing: 135 ± 25 ns
    Statistics of 1000 samples:
     Minimum: 2
     Median: 6
     Maximum: 10
     Mean: 6.024
     Std Deviation: 2.87883860466538
    Distribution of 100000 samples:
     2: 20.074%
     4: 19.829%
     6: 20.044%
     8: 19.896%
     10: 20.157%
    
    Output Analysis: FortranRNG.d(10) => [1, 10]
    Typical Timing: 100 ± 15 ns
    Statistics of 1000 samples:
     Minimum: 1
     Median: 5
     Maximum: 10
     Mean: 5.482
     Std Deviation: 2.870874068627518
    Distribution of 100000 samples:
     1: 10.057%
     2: 10.056%
     3: 10.174%
     4: 9.988%
     5: 10.058%
     6: 9.995%
     7: 9.796%
     8: 10.119%
     9: 9.956%
     10: 9.801%
    
    Output Analysis: FortranRNG.dice(3, 6) => [3, 18] ~= 10.5
    Typical Timing: 142 ± 25 ns
    Statistics of 1000 samples:
     Minimum: 3
     Median: 11
     Maximum: 18
     Mean: 10.483
     Std Deviation: 3.0071171832427406
    Distribution of 100000 samples:
     3: 0.428%
     4: 1.366%
     5: 2.836%
     6: 4.515%
     7: 6.92%
     8: 9.723%
     9: 11.44%
     10: 12.45%
     11: 12.566%
     12: 11.87%
     13: 9.612%
     14: 6.983%
     15: 4.637%
     16: 2.771%
     17: 1.359%
     18: 0.524%
    
    Output Analysis: FortranRNG.plus_or_minus(3) => [-3, 3]
    Typical Timing: 102 ± 15 ns
    Statistics of 1000 samples:
     Minimum: -3
     Median: 0
     Maximum: 3
     Mean: 0.043
     Std Deviation: 1.995277457430954
    Distribution of 100000 samples:
     -3: 14.139%
     -2: 14.284%
     -1: 14.318%
     0: 14.391%
     1: 14.27%
     2: 14.405%
     3: 14.193%
    
    Output Analysis: FortranRNG.plus_or_minus_linear(3) => [-3, 3] ~= 0
    Typical Timing: 110 ± 14 ns
    Statistics of 1000 samples:
     Minimum: -3
     Median: 0
     Maximum: 3
     Mean: 0.064
     Std Deviation: 1.5888449982387924
    Distribution of 100000 samples:
     -3: 6.369%
     -2: 12.269%
     -1: 18.903%
     0: 24.888%
     1: 18.699%
     2: 12.472%
     3: 6.4%
    
### Float Generator Tests
    Output Analysis: FortranRNG.canonical() => int(10x)[0, 10)
    Typical Timing: 85 ± 13 ns
    Statistics of 1000 samples:
     Minimum: 0.0001437314361470987
     Median: (0.47898183947610284, 0.4799430144428002)
     Maximum: 0.9986498624978831
     Mean: 0.4818263909300376
     Std Deviation: 0.28725349102428854
    <lambda> distribution of 100000:
     0: 9.885%
     1: 10.105%
     2: 10.208%
     3: 9.961%
     4: 10.137%
     5: 9.876%
     6: 9.99%
     7: 10.039%
     8: 9.939%
     9: 9.86%
    
    Output Analysis: FortranRNG.random_float(1, 10) => int[1, 10)
    Typical Timing: 131 ± 6 ns
    Statistics of 1000 samples:
     Minimum: 1.0054781442856227
     Median: (5.375957297057434, 5.376608974917234)
     Maximum: 9.990307261453857
     Mean: 5.373978282890207
     Std Deviation: 2.58681950126106
    int distribution of 100000:
     1: 11.229%
     2: 11.154%
     3: 11.153%
     4: 11.028%
     5: 11.146%
     6: 10.916%
     7: 11.117%
     8: 11.145%
     9: 11.112%
    
    Output Analysis: FortranRNG.triangular(0.0, 10.0, 5.0) => round[0, 10] ~= 5.0
    Typical Timing: 136 ± 25 ns
    Statistics of 1000 samples:
     Minimum: 0.12270967323347377
     Median: (4.97445584661811, 4.978309825559268)
     Maximum: 9.805544357972423
     Mean: 4.951977305465725
     Std Deviation: 2.0311774162488905
    round distribution of 100000:
     0: 0.491%
     1: 4.021%
     2: 7.985%
     3: 11.911%
     4: 15.995%
     5: 18.831%
     6: 16.205%
     7: 12.107%
     8: 7.991%
     9: 3.942%
     10: 0.521%
    
### ZeroCool Index Generator Tests
    Output Analysis: FortranRNG.random_index(10) => [0, 9]
    Typical Timing: 102 ± 15 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 4
     Maximum: 9
     Mean: 4.401
     Std Deviation: 2.8142706193824214
    Distribution of 100000 samples:
     0: 9.955%
     1: 10.027%
     2: 9.958%
     3: 10.076%
     4: 10.07%
     5: 10.11%
     6: 9.986%
     7: 9.828%
     8: 9.867%
     9: 10.123%
    
    Output Analysis: FortranRNG.random_index(-10) => [-10, -1]
    Typical Timing: 101 ± 9 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -5
     Maximum: -1
     Mean: -5.512
     Std Deviation: 2.858325738264627
    Distribution of 100000 samples:
     -10: 9.97%
     -9: 10.032%
     -8: 9.951%
     -7: 10.048%
     -6: 9.997%
     -5: 10.07%
     -4: 9.942%
     -3: 10.039%
     -2: 10.078%
     -1: 9.873%
    
    Output Analysis: FortranRNG.front_linear(10) => [0, 9] ~= 0
    Typical Timing: 105 ± 15 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 2
     Maximum: 9
     Mean: 2.854
     Std Deviation: 2.3156092170411755
    Distribution of 100000 samples:
     0: 18.988%
     1: 16.965%
     2: 15.236%
     3: 13.023%
     4: 10.995%
     5: 8.919%
     6: 6.902%
     7: 4.995%
     8: 3.005%
     9: 0.972%
    
    Output Analysis: FortranRNG.front_linear(-10) => [-10, -1] ~= -10
    Typical Timing: 120 ± 18 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -7
     Maximum: -1
     Mean: -7.13
     Std Deviation: 2.357256171199188
    Distribution of 100000 samples:
     -10: 18.929%
     -9: 17.261%
     -8: 14.94%
     -7: 13.062%
     -6: 11.018%
     -5: 8.969%
     -4: 6.842%
     -3: 5.002%
     -2: 2.97%
     -1: 1.007%
    
    Output Analysis: FortranRNG.middle_linear(10) => [0, 9] ~= 4.5
    Typical Timing: 121 ± 29 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 4
     Maximum: 9
     Mean: 4.435
     Std Deviation: 2.1232718345240875
    Distribution of 100000 samples:
     0: 1.98%
     1: 5.802%
     2: 10.146%
     3: 14.207%
     4: 17.938%
     5: 17.931%
     6: 13.939%
     7: 10.058%
     8: 5.994%
     9: 2.005%
    
    Output Analysis: FortranRNG.middle_linear(-10) => [-10, -1] ~= -5.5
    Typical Timing: 108 ± 11 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -6
     Maximum: -1
     Mean: -5.531
     Std Deviation: 2.082636880585854
    Distribution of 100000 samples:
     -10: 1.998%
     -9: 6.146%
     -8: 9.956%
     -7: 13.979%
     -6: 17.97%
     -5: 17.869%
     -4: 14.086%
     -3: 10.147%
     -2: 5.903%
     -1: 1.946%
    
    Output Analysis: FortranRNG.back_linear(10) => [0, 9] ~= 9
    Typical Timing: 105 ± 14 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 7
     Maximum: 9
     Mean: 6.092
     Std Deviation: 2.4090121085912664
    Distribution of 100000 samples:
     0: 0.959%
     1: 3.032%
     2: 4.994%
     3: 7.03%
     4: 8.967%
     5: 11.024%
     6: 13.018%
     7: 15.017%
     8: 17.039%
     9: 18.92%
    
    Output Analysis: FortranRNG.back_linear(-10) => [-10, -1] ~= -1
    Typical Timing: 116 ± 18 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -4
     Maximum: -1
     Mean: -3.882
     Std Deviation: 2.317206388185016
    Distribution of 100000 samples:
     -10: 1.013%
     -9: 3.004%
     -8: 5.017%
     -7: 6.971%
     -6: 9.024%
     -5: 10.986%
     -4: 12.961%
     -3: 15.077%
     -2: 17.031%
     -1: 18.916%
    
    Output Analysis: FortranRNG.quantum_linear(10) => [0, 9] ~= 4.5
    Typical Timing: 116 ± 12 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 5
     Maximum: 9
     Mean: 4.593
     Std Deviation: 2.621874372510099
    Distribution of 100000 samples:
     0: 7.394%
     1: 8.62%
     2: 9.923%
     3: 11.391%
     4: 12.579%
     5: 12.563%
     6: 11.283%
     7: 10.122%
     8: 8.83%
     9: 7.295%
    
    Output Analysis: FortranRNG.quantum_linear(-10) => [-10, -1] ~= -5.5
    Typical Timing: 148 ± 35 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -6
     Maximum: -1
     Mean: -5.557
     Std Deviation: 2.6592899095102105
    Distribution of 100000 samples:
     -10: 7.469%
     -9: 8.623%
     -8: 10.177%
     -7: 11.05%
     -6: 12.61%
     -5: 12.731%
     -4: 11.473%
     -3: 9.951%
     -2: 8.553%
     -1: 7.363%
