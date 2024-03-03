from os import environ

from .settings import *

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

NPM_BIN_PATH = "/usr/local/bin/npm"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": environ["POSTGRES_DB"],
        "USER": environ["CACHE_HOST"],
        "PASSWORD": environ["CACHE_HOST"],
        "HOST": environ["CACHE_HOST"],
        "PORT": "5432",
    }
}
