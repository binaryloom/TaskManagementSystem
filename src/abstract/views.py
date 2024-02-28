from rest_framework.generics import CreateAPIView


class CreateAPIView(CreateAPIView):
    pass


from django.views.generic import DetailView, FormView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class View(View):
    pass


class TemplateView(TemplateView):
    pass


class FormView(FormView):
    pass


class ListView(ListView):
    paginate_by = 12
    template_name = "default/list.html"


class DetailView(DetailView):
    template_name = "default/detail.html"


class CreateView(CreateView):
    template_name = "default/form.html"


class DeleteView(DeleteView):
    template_name = "default/form_delete.html"


class UpdateView(UpdateView):
    template_name = "default/form.html"
