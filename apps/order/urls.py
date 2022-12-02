from apps.order.views import OrderCreateView, OrderListView, GetLastOrderView, OrderCancelView, GetUserOrderView
from django.urls import path
from apps.order.access.views import GetAccessView, GetStatusToCallPhoneView

urlpatterns = [
    path('', OrderListView.as_view()),
    path('user/', GetUserOrderView.as_view()),
    path('create/', OrderCreateView.as_view()),
    path('access/', GetAccessView.as_view()),
    path('get-status-to-call-phone/', GetStatusToCallPhoneView.as_view()),
    path('get-last-order/', GetLastOrderView.as_view()),
    path('cancel/<int:pk>/', OrderCancelView.as_view())
]
