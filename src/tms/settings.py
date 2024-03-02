from os import mkdir, path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEV_DIR = Path(path.join(BASE_DIR, "dev_junk"))

if not path.exists(DEV_DIR):
    mkdir(DEV_DIR)


SECRET_KEY = "django-insecure-_3815k(6u9$9d4a)ps=-b^^8w!jp!xn^z5ex0**ry53)oo$s-s"

# DEBUG = True
MANAGE_DATABASE = True
DEFAULT_PERMISSIONS = True
ENABLE_ADMIN = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # custom app
    "tms",
    "user",
    "abstract",
    "task_management",
    # 3rd party app
    "rest_framework",
    "rest_framework.authtoken",
    "rest_registration",
    "tailwind",
    "tailwind_theme",
    "django_browser_reload",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Custom middleware
    "abstract.middleware.InjectUserObj",
    # browser reload middleware for dev
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


ROOT_URLCONF = "tms.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            path.join(Path(__file__).resolve().parent.parent, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "abstract.processors.meta_processor",
                "abstract.processors.breadcrumb",
            ],
        },
    },
]

WSGI_APPLICATION = "tms.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DEV_DIR / "dev_db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# custom configs for user & bulk import
AUTH_USER_MODEL = "user.User"
FIXTURE_DIRS = [Path(path.join(BASE_DIR, "fixtures"))]

# Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.DjangoModelPermissions"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 12,
}
# Login redirect url
# LOGIN_REDIRECT_URL = "/api"


REST_REGISTRATION = {
    "REGISTER_VERIFICATION_ENABLED": False,
    "REGISTER_EMAIL_VERIFICATION_ENABLED": False,
    "RESET_PASSWORD_VERIFICATION_ENABLED": False,
}


# Tailwind Config

TAILWIND_APP_NAME = "tailwind_theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = "npm.cmd"


# Logout

LOGOUT_REDIRECT_URL = "user:login_view"

LOGIN_REDIRECT_URL = "user:dashboard_view"


# Admin Setup

ADMINS = {
    "default": {
        "USER": "admin",
        "PASSWORD": "password",
        "EMAIL": "extinctCoder@outlook.com",
    }
}


# static Files Config
STATIC_ROOT = BASE_DIR / "static_files"
