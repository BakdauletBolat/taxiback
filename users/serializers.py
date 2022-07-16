from rest_framework import serializers

from users.models import Profile

class TokenLoginSerializer(serializers.Serializer):

    phone_number = serializers.CharField()


class VerifyUserSerializer(serializers.Serializer):

    otp = serializers.CharField()
    phone_number = serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('__all__')
        model = Profile