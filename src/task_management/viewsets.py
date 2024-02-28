from rest_framework import permissions

from abstract.viewsets import ModelViewSet
from task_management.models import Board, List, Task
from task_management.serializers import BoardSerializer, ListSerializer, TaskSerializer


class BoardViewSet(ModelViewSet):
    """
    API endpoint that allows boards to be viewed or edited.
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class ListViewSet(ModelViewSet):
    """
    API endpoint that allows list to be viewed or edited.
    """

    queryset = List.objects.all()
    serializer_class = ListSerializer


class TaskViewSet(ModelViewSet):
    """
    API endpoint that allows task to be viewed or edited.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
