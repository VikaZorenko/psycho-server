import dj_database_url

from .common import *

DEBUG = False
PRODUCTION = True

HOSTNAME = os.environ.get('SERVER_NAME', '')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'odev4$y_1l_wc-6r95uqi_ig!dpj5)vpa)s)&w0%lpx6mwwp7l')

ALLOWED_HOSTS = ['*']

PROTOCOL = 'https://'

# Database
DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'psycho'),
        'USER': os.environ.get('DB_USERNAME', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Heroku: Update database configuration from $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
