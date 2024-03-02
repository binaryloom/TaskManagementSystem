#!/bin/sh
echo -e "Strating django task management Server"
python manage.py tailwind build
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py init_superuser
# python manage.py runserver 0.0.0.0:80 --settings tms.settings_prod
gunicorn tms.wsgi:application --bind 0.0.0.0:80 --workers 4
