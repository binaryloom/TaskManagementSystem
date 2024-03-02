from django.shortcuts import render
from django.urls import reverse_lazy

from abstract.views import CreateView, DeleteView, DetailChildView, ListView, UpdateView
from task_management.forms import BoardForm, ListForm, TaskForm
from task_management.models import Board, List, Task


class BoardListView(ListView):
    """
    View for listing all boards.

    Displays a list of all boards available in the system.
    """

    model = Board
    child_header = "Boards List"
    template_name = "task_management/boards.html"


class ListListView(ListView):
    """
    View for listing all lists.

    Displays a list of all lists available in the system.
    """

    model = List
    child_header = "Lists"
    template_name = "task_management/lists.html"


class TaskListView(ListView):
    """
    View for listing all tasks.

    Displays a list of all tasks available in the system.
    """

    model = Task
    child_header = "Task List"
    template_name = "task_management/tasks.html"


class BoardDetailView(DetailChildView):
    """
    View for displaying details of a board.

    Displays details of a specific board along with its linked lists.
    """

    model = Board
    field = "lists"
    child_header = "Linked Lists"
    template_name = "task_management/board.html"


class ListDetailView(DetailChildView):
    """
    View for displaying details of a list.

    Displays details of a specific list along with its linked tasks.
    """

    model = List
    field = "tasks"
    child_header = "Linked Tasks"
    template_name = "task_management/list.html"


class TaskDetailView(DetailChildView):
    """
    View for displaying details of a task.

    Displays details of a specific task along with its assigned user (if any).
    """

    model = Task
    filter_by_user = False
    field = "assigned_to"
    child_header = "Task Description"
    template_name = "task_management/task.html"


class BoardCreateView(CreateView):
    """
    View for creating a new board.

    Renders a form to create a new board.
    """

    model = Board
    form_class = BoardForm


class BoardListCreateView(CreateView):
    """
    View for creating a new list within a board.

    Renders a form to create a new list associated with a specific board.
    """

    model = List
    form_class = ListForm

    def get_initial(self):
        initial = super().get_initial()
        initial["assigned_board"] = Board.objects.get(pk=self.kwargs.get("pk"))
        return initial


class ListCreateView(CreateView):
    """
    View for creating a new list.

    Renders a form to create a new list.
    """

    model = List
    form_class = ListForm


class ListTaskCreateView(CreateView):
    """
    View for creating a new task within a list.

    Renders a form to create a new task associated with a specific list.
    """

    model = Task
    form_class = TaskForm

    def get_initial(self):
        initial = super().get_initial()
        initial["assigned_list"] = List.objects.get(pk=self.kwargs.get("pk"))
        return initial


class TaskCreateView(CreateView):
    """
    View for creating a new task.

    Renders a form to create a new task.
    """

    model = Task
    form_class = TaskForm


class BoardUpdateView(UpdateView):
    """
    View for updating a board.

    Renders a form to update an existing board.
    """

    model = Board
    form_class = BoardForm


class ListUpdateView(UpdateView):
    """
    View for updating a list.

    Renders a form to update an existing list.
    """

    model = List
    form_class = ListForm


class TaskUpdateView(UpdateView):
    """
    View for updating a task.

    Renders a form to update an existing task.
    """

    model = Task
    form_class = TaskForm


class BoardDeleteView(DeleteView):
    """
    View for deleting a board.

    Renders a confirmation page to delete an existing board.
    """

    model = Board
    success_url = reverse_lazy("task_management:boardlist_view")


class ListDeleteView(DeleteView):
    """
    View for deleting a list.

    Renders a confirmation page to delete an existing list.
    """

    model = List
    success_url = reverse_lazy("task_management:listlist_view")


class TaskDeleteView(DeleteView):
    """
    View for deleting a task.

    Renders a confirmation page to delete an existing task.
    """

    model = Task
    success_url = reverse_lazy("task_management:tasklist_view")
