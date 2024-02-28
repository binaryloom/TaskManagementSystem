from django.shortcuts import render

from abstract.views import ListView, TemplateView
from task_management.models import Board, List, Task

# Create your views here.


class DashboardView(TemplateView):
    template_name = "task_management/dashboard.html"


class BoardListView(ListView):
    model = Board
    template_name = "task_management/boards.html"


class ListListView(ListView):
    model = List


class TaskListView(ListView):
    model = Task
