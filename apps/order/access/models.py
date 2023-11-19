from django.db import models

from apps.users.models import User


class Access(models.Model):
    from_city = models.ForeignKey('regions.City',verbose_name='От города', on_delete=models.CASCADE, related_name='access_from')
    to_city = models.ForeignKey('regions.City', verbose_name='До города', on_delete=models.CASCADE, related_name='access_to')
    coin = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f"Id: {self.id} {self.from_city} - {self.to_city} - {self.coin}"

    class Meta:
        verbose_name = 'Доступ'
        verbose_name_plural = 'Доступы'


class AccessOrder(models.Model):
    access = models.ForeignKey(Access, on_delete=models.CASCADE, related_name='access_orders', null=True, blank=True)
    coin = models.IntegerField()
    can_access_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_orders')
