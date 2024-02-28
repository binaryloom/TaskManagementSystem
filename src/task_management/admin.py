from django.conf import settings
from django.contrib import admin

from abstract.admin import ModelAdmin
from task_management.models import Board, List, Task


class BoardAdmin(ModelAdmin):
    pass


class ListAdmin(ModelAdmin):
    pass


class TaskAdmin(ModelAdmin):
    pass
    # list_display = BaseAdmin.list_display + [
    #     "country",
    #     "branch_count",
    #     "faculty_count",
    #     "discipline_count",
    #     "session_count",
    # ]


if settings.ENABLE_ADMIN:
    admin.site.register(Board, BoardAdmin)
    admin.site.register(List, ListAdmin)
    admin.site.register(Task, TaskAdmin)
