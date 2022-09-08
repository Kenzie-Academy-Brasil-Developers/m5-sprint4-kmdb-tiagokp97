from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
  def has_permission(self, request:Request, view:View)-> bool:
    if request.method in permissions.SAFE_METHODS:
      return True

    return request.user.is_superuser

class IsAdminOrCritic(permissions.IsAuthenticatedOrReadOnly):
  def has_object_permission(self, request, view:View, user:User):
    return request.user == user
  ...
