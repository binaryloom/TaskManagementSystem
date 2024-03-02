#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations
python3 manage.py migrate
python manage.py initadmin
