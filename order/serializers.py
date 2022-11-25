from rest_framework import serializers

from order.models import CitiToCityPrice, Order, TypeOrder
from regions.models import City
from users.serializers import ProfileSerializer


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
    from_address = serializers.CharField(allow_null=True, required=False)
    to_city_id = serializers.IntegerField()
    to_address = serializers.CharField(allow_null=True, required=False)
    price = serializers.IntegerField()
    comment = serializers.CharField(allow_null=True, required=False)
    date_time = serializers.DateTimeField()


class OrderSerializer(serializers.ModelSerializer):
    from_city = CitySerializer(read_only=True)
    to_city = CitySerializer(read_only=True)
    user = ProfileSerializer(read_only=True)
    type_order = TypeOrderSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('__all__')


class CityToCityPriceSerializer(serializers.ModelSerializer):
    from_city = CitySerializer()
    to_city = CitySerializer()

    class Meta:
        model = CitiToCityPrice
        fields = ('__all__')


class GetCityToCityPriceSerializer(serializers.Serializer):

    from_city_id = serializers.IntegerField()
    to_city_id = serializers.IntegerField()


class CityToCityOrderSerializer(serializers.Serializer):
    coin = serializers.IntegerField()
    profile_id = serializers.IntegerField()
    city_to_city_id = serializers.IntegerField()
    driver_can_view_order_date = serializers.DateField()
    #
    # city_to_city = CityToCityPriceSerializer(read_only=True)
    # profile = ProfileSerializer(read_only=True)

