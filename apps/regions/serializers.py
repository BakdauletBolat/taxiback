from rest_framework import serializers
from apps.regions.models import City, Region





class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name')



class RegionSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)
    
    class Meta:
        model = Region
        fields = ('id', 'name', 'cities')