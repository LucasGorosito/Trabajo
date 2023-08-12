from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Base_De_Datos',
        'USER': 'postgres',
		'PASSWORD': 'lucasgorosito',
		'HOST': 'localhost',
		'PORT': '5432',
        }
}
