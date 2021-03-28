import os

import dj_database_url
from decouple import config

from libStash.settings.base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = 0

ALLOWED_HOSTS = ["libstash.herokuapp.com"]


DATABASES = {"default": {}}

DATABASE_URL = os.environ.get("DATABASE_URL")
db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True
)
DATABASES["default"].update(db_from_env)

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_CONTENT_TYPE_NOSNIFF = True

ADMINS = [("Aremu", "kingremzy1407@gmail.com")]
