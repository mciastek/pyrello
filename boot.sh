#!/bin/sh
source venv/bin/activate
# flask db upgrade
# flask translate compile
exec gunicorn -w 2 -b :5000 --reload --access-logfile - --error-logfile - pyrello:app