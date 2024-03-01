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
    child_header = None

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.child_header:
            context["child_header"] = self.child_header
        return context


class DetailView(generic.DetailView):
    template_name = "default/detail.html"


class DetailChildView(DetailView):
    template_name = "default/detail_child.html"
    field = None
    child_header = None
    filter_by_user = True

    def get_objects ()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.field and hasattr(context["object"], self.field):
            if self.child_header:
                context["child_header"] = self.child_header
            context["object_list"] = getattr(context["object"], self.field).filter(
                created_by=self.request.user
            )
        return context


class CreateView(edit.CreateView):
    template_name = "default/form.html"


class DeleteView(edit.DeleteView):
    template_name = "default/form_delete.html"


class UpdateView(edit.UpdateView):
    template_name = "default/form.html"
