from abstract.serializers import HyperlinkedModelSerializer
from task_management.models import Board, List, Task


class BoardSerializer(HyperlinkedModelSerializer):
    """
    Serializer for Board model.

    This serializer serializes Board instances to JSON representations.
    """

    class Meta:
        model = Board
        fields = ["url", "name"]


class ListSerializer(HyperlinkedModelSerializer):
    """
    Serializer for List model.

    This serializer serializes List instances to JSON representations.
    """

    class Meta:
        model = List
        fields = ["url", "name", "assigned_board"]


class TaskSerializer(HyperlinkedModelSerializer):
    """
    Serializer for Task model.

    This serializer serializes Task instances to JSON representations.
    """

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
