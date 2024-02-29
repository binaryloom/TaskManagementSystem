from django.urls import path
from rest_framework import routers

from task_management.views import (
    BoardDetailView,
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
    path(route="boards/", view=BoardListView.as_view(), name="boardlist_view"),
    path(route="lists/", view=ListListView.as_view(), name="listlist_view"),
    path(route="tasks/", view=TaskListView.as_view(), name="tasklist_view"),
]
# fmt: on
