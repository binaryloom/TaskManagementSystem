from django.urls import path
from rest_framework import routers

from user.views import DashboardView, LoginView, RegistrationView
from user.viewsets import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"group", GroupViewSet)

from django.contrib.auth.views import LogoutView

# fmt: off
urlpatterns = [
    path(route="", view=DashboardView.as_view(), name="dashboard_view"),
    path(route="login", view=LoginView.as_view(), name="login_view"),
    path(route="logout", view=LogoutView.as_view(), name="logout_view"),
    path(route="registration", view=RegistrationView.as_view(), name="registration_view"),
]
# fmt: on
