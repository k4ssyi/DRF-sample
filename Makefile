ALL: image
collectstatic:
	docker-compose run --rm app python3 manage.py collectstatic --noinput
createsuperuser:
	docker-compose run --rm app python3 manage.py createsuperuser
makemigrations:
	docker-compose run --rm app python3 manage.py makemigrations
migrate:
	docker-compose run --rm app python3 manage.py migrate
shell:
	docker-compose run --rm app python3 manage.py shell_plus
image:
	docker-compose -f docker-compose.yml build
container:
	docker-compose -f docker-compose.yml up
up:
	docker-compose -f docker-compose.yml up -d
stop:
	docker-compose -f docker-compose.yml stop
test:
	docker-compose run --rm app python manage.py test --settings config.settings.test
