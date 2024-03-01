from abstract.forms import ModelForm
from task_management.models import Board, List, Task


class BoardForm(ModelForm):
    class Meta(ModelForm.Meta):
        model = Board
        fields = "__all__"


class ListForm(ModelForm):

    class Meta(ModelForm.Meta):
        model = List
        fields = "__all__"


class TaskForm(ModelForm):

    class Meta(ModelForm.Meta):
        model = Task
        exclude_models = ["user.User"]
        fields = "__all__"
