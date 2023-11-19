from django.db import models
from apps.users.models import User
from apps.car.models import CarInfo
from django.utils.html import mark_safe

class UserDocument(models.Model):
    passport_photo_front = models.FileField(upload_to='user-passports/',verbose_name='Водительское удостоверение (лицевая сторона)')
    passport_photo_back = models.FileField(upload_to='user-passports/',verbose_name='Водительское удостоверение (обратная сторона)')
    car_passport_front = models.FileField(upload_to='car-passports/',verbose_name='Свидетелесьтво о регистраций ТС (тех. паспорт)')
    car_passport_back = models.FileField(upload_to='car-passports/',verbose_name='Свидетелесьтво о регистраций ТС (обратная сторона)')
    car = models.ForeignKey(CarInfo, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Автомобиль')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_document')

    def preview_passport_photo_front(self):
        return mark_safe(f'<a href="{self.passport_photo_front.url}"><img src="{self.passport_photo_front.url}" width="200" /></a>')
    preview_passport_photo_front.short_description = 'Водительское удостоверение (лицевая сторона)'
    def preview_passport_photo_back(self):
        return mark_safe(f'<a href="{self.passport_photo_back.url}"><img src="{self.passport_photo_back.url}" width="200" /></a>')
    preview_passport_photo_back.short_description = 'Водительское удостоверение (обратная сторона)'
    def preview_car_passport_front(self):
        return mark_safe(f'<a href="{self.car_passport_front.url}"><img src="{self.car_passport_front.url}"  width="200" /></a>')
    preview_car_passport_front.short_description = 'Свидетелесьтво о регистраций ТС (тех. паспорт)'
    def preview_car_passport_back(self):
        return mark_safe(f'<a href="{self.car_passport_back.url}"><img src="{self.car_passport_back.url}" width="200"  /></a>')
    preview_car_passport_back.short_description = 'Свидетелесьтво о регистраций ТС (обратная сторона)'

    def __str__(self):
        return f'Документы для {self.user.user_info.first_name}'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
