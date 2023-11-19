from typing import TYPE_CHECKING
from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.users.managers import CustomUserManager
from django.utils import timezone
from django.utils.html import mark_safe


class TypeUser(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = 'Цена заказа'
        verbose_name_plural = 'Цены заказа'


class User(AbstractUser):
    # if TYPE_CHECKING:
    #     user_info: UserInfo
    USER_STATUS_CHOICES = (
        ('registered', 'Зарегистрирован'),
        ('requested_to_driver', 'Запрос от водителя'),
        ('allowed_drive', 'Разрешено водить'),
        ('disallowed_drive', 'Недопущено к управлению')
    )
    firebase_token = models.CharField('Токен Firebase', max_length=200, null=True, blank=True)
    phone = models.CharField('Телефон пользователя', unique=True, max_length=255)
    type_user = models.ForeignKey(TypeUser,verbose_name='Тип пользователя', on_delete=models.CASCADE, null=True, blank=True)
    is_driver = models.BooleanField(default=False, verbose_name='Получил статус?')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата присоединения')
    status = models.CharField('Статус', max_length=255, null=True, blank=True, choices=USER_STATUS_CHOICES,
                              default='registered')
    
    username = None
    last_name = None
    first_name = None
    groups = None
    email = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone


class UserInfo(models.Model):
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', null=True, blank=True)
    email = models.EmailField(verbose_name='Почта', unique=True, null=True, blank=True)
    city = models.ForeignKey('regions.City',verbose_name='Город', on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    birthday = models.DateTimeField(null=True,verbose_name='День рождение', blank=True)
    last_name = models.CharField(verbose_name='Фамилия',max_length=255, null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя',max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')

    def preview_image(self):
        return mark_safe(f'<a href="{self.avatar.url}"><img src="{self.avatar.url}" width="150" height="150" /></a>')

    preview_image.short_description = 'Аватар'

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователе'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Payment(models.Model):
    coin = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coins')
    created_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(null=True,blank=True)
    is_confirmed = models.BooleanField(default=False)
    payment_order_id = models.CharField(unique=True, max_length=50, null=True, blank=True)
    gen_id = models.CharField(unique=True, max_length=255, null=True, blank=True)
