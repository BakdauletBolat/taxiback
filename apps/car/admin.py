from django.contrib import admin
from .models import CarModel, Car, CarInfo


class CarInfoAdmin(admin.ModelAdmin):
    raw_id_fields = ('car', 'model')


class CarAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(CarInfo, CarInfoAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarModel, CarAdmin)
