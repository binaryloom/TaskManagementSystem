from abstract.forms import ModelForm
from task_management.models import Board, List, Task


class BoardForm(ModelForm):
    """
    Form for creating and updating Board instances.
    """

    class Meta(ModelForm.Meta):
        model = Board
        fields = "__all__"


class ListForm(ModelForm):
    """
    Form for creating and updating List instances.
    """

    class Meta(ModelForm.Meta):
        model = List
        fields = "__all__"


class TaskForm(ModelForm):
    """
    Form for creating and updating Task instances.
    """

    class Meta(ModelForm.Meta):
        model = Task
        fields = "__all__"
