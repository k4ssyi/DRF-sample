import environ

env = environ.Env()

READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=False)
if READ_ENV_FILE is True:
    env.read_env('.env')
    if env('DJANGO_ENV') == 'production':
        from application.settings.production import *
    else:
        # ローカル環境
        from application.settings.local import *
