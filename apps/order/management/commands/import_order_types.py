import logging

from django.core.management.base import BaseCommand
from apps.order.models import TypeOrder
from apps.regions.models import City, Region
from apps.users.models import User, TypeUser
import csv


class Command(BaseCommand):
    help = 'Импорт типов заказов'

    @staticmethod
    def create_type_order():
        TypeOrder.objects.get_or_create(id=1, name='driver')
        TypeOrder.objects.get_or_create(id=2, name='passenger')

    def handle(self, *args, **options):
        self.create_type_order()
        self.stdout.write(self.style.SUCCESS('Импортированы типы заказов'))
