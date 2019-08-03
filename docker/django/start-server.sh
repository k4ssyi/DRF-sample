#!/bin/sh

source .venv/bin/activate
poetry install

if [ "${DJANGO_ENV}" = 'production' ]; then
    sleep 5
    python manage.py migrate
    python manage.py collectstatic --noinput
    gunicorn config.wsgi:application -c /var/app/etc/gunicorn.conf
else
    python manage.py migrate --settings application.settings.local
    python manage.py runserver 0.0.0.0:8000 --settings application.settings.local
fi
