from django.contrib import admin

from apps.order.models import Order, TypeOrder, DefaultSettings

admin.site.register(Order)
admin.site.register(TypeOrder)
admin.site.register(DefaultSettings)