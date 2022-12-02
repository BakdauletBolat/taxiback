from django.core.management.base import BaseCommand, CommandError
from order.models import TypeOrder
from regions.models import City, Region
from users.models import Profile, TypeUser
import csv


class Command(BaseCommand):
    help = 'Create Seed'

    def create_regions(self):
        with open("region.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                Region.objects.get_or_create(id=row[0], name=row[1])

    def create_cities(self):
        with open("cities.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                City.objects.get_or_create(name=row[0], status=row[1], region_id=row[2])

    def create_type_order(self):
        TypeOrder.objects.get_or_create(id=1, name='driver')
        TypeOrder.objects.get_or_create(id=2, name='passenger')

    def create_type_user(self):
        TypeUser.objects.get_or_create(id=1, name='driver')
        TypeUser.objects.get_or_create(id=2, name='passenger')
        TypeUser.objects.get_or_create(id=3, name='manager')

    def create_user(self):
        try:
            Profile.objects.get(phone='87059943864')
        except Exception as e:
            Profile.objects.create_superuser(phone='87059943864', password='123', type_user_id=2)

    def handle(self, *args, **options):
        self.create_regions()
        self.create_cities()
        self.stdout.write(self.style.SUCCESS('Successfully created regions and cities'))
        self.create_type_order()
        self.stdout.write(self.style.SUCCESS('Successfully created order types'))
        self.create_type_user()
        self.stdout.write(self.style.SUCCESS('Successfully created user types'))
        self.create_user()
        self.stdout.write(self.style.SUCCESS('Successfully created admin user'))
