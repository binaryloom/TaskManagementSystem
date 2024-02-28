from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


class UserAdmin(UserAdmin):
    search_fields = ("username", "password")
    ordering = ("username", "email")


if settings.ENABLE_ADMIN:
    admin.site.register(User, UserAdmin)
