from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User


class IsAdminUser(permissions.IsAdminUser):
  def has_permission(self, request, view):
    return bool(request.user and request.user.is_superuser)

class IsAdminOrReadOnly(permissions.BasePermission):
  def has_permission(self, request: Request, view: View):
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return request.user.is_superuser

class OwnerOrAdmin(permissions.BasePermission):
  def has_object_permission(self, request: Request, view:View, user:User):
    return request.user == user or request.user.is_superuser
