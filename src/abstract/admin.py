from django.conf import settings
from django.contrib import admin, messages


@admin.action(description="Recover Selected Items")
def mark_undo(modeladmin, request, queryset):
    """
    Custom admin action to mark selected items as recovered.

    Args:
        modeladmin: The ModelAdmin instance.
        request (HttpRequest): The HTTP request object.
        queryset (QuerySet): The queryset containing the selected items.
    """
    updated_count = queryset.update(status=True)
    modeladmin.message_user(
        request,
        f"Successfully Recovered {updated_count} {modeladmin.model._meta.verbose_name_plural}",
        messages.SUCCESS,
    )


class ModelAdmin(admin.ModelAdmin):
    """
    Custom ModelAdmin class with additional functionalities.

    Attributes:
        list_per_page (int): Number of items to display per page in the admin list view.
        exclude (list): List of fields to exclude from the admin interface.
        list_display (list): List of fields to display in the admin list view.
        actions (list): List of custom actions to perform on selected items in the admin interface.
    """

    list_per_page = 12
    exclude = ["status", "created_by", "updated_by"]
    list_display = ["__str__", "status", "created_by", "updated_by"]
    actions = [mark_undo]

    def delete_queryset(self, request, queryset):
        """
        Custom action to soft-delete selected items in the queryset.

        Args:
            request (HttpRequest): The HTTP request object.
            queryset (QuerySet): The queryset containing the selected items to delete.
        """
        queryset.update(status=False)
