from rest_framework.generics import ListAPIView
from apps.order.exceptions import NotEnoughBalanceException
from apps.regions.models import City, Region

from apps.regions.serializers import CitySerializer, RegionSerializer
from rest_framework import filters

class CitiesListView(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    


class RegionListView(ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()