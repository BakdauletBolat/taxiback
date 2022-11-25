from rest_framework.views import APIView
from users.models import Payment, Profile, ProfileInfo, ProfileLoginOTP, UserDocuments
from users.serializers import CreatePaymentSerializer, PaymentSerializer, ProfileInfoSerializer, ProfileSerializer, \
    RequestDriverSerializer, TokenLoginSerializer, VerifyUserSerializer
from rest_framework.response import Response
import random
from datetime import datetime, timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError, transaction
from rest_framework import status
from users.types import UserStatus
from users.actions import SendSmsAction


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'user': ProfileSerializer(user).data,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class AuthMeView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, *args, **extra_fields):
        user = request.user
        token = request.GET.get('token', None)

        if token is not None:
            user.firebase_token = token
            user.save()

        return Response(data=ProfileSerializer(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class RegisterUserView(APIView):

    @staticmethod
    def post(request, **kwargs):
        serializer = TokenLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                profile, created = Profile.objects.get_or_create(phone=f"7{serializer.validated_data['phone_number']}")
                if created:
                    profile.set_password('baguvix123F')
                    profile.type_user_id = 2
                    profile.save()
                otp_obj = ProfileLoginOTP.objects.create(profile=profile, otp=random.randint(1000, 9999))
                SendSmsAction.run(phone_number=profile.phone, code=otp_obj.otp)
                return Response({'status': 'success'}, status=200)
            except Exception as e:
                return Response({'status': 'fail'}, status=400)


class ListUser(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class VerifyUserView(APIView):

    def post(self, request, **kwargs):
        serializer = VerifyUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            otps = ProfileLoginOTP.objects.filter(profile__phone=f"7{serializer.validated_data['phone_number']}",
                                                  otp=serializer.validated_data['otp']).order_by('created_at')

            print(otps)
            if len(otps) > 0:
                otp = otps.last()
                try:

                    now = datetime.now(timezone.utc)
                    created_at = otp.created_at
                    difference = now - created_at
                    minutes = difference.total_seconds() / 60

                    if minutes > 5:
                        return Response({'details': 'Время кода истекло'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                    else:

                        user = Profile.objects.get(phone=f"7{serializer.validated_data['phone_number']}")
                        data = get_tokens_for_user(user)
                        print(data)
                    return Response(data)
                except Exception as e:
                    print(e)
                    return Response({'details': 'Не правильный код, пожалуйста попробуйте еще'},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                return Response({'details': 'Не правильный код, пожалуйста попробуйте еще'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RequestDriverView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):

        with transaction.atomic():
            serializer = RequestDriverSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            dto = dict(serializer.validated_data)
            dto.update({'user_id': request.user.id})
            user = Profile.objects.get(id=request.user.id)
            try:
                UserDocuments.objects.create(**dto)
                user.status = UserStatus.REQUESTED_TO_DRIVER.value
                user.save()
            except IntegrityError as e:
                return Response({'details': 'Документы уже отправлены ждите результатов'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            except Exception as e:
                return Response({'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data=ProfileSerializer(user, context={'request': request}).data)


class UpdateProfileInfoView(APIView):
    allowed_methods = ['PATCH']
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
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
            serializer.validated_data.update({
                'user_id': request.user.id
            })
            profile_info = ProfileInfo.objects.create(**serializer.validated_data)

        return Response(data=ProfileSerializer(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class PaymentCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        serializer = CreatePaymentSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():

                p_object = Payment.objects.create(**serializer.validated_data)
                p_object.gen_id = 1000 + int(p_object.id)
                p_object.save()

            return Response(data=PaymentSerializer(p_object).data, status=201)

        except Exception as e:
            return Response(data=str(e), status=500)


class UserPaymentsListView(APIView):
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            return Response(
                data=PaymentSerializer(self.queryset.filter(user=request.user).order_by('-id'), many=True).data,
                status=200)
        except Exception as e:
            return Response(data=str(e), status=500)
