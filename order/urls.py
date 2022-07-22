
from order.views import OrderCreateView, OrderListView
from django.urls import path 




urlpatterns = [
    path('',OrderListView.as_view()),
    path('order-create/',OrderCreateView.as_view()),
]