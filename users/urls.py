from users.views import AuthMeView, ListUser, PaymentCreateView, RegisterUserView, RequestDriverView, \
    UpdateProfileInfoView, UpdateProfileInfoView, UserPaymentsListView, VerifyUserView
from django.urls import path

urlpatterns = [
    path('sign-in/', RegisterUserView.as_view()),
    path('verify-user/', VerifyUserView.as_view()),
    path('list/', ListUser.as_view()),
    path('request-driver/', RequestDriverView.as_view()),
    path('profile-info/', UpdateProfileInfoView.as_view()),
    path('payment/', PaymentCreateView.as_view()),
    path('payments/', UserPaymentsListView.as_view()),
    path('me/', AuthMeView.as_view()),
]
