#!/bin/sh

cd /app

python3.6 manage.py collectstatic --noinput

python3.6 manage.py migrate

python3.6 manage.py loaddata default_fixtures/*.json

uwsgi /uwsgi.ini
