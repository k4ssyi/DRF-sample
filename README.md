# DRF Example

```bash
$ export DJANGO_READ_ENV_FILE=True
```

example envfile

```
DJANGO_ENV=local
ALLOWED_HOSTS=localhost,127.0.0.1
SECRET_KEY=(z8*1%w)s2m)y!*ckdkn11a3kb%k$gjp!_w9*=2v%+k6ey-jj2
DATABASE_URL=sqlite:///db.sqlite3
```

## Install
```bash
$ pip install poetry
$ poetry install
```

## Django runserver
```bash
$ python manage.py runserver 0.0.0.0:8000
```
## Vue runserver
```bash
$ cd ./application/frontend
$ yarn server --port 3000
```

## development Docker
```bash
$ make image # docker-compose -f docker-compose.yml build
$ make container # docker-compose -f docker-compose.yml up
```
