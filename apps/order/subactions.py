<<<<<<< HEAD:apps/order/subactions.py
import logging

from apps.order.access.models import Access, AccessOrder
from apps.order.access.serializers import AccessOrderSerializer
from apps.order.models import Order
from apps.order.tasks import GetAvailableCoinsFromUser
from apps.users.models import User
from datetime import date
from rest_framework.exceptions import NotFound
from apps.order.exceptions import NotEnoughBalanceException
=======
from order.models import CitiToCityPrice, Order
from order.serializers import CityToCityOrderSerializer
from order.tasks import GetAvailableCoinsFromProfile
from users.models import CityToCityOrder, Profile
from datetime import date
from rest_framework.exceptions import NotFound
from order.exceptions import TimeExpiredException, NotEnoughBalanceException
from django.db.models import Sum
>>>>>>> origin/release:order/subactions.py


class CreatePassengerOrderSubAction:

    @staticmethod
    def run(data) -> Order:
        return Order.objects.create(**data)


<<<<<<< HEAD:apps/order/subactions.py
class CreateAccessOrder:

    @staticmethod
    def run(serializer: AccessOrderSerializer) -> AccessOrder:
        return AccessOrder.objects.create(**serializer.data)
=======
class CreateCityToCityOrder:

    @staticmethod
    def run(serializer: CityToCityOrderSerializer) -> CityToCityOrder:
        print(serializer.data)
        return CityToCityOrder.objects.create(**serializer.data)
>>>>>>> origin/release:order/subactions.py


class CreateDriverOrderSubAction:

    @staticmethod
    def run(data) -> Order:
        today = date.today()
<<<<<<< HEAD:apps/order/subactions.py
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
=======

        price = CitiToCityPrice.objects.filter(from_city_id=data['from_city_id'], to_city_id=data['to_city_id']).first()

        if price is not None:
            profile = Profile.objects.get(id=data['user_id'])

            city_to_cities_order = CityToCityOrder.objects.filter(city_to_city_id=price.id, profile=profile).order_by(
                'driver_can_view_order_date')

            sum_coin = GetAvailableCoinsFromProfile.run(profile)

            city_to_city_order = city_to_cities_order.last()

            if city_to_city_order is None or city_to_city_order.driver_can_view_order_date < today:
                if sum_coin >= price.coin:
                    try:

                        CreateCityToCityOrder.run(serializer=CityToCityOrderSerializer(
                            CityToCityOrder(city_to_city_id=price.id,
                                            profile_id=profile.id,
                                            coin=price.coin,
                                            driver_can_view_order_date=today
                                            )))
                    except Exception as e:
                        print(e,'asdas')
>>>>>>> origin/release:order/subactions.py
                else:
                    raise NotEnoughBalanceException()

            return Order.objects.create(**data)

        else:
            raise NotFound('Не создана цены для в этих направлениях')
