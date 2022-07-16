from rest_framework.views import APIView
from users.models import Profile, ProfileLoginOTP
from users.serializers import ProfileSerializer, TokenLoginSerializer, VerifyUserSerializer
from rest_framework.response import Response
import random
from datetime import datetime,timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'user': user.phone,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterUserView(APIView):

    def post(self,request,**kwargs):
        serializer = TokenLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                profile,created = Profile.objects.get_or_create(phone=serializer.validated_data['phone_number'])
                login_otp = ProfileLoginOTP.objects.create(profile=profile,otp=random.randint(1000, 9999))
                return Response({'status':'success'})
            except Exception as e:
                print(e)
                return Response({'status':'fail'})


class ListUser(ListAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    

class VerifyUserView(APIView):

    def post(self,request,**kwargs):
        serializer = VerifyUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            otps = ProfileLoginOTP.objects.filter(profile__phone=serializer.validated_data['phone_number'],otp=serializer.validated_data['otp']).order_by('created_at')

            if len(otps) > 0:
                otp = otps.last()
                try:
                    now = datetime.now(timezone.utc)
                    created_at = otp.created_at
                    difference = now-created_at
                    minutes = difference.total_seconds() / 60

                    if minutes > 5:   
                        return Response({'status':'time failed'})

                    else:
                        user = Profile.objects.get(phone=serializer.validated_data['phone_number'])
                        data = get_tokens_for_user(user)
                    return Response(data)
                except Exception as e:
                    print(e)
                    return Response({'status':'fail'})
            else:
                print(otps)
                return Response({'status':'not otp'})
            
                
