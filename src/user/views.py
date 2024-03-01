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
    pass


class RegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class DashboardView(TemplateView):
    template_name = "task_management/dashboard.html"


class LoginView(views.LoginView):
    template_name = "default/form.html"
    authentication_form = AuthForm

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(views.LogoutView):
    pass


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "default/form.html"
    success_url = reverse_lazy("user:login_view")
