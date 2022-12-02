import datetime
import logging

from .models import UserCode
import random
from .enums import StatusUserCode


class CreateUserCodeAction:

    @staticmethod
    def run(user):
        return UserCode.objects.create(user=user, otp=random.randint(1000, 9999))


class GetStatusUserCodeAction:

    @staticmethod
    def run(user, otp):
        otp_object = UserCode.objects.filter(user=user,
                                             otp=otp).order_by('created_at').last()

        if otp_object is not None:
            try:
                now = datetime.datetime.now(datetime.timezone.utc)
                created_at = otp_object.created_at
                difference = now - created_at
                minutes = difference.total_seconds() / 60
                if minutes < 5:
                    return StatusUserCode.SUCCESS
                else:
                    return StatusUserCode.TIMEOUT

            except Exception as e:
                logging.exception(e)
                return StatusUserCode.INVALID_CODE
        else:
            return StatusUserCode.NOT_CREATED
