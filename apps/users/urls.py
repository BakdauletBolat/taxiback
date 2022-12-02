from apps.users.views import AuthMeView, ListUser, PaymentCreateView, RegisterUserView, \
    UpdateUserInfoView, UserPaymentsListView, VerifyUserView
from .userdocument.views import RequestDriverView
from django.urls import path
from apps.message.views import ListUserMessageView

urlpatterns = [
    path('request-driver/', RequestDriverView.as_view()),
    path('sign-in/', RegisterUserView.as_view(), name='sign-in'),
    path('verify-user/', VerifyUserView.as_view()),
    path('list/', ListUser.as_view()),
    path('profile-info/', UpdateUserInfoView.as_view()),
    path('payment/', PaymentCreateView.as_view()),
    path('payments/', UserPaymentsListView.as_view()),
    path('messages/', ListUserMessageView.as_view()),
    path('me/', AuthMeView.as_view()),
]
