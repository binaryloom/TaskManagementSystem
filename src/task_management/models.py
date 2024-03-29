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
from django.urls import reverse_lazy

from abstract.enums import CellSize
from abstract.models import BaseModel


class Board(BaseModel):
    """
    Model representing a board.
    """

    name = CharField(max_length=255)

    def __str__(self):
        """
        Return string representation of the board.
        """
        return self.name

    def get_absolute_url(self):
        """
        Return the absolute URL to view the board.
        """
        return reverse_lazy("task_management:boarddetail_view", kwargs={"pk": self.pk})

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_board"
        verbose_name_plural = "Boards"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []


class List(BaseModel):
    """
    Model representing a list.
    """

    name = CharField(max_length=100)
    assigned_board = ForeignKey(
        "task_management.Board", related_name="lists", on_delete=CASCADE
    )

    def __str__(self):
        """
        Return string representation of the list.
        """
        return self.name

    def get_absolute_url(self):
        """
        Return the absolute URL to view the list.
        """
        return reverse_lazy("task_management:listdetail_view", kwargs={"pk": self.pk})

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_list"
        verbose_name_plural = "Lists"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []


class Task(BaseModel):
    """
    Model representing a task.
    """

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
        """
        Return string representation of the task.
        """
        return self.title

    def get_absolute_url(self):
        """
        Return the absolute URL to view the task.
        """
        return reverse_lazy("task_management:taskdetail_view", kwargs={"pk": self.pk})

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_task"
        verbose_name_plural = "Tasks"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
