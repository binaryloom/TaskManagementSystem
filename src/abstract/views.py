from django.views import generic
from django.views.generic import edit
from rest_framework import generics


class CreateAPIView(generics.CreateAPIView):
    pass


class View(generic.View):
    pass


class TemplateView(generic.TemplateView):
    pass


class FormView(generic.FormView):
    pass


class ListView(generic.ListView):
    paginate_by = 12
    template_name = "default/list.html"


class DetailView(generic.DetailView):
    template_name = "default/detail.html"


class DetailChildView(DetailView):
    template_name = "default/detail.html"
    field = None


class CreateView(edit.CreateView):
    template_name = "default/form.html"


class DeleteView(edit.DeleteView):
    template_name = "default/form_delete.html"


class UpdateView(edit.UpdateView):
    template_name = "default/form.html"
