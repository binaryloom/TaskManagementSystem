FROM python:3.10-bullseye

LABEL maintainer="write2shourov@gmail.com" \
    vendor="fiery.snowflake"

WORKDIR /src

RUN python3 -m pip install --upgrade --force-reinstall pip && python3 -m pip install pipenv

COPY Pipfile .
# RUN pipenv lock && pipenv install --system --deploy
RUN pipenv sync

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80", "--settings", "versity_info.settings.production" ]