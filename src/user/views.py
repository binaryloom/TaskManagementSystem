from django.contrib import messages
from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.permissions import AllowAny

from abstract.views import CreateAPIView, RedirectView, TemplateView
from user.forms import AuthForm, RegistrationForm
from user.models import User
from user.serializers import RegistrationSerializer


class RedirectView(RedirectView):
    """
    Redirect view.

    This class is a simple redirection view, inheriting from the abstract RedirectView.
    """

    pass


class RegistrationView(CreateAPIView):
    """
    Endpoint for user registration.

    This class provides an API endpoint for user registration, allowing new users to register
    with the system.

    Attributes:
        permission_classes (list): List of permission classes allowed for accessing this endpoint.
        queryset (QuerySet): QuerySet of User model instances.
        serializer_class (Serializer): Serializer class used for validation and serialization of registration data.
    """

    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class DashboardView(TemplateView):
    """
    View for displaying the dashboard.

    This class represents a view for displaying the user dashboard.

    Attributes:
        template_name (str): The name of the template used for rendering the dashboard.
    """

    template_name = "task_management/dashboard.html"


class LoginView(views.LoginView):
    """
    View for user login.

    This class represents a view for user login, inheriting from the Django built-in LoginView.

    Attributes:
        template_name (str): The name of the template used for rendering the login form.
        authentication_form (Form): The form class used for user authentication.
    """

    template_name = "default/form.html"
    authentication_form = AuthForm

    def form_invalid(self, form):
        """
        Handles invalid form submission.

        This method handles the case when the login form submission is invalid,
        displaying an error message to the user.

        Args:
            form (Form): The invalid form instance.

        Returns:
            HttpResponse: The HTTP response with the rendered form and error message.
        """
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(views.LogoutView):
    """
    View for user logout.

    This class represents a view for user logout, inheriting from the Django built-in LogoutView.
    """

    pass


class RegistrationView(CreateView):
    """
    View for user registration.

    This class represents a view for user registration, inheriting from the Django built-in CreateView.

    Attributes:
        model (Model): The model class used for user registration.
        form_class (Form): The form class used for user registration.
        template_name (str): The name of the template used for rendering the registration form.
        success_url (str): The URL to redirect to after successful registration.
    """

    model = User
    form_class = RegistrationForm
    template_name = "default/form.html"
    success_url = reverse_lazy("user:login_view")
