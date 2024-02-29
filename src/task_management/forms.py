from abstract.forms import ModelForm
from task_management.models import Board, List, Task


class BoardForm(ModelForm):
    class Meta:
        model = Board


class ListForm(ModelForm):
    class Meta:
        model = List


class TaskForm(ModelForm):
    class Meta:
        model = Task
