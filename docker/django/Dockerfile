FROM python:alpine
LABEL maintainer "k4ssyi <hogehoge@example.co.jp>"

RUN apk --no-cache add gcc libc-dev libxml2-dev libxslt-dev vim

WORKDIR /code

ENV DJANGO_READ_ENV_FILE=True

# Using pip:
RUN pip install --upgrade pip setuptools wheel
RUN pip install poetry
