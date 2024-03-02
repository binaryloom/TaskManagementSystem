from django.urls import path
from rest_framework import routers

from task_management.views import (
    BoardCreateView,
    BoardDeleteView,
    BoardDetailView,
    BoardListCreateView,
    BoardListView,
    BoardUpdateView,
    ListCreateView,
    ListDeleteView,
    ListDetailView,
    ListListView,
    ListTaskCreateView,
    ListUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
)
from task_management.viewsets import BoardViewSet, ListViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"board", BoardViewSet)
router.register(r"list", ListViewSet)
router.register(r"task", TaskViewSet)

"""
This module defines URL patterns for task management application.

Each URL pattern maps to a specific view in the application. The urlpatterns list contains individual URL patterns for various views:

- For board-related views:
    - boardlist_view: Lists all boards.
    - boardcreate_view: Renders form for creating a new board.
    - boarddetail_view: Displays details of a specific board.
    - boardlistcreate_view: Renders form for creating a new list within a board.
    - boardupdate_view: Renders form for updating a specific board.
    - boarddelete_view: Renders confirmation page for deleting a specific board.

- For list-related views:
    - listlist_view: Lists all lists.
    - listcreate_view: Renders form for creating a new list.
    - listdetail_view: Displays details of a specific list.
    - listtaskcreate_view: Renders form for creating a new task within a list.
    - listupdate_view: Renders form for updating a specific list.
    - listdelete_view: Renders confirmation page for deleting a specific list.

- For task-related views:
    - tasklist_view: Lists all tasks.
    - taskcreate_view: Renders form for creating a new task.
    - taskdetail_view: Displays details of a specific task.
    - taskupdate_view: Renders form for updating a specific task.
    - taskdelete_view: Renders confirmation page for deleting a specific task.
"""
# fmt: off
urlpatterns = [
    path(route="", view=BoardListView.as_view(), name="boardlist_view"),
    path(route="add", view=BoardCreateView.as_view(), name="boardcreate_view"),
    path(route="<int:pk>",view=BoardDetailView.as_view(),name="boarddetail_view"),
    path(route="<int:pk>/add", view=BoardListCreateView.as_view(), name="boardlistcreate_view"),
    path(route="<int:pk>/update",view=BoardUpdateView.as_view(),name="boardupdate_view"),
    path(route="<int:pk>/delete",view=BoardDeleteView.as_view(),name="boarddelete_view"),

    path(route="lists/", view=ListListView.as_view(), name="listlist_view"),
    path(route="lists/add", view=ListCreateView.as_view(), name="listcreate_view"),
    path(route="lists/<int:pk>",view=ListDetailView.as_view(),name="listdetail_view"),
    path(route="lists/<int:pk>/add", view=ListTaskCreateView.as_view(), name="listtaskcreate_view"),
    path(route="lists/<int:pk>/update",view=ListUpdateView.as_view(),name="listupdate_view"),
    path(route="lists/<int:pk>/delete",view=ListDeleteView.as_view(),name="listdelete_view"),
    
    path(route="lists/tasks/", view=TaskListView.as_view(), name="tasklist_view"),
    path(route="lists/tasks/add", view=TaskCreateView.as_view(), name="taskcreate_view"),
    path(route="lists/tasks/<int:pk>",view=TaskDetailView.as_view(),name="taskdetail_view"),
    path(route="lists/tasks/<int:pk>/update",view=TaskUpdateView.as_view(),name="taskupdate_view"),
    path(route="lists/tasks/<int:pk>/delete",view=TaskDeleteView.as_view(),name="taskdelete_view"),
]
# fmt: on
