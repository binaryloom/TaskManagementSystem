from abstract.serializers import HyperlinkedModelSerializer
from task_management.models import Board, List, Task


class BoardSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class ListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class TaskSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
