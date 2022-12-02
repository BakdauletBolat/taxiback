from rest_framework import serializers

from apps.order.access.models import Access
from apps.regions.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class AccessSerializer(serializers.ModelSerializer):
    from_city = CitySerializer()
    to_city = CitySerializer()

    class Meta:
        model = Access
        fields = '__all__'


class GetAccessSerializer(serializers.Serializer):
    from_city_id = serializers.IntegerField()
    to_city_id = serializers.IntegerField()


class AccessOrderSerializer(serializers.Serializer):
    coin = serializers.IntegerField()
    user_id = serializers.IntegerField()
    access_id = serializers.IntegerField()
    can_access_date = serializers.DateField()
