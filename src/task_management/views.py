from django.shortcuts import render

from abstract.views import CreateView, DetailChildView, ListView, UpdateView
from task_management.forms import BoardForm, ListForm, TaskForm
from task_management.models import Board, List, Task


class BoardListView(ListView):
    model = Board
    child_header = "Boards List"
    template_name = "task_management/boards.html"


class ListListView(ListView):
    model = List
    child_header = "Lists"
    template_name = "task_management/lists.html"


class TaskListView(ListView):
    model = Task
    child_header = "Task List"
    template_name = "task_management/tasks.html"


class BoardDetailView(DetailChildView):
    model = Board
    field = "lists"
    child_header = "Linked Lists"
    template_name = "task_management/board.html"


class ListDetailView(DetailChildView):
    model = List
    field = "tasks"
    filter_by_user = False
    child_header = "Linked Tasks"
    template_name = "task_management/list.html"


class TaskDetailView(DetailChildView):
    model = Task
    field = "assigned_to"
    template_name = "task_management/task.html"


class BoardCreateView(CreateView):
    model = Board
    form_class = BoardForm


class ListCreateView(CreateView):
    model = List
    form_class = ListForm


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm


class BoardUpdateView(UpdateView):
    model = Board
    form_class = BoardForm


class ListUpdateView(UpdateView):
    model = List
    form_class = ListForm


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
