from django.conf import settings
from django.contrib import admin

from abstract.admin import ModelAdmin
from task_management.models import Board, List, Task


class BoardAdmin(ModelAdmin):
    """
    Admin configuration for the Board model.
    """

    pass


class ListAdmin(ModelAdmin):
    """
    Admin configuration for the List model.
    """

    pass


class TaskAdmin(ModelAdmin):
    """
    Admin configuration for the Task model.
    """

    pass


if settings.ENABLE_ADMIN:
    admin.site.register(Board, BoardAdmin)
    admin.site.register(List, ListAdmin)
    admin.site.register(Task, TaskAdmin)
