from apps.order.serializers import OrderCreateSerializer
from apps.order.subactions import CreateDriverOrderSubAction, CreatePassengerOrderSubAction


class OrderCreateAction:

    @staticmethod
    def run(request):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data['user_id'] = request.user.id

        if request.user.type_user.id == 1:
            data['type_order_id'] = 1
            order = CreateDriverOrderSubAction.run(data=data)
        else:
            data['type_order_id'] = 2
            order = CreatePassengerOrderSubAction.run(data=data)

        return order
