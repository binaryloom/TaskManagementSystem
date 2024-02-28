from abstract.serializers import HyperlinkedModelSerializer
from task_management.models import Board, List, Task


class BoardSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ["url", "name"]


class ListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ["url", "name", "assigned_board"]


class TaskSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = [
            "url",
            "title",
            "description",
            "assigned_list",
            "assigned_to",
            "due_date",
        ]
