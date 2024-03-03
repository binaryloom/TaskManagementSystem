FROM nikolaik/python-nodejs:python3.10-nodejs20-bullseye

WORKDIR /src

RUN python3 -m pip install --upgrade --force-reinstall pip && python3 -m pip install pipenv

COPY ./Pipfile .
RUN pipenv lock && pipenv install --system --deploy

COPY ./src .

COPY start_django.sh /start_django.sh
RUN chmod +x /start_django.sh

RUN mkdir -p /src/tailwind_theme/static

RUN python manage.py tailwind install --settings tms.settings_prod
RUN python manage.py tailwind build --settings tms.settings_prod
RUN python manage.py collectstatic --noinput --settings tms.settings_prod

ENTRYPOINT "/start_django.sh"