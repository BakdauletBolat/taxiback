from django.db import transaction, IntegrityError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import RequestDriverSerializer, UserSerializer
from taxiback.telegrambot import TelegramBot
from .enums import UserStatus
from .models import UserDocument
import datetime

telegrambot = TelegramBot('-1002036283116')


def _send_request_message(user: User):
    _send_date = datetime.datetime.now()
    message = f"""
Время отправки: {_send_date.strftime('%Y-%m-%d %H:%M:%')}
Пользователь: {user.user_info.first_name} {user.user_info.last_name}
Номер: {user.phone}
"""
    telegrambot.send_message(message)

class RequestDriverView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request, **kwargs):
        with transaction.atomic():
            try:
                serializer = RequestDriverSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                dto = dict(serializer.validated_data)
                dto.update({'user_id': request.user.id})
                user = User.objects.get(id=request.user.id)
                UserDocument.objects.create(**dto)
                user.status = UserStatus.REQUESTED_TO_DRIVER.value
                user.save()
                _send_request_message(user)
            except IntegrityError as e:
                return Response({'details': 'Документы уже отправлены ждите результатов'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            except Exception as e:
                return Response({'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data=UserSerializer(user, context={'request': request}).data)
