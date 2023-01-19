import re

from django.utils import timezone
from rest_framework import serializers

from apps.car.serializers import CarInfoSerializer
from apps.order.tasks import GetExceptedCoinsFromUser, GetAvailableCoinsFromUser
from apps.users.models import Payment, User


def phone_validator(value):
    reg = re.fullmatch(r"((8|\+7|7)-?)?\(?\d{3}\)?-?\d{1}-?\d{1}-?\d{1}-?\d{1}-?\d{1}-?\d{1}-?\d{1}", value)
    if reg is None:
        raise serializers.ValidationError('Не правильный формат номера')


class TokenLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[phone_validator])


class VerifyUserSerializer(serializers.Serializer):
    otp = serializers.CharField()
    phone_number = serializers.CharField()


class RequestDriverSerializer(serializers.Serializer):
    passport_photo_front = serializers.FileField()
    passport_photo_back = serializers.FileField()
    car_passport_front = serializers.FileField()
    car_passport_back = serializers.FileField()
    car = CarInfoSerializer()


class UserInfoSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_null=True)
    city_id = serializers.IntegerField(required=False, allow_null=True)
    birthday = serializers.DateTimeField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    first_name = serializers.CharField(required=False, allow_null=True)
    avatar = serializers.FileField(required=False, allow_null=True)


class UserSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(read_only=True)
    user_document = RequestDriverSerializer(read_only=True)
    coins = serializers.SerializerMethodField('get_coins')
    coins_expected = serializers.SerializerMethodField('get_coins_expected')
    access_orders_ids = serializers.SerializerMethodField('get_access_orders_ids')

    def get_access_orders_ids(self, obj: User):
        return obj.access_orders.filter(can_access_date__gte=timezone.now().date()).values_list('access_id', flat=True)

    @staticmethod
    def get_coins_expected(obj):
        return GetExceptedCoinsFromUser.run(obj)

    @staticmethod
    def get_coins(obj):
        return GetAvailableCoinsFromUser.run(obj)

    class Meta:
        fields = ('id', 'is_driver', 'coins',
                  'coins_expected', 'phone',
                  'type_user', 'user_document',
                  'access_orders_ids',
                  'user_info')
        model = User


class CreatePaymentSerializer(serializers.Serializer):
    coin = serializers.IntegerField()
    user_id = serializers.IntegerField()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'gen_id', 'coin', 'user_id', 'created_at', 'is_confirmed')


class UserTypeChangeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    change_user_type_id = serializers.IntegerField()
