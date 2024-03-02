from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import base, edit
from rest_framework import generics


class CreateAPIView(generics.CreateAPIView):
    """
    A view for creating instances of a model using Django REST Framework's CreateAPIView.

    Inherits:
        generics.CreateAPIView

    Usage:
        Define your view class inheriting from this class and specify the serializer_class
        attribute with the appropriate serializer for creating instances.

    Example:
        class MyCreateAPIView(CreateAPIView):
            serializer_class = MyModelSerializer
    """

    pass


class View(LoginRequiredMixin, generic.View):
    """
    A base view class with login required, inheriting from Django's generic View.

    Inherits:
        generic.View

    Usage:
        Define your view class inheriting from this class and implement the appropriate
        HTTP methods (e.g., get, post, etc.).

    Example:
        class MyView(View):
            def get(self, request, *args, **kwargs):
                # implement get method logic
    """

    pass


class TemplateView(LoginRequiredMixin, generic.TemplateView):
    """
    A view rendering a template, with login required, inheriting from Django's generic TemplateView.

    Inherits:
        generic.TemplateView

    Usage:
        Define your view class inheriting from this class and specify the template_name
        attribute with the path to the template to render.

    Example:
        class MyTemplateView(TemplateView):
            template_name = "my_template.html"
    """

    pass


class FormView(LoginRequiredMixin, generic.FormView):
    pass


class ListView(LoginRequiredMixin, generic.ListView):
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


class DetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "default/detail.html"


class DetailChildView(DetailView):
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


class CreateView(LoginRequiredMixin, edit.CreateView):
    template_name = "default/form.html"

    def get_form_kwargs(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        kwargs = super().get_form_kwargs()
        kwargs["operating_user"] = self.request.user
        return kwargs


class DeleteView(LoginRequiredMixin, edit.DeleteView):
    template_name = "default/form_delete.html"


class UpdateView(LoginRequiredMixin, edit.UpdateView):
    template_name = "default/form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["operating_user"] = self.request.user
        return kwargs


class RedirectView(base.RedirectView):
    permanent = False
    url = reverse_lazy("user:login_view")
