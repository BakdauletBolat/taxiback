import logging

from apps.order.access.models import Access, AccessOrder
from apps.order.access.serializers import AccessOrderSerializer
from apps.order.models import DefaultSettings, Order
from apps.order.tasks import GetAvailableCoinsFromUser
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
    def run(serializer: AccessOrderSerializer) -> AccessOrder:
        return AccessOrder.objects.create(**serializer.data)


class CreateDriverOrderSubAction:
    @staticmethod
    def run(data) -> Order:
        today = date.today()
        access = Access.objects.filter(
            from_city_id=data["from_city_id"], to_city_id=data["to_city_id"]
        ).first()
        user = User.objects.get(id=data["user_id"])
        sum_coin = GetAvailableCoinsFromUser.run(user)
        if sum_coin >= access.coin:
            if access is not None:
                CreateAccessOrder.run(
                    serializer=AccessOrderSerializer(
                        AccessOrder(
                            access_id=access.id,
                            user_id=user.id,
                            coin=access.coin,
                            can_access_date=today,
                        )
                    )
                )
            else:
                default_settings = DefaultSettings.objects.all().first()
                CreateAccessOrder.run(
                    serializer=AccessOrderSerializer(
                        AccessOrder(
                            user_id=user.id,
                            coin=default_settings.default_coin,
                            can_access_date=today,
                        )
                    )
                )
        else:
            raise NotEnoughBalanceException(
                errors_data={
                    "to_city": access.to_city.name,
                    "from_city": access.from_city.name,
                    "coin": access.coin,
                }
            )

        return Order.objects.create(**data)
