# FortranRNG API Developer Notes
To run the API locally you have two options: 1. Virtual environment or 2. Docker image. You do not need both. Handy shell scripts for both strategies are included for *nix environments.

## 1. Local Virtual Environment
Rebuilding is only required if changes are made to `/FortranRNG` or `requirements.txt`.

### Build API: Virtual Environment `./venv-build.sh`
This assumes a virtual environment is active. The virtual environment used in testing is `venv` but feel free to use whatever you like. The build and run scripts may not work with all virtual environments without alteration. Season to taste.

```shell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m pip install ./FortranRNG
rm -rf ./FortranRNG/build
rm -rf ./FortranRNG/FortranRNG.egg-info
```

### Run API: Virtual Environment `./venv-run.sh`
Assumes port 8000 is available on localhost.
```shell
python -m uvicorn app.api:API --host=0.0.0.0 --port=8000
```
Restart the server if any minor changes are made to local files, or add the `--reload` flag to the above script to restart the server automatically when changes are made. This works for detecting change in Python files only.

## 2. Local Docker Environment
Rebuilding docker is required for any changes made locally.

### Build API: Docker Image `./docker-build.sh`
Assumes Docker Desktop is running in the background.
```shell
docker build . -t fortran-rng-api
```

### Run API: Docker Image `./docker-run.sh`
Assumes port 8000 is available on localhost.
```shell
docker run -it -p 8000:8000 fortran-rng-api
```

---
## FortranRNG API Developer Log
### FortranRNG API v1.0.6
- Bug fix: dice (reset tmp var each iteration)

### FortranRNG API v1.0.5
- Minor cleanup

### FortranRNG API v1.0.4
- Updates documentation

### FortranRNG API v1.0.3
- Updates documentation

### FortranRNG API v1.0.2
- Updates documentation

### FortranRNG API v1.0.1
- Adds LICENSE (Free for non-commercial use)
- Updates documentation

### FortranRNG API v1.0.0
- First Release Candidate
- Updates build and run scripts

### FortranRNG API v0.1.1
- Adds links to repo & docs
- Updates documentation

### FortranRNG API v0.1.0
- Adds ZeroCool algorithms: `middle_linear` and `quantum_linear`
- Updates test suite to include new algorithms

### FortranRNG API v0.0.9
- Adds ZeroCool algorithms: `random_index`, `front_linear` and `back_linear`

### FortranRNG API v0.0.8
- Updates test suite format

### FortranRNG API v0.0.7
- Moves developer log to `/NOTES.md`

### FortranRNG API v0.0.6
- Fixes random typos

### FortranRNG API v0.0.5
- Updates documentation
- Fixes a few minor typos

### FortranRNG API v0.0.4
- Adds development log
- Updates documentation
- Renames shell script to lesson confusion

### FortranRNG API v0.0.3
- Fixes name conflict `random_int` => `random_integer`

### FortranRNG API v0.0.2
- Adds `percent_true`, `plus_or_minus` and `plus_or_minus_linear`

### FortranRNG API v0.0.1
- Basic Functionality

---
## Future Plans
- Random Array
- Random Matrix
- Linear Algebra
- Abstract Algebra
- Category Theory
- Lambda Calculus
- Theory of Everything
