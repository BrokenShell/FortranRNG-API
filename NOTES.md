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
