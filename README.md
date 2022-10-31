## FortranRNG for Python API

### Tech Stack
- FastAPI
- FortranRNG
- Python3
- Fortran
- Amazon Linux
- Docker

### Random Generator Features

#### Random Boolean
- `percent_true(percent: float) -> bool`

#### Random Integer
- `d(sides: int) -> int`
- `dice(rolls: int, sides: int) -> int`
- `random_below(limit: int) -> int`
- `random_integer(low: int, high: int) -> int`
- `random_range(start: int, stop: int, step: int) -> int`
- `plus_or_minus(amount: int) -> int`
- `plus_or_minus_linear(amount: int -> int)`

#### Random Float
- `canonical() -> float`
- `random_float(low: float, high: float) -> float`
- `triangular(low: float, high: float, mode: float) -> float`

### Development Log
#### FortranRNG API v0.0.6
- Fixes random typos

#### FortranRNG API v0.0.5
- Updates documentation
- Fixes a few minor typos
- Adds test suite `/tests/main.py`

#### FortranRNG API v0.0.4
- Adds development log
- Updates documentation
- Renames shell script to lesson confusion

#### FortranRNG API v0.0.3
- Fixes name conflict `random_int` => `random_integer`
- FortranRNG Release v1.1.1

#### FortranRNG API v0.0.2
- Adds `percent_true`, `plus_or_minus` & `plus_or_minus_linear`
- FortranRNG Beta v0.1.1

#### FortranRNG API v0.0.1
- Basic Functionality
- FortranRNG Alpha v0.0.1
