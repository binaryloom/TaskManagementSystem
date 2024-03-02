FROM nikolaik/python-nodejs:python3.10-nodejs20-bullseye


LABEL maintainer="write2shourov@gmail.com" \
    vendor="fiery.snowflake"

WORKDIR /src

RUN python3 -m pip install --upgrade --force-reinstall pip && python3 -m pip install pipenv

COPY ./Pipfile .
RUN pipenv lock && pipenv install --system --deploy

COPY ./src .

COPY start_django.sh /start_django.sh
RUN chmod +x /start_django.sh

RUN mkdir -p /src/tailwind_theme/static

ENTRYPOINT "/start_django.sh"