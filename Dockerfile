FROM python:3.10-bullseye

LABEL maintainer="write2shourov@gmail.com" \
    vendor="fiery.snowflake"

RUN apt install -y node npm

WORKDIR /src

RUN python3 -m pip install --upgrade --force-reinstall pip && python3 -m pip install pipenv

COPY ./Pipfile .
RUN pipenv lock && pipenv install --system --deploy

COPY ./src .

COPY start_django.sh /start_django.sh
RUN chmod +x /start_django.sh

ENTRYPOINT "/start_django.sh"








