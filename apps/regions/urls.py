
from apps.regions.views import CitiesListView, RegionListView
from django.urls import path 




urlpatterns = [
    path('regions/', RegionListView.as_view()),
    path('city/',CitiesListView.as_view()),
]