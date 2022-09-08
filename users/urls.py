from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token

from . import views

urlpatterns = [
    path('users/register/', views.UserRegisterView.as_view(), name='user_register'),
    path('users/login/auth_token/', obtain_auth_token, name='login_auth_token'),
    path('users/login/custom_auth_token/', views.CustomAuthToken.as_view()),
    path('users/login/', views.UserLoginView.as_view(), name='api_token_auth'),
    path('users/', views.UsersListAdminView.as_view()),
    path('users/<int:user_id>/', views.UserDetailView.as_view()),

]
