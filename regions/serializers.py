import imp
from pyexpat import model


from rest_framework import serializers
from regions.models import City, Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')

class CitySerializer(serializers.ModelSerializer):

    region = RegionSerializer()
    
    class Meta:
        model = City
        fields = ('id', 'name','region')
