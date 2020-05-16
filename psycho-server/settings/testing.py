from .common import *

DEBUG = False
PRODUCTION = False
TESTING = True

HOSTNAME = os.environ.get('SERVER_NAME', '')

SECRET_KEY = 'odev4$y_1l_wc-6r95uqi_ig!dpj5)vpa)s)&w0%lpx6mwwp7l'

ALLOWED_HOSTS = ['*']

MEDIA_ROOT = os.path.join(BASE_DIR, 'test-media/')

PROTOCOL = 'http://'

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TEST_DB_NAME', 'psycho'),
        'USER': os.environ.get('TEST_DB_USERNAME', 'postgres'),
        'PASSWORD': os.environ.get('TEST_DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('TEST_DB_HOST', 'db'),
        'PORT': os.environ.get('TEST_DB_PORT', '5432'),
    }
}
