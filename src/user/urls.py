from django.urls import path
from rest_framework import routers

from user.views import DashboardView, HealthCheckView, LoginView, RegistrationView
from user.viewsets import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"group", GroupViewSet)

from django.contrib.auth.views import LogoutView

"""
Defines urlpatterns for user-related views and endpoints.

This module defines the URL patterns for various user-related views and endpoints, including dashboard, login, logout, and registration.

Attributes:
    router (DefaultRouter): Instance of DefaultRouter for registering viewsets.
    urlpatterns (list): List of URL patterns for user-related views and endpoints.

Note:
    This module assumes the existence of views and viewsets imported from user.views and user.viewsets modules.
"""
# fmt: off
urlpatterns = [
    path(route="", view=DashboardView.as_view(), name="dashboard_view"),
    path(route="login", view=LoginView.as_view(), name="login_view"),
    path(route="logout", view=LogoutView.as_view(), name="logout_view"),
    path(route="registration", view=RegistrationView.as_view(), name="registration_view"),
    # health check
    path('healthcheck', HealthCheckView.as_view(), name='healthcheck_view'),
]
# fmt: on
