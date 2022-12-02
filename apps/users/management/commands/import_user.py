import logging

from django.core.management.base import BaseCommand
from apps.order.models import TypeOrder
from apps.regions.models import City, Region
from apps.users.models import User, TypeUser
import csv


class Command(BaseCommand):
    help = 'Импорт суперпользователя'

    @staticmethod
    def create_user():
        try:
            User.objects.get(phone='87059943864')
        except Exception as _:
            User.objects.create_superuser(phone='87059943864', password='123', type_user_id=2)

    def handle(self, *args, **options):
        self.create_user()
        self.stdout.write(self.style.SUCCESS('Импортирован суперпользователь'))
