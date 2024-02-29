from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.permissions import AllowAny

from abstract.views import CreateAPIView, TemplateView
from user.forms import AuthForm
from user.models import User
from user.serializers import RegistrationSerializer


class RegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class DashboardView(TemplateView):
    template_name = "task_management/dashboard.html"


class LoginView(LoginView):
    template_name = "login.html"
    authentication_form = AuthForm

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(LogoutView):
    pass
