from django.contrib import admin

from apps.order.access.models import Access, AccessOrder

# Register your models here.
admin.site.register(Access)
admin.site.register(AccessOrder)