from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

admin.site.register(User)

class customUserAdmin(UserAdmin):
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        ("Credentials", {"Fields": ("username", "password")}),
        ("Permissions", {"Fields": ("is_super_user", "is_active")}),
        ("Important Date", {"Fields": ("date_joined", "last_login")}),
        )
