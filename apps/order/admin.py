from django.contrib import admin

<<<<<<< HEAD:apps/order/admin.py
from apps.order.models import Order, TypeOrder
=======
from order.models import CitiToCityPrice, Order, TypeOrder
>>>>>>> origin/release:order/admin.py

# Register your models here.


admin.site.register(Order)
admin.site.register(TypeOrder)
admin.site.register(CitiToCityPrice)
