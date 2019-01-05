#!/bin/sh
source venv/bin/activate
# flask db upgrade
# flask translate compile
exec gunicorn -b :5000 --reload --access-logfile - --error-logfile - pyrello:app