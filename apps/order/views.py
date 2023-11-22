from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from apps.order.models import Order
from apps.order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from apps.order.actions import OrderCreateAction
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from datetime import date
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


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
    pagination_class = StandardResultsSetPagination
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


class GetUserOrderView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-created_at')
