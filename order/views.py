from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from order.models import Order, CitiToCityPrice
from users.models import CityToCityOrder
from order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from order.actions import OrderCreateAction
from rest_framework.response import Response
from order.serializers import CityToCityPriceSerializer, CityToCityOrderSerializer, GetCityToCityPriceSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from datetime import date
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django.shortcuts import get_object_or_404


class DriverFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if request.user.type_user.id == 2:
            return queryset.filter(type_order=1)

        return queryset


class OrderFilter(django_filters.FilterSet):
    type_order = django_filters.NumberFilter()
    from_city_id = django_filters.NumberFilter()
    to_city_id = django_filters.NumberFilter()
    date_time = django_filters.DateFilter(field_name='date_time__date')

    class Meta:
        model = Order
        fields = ['type_order', 'from_city_id', 'to_city_id', 'date_time']


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().filter(is_active=True).order_by('-id')
    filter_backends = [DjangoFilterBackend, DriverFilterBackend]
    filterset_class = OrderFilter
    permission_classes = (IsAuthenticated,)


class OrderCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        with transaction.atomic():
            order = OrderCreateAction.run(request=request)
            return Response(data=OrderSerializer(instance=order).data)


class OrderCancelView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, pk):
        with transaction.atomic():

            order = get_object_or_404(Order, id=pk)
            if order.user != request.user:
                raise PermissionDenied()
            else:
                order.is_active = False
                order.save()
                return Response(data={'status': 'success'}, status=200)


class GetCityToCityPriceView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        serializer = GetCityToCityPriceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        city_to_city_price = CitiToCityPrice.objects.filter(**serializer.validated_data).last()

        if city_to_city_price is None:
            raise NotFound()

        return Response(data=CityToCityPriceSerializer(city_to_city_price).data, status=200)


class GetLastOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        order = Order.objects.filter(date_time__date__gte=date.today(), user=request.user, is_active=True, ).order_by(
            'created_at').last()

        if order is not None:
            return Response(data=OrderSerializer(order).data, status=200)
        else:
            raise NotFound('Нет активных заказов')


class GetStatusToCallPhoneView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        serializer = GetCityToCityPriceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city_to_city_price = CitiToCityPrice.objects.filter(**serializer.validated_data).last()

        print(city_to_city_price)
        if city_to_city_price is None:
            raise NotFound()

        data = {
            'city_to_city_id': city_to_city_price.id,
            'profile_id': request.user.id,
            'driver_can_view_order_date': date.today()
        }

        city_to_city_order = CityToCityOrder.objects.filter(**data).last()

        if city_to_city_order is None:
            return Response(data={'status': False}, status=400)

        return Response(data={'status': True}, status=200)
