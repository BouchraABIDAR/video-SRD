#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development

python3 -m venv app-env
source app-env/bin/activate
pip install --upgrade pip
pip install flask==2.0.3 
pip install flask_sqlalchemy

flask run