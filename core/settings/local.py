from decouple import config
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = config('ALLOWED_HOSTS')

if not DEBUG:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '<db_name>',
            'USER': '<db_username>',
            'PASSWORD': '<password>',
            'HOST': '<db_hostname_or_ip>',
            'PORT': '<db_port>',
        }
    }
