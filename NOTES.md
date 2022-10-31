# FortranRNG Developer Notes
To run the API locally you two choices: local virtual environment or Docker. Shell scripts are included for *nix environments.

## Local Virtual Environments

### Install Virtual Environment `./venv-install.sh`
Assumes venv is built and active.
```shell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m pip install ./FortranRNG
rm -rf ./FortranRNG/build
rm -rf ./FortranRNG/FortranRNG.egg-info
```

### Run Virtual Environment `./venv-run.sh`
```shell
python -m uvicorn app.api:API --host=0.0.0.0 --port=8000
```

## Local Docker Environments

### Build Docker Image Locally `./docker-build.sh`
Assumes Docker Desktop is running in the background.
```shell
docker build . -t fortran-rng
```

### Run Docker Image Locally `./docker-run.sh`
Assumes port 8000 is available on localhost.
```shell
docker run -it -p 8000:8000 fortran-rng
```

---
## FortranRNG Developer Log
### FortranRNG API v0.0.9
- Adds ZeroCool algorithms: `random_index`, `front_linear` and `back_linear`
- FortranRNG Release v1.1.2
- Updates test suite to include ZeroCool algorithms

### FortranRNG API v0.0.8
- Updates test suite format

### FortranRNG API v0.0.7
- Moves developer log to `/NOTES.md`

### FortranRNG API v0.0.6
- Fixes random typos

### FortranRNG API v0.0.5
- Updates documentation
- Fixes a few minor typos
- Adds test suite `/tests/main.py`

### FortranRNG API v0.0.4
- Adds development log
- Updates documentation
- Renames shell script to lesson confusion

### FortranRNG API v0.0.3
- Fixes name conflict `random_int` => `random_integer`
- FortranRNG Release v1.1.1

### FortranRNG API v0.0.2
- Adds `percent_true`, `plus_or_minus` and `plus_or_minus_linear`
- FortranRNG Beta v0.1.1

### FortranRNG API v0.0.1
- Basic Functionality
- FortranRNG Alpha v0.0.1
