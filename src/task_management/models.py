from abstract.models import BaseModel
from abstract.enums import CellSize
from django.db.models import CharField

# Create your models here.


class Board(BaseModel):
    name = CharField(max_length=CellSize.XL)

    def __str__(self):
        return self.name


class List(BaseModel):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, related_name="lists", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    list = models.ForeignKey(List, related_name="tasks", on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(
        User, related_name="tasks_assigned_to", blank=True
    )
    due_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
