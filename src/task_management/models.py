from abstract.models import BaseModel
from abstract.enums import CellSize
from django.db.models import CharField, ForeignKey, TextField, CASCADE, DO_NOTHING
from django.conf import settings

# Create your models here.


class Board(BaseModel):
    name = CharField(max_length=CellSize.XL)

    def __str__(self):
        return self.name

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_board"
        verbose_name_plural = "Boards"


class List(BaseModel):
    name = CharField(max_length=CellSize.LARGE)
    board = ForeignKey("task_management.board", related_name="lists", on_delete=CASCADE)

    class Meta:
        managed = settings.MANAGE_DATABASE
        db_table = "task_list"
        verbose_name_plural = "Lists"


class Task(BaseModel):
    title = CharField(max_length=100)
    description = TextField()
    list = models.ForeignKey(List, related_name="tasks", on_delete=CASCADE)
    assigned_to = models.ManyToManyField(
        User, related_name="tasks_assigned_to", blank=True
    )
    due_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
