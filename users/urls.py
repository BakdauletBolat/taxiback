
from users.views import ListUser, RegisterUserView, VerifyUserView
from django.urls import path 




urlpatterns = [
    path('sign-in/',RegisterUserView.as_view()),
    path('verify-user/',VerifyUserView.as_view()),
    path('list/',ListUser.as_view())
]