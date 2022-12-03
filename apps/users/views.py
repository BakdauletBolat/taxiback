from rest_framework.views import APIView
from apps.users.models import Payment, User, UserInfo
from apps.users.serializers import CreatePaymentSerializer, PaymentSerializer, UserInfoSerializer, UserSerializer, \
    TokenLoginSerializer, VerifyUserSerializer
from rest_framework.response import Response
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework import status
from apps.users.actions import SendSmsAction
from apps.users.usercode.actions import CreateUserCodeAction, GetStatusUserCodeAction
from apps.users.usercode.enums import StatusUserCode
from django.shortcuts import get_object_or_404


def get_tokens_for_user(user, request):
    refresh = RefreshToken.for_user(user)
    return {
        'user': UserSerializer(user, context={'request': request}).data,
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

        return Response(data=UserSerializer(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class RegisterUserView(APIView):

    @staticmethod
    def post(request, **kwargs):
        serializer = TokenLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone_number = serializer.validated_data['phone_number']
            try:
                user, created = User.objects.get_or_create(phone=phone_number)
                if created:
                    user.set_password(f"{random.randint(100000, 999999)}")
                    user.type_user_id = 2
                    user.save()
                otp_obj = CreateUserCodeAction.run(user=user)
                if not request.data.get('test', False):
                    SendSmsAction.run(phone_number=user.phone, code=otp_obj.otp)
                return Response({'status': 'success'}, status=200)
            except Exception as e:
                return Response({'status': str(e)}, status=400)


class ListUser(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class VerifyUserView(APIView):

    @staticmethod
    def post(request, **kwargs):
        serializer = VerifyUserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            phone_number = serializer.validated_data['phone_number']
            otp = serializer.validated_data['otp']
            user = get_object_or_404(User, phone=phone_number)

            code_status = GetStatusUserCodeAction.run(user=user,
                                                      otp=otp)

            if code_status == StatusUserCode.SUCCESS:
                data = get_tokens_for_user(user, request)
                return Response(data)
            elif code_status == StatusUserCode.TIMEOUT:
                return Response({'details': 'Время кода истекло'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif code_status == StatusUserCode.INVALID_CODE:
                return Response({'details': 'Не правильный код, пожалуйста попробуйте еще'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                return Response({'details': 'Не правильный код, пожалуйста попробуйте еще'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class UpdateUserInfoView(APIView):
    allowed_methods = ['PATCH']
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def patch(request):
        serializer = UserInfoSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user_info = UserInfo.objects.filter(user_id=request.user.id)

        if len(user_info) > 0:
            user_info.update(**serializer.validated_data)
            user_info_object = user_info.first()

            try:
                user_info_object.avatar = serializer.validated_data['avatar']
                user_info_object.save()
            except Exception as e:
                print(e)

        else:
            serializer.validated_data.update({
                'user_id': request.user.id
            })
            UserInfo.objects.create(**serializer.validated_data)

        return Response(data=UserSerializer(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class PaymentCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request, *args, **kwargs):

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
