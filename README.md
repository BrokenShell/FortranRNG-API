## FortranRNG for Python API

### Tech Stack
- FastAPI
- FortranRNG
- Python3
- Fortran
- Amazon Linux
- Docker

### Random Generator Features

#### Random Boolean Generators
- `percent_true(percent: float) -> bool`

#### Random Integer Generators
- `d(sides: int) -> int`
- `dice(rolls: int, sides: int) -> int`
- `random_below(limit: int) -> int`
- `random_integer(low: int, high: int) -> int`
- `random_range(start: int, stop: int, step: int) -> int`
- `plus_or_minus(amount: int) -> int`
- `plus_or_minus_linear(amount: int) -> int`

#### Random Float Generators
- `canonical() -> float`
- `random_float(low: float, high: float) -> float`
- `triangular(low: float, high: float, mode: float) -> float`
