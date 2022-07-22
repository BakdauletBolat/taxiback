from django.shortcuts import render
from rest_framework.generics import ListAPIView
from regions.models import City

from regions.serializers import CitySerializer
from rest_framework import filters

class CitiesListView(ListAPIView):  

    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']