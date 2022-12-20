# Pyserver
## Project Description:
is a monolothic Python Server designed to perform many backend tasks.

## Requirements:
- Python version 3.7.2 (virtual environment)
- pip version <= 22.3.1

# Local Installation:
## Create a virtualenv using venv (from project root):
```
python3 -m venv <virtual env name>
```
example, where venv is virtual env name:
```
python3 -m venv venv
```
### How to activate the virtual environment, venv:
```
. venv/bin/activate
```
### How to deactivate virtual environment:
```
deactivate
```

## Install Flask
```
pip install Flask
```

### After you initialize virtual env, install dependencies: 
```
pip install -r requirements.txt
```
#### to freeze into file (requirements.txt):
```
pip freeze > requirements.txt
```

## Run local server on port :5000, cd to root:
```
python3 web_server.py
```



