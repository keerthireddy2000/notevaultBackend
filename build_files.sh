#!/bin/bash
# Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install --no-dev -r requirements.txt


# Collect static files
python3 manage.py collectstatic --noinput
