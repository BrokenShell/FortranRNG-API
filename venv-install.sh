python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt --no-cache-dir
python -m pip install ./FortranRNG
rm -rf ./FortranRNG/build
rm -rf ./FortranRNG/FortranRNG.egg-info
