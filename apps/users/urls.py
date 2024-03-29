from apps.users.views import AuthMeView, ListUser, RegisterUserView, \
    UpdateUserInfoView, UserPaymentsListView, VerifyUserView, UserTypeChangeView
from .userdocument.views import RequestDriverView
from django.urls import path
from apps.message.views import ListUserMessageView
from rest_framework import routers
from apps.users import views


router = routers.DefaultRouter()
router.register('payment', views.PaymentViewSet)


urlpatterns = [
    path('request-driver/', RequestDriverView.as_view()),
    path('sign-in/', RegisterUserView.as_view(), name='sign-in'),
    path('verify-user/', VerifyUserView.as_view()),
    path('list/', ListUser.as_view()),
    path('profile-info/', UpdateUserInfoView.as_view()),
    path('user-type-change/', UserTypeChangeView.as_view()),
    path('payments/', UserPaymentsListView.as_view()),
    path('messages/', ListUserMessageView.as_view()),
    path('me/', AuthMeView.as_view()),
]

urlpatterns += router.urls