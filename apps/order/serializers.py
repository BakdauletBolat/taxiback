from rest_framework import serializers

from apps.order.models import Order, TypeOrder
from apps.regions.models import City
from apps.users.serializers import UserSerializer


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class TypeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOrder
        fields = ('id', 'name')


class OrderCreateSerializer(serializers.Serializer):
    from_city_id = serializers.IntegerField()
    from_address = serializers.CharField(allow_null=True, required=False, allow_blank=True)
    to_city_id = serializers.IntegerField()
    to_address = serializers.CharField(allow_null=True, required=False, allow_blank=True)
    price = serializers.IntegerField()
    comment = serializers.CharField(allow_null=True, required=False, allow_blank=True)
    date_time = serializers.DateTimeField()


class OrderSerializer(serializers.ModelSerializer):
    from_city = CitySerializer(read_only=True)
    to_city = CitySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    type_order = TypeOrderSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('__all__')
