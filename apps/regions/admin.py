from django.contrib import admin

from apps.regions.models import City, Region

# Register your models here.
admin.site.register(Region)
admin.site.register(City)
