from django.core.management.base import BaseCommand
from apps.car.models import Car, CarModel
import csv


class Command(BaseCommand):
    help = 'Создание базы машин'

    @staticmethod
    def import_cars():
        cars = []
        models = []
        with open("cars.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            for row in file_reader:
                cars.append(Car(name=row[0]))
                models.append(CarModel(name=row[1]))

            Car.objects.bulk_create(cars,
                                    ignore_conflicts=True,
                                    unique_fields=['name'])

            CarModel.objects.bulk_create(models,
                                         ignore_conflicts=True,
                                         unique_fields=['name'])

    def handle(self, *args, **options):
        self.import_cars()
        self.stdout.write(self.style.SUCCESS('Импортировано машины'))
