from django.core.management.base import BaseCommand, CommandError
from order.models import TypeOrder
from users.models import Profile,TypeUser

class Command(BaseCommand):
    help = 'Create Seed'

    def create_type_order(self):
        type_order_driver,created = TypeOrder.objects.get_or_create(id=1,name='driver')
        type_order_passenger,created = TypeOrder.objects.get_or_create(id=2,name='passenger')
    
    def create_type_user(self):
        type_user_driver,created = TypeUser.objects.get_or_create(id=1,name='driver')
        type_user_passenger,created = TypeUser.objects.get_or_create(id=2,name='passenger')
        type_user_manager,created = TypeUser.objects.get_or_create(id=3,name='manager')
    
    def create_user(self):
        try:
            user = Profile.objects.get(phone='87059943864')
        except Exception as e:
            admin_user = Profile.objects.create_superuser(phone='87059943864',password='123')

    def handle(self, *args, **options):
        self.create_type_order()
        self.stdout.write(self.style.SUCCESS('Successfully created order types'))
        self.create_type_user()
        self.stdout.write(self.style.SUCCESS('Successfully created user types'))
        self.create_user()
        self.stdout.write(self.style.SUCCESS('Successfully created admin user'))