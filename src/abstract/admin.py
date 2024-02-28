from django.conf import settings

# GuardedModelAdmin, SimpleHistoryAdmin
from django.contrib import admin, messages
from django.http.request import HttpRequest

from abstract.enums import Status

# Register your models here.


@admin.action(description="Recover Selected Items")
def mark_undo(modeladmin, request, queryset):
    updated_count = queryset.update(status=Status.PUBLISHED)
    modeladmin.message_user(
        request,
        f"Successfully published {updated_count} {modeladmin.model._meta.verbose_name_plural}",
        messages.SUCCESS,
    )


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 12

    # exclude = ['status']
    # actions_on_top = False
    def delete_queryset(self, request, queryset):
        queryset.update(status=Status.DELETED)

    list_display = ["__str__", "status"]
    actions = [mark_undo]
