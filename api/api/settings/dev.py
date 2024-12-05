# Development settings
from .base import *

"""
Development Settings
"""

import environ
from pathlib import Path

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env.dev'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env('DEBUG')

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

# ALLOWED_HOSTS = [
#     'localhost:3000'
# ]

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000'
# ]

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(' ')
CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST').split(' ')

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': env.db(),

    'extra': env.db_url(
        'SQLITE_URL',
        default='sqlite:////db.sqlite3'
    )
}

# DATABASES = {
#     'default': {
#         "ENGINE": env("DB_ENGINE"),
#         "NAME": env("DB_DATABASE"),
#         "USER": env("DB_USER"),
#         "PASSWORD": env("DB_PASSWORD"),
#         "HOST": env("DB_HOST"),
#         "PORT": env("DB_PORT"),
#     },

#     'extra': env.db_url(
#         'SQLITE_URL',
#         default='sqlite:////db.sqlite3'
#     )
# }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SMS_BACKEND = 'sms.backends.console.SmsBackend'