from django.db.models import Sum


<<<<<<< HEAD:apps/order/tasks.py
class GetAvailableCoinsFromUser:

    @staticmethod
    def run(user) -> float:
        coins_payment = user.coins.filter(is_confirmed=True).aggregate(Sum('coin'))
        coins_orders = user.access_orders.aggregate(Sum('coin'))
=======
class GetAvailableCoinsFromProfile:

    @staticmethod
    def run(profile) -> float:
        coins_payment = profile.coins.filter(is_confirmed=True).aggregate(Sum('coin'))
        coins_orders = profile.city_to_city_orders.aggregate(Sum('coin'))
>>>>>>> origin/release:order/tasks.py

        coins_payment_sum = coins_payment['coin__sum']
        coins_payment_orders = coins_orders['coin__sum']
        if coins_payment['coin__sum'] is None:
            coins_payment_sum = 0
        if coins_orders['coin__sum'] is None:
            coins_payment_orders = 0

        return coins_payment_sum - coins_payment_orders


<<<<<<< HEAD:apps/order/tasks.py
class GetExceptedCoinsFromUser:

    @staticmethod
    def run(user) -> float:
        coins_payment = user.coins.filter(is_confirmed=False).aggregate(Sum('coin'))
=======
class GetExceptedCoinsFromProfile:

    @staticmethod
    def run(profile) -> float:
        coins_payment = profile.coins.filter(is_confirmed=False).aggregate(Sum('coin'))
>>>>>>> origin/release:order/tasks.py

        if coins_payment['coin__sum'] is None:
            return 0

        return coins_payment['coin__sum']