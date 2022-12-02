from order.views import OrderCreateView, OrderListView, GetLastOrderView, GetCityToCityPriceView, OrderCancelView, \
    GetStatusToCallPhoneView
from django.urls import path

urlpatterns = [
    path('', OrderListView.as_view()),
    path('create/', OrderCreateView.as_view()),
    path('city-to-city-price/', GetCityToCityPriceView.as_view()),
    path('get-status-to-call-phone/', GetStatusToCallPhoneView.as_view()),
    path('get-last-order/', GetLastOrderView.as_view()),
    path('cancel/<int:pk>/', OrderCancelView.as_view())
]
