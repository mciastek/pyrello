#!/bin/sh
source venv/bin/activate

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

exec gunicorn -w 2 -b :5000 --reload --access-logfile - --error-logfile - manage:app