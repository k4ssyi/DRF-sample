from application.settings.base import *

DEBUG = True

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        'django_extensions'
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
