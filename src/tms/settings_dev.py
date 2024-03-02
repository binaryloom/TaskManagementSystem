from .settings import *

DEBUG = True


INSTALLED_APPS = INSTALLED_APPS + ["django_browser_reload"]


MIDDLEWARE = MIDDLEWARE + [
    # browser reload middleware for dev
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
