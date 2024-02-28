from django.conf import settings
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    CharField,
    DateField,
    ForeignKey,
    ManyToManyField,
    TextField,
)

from abstract.enums import CellSize
from abstract.models import BaseModel


class Board(BaseModel):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_board"
        verbose_name_plural = "Boards"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []


class List(BaseModel):
    name = CharField(max_length=100)
    assigned_board = ForeignKey(
        "task_management.Board", related_name="lists", on_delete=CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_list"
        verbose_name_plural = "Lists"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []


class Task(BaseModel):
    title = CharField(max_length=100)
    description = TextField(max_length=1000, null=True, blank=True)
    assigned_list = ForeignKey(
        "task_management.List", related_name="tasks", on_delete=CASCADE
    )
    assigned_to = ManyToManyField(
        "user.User", related_name="assigned_tasks", blank=True
    )
    due_date = DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_task"
        verbose_name_plural = "Tasks"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
