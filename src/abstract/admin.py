from django.conf import settings

# GuardedModelAdmin, SimpleHistoryAdmin
from django.contrib import admin, messages
from django.http.request import HttpRequest

from abstract.enums import Status

# Register your models here.


@admin.action(description="Mark selected as published")
def make_publish(modeladmin, request, queryset):
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
    actions = [make_publish, make_draft]

    def has_permission(self, request, obj, action):
        # TODO : check permissions
        if not obj:
            return self.get_model_objects(request).exists()
        return request.user.has_perm(
            f"{self.opts.app_label}.{action}_{self.opts.model_name}", obj
        )

    def has_module_permission(self, request):
        return (
            True
            if super().has_module_permission(request)
            else self.get_model_objects(request).exists()
        )

    def get_queryset(self, request):
        return (
            super().get_queryset(request)
            if request.user.is_superuser
            else self.get_model_objects(request)
        )

    def get_model_objects(self, request, klass=None):
        klass = klass or self.opts.model
        permissions_list = [
            f"{perm}_{klass._meta.model_name}"
            for perm in klass._meta.default_permissions
        ] + list(map(lambda item: item[0], klass._meta.permissions))

        return get_objects_for_user(
            user=request.user,
            perms=permissions_list,
            klass=klass or self.opts.model,
            any_perm=True,
        )

    def has_add_permission(self, request, obj=None):
        return super().has_add_permission(request)

    def has_view_permission(self, request, obj=None):
        return (
            True
            if super().has_view_permission(request)
            else self.has_permission(request, obj, "view")
        )

    def has_change_permission(self, request, obj=None):
        return (
            True
            if super().has_change_permission(request)
            else self.has_permission(request, obj, "change")
        )

    def has_delete_permission(self, request, obj=None):
        return (
            True
            if super().has_delete_permission(request)
            else self.has_permission(request, obj, "delete")
        )
