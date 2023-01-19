from rest_framework import serializers

from apps.car.models import CarInfo, Car, CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarInfoSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    model = CarModelSerializer()

    class Meta:
        model = CarInfo
        fields = '__all__'
