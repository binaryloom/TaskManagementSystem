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
    """
    A view rendering a form, with login required, inheriting from Django's generic FormView.

    Inherits:
        generic.FormView

    Usage:
        Define your view class inheriting from this class and specify the form_class
        attribute with the appropriate form class.

    Example:
        class MyFormView(FormView):
            form_class = MyForm

    Note:
        Make sure to define the template_name attribute to specify the template for rendering
        the form. By default, it looks for a template with the name <app>/<model>_form.html.
    """

    pass


class ListView(LoginRequiredMixin, generic.ListView):
    """
    A view rendering a list of objects, with login required, inheriting from Django's generic ListView.

    Inherits:
        generic.ListView

    Attributes:
        paginate_by (int): Number of objects to display per page.
        template_name (str): Path to the template for rendering the list view.
        child_header (str): Header for the child view, if applicable.

    Methods:
        get_queryset(): Returns the queryset of objects to display.
        get_context_data(**kwargs): Returns the context data to pass to the template.

    Usage:
        Define your view class inheriting from this class and specify the model attribute
        with the model to list.

    Example:
        class MyListView(ListView):
            model = MyModel

    Notes:
        - The template for rendering the list view is determined by the 'template_name' attribute.
        - Pagination is enabled by default and can be adjusted using the 'paginate_by' attribute.
        - Additional context data can be provided to the template by overriding the 'get_context_data' method.
    """

    paginate_by = 12
    template_name = "default/list.html"
    ordering = ["-updated_by"]
    child_header = None

    def get_queryset(self):
        """
        Retrieve objects related to the main object based on the specified field.

        Args:
            context (dict): The context containing the main object.

        Returns:
            queryset: A queryset containing the related objects filtered based on the user if applicable.
        """
        if self.request.user.is_authenticated:
            return super().get_queryset().filter(created_by=self.request.user)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        """
        Retrieve keyword arguments for form instantiation.

        Returns:
            dict: Keyword arguments for form instantiation including the operating user.
        """
        context = super().get_context_data(**kwargs)
        if self.child_header:
            context["child_header"] = self.child_header
        return context


class DetailView(LoginRequiredMixin, generic.DetailView):
    """
    A view rendering the details of a single object, with login required, inheriting from Django's generic DetailView.

    Inherits:
        generic.DetailView

    Attributes:
        template_name (str): Path to the template for rendering the detail view.

    Usage:
        Define your view class inheriting from this class and specify the model attribute
        with the model whose details are to be displayed.

    Example:
        class MyDetailView(DetailView):
            model = MyModel

    Notes:
        - The template for rendering the detail view is determined by the 'template_name' attribute.
        - The object to display details for is fetched automatically based on the URL parameters.
    """

    template_name = "default/detail.html"


class DetailChildView(DetailView):
    """
    A view rendering details of child objects related to a main object,
    with login required, inheriting from DetailView.

    Inherits:
        DetailView

    Attributes:
        template_name (str): Path to the template for rendering the detail view.
        field (str): The field name specifying the relationship to the child objects.
        child_header (str): Header for the child view, if applicable.
        filter_by_user (bool): Flag indicating whether to filter child objects based on the user.

    Methods:
        get_objects(context): Retrieve child objects related to the main object.
        get_context_data(**kwargs): Retrieve context data including child objects.

    Usage:
        Define your view class inheriting from this class and specify the model attribute
        with the model whose details are to be displayed, along with other necessary attributes.

    Example:
        class MyDetailChildView(DetailChildView):
            model = MyModel
            field = 'related_objects'

    Notes:
        - The template for rendering the detail view is determined by the 'template_name' attribute.
        - Child objects are fetched automatically based on the relationship specified in 'field'.
        - Child objects can be filtered based on the user if 'filter_by_user' is set to True.
    """

    template_name = "default/detail_child.html"
    field = None
    child_header = None
    filter_by_user = True

    def get_objects(self, context):
        """
        Retrieve child objects related to the main object based on the specified field.

        Args:
            context (dict): The context containing the main object.

        Returns:
            queryset: A queryset containing the related child objects, optionally filtered based on the user.
        """
        if self.request.user.is_authenticated and self.filter_by_user:
            return getattr(context["object"], self.field).filter(
                created_by=self.request.user
            )
        return getattr(context["object"], self.field).all()

    def get_context_data(self, **kwargs):
        """
        Retrieve context data including child objects related to the main object.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: Context data including child objects.
        """
        context = super().get_context_data(**kwargs)
        if self.field and hasattr(context["object"], self.field):
            if self.child_header:
                context["child_header"] = self.child_header
            context["object_list"] = self.get_objects(context=context)
        return context


class CreateView(LoginRequiredMixin, edit.CreateView):
    """
    A view for creating new instances of a model, with login required, inheriting from Django's generic CreateView.

    Inherits:
        edit.CreateView

    Attributes:
        template_name (str): Path to the template for rendering the create view.

    Methods:
        get_form_kwargs(): Retrieve keyword arguments for form instantiation.

    Usage:
        Define your view class inheriting from this class and specify the model and form_class attributes.

    Example:
        class MyCreateView(CreateView):
            model = MyModel
            form_class = MyForm

    Notes:
        - The template for rendering the create view is determined by the 'template_name' attribute.
        - The form for creating instances is automatically generated based on the 'form_class' attribute.
        - Additional keyword arguments for form instantiation can be retrieved by overriding the 'get_form_kwargs' method.
    """

    template_name = "default/form.html"

    def get_form_kwargs(self):
        """
        Retrieve keyword arguments for form instantiation.

        Returns:
            dict: Keyword arguments for form instantiation including the operating user.
        """
        kwargs = super().get_form_kwargs()
        kwargs["operating_user"] = self.request.user
        return kwargs


class DeleteView(LoginRequiredMixin, edit.DeleteView):
    """
    A view for deleting an instance of a model, with login required, inheriting from Django's generic DeleteView.

    Inherits:
        edit.DeleteView

    Attributes:
        template_name (str): Path to the template for rendering the delete view.

    Usage:
        Define your view class inheriting from this class and specify the model attribute.

    Example:
        class MyDeleteView(DeleteView):
            model = MyModel

    Notes:
        - The template for rendering the delete view is determined by the 'template_name' attribute.
        - Confirmation of deletion is handled by the associated template.
    """

    template_name = "default/form_delete.html"


class UpdateView(LoginRequiredMixin, edit.UpdateView):
    """
    A view for updating an instance of a model, with login required, inheriting from Django's generic UpdateView.

    Inherits:
        edit.UpdateView

    Attributes:
        template_name (str): Path to the template for rendering the update view.

    Methods:
        get_form_kwargs(): Retrieve keyword arguments for form instantiation.

    Usage:
        Define your view class inheriting from this class and specify the model attribute.

    Example:
        class MyUpdateView(UpdateView):
            model = MyModel

    Notes:
        - The template for rendering the update view is determined by the 'template_name' attribute.
        - The form for updating instances is automatically generated based on the model.
        - Additional keyword arguments for form instantiation can be retrieved by overriding the 'get_form_kwargs' method.
    """

    template_name = "default/form.html"

    def get_form_kwargs(self):
        """
        Retrieve keyword arguments for form instantiation.

        Returns:
            dict: Keyword arguments for form instantiation including the operating user.
        """
        kwargs = super().get_form_kwargs()
        kwargs["operating_user"] = self.request.user
        return kwargs


class RedirectView(base.RedirectView):
    """
    A view for redirecting to a specified URL, inheriting from Django's generic RedirectView.

    Inherits:
        base.RedirectView

    Attributes:
        permanent (bool): Flag indicating whether the redirection is permanent.
        url (str): URL to redirect to.

    Usage:
        Define your view class inheriting from this class and specify the 'url' attribute.

    Example:
        class MyRedirectView(RedirectView):
            url = '/my-redirect-url/'

    Notes:
        - The 'permanent' attribute determines whether the redirection is permanent (HTTP status code 301) or temporary (HTTP status code 302).
        - The 'url' attribute specifies the destination URL to redirect to.
    """

    permanent = False
    url = reverse_lazy("user:login_view")
