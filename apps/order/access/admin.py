from django.contrib import admin

from apps.order.access.models import Access, AccessOrder

class AccessAdmin(admin.ModelAdmin):
    fields = ('from_city', 'to_city', 'coin')
    autocomplete_fields = ['from_city', 'to_city']

    

admin.site.register(Access, AccessAdmin)

admin.site.register(AccessOrder)

