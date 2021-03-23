import os
import dj_database_url
from decouple import config
from libStash.settings.base import *

SECRET_KEY = config("PROD_SECRET_KEY")

DEBUG = 0

ALLOWED_HOSTS = ["libstash"]


DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

DATABASE_URL = os.environ.get("DATABASE_URL")
db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True
)
DATABASES["default"].update(db_from_env)

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

CONN_MAX_AGE = 60 * 60

ADMINS = [("Aremu", "kingremzy1407@gmail.com")]

MIDDLEWARE += "django.middleware.common.BrokenLinkEmailsMiddleware"
