from django.db.models import Sum


class GetAvailableCoinsFromUser:

    @staticmethod
    def run(user) -> float:
        coins_payment = user.coins.filter(is_confirmed=True).aggregate(Sum('coin'))
        coins_orders = user.access_orders.aggregate(Sum('coin'))

        coins_payment_sum = coins_payment['coin__sum']
        coins_payment_orders = coins_orders['coin__sum']
        if coins_payment['coin__sum'] is None:
            coins_payment_sum = 0
        if coins_orders['coin__sum'] is None:
            coins_payment_orders = 0

        return coins_payment_sum - coins_payment_orders


class GetExceptedCoinsFromUser:

    @staticmethod
    def run(user) -> float:
        coins_payment = user.coins.filter(is_confirmed=False).aggregate(Sum('coin'))

        if coins_payment['coin__sum'] is None:
            return 0

        return coins_payment['coin__sum']
