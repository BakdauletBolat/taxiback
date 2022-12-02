from django.db import models

from apps.users.models import User


class Access(models.Model):
    from_city = models.ForeignKey('regions.City', on_delete=models.CASCADE, related_name='access_from')
    to_city = models.ForeignKey('regions.City', on_delete=models.CASCADE, related_name='access_to')
    coin = models.IntegerField()

    def __str__(self):
        return f"{self.from_city} - {self.to_city} - {self.coin}"

    class Meta:
        verbose_name = 'Доступ'
        verbose_name_plural = 'Доступы'


class AccessOrder(models.Model):
    access = models.ForeignKey(Access, on_delete=models.CASCADE, related_name='access_orders')
    coin = models.IntegerField()
    can_access_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_orders')
