from rest_framework import serializers
from order.tasks import GetAvailableCoinsFromProfile, GetExceptedCoinsFromProfile
from users.models import Payment, Profile


class TokenLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class VerifyUserSerializer(serializers.Serializer):
    otp = serializers.CharField()
    phone_number = serializers.CharField()


class RequestDriverSerializer(serializers.Serializer):
    passport_photo_front = serializers.FileField()
    passport_photo_back = serializers.FileField()
    car_passport = serializers.FileField()


class ProfileInfoSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_null=True)
    city_id = serializers.IntegerField(required=False, allow_null=True)
    birthday = serializers.DateTimeField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    first_name = serializers.CharField(required=False, allow_null=True)
    avatar = serializers.FileField(required=False, allow_null=True)


class ProfileSerializer(serializers.ModelSerializer):
    profile_info = ProfileInfoSerializer(read_only=True)
    user_document = RequestDriverSerializer(read_only=True)
    coins = serializers.SerializerMethodField('get_coins')
    coins_expected = serializers.SerializerMethodField('get_coins_expected')

    @staticmethod
    def get_coins_expected(obj):
        return GetExceptedCoinsFromProfile.run(obj)

    @staticmethod
    def get_coins(obj):
        return GetAvailableCoinsFromProfile.run(obj)

    class Meta:
        fields = ('id', 'is_driver', 'coins',
                  'coins_expected', 'phone',
                  'type_user', 'user_document',
                  'profile_info')
        model = Profile


class CreatePaymentSerializer(serializers.Serializer):
    coin = serializers.IntegerField()
    user_id = serializers.IntegerField()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'gen_id', 'coin', 'user_id', 'created_at', 'is_confirmed')
