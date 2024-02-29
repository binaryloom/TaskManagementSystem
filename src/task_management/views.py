from django.shortcuts import render

from abstract.views import DetailView, ListView, TemplateView
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


class BoardDetailView(DetailView):
    model = Board
