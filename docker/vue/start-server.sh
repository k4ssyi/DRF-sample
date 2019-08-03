#!/bin/sh

cd /code/application/frontend

yarn cache clear --force
yarn install

if [ "${DJANGO_ENV}" = 'production' ]; then
    /bin/sh
else
    yarn serve --port 3000
fi
