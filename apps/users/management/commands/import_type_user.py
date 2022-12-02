import logging

from django.core.management.base import BaseCommand
from apps.order.models import TypeOrder
from apps.regions.models import City, Region
from apps.users.models import User, TypeUser
import csv


class Command(BaseCommand):
    help = 'Импортирование типей пользователей'

    @staticmethod
    def create_type_user():
        TypeUser.objects.get_or_create(id=1, name='driver')
        TypeUser.objects.get_or_create(id=2, name='passenger')
        TypeUser.objects.get_or_create(id=3, name='manager')

    def handle(self, *args, **options):
        self.create_type_user()
        self.stdout.write(self.style.SUCCESS('Импортировано типы пользователей'))
