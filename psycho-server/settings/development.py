from .common import *

DEBUG = True
PRODUCTION = False

HOSTNAME = 'localhost'

SECRET_KEY = 'odev4$y_1l_wc-6r95uqi_ig!dpj5)vpa)s)&w0%lpx6mwwp7l'

ALLOWED_HOSTS = ['*']

PROTOCOL = 'http://'

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
