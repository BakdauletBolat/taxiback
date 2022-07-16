from django.db import models

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