import logging

from django.core.management.base import BaseCommand
from apps.order.models import TypeOrder
from apps.regions.models import City, Region
from apps.users.models import User, TypeUser
import json


class Command(BaseCommand):
    help = 'Импортирование регионов'

    @staticmethod
    def create_regions():
        with open("city.json") as r_file:
            region_with_city = json.load(r_file)
            for region, cities in region_with_city.items():
                region, is_credited = Region.objects.get_or_create(name=region)
                for city in cities:
                    city = City.objects.get_or_create(name=city, region=region)

    def handle(self, *args, **options):
        self.create_regions()
        self.stdout.write(self.style.SUCCESS('Успешно импортированы регионы'))
