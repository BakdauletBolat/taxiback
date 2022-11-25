from django.contrib import admin

from order.models import CitiToCityPrice, Order, TypeOrder

# Register your models here.


admin.site.register(Order)
admin.site.register(TypeOrder)
admin.site.register(CitiToCityPrice)
