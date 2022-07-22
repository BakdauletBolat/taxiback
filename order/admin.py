from django.contrib import admin

from order.models import Order, TypeOrder

# Register your models here.


admin.site.register(Order)
admin.site.register(TypeOrder)
