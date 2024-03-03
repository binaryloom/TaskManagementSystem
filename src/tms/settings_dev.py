from .settings import *

DEBUG = True
NPM_BIN_PATH = "npm.cmd"

INSTALLED_APPS = INSTALLED_APPS + ["django_browser_reload"]


MIDDLEWARE = MIDDLEWARE + [
    # browser reload middleware for dev
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
