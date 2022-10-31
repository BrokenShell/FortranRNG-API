# FortranRNG
## Fortran RNG for Python3

### PyPi Installation
```shell
python3 -m pip install FortranRNG
```

### Source Installation
```shell
python3 -m pip install ./FortranRNG
```

### FortranRNG Interface
- `FortranRNG.canonical() -> float`
- `FortranRNG.random_below(limit: int) -> int`
- `FortranRNG.random_int(low: int, high: int) -> int`
- `FortranRNG.random_range(start: int, stop: int, step: int) -> int`
- `FortranRNG.d(sides: int) -> int`
- `FortranRNG.dice(rolls: int, sides: int) -> int`
- `FortranRNG.percent_true(percent: float) -> bool(int)`
- `FortranRNG.triangular(low: float, high: float, mode: float) -> float`
- `FortranRNG.plus_or_minus(amount: int) -> int`
- `FortranRNG.plus_or_minus_linear(amount: int) -> int`
