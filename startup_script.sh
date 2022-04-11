#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development

python3 -m venv app-env
source app-env/bin/activate
pip install --upgrade pip
pip flask==2.0.3

flask run 
./startup_script.sh