FROM node:20 AS tailwind_builder
FROM python:3.10-bullseye

LABEL maintainer="write2shourov@gmail.com" \
    vendor="Sabbir Ahmed Shourov"

COPY --from=tailwind_builder /usr/local/bin/node /usr/local/bin/node
COPY --from=tailwind_builder /usr/local/bin/npm /usr/local/bin/npm

ENV PATH="/usr/local/bin:${PATH}"

WORKDIR /src

RUN python3 -m pip install --upgrade --force-reinstall pip && python3 -m pip install pipenv

COPY ./Pipfile .
RUN pipenv lock && pipenv install --system --deploy

COPY ./src .

COPY start_django.sh /start_django.sh
RUN chmod +x /start_django.sh

ENTRYPOINT "/start_django.sh"




