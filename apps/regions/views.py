from rest_framework.generics import ListAPIView
from apps.regions.models import City

from apps.regions.serializers import CitySerializer
from rest_framework import filters


class CitiesListView(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
