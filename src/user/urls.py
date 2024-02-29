from django.urls import path
from rest_framework import routers

from user.views import DashboardView, LoginView, LogoutView
from user.viewsets import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"group", GroupViewSet)


# fmt: off
urlpatterns = [
    path(route="", view=DashboardView.as_view(), name="dashboard_view"),
    path(route="login", view=LoginView.as_view(), name="login_view"),
    path(route="logout", view=LogoutView.as_view(), name="logout_view"),
]
# fmt: on
