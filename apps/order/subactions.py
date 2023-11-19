import logging

from apps.order.access.models import Access, AccessOrder
from apps.order.access.serializers import AccessOrderSerializer
from apps.order.models import DefaultSettings, Order
from apps.order.tasks import GetAvailableCoinsFromUser
from apps.regions.models import City
from apps.users.models import User
from datetime import date
from rest_framework.exceptions import NotFound
from apps.order.exceptions import NotEnoughBalanceException


class CreatePassengerOrderSubAction:
    @staticmethod
    def run(data) -> Order:
        return Order.objects.create(**data)


class CreateAccessOrder:
    @staticmethod
    def run(access: Access, user: User, coin:int) -> AccessOrder:
        today = date.today()
        access_order = AccessOrder(user_id=user.id,coin=coin,can_access_date=today)
        if access is not None:
            access_order.access_id = access.id
        serializer = AccessOrderSerializer(access_order)
        return AccessOrder.objects.create(**serializer.data)


class CreateDriverOrderSubAction:
    @staticmethod
    def run(data) -> Order:
        access = Access.objects.filter(
            from_city_id=data["from_city_id"], to_city_id=data["to_city_id"]
        ).first()
        from_city = City.objects.get(id=data['from_city_id'])
        to_city = City.objects.get(id=data['to_city_id'])
        user = User.objects.get(id=data["user_id"])
        sum_coin = GetAvailableCoinsFromUser.run(user)
        default_settings = DefaultSettings.objects.all().first()
        if access is not None and sum_coin >= access.coin:
            CreateAccessOrder.run(access=access, user=user, coin=access.coin)
        elif default_settings is not None and sum_coin >= default_settings.default_coin:
            CreateAccessOrder.run(access=access, user=user, coin=default_settings.default_coin)
        else:
            raise NotEnoughBalanceException(
                errors_data={
                    "to_city": to_city.name,
                    "from_city": from_city.name,
                    "coin": access.coin if access is not None else default_settings.default_coin,
                }
            )

        return Order.objects.create(**data)
