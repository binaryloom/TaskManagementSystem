from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.action(description="Recover Selected Items")
def mark_undo(modeladmin, request, queryset):
    """
    Custom admin action to mark selected users as recovered.

    Args:
        modeladmin: The ModelAdmin instance.
        request (HttpRequest): The HTTP request object.
        queryset (QuerySet): The queryset containing the selected users.
    """
    updated_count = queryset.update(is_staff=True)
    modeladmin.message_user(
        request,
        f"Successfully Recovered {updated_count} {modeladmin.model._meta.verbose_name_plural}",
        messages.SUCCESS,
    )


class UserAdmin(UserAdmin):
    search_fields = ("username", "mobile_no", "email")
    ordering = ("username", "email", "first_name", "last_name")

    fieldsets = UserAdmin.fieldsets + (("Custom Fields", {"fields": ("mobile_no",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("mobile_no",)}),)
    actions = [mark_undo]


if settings.ENABLE_ADMIN:
    admin.site.register(User, UserAdmin)
