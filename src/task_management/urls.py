from rest_framework import routers

from task_management.viewsets import BoardViewSet, ListViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"board", BoardViewSet)
router.register(r"list", ListViewSet)
router.register(r"task", TaskViewSet)
