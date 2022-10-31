## FortranRNG API

### Tech Stack
- FortranRNG
- FastAPI
- Python 3.7
- Fortran 90
- Amazon Linux 2
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

### Build API Docker Image Locally
```shell
docker build . -t fortran-rng
```

### Run API Docker Image Locally
```shell
docker run -it -p 8000:8000 fortran-rng
```
