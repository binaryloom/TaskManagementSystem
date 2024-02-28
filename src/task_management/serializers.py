from abstract.serializers import HyperlinkedModelSerializer
from task_management.models import Board, List, Task


class BoardSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ["name"]


class ListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ["name", "assigned_board"]


class TaskSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "assigned_list", "due_date"]
