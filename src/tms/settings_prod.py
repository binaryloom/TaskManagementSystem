from os import environ

from .settings import *

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

NPM_BIN_PATH = "/usr/local/bin/npm"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": environ["APP_DB_DATABASE"],
        "USER": environ["APP_DB_USER"],
        "PASSWORD": environ["APP_DB_PASSWORD"],
        "HOST": environ["APP_DB_HOST"],
        "PORT": "5432",
    }
}
