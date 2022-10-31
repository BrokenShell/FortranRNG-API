## FortranRNG Test Suite

### Boolean Generator Tests
    Output Analysis: FortranRNG.percent_true(33.333) => bool[True, False] : True ~= 33.333%
    Typical Timing: 104 ± 12 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 0
     Maximum: 1
     Mean: 0.341
     Std Deviation: 0.4742825570732535
    bool distribution of 100000:
     False: 66.314%
     True: 33.686%

### Integer Generator Tests
    Output Analysis: FortranRNG.random_below(10) => [0, 10)
    Typical Timing: 104 ± 10 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 5
     Maximum: 9
     Mean: 4.545
     Std Deviation: 2.833726346174769
    Distribution of 100000 samples:
     0: 9.862%
     1: 9.971%
     2: 9.994%
     3: 9.998%
     4: 9.968%
     5: 10.155%
     6: 10.1%
     7: 9.829%
     8: 10.083%
     9: 10.04%
    
    Output Analysis: FortranRNG.random_int(1, 10) => [1, 10]
    Typical Timing: 116 ± 8 ns
    Statistics of 1000 samples:
     Minimum: 1
     Median: (5, 6)
     Maximum: 10
     Mean: 5.523
     Std Deviation: 2.8767597652127206
    Distribution of 100000 samples:
     1: 10.174%
     2: 9.989%
     3: 9.988%
     4: 9.958%
     5: 9.938%
     6: 9.964%
     7: 9.821%
     8: 9.979%
     9: 10.169%
     10: 10.02%
    
    Output Analysis: FortranRNG.random_range(2, 11, 2) => [2, 10] by 2
    Typical Timing: 138 ± 26 ns
    Statistics of 1000 samples:
     Minimum: 2
     Median: 6
     Maximum: 10
     Mean: 6.106
     Std Deviation: 2.8832407247881813
    Distribution of 100000 samples:
     2: 20.156%
     4: 19.835%
     6: 20.047%
     8: 20.147%
     10: 19.815%
    
    Output Analysis: FortranRNG.d(10) => [1, 10]
    Typical Timing: 105 ± 22 ns
    Statistics of 1000 samples:
     Minimum: 1
     Median: 5
     Maximum: 10
     Mean: 5.442
     Std Deviation: 2.8797445943918234
    Distribution of 100000 samples:
     1: 9.984%
     2: 10.006%
     3: 10.234%
     4: 9.888%
     5: 10.015%
     6: 9.91%
     7: 10.034%
     8: 9.949%
     9: 9.982%
     10: 9.998%
    
    Output Analysis: FortranRNG.dice(3, 6) => [3, 18] ~= 10.5
    Typical Timing: 135 ± 19 ns
    Statistics of 1000 samples:
     Minimum: 3
     Median: 11
     Maximum: 18
     Mean: 10.656
     Std Deviation: 2.9227052889756444
    Distribution of 100000 samples:
     3: 0.469%
     4: 1.368%
     5: 2.713%
     6: 4.599%
     7: 7.054%
     8: 9.743%
     9: 11.497%
     10: 12.5%
     11: 12.541%
     12: 11.601%
     13: 9.615%
     14: 6.948%
     15: 4.589%
     16: 2.852%
     17: 1.429%
     18: 0.482%
    
    Output Analysis: FortranRNG.plus_or_minus(3) => [-3, 3]
    Typical Timing: 107 ± 20 ns
    Statistics of 1000 samples:
     Minimum: -3
     Median: 0
     Maximum: 3
     Mean: 0.077
     Std Deviation: 1.9700131857304792
    Distribution of 100000 samples:
     -3: 14.085%
     -2: 14.207%
     -1: 14.419%
     0: 14.274%
     1: 14.351%
     2: 14.205%
     3: 14.459%
    
    Output Analysis: FortranRNG.plus_or_minus_linear(3) => [-3, 3] ~= 0
    Typical Timing: 115 ± 20 ns
    Statistics of 1000 samples:
     Minimum: -3
     Median: 0
     Maximum: 3
     Mean: -0.045
     Std Deviation: 1.5222655130732918
    Distribution of 100000 samples:
     -3: 6.163%
     -2: 12.387%
     -1: 19.114%
     0: 24.901%
     1: 18.671%
     2: 12.567%
     3: 6.197%
    
    Float Generator Tests
    Output Analysis: FortranRNG.canonical() => int(10x)[0, 10)
    Typical Timing: 91 ± 20 ns
    Statistics of 1000 samples:
     Minimum: 0.0014969969873245281
     Median: (0.48528149642584184, 0.4854366308772783)
     Maximum: 0.9965887397190528
     Mean: 0.4872161136667753
     Std Deviation: 0.2842012577946864
    <lambda> distribution of 100000:
     0: 10.077%
     1: 10.07%
     2: 9.967%
     3: 9.974%
     4: 10.065%
     5: 9.922%
     6: 10.102%
     7: 9.931%
     8: 9.876%
     9: 10.016%
    
    Output Analysis: FortranRNG.random_float(1, 10) => int[1, 10)
    Typical Timing: 143 ± 17 ns
    Statistics of 1000 samples:
     Minimum: 1.0377889034493215
     Median: (5.629063080755491, 5.67459483182971)
     Maximum: 9.99893034047167
     Mean: 5.5782516333088425
     Std Deviation: 2.6320386155546687
    int distribution of 100000:
     1: 11.212%
     2: 11.184%
     3: 11.227%
     4: 11.174%
     5: 11.127%
     6: 10.89%
     7: 11.146%
     8: 10.967%
     9: 11.073%
    
    Output Analysis: FortranRNG.triangular(0.0, 10.0, 5.0) => round[0, 10] ~= 5.0
    Typical Timing: 130 ± 15 ns
    Statistics of 1000 samples:
     Minimum: 0.20004448119171003
     Median: (5.031128300624697, 5.03121842785121)
     Maximum: 9.589481911391328
     Mean: 4.940095055708186
     Std Deviation: 2.0250267128310027
    round distribution of 100000:
     0: 0.542%
     1: 3.943%
     2: 7.935%
     3: 11.937%
     4: 16.095%
     5: 18.868%
     6: 16.181%
     7: 11.866%
     8: 8.079%
     9: 4.034%
     10: 0.52%

### ZeroCool Index Generator Tests
    Output Analysis: FortranRNG.random_index(10) => [0, 9]
    Typical Timing: 113 ± 25 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 4
     Maximum: 9
     Mean: 4.465
     Std Deviation: 2.8804638640455242
    Distribution of 100000 samples:
     0: 10.0%
     1: 10.053%
     2: 9.888%
     3: 9.893%
     4: 10.001%
     5: 9.893%
     6: 10.077%
     7: 10.137%
     8: 9.924%
     9: 10.134%
    
    Output Analysis: FortranRNG.random_index(-10) => [-10, -1]
    Typical Timing: 111 ± 17 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -5
     Maximum: -1
     Mean: -5.497
     Std Deviation: 2.8541438536165513
    Distribution of 100000 samples:
     -10: 10.002%
     -9: 10.044%
     -8: 10.137%
     -7: 10.145%
     -6: 9.984%
     -5: 9.846%
     -4: 9.89%
     -3: 10.001%
     -2: 9.92%
     -1: 10.031%
    
    Output Analysis: FortranRNG.front_linear(10) => [0, 9] ~= 0
    Typical Timing: 117 ± 24 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 2
     Maximum: 9
     Mean: 2.877
     Std Deviation: 2.3162979592954436
    Distribution of 100000 samples:
     0: 19.02%
     1: 17.09%
     2: 14.887%
     3: 12.958%
     4: 10.941%
     5: 8.948%
     6: 7.008%
     7: 4.994%
     8: 3.122%
     9: 1.032%
    
    Output Analysis: FortranRNG.front_linear(-10) => [-10, -1] ~= -10
    Typical Timing: 118 ± 14 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -8
     Maximum: -1
     Mean: -7.043
     Std Deviation: 2.4312675833939097
    Distribution of 100000 samples:
     -10: 18.839%
     -9: 17.161%
     -8: 15.002%
     -7: 12.991%
     -6: 10.965%
     -5: 9.116%
     -4: 7.003%
     -3: 4.897%
     -2: 3.052%
     -1: 0.974%
    
    Output Analysis: FortranRNG.back_linear(10) => [0, 9] ~= 9
    Typical Timing: 110 ± 18 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 6
     Maximum: 9
     Mean: 6.091
     Std Deviation: 2.3609941324139907
    Distribution of 100000 samples:
     0: 1.004%
     1: 2.973%
     2: 5.009%
     3: 7.007%
     4: 9.105%
     5: 11.062%
     6: 12.948%
     7: 14.737%
     8: 17.124%
     9: 19.031%
    
    Output Analysis: FortranRNG.back_linear(-10) => [-10, -1] ~= -1
    Typical Timing: 111 ± 13 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -3
     Maximum: -1
     Mean: -3.852
     Std Deviation: 2.364251612177876
    Distribution of 100000 samples:
     -10: 1.007%
     -9: 2.918%
     -8: 4.98%
     -7: 7.01%
     -6: 8.972%
     -5: 11.067%
     -4: 12.933%
     -3: 14.997%
     -2: 17.089%
     -1: 19.027%
    
    Output Analysis: FortranRNG.middle_linear(10) => [0, 9] ~= 4.5
    Typical Timing: 115 ± 22 ns
    Statistics of 1000 samples:
     Minimum: 0
     Median: 5
     Maximum: 9
     Mean: 4.52
     Std Deviation: 2.0933184139021903
    Distribution of 100000 samples:
     0: 1.956%
     1: 6.053%
     2: 9.918%
     3: 14.028%
     4: 18.086%
     5: 18.176%
     6: 13.915%
     7: 10.028%
     8: 5.889%
     9: 1.951%
    
    Output Analysis: FortranRNG.middle_linear(-10) => [-10, -1] ~= -5.5
    Typical Timing: 120 ± 23 ns
    Statistics of 1000 samples:
     Minimum: -10
     Median: -5
     Maximum: -1
     Mean: -5.448
     Std Deviation: 2.0764410917740017
    Distribution of 100000 samples:
     -10: 1.937%
     -9: 6.053%
     -8: 9.884%
     -7: 14.171%
     -6: 17.986%
     -5: 17.919%
     -4: 14.166%
     -3: 9.988%
     -2: 5.959%
     -1: 1.937%
