from django.contrib import admin

from apps.regions.models import City, Region

# Register your models here.
admin.site.register(Region)


class CityAdmin(admin.ModelAdmin):
    search_fields = ('name', )
admin.site.register(City, CityAdmin)
