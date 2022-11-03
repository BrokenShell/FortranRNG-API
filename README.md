## FortranRNG for Python API

### Repository & Documentation
- [API on GitHub](https://github.com/BrokenShell/FortranRNG-API)
- [General Documentation](https://github.com/BrokenShell/FortranRNG-API/blob/main/README.md)
- [Developer Notes](https://github.com/BrokenShell/FortranRNG-API/blob/main/NOTES.md)
- [FortranRNG on PyPi](https://pypi.org/project/FortranRNG)

### API Tech Stack
- Host Logic: Python3.7
- Web Framework: FastAPI
- Performance & Test Suite: MonkeyScope
- Engine Logic: Fortran90 compiled for Python
- Random Engine: FortranRNG.f90
- DevOps: Shell Scripts
- Server: Uvicorn on NGINX
- Platform: Amazon Linux in Docker
- Hosting: AWS Elastic Beanstalk

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

#### ZeroCool Index Generators
- `random_index(limit: int) -> int`
- `front_linear(limit: int) -> int`
- `middle_linear(limit: int) -> int`
- `back_linear(limit: int) -> int`
- `quantum_linear(limit: int) -> int`
