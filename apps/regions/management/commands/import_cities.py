import logging

from django.core.management.base import BaseCommand
from apps.order.models import TypeOrder
from apps.regions.models import City, Region
from apps.users.models import User, TypeUser
import csv


class Command(BaseCommand):
    help = 'Импортирование городов'

    @staticmethod
    def create_cities():
        with open("cities.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                City.objects.get_or_create(name=row[0], status=row[1], region_id=row[2])

    def handle(self, *args, **options):
        self.create_cities()
        self.stdout.write(self.style.SUCCESS('Успешно импортированы городы'))
