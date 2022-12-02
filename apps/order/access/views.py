from datetime import date

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.order.access.models import Access, AccessOrder
from apps.order.access.serializers import GetAccessSerializer, AccessSerializer

# Create your views here.
class GetAccessView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        serializer = GetAccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        city_to_city_price = Access.objects.filter(**serializer.validated_data).last()

        if city_to_city_price is None:
            raise NotFound()

        return Response(data=AccessSerializer(city_to_city_price).data, status=200)


class GetStatusToCallPhoneView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        serializer = GetAccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        access = Access.objects.filter(**serializer.validated_data).last()
        if access is None:
            raise NotFound()

        data = {
            'access_id': access.id,
            'user_id': request.user.id,
            'can_access_date': date.today()
        }

        order = AccessOrder.objects.filter(**data).last()

        if order is None:
            return Response(data={'status': False}, status=400)

        return Response(data={'status': True}, status=200)
