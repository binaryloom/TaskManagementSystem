from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import edit
from rest_framework import generics


class CreateAPIView(generics.CreateAPIView):
    pass


class View(generic.View, LoginRequiredMixin):
    pass


class TemplateView(generic.TemplateView, LoginRequiredMixin):
    pass


class FormView(generic.FormView, LoginRequiredMixin):
    pass


class ListView(generic.ListView, LoginRequiredMixin):
    paginate_by = 12
    template_name = "default/list.html"
    child_header = None

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super().get_queryset().filter(created_by=self.request.user)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.child_header:
            context["child_header"] = self.child_header
        return context


class DetailView(generic.DetailView, LoginRequiredMixin):
    template_name = "default/detail.html"


class DetailChildView(DetailView, LoginRequiredMixin):
    template_name = "default/detail_child.html"
    field = None
    child_header = None
    filter_by_user = True

    def get_objects(self, context):
        if self.request.user.is_authenticated and self.filter_by_user:
            return getattr(context["object"], self.field).filter(
                created_by=self.request.user
            )
        return getattr(context["object"], self.field).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.field and hasattr(context["object"], self.field):
            if self.child_header:
                context["child_header"] = self.child_header
            context["object_list"] = self.get_objects(context=context)
        return context


class CreateView(edit.CreateView, LoginRequiredMixin):
    template_name = "default/form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["operating_user"] = self.request.user
        return kwargs


class DeleteView(edit.DeleteView, LoginRequiredMixin):
    template_name = "default/form_delete.html"


class UpdateView(edit.UpdateView, LoginRequiredMixin):
    template_name = "default/form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["operating_user"] = self.request.user
        return kwargs
