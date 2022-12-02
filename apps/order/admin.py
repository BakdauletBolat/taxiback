from django.contrib import admin

from apps.order.models import Order, TypeOrder

admin.site.register(Order)
admin.site.register(TypeOrder)
