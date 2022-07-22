from rest_framework.views import APIView
from users.models import Profile, ProfileInfo, ProfileLoginOTP, UserDocuments
from users.serializers import ProfileInfoSerializer, ProfileSerializer, RequestDriverSerializer, TokenLoginSerializer, VerifyUserSerializer
from rest_framework.response import Response
import random
from datetime import datetime,timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError, transaction
from rest_framework import status
from users.types import UserStatus

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'user':ProfileSerializer(user).data,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class AuthMeView(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **extra_fields):
        return Response(data=ProfileSerializer(request.user,context={'request':request}).data,status=status.HTTP_200_OK)

class RegisterUserView(APIView):

    def post(self,request,**kwargs):
        serializer = TokenLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                profile,created = Profile.objects.get_or_create(phone=serializer.validated_data['phone_number'])
                if created:
                    profile.set_password('baguvix123F')
                    profile.type_user_id = 2
                    profile.save()
                login_otp = ProfileLoginOTP.objects.create(profile=profile,otp=random.randint(1000, 9999))
                return Response({'status':'success'})
            except Exception as e:
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
                        return Response({'details':'time'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                    else:
                        user = Profile.objects.get(phone=serializer.validated_data['phone_number'])
                        data = get_tokens_for_user(user)
                    return Response(data)
                except Exception as e:
                    return Response({'details':'error'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                return Response({'details':'error'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)



class RequestDriverView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,**kwargs):

        with transaction.atomic():
            serializer = RequestDriverSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            dto = dict(serializer.validated_data)
            dto.update({'user_id':request.user.id})
            user = Profile.objects.get(id=request.user.id)
            try:
                UserDocuments.objects.create(**dto)
                user.status = UserStatus.REQUESTED_TO_DRIVER.value
                user.save()
            except IntegrityError as e:
                return Response({'details':str(e)},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
            except Exception as e:
                return Response({'details':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data=ProfileSerializer(user,context={'request':request}).data)


class UpdateProfileInfoView(APIView):

    allowed_methods = ['PATCH']
    permission_classes = (IsAuthenticated,)

    def patch(self,request):
        serializer = ProfileInfoSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

    
        profile_info = ProfileInfo.objects.filter(user_id=request.user.id)   

        if len(profile_info) > 0:
            profile_info.update(**serializer.validated_data)
            profile_info_object = profile_info.first()

            try:
                profile_info_object.avatar = serializer.validated_data['avatar']
                profile_info_object.save()
            except Exception as e:
                print(e)
                
        else:
            print('as')
            serializer.validated_data.update({
            'user_id':request.user.id
            })
            profile_info = ProfileInfo.objects.create(**serializer.validated_data)

    
        return Response(data=ProfileSerializer(request.user,context={'request':request}).data,status=status.HTTP_200_OK)
            
                
