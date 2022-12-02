from django.db import models


class TypeOrder(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = 'Тип заказа'
        verbose_name_plural = 'Типы заказа'


class Order(models.Model):
    from_city = models.ForeignKey('regions.City', on_delete=models.CASCADE, related_name='orders_from')
    from_address = models.CharField(null=True, blank=True, max_length=255)
    to_city = models.ForeignKey('regions.City', on_delete=models.CASCADE, related_name='orders_to')
    to_address = models.CharField(null=True, blank=True, max_length=255)
    price = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    type_order = models.ForeignKey(TypeOrder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.from_city} - {self.from_address}, {self.to_city} - {self.to_address}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



