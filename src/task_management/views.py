from django.shortcuts import render

from abstract.views import DetailChildView, DetailView, ListView, TemplateView
from task_management.models import Board, List, Task

# Create your views here.


class DashboardView(TemplateView):
    template_name = "task_management/dashboard.html"


class BoardListView(ListView):
    model = Board
    template_name = "task_management/boards.html"


class ListListView(ListView):
    model = List
    template_name = "task_management/lists.html"


class TaskListView(ListView):
    model = Task
    template_name = "task_management/tasks.html"


class BoardDetailView(DetailChildView):
    model = Board
    field = "lists"
    template_name = "task_management/board.html"


class ListDetailView(DetailChildView):
    model = List
    field = "tasks"
    template_name = "task_management/list.html"


class TaskDetailView(DetailChildView):
    model = Task
    field = "assigned_to"
    template_name = "task_management/task.html"
