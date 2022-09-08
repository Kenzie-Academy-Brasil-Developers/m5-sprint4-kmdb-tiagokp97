from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from rest_framework.views import APIView, Request, Response, status

from .models import User
from .permissions import IsAdminOrReadOnly, IsAdminUser, OwnerOrAdmin
from .serializers import UserSerializer


class UsersListAdminView(APIView, PageNumberPagination):
  permission_classes = [IsAdminUser]
  
  def get(self, request: Request) -> Response:
    users = User.objects.all()
    
    result_page = self.paginate_queryset(users, request, view=self)
    
    serializer = UserSerializer(result_page, many=True)

    return self.get_paginated_response(serializer.data)

class UserDetailView(APIView):
  permission_classes = [OwnerOrAdmin]

  def get(self, request: Request, user_id:int)-> Response:
    user = get_object_or_404(User, id=user_id)
    self.check_object_permissions(request, user)
    serializer = UserSerializer(user)

    return Response(serializer.data, status.HTTP_200_OK)
    

class UserRegisterView(APIView):
  def post (self, request: Request) -> Response:
    serializer = UserSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    serializer.save()

    return Response(serializer.data, status.HTTP_201_CREATED)


class UserLoginView(ObtainAuthToken):
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

  def post (self, request: Request) -> Response:
    serializer = self.serializer_class(
      data=request.data, context={'request': request}
    )
    
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']
    token, _ = Token.objects.get_or_create(user=user)

    return Response({
      'token': token.key,
    })

class CustomAuthToken(ObtainAuthToken):
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

  def post(self, request:Request, *args, **kwargs):
    serializer = self.serializer_class(
      data=request.data, context={'request': request}
    )

    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)

    return Response({
      'token': token.key,
      'user_id': user.id,
      'is_superuser': user.is_superuser,
      'is_critic': user.is_critic,
    })
