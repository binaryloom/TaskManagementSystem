#!/bin/sh

echo "Strating django task management Server"
python manage.py makemigrations --settings tms.settings_prod
python manage.py migrate --settings tms.settings_prod
python manage.py init_superuser --settings tms.settings_prod
gunicorn tms.wsgi:application --bind 0.0.0.0:80 --workers 5
