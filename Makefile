import_all_data:
	python manage.py import_cars
	python manage.py import_order_types
	python manage.py import_type_user
	python manage.py import_user
	python manage.py import_regions
	python manage.py import_cities
clearmigrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete

