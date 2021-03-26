#!/bin/sh

set -e

python3.8 manage.py collectstatic --noinput --settings=libStash.settings.production 
python3.8 manage.py makemigrations --settings=libStash.settings.production 
python3.8 manage.py migrate --settings=libStash.settings.production

gunicorn libStash.wsgi:application --bind 0.0.0.0:$PORT
