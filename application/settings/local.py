from application.settings.base import *

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DEBUG = True

if DEBUG:
    INTERNAL_IPS = env('ALLOWED_HOSTS')

    INSTALLED_APPS += (
        'corsheaders',
        'debug_toolbar',
        'django_extensions'
    )
    MIDDLEWARE += (
        'corsheaders.middleware.CorsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
        'http://0.0.0.0:3000',
        'http://127.0.0.1:3000',
        'http://172.18.0.1:3000',
    )
