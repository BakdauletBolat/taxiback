from rest_framework import serializers

from order.models import Order, TypeOrder
from regions.models import City
from users.serializers import ProfileSerializer



class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id','name')



class TypeOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeOrder
        fields = ('id','name')

class OrderCreateSerializer(serializers.Serializer):

    from_city_id = serializers.IntegerField()
    from_address = serializers.CharField(allow_null=True,required=False)
    to_city_id = serializers.IntegerField()
    to_address = serializers.CharField(allow_null=True,required=False)
    price = serializers.IntegerField()
    comment = serializers.CharField(allow_null=True,required=False)
    date_time = serializers.DateTimeField()

class OrderSerializer(serializers.ModelSerializer):

    from_city = CitySerializer(read_only=True)
    to_city = CitySerializer(read_only=True)
    user = ProfileSerializer(read_only=True)
    type_order = TypeOrderSerializer(read_only=True)

    class Meta:

        model = Order
        fields = ('__all__')