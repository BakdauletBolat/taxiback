import logging

from django.core.management.base import BaseCommand
from apps.order.models import TypeOrder
from apps.regions.models import City, Region
from apps.users.models import User, TypeUser
import csv


class Command(BaseCommand):
    help = 'Импортирование регионов'

    @staticmethod
    def create_regions():
        with open("region.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                Region.objects.get_or_create(id=row[0], name=row[1])

    def handle(self, *args, **options):
        self.create_regions()
        self.stdout.write(self.style.SUCCESS('Успешно импортированы регионы'))
