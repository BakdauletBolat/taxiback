from rest_framework.exceptions import APIException, NotFound


class TimeExpiredException(APIException):

    default_code = 'expired'


class NotEnoughBalanceException(APIException):

    default_code = 'notenough'
    default_detail = 'Не хватает баланса'
    status_code = 422
