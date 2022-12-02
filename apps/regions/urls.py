
from apps.regions.views import CitiesListView
from django.urls import path 




urlpatterns = [
    path('city/',CitiesListView.as_view()),
]