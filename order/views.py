from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from order.models import Order
from order.serializers import OrderCreateSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class OrderListView(ListAPIView):

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type_order','date_time']


class OrderCreateView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self,request):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dto = dict(serializer.validated_data)
        dto.update({'user_id':request.user.id})
        if request.user.is_driver:
            dto.update({'type_order_id': 1})
        else:
            dto.update({'type_order_id': 2})
        order = Order.objects.create(**dto)

        return Response(data=OrderSerializer(instance=order).data)

