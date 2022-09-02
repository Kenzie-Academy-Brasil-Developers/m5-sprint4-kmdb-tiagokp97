
from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair

from users.views import LoginView, UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", token_obtain_pair),
]
