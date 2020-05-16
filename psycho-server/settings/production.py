from .common import *

DEBUG = False
PRODUCTION = True

HOSTNAME = os.environ.get('SERVER_NAME', '')

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
