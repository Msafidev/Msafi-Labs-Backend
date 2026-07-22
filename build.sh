#!/usr/bin/env bash
# Render build script. In the Render dashboard, set:
#   Build Command: ./build.sh
#   Start Command: gunicorn core.wsgi:application   (or leave blank to use the Procfile)
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
