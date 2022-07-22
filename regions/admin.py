from django.contrib import admin

from regions.models import City, Region

# Register your models here.
admin.site.register(Region)
admin.site.register(City)