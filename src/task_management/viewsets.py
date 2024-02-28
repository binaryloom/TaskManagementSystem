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
    permission_classes = [permissions.IsAuthenticated]
