from django.urls import path
from rest_framework import routers

from task_management.views import (
    BoardListView,
    DashboardView,
    ListListView,
    TaskListView,
)
from task_management.viewsets import BoardViewSet, ListViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"board", BoardViewSet)
router.register(r"list", ListViewSet)
router.register(r"task", TaskViewSet)


# fmt: off
urlpatterns = [
    path(route="", view=DashboardView.as_view(), name="dashboard_view"),
    path(route="boards/", view=DashboardView.as_view(), name="dashboard_view"),
    path(route="", view=DashboardView.as_view(), name="dashboard_view"),
    path(route="", view=DashboardView.as_view(), name="dashboard_view"),
]
# fmt: on
