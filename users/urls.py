
from users.views import AuthMeView, ListUser, RegisterUserView, RequestDriverView, UpdateProfileInfoView, UpdateProfileInfoView, VerifyUserView
from django.urls import path 




urlpatterns = [
    path('sign-in/',RegisterUserView.as_view()),
    path('verify-user/',VerifyUserView.as_view()),
    path('list/',ListUser.as_view()),
    path('request-driver/',RequestDriverView.as_view()),
    path('profile-info/',UpdateProfileInfoView.as_view()),
    path('me/',AuthMeView.as_view()),
]