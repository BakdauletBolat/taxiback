from django.db import models
from apps.users.models import User
from apps.car.models import CarInfo


class UserDocument(models.Model):
    passport_photo_front = models.FileField(upload_to='user-passports/')
    passport_photo_back = models.FileField(upload_to='user-passports/')
    car_passport_front = models.FileField(upload_to='car-passports/')
    car_passport_back = models.FileField(upload_to='car-passports/')
    car = models.ForeignKey(CarInfo, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_document')

    def __str__(self):
        return f'Документы для {self.user.user_info.first_name}'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
