from django.urls import path
from rest_framework import routers

from task_management.views import (
    BoardCreateView,
    BoardDetailView,
    BoardListView,
    BoardUpdateView,
    ListCreateView,
    ListDetailView,
    ListListView,
    ListUpdateView,
    TaskCreateView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
)
from task_management.viewsets import BoardViewSet, ListViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"board", BoardViewSet)
router.register(r"list", ListViewSet)
router.register(r"task", TaskViewSet)


# fmt: off
urlpatterns = [
    path(route="", view=BoardListView.as_view(), name="boardlist_view"),
    path(route="add", view=BoardCreateView.as_view(), name="boardcreate_view"),
    path(route="<int:pk>",view=BoardDetailView.as_view(),name="boarddetail_view"),
    path(route="lists/add", view=BoardCreateView.as_view(), name="boardlistcreate_view"),
    path(route="<int:pk>/update",view=BoardUpdateView.as_view(),name="boardupdate_view"),
    path(route="lists/", view=ListListView.as_view(), name="listlist_view"),
    path(route="lists/add", view=ListCreateView.as_view(), name="listcreate_view"),
    path(route="lists/<int:pk>",view=ListDetailView.as_view(),name="listdetail_view"),
    path(route="lists/task/add", view=BoardCreateView.as_view(), name="boardcreate_view"),
    path(route="lists/<int:pk>/update",view=ListUpdateView.as_view(),name="listupdate_view"),
    path(route="tasks/", view=TaskListView.as_view(), name="tasklist_view"),
    path(route="tasks/add", view=TaskCreateView.as_view(), name="taskcreate_view"),
    path(route="tasks/<int:pk>",view=TaskDetailView.as_view(),name="taskdetail_view"),
    path(route="tasks/<int:pk>/update",view=TaskUpdateView.as_view(),name="taskupdate_view"),
]
# fmt: on
