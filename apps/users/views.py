from ctypes import py_object
import datetime
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from apps.users.models import Payment, User, UserInfo
from apps.users.serializers import CreatePaymentSerializer, PaymentSerializer, UserInfoSerializer, UserSerializer, \
    TokenLoginSerializer, VerifyUserSerializer, UserTypeChangeSerializer
from rest_framework.response import Response
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework import status
from apps.users.actions import FreedomPay, SendSmsAction
from sentry_sdk import capture_event
from apps.users.usercode.actions import CreateUserCodeAction, GetStatusUserCodeAction
from apps.users.usercode.enums import StatusUserCode
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
import logging

logger = logging.getLogger(__name__)


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
    @transaction.atomic
    def delete(request):
        user = request.user
        user.delete()
        return Response(data={
            'status': 'deleted'
        }, status=status.HTTP_200_OK)

    @staticmethod
    def get(request, *args, **extra_fields):
        user = request.user
        token = request.GET.get('token', None)

        if token is not None:
            user.firebase_token = token
            user.save()

        return Response(data=UserSerializer(user, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class RegisterUserView(APIView):

    @staticmethod
    @transaction.atomic
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
                capture_event(event={'user_id': user.id, 'type': 'user_register'})
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
    @transaction.atomic
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
    @transaction.atomic
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


class PaymentViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = CreatePaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.update({'user_id': request.user.id})
        p_object = Payment.objects.create(**serializer.validated_data)
        p_object.gen_id = 1000 + int(p_object.id)
        p_object.save()
        freedom_pay = FreedomPay()
        freedom_pay.prepare_data(request.user, p_object)
        text = freedom_pay.create_payment()
        return Response(data={'link': text, 'payment_order_id': p_object.id}, status=200)
    
    @transaction.atomic
    def partial_update(self, request, pk, *args, **kwargs):
        p_object = get_object_or_404(Payment, gen_id=pk)
        freedom_pay = FreedomPay()
        freedom_pay.prepare_data(request.user, p_object)
        text = freedom_pay.create_payment()
        return Response(data={'link': text, 'payment_order_id': p_object.gen_id}, status=200)
    
    
    @action(detail=False, methods=['POST'])
    def result(self, request):
        if int(request.data['pg_result']) == 1:
            payment = Payment.objects.get(gen_id=request.data['pg_order_id'])
            payment.is_confirmed = True
            payment.payment_order_id = request.data['pg_payment_id']
            payment.paid_at = request.data['pg_payment_date']
            payment.save()
        else:
            pass
            # _send_telegram_error_pay(payment)
        return Response(data={"status": 'success'}, status=201)
    


class UserPaymentsListView(APIView):
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            return Response(
                data=PaymentSerializer(self.queryset.filter(user=request.user).order_by('-id')[:5], many=True).data,
                status=200)
        except Exception as e:
            return Response(data=str(e), status=500)


class UserTypeChangeView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        serializer = UserTypeChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, id=serializer.validated_data['user_id'])

        if not user.is_driver:
            raise APIException('Вы не водитель')

        user.type_user_id = serializer.validated_data['change_user_type_id']
        user.save()

        return Response(data=UserSerializer(user).data, status=200)
