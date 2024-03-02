#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py init_superuser
python manage.py runserver 0.0.0.0:80 --settings tms.settings_prod
