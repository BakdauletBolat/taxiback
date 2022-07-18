from django.db import models



class TypeOrder(models.Model):

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class Order(models.Model):

    from_city = models.ForeignKey('regions.City',on_delete=models.CASCADE,related_name='orders_from')
    from_address = models.CharField(null=True,blank=True,max_length=255)
    to_city = models.ForeignKey('regions.City',on_delete=models.CASCADE,related_name='orders_to')
    to_address = models.CharField(null=True,blank=True,max_length=255)
    price = models.IntegerField()
    comment = models.TextField()
    date_time = models.DateTimeField()
    user = models.ForeignKey('users.Profile',on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    type_order = models.ForeignKey(TypeOrder,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)