import logging

from apps.order.access.models import Access, AccessOrder
from apps.order.access.serializers import AccessOrderSerializer
from apps.order.models import Order
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
        access = Access.objects.filter(from_city_id=data['from_city_id'], to_city_id=data['to_city_id']).first()

        if access is not None:
            user = User.objects.get(id=data['user_id'])
            access_orders = AccessOrder.objects.filter(access_id=access.id, user=user).order_by(
                'can_access_date')

            sum_coin = GetAvailableCoinsFromUser.run(user)

            access_order = access_orders.last()

            if access_order is None or access_order.can_access_date < today:
                if sum_coin >= access.coin:
                    try:
                        CreateAccessOrder.run(serializer=AccessOrderSerializer(
                            AccessOrder(access_id=access.id,
                                        user_id=user.id,
                                        coin=access.coin,
                                        can_access_date=today
                                        )))
                    except Exception as e:
                        logging.exception(e)
                else:
                    raise NotEnoughBalanceException(errors_data={
                        'to_city': access.to_city.name,
                        'from_city': access.from_city.name,
                        'coin': access.coin
                    })

            return Order.objects.create(**data)

        else:
            raise NotFound('Не создана цены для в этих направлениях')