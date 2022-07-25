from asyncore import read
from pkg_resources import require
from rest_framework import serializers

from users.models import Profile

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

    email = serializers.EmailField(required=False,allow_null=True)
    city_id = serializers.IntegerField(required=False,allow_null=True)
    birthday = serializers.DateTimeField(required=False,allow_null=True)
    last_name = serializers.CharField(required=False,allow_null=True)
    first_name = serializers.CharField(required=False,allow_null=True)
    avatar = serializers.FileField(required=False,allow_null=True)




class ProfileSerializer(serializers.ModelSerializer):

    profile_info = ProfileInfoSerializer(read_only=True)
    user_document = RequestDriverSerializer(read_only=True)

    
    

    class Meta:

        fields = ('id','is_driver','phone','driver_can_view_order_date','type_user','user_document','profile_info')
        model = Profile