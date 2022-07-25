docker-compose up -d --build  build

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py seed_app

docker-compose exec web python manage.py collectstatic --no-input

