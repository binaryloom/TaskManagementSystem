from django.shortcuts import render

from abstract.views import ListView, TemplateView
from task_management.models import Board, List, Task

# Create your views here.


class DashboardView(TemplateView):
    template_name = "task_management/dashboard.html"


class BoardListView(ListView):
    model = Board


class ListListView(ListView):
    model = Board


class TaskListView(ListView):
    model = Board
