from django.urls import path
from rest_framework import routers

from user.views import DashboardView
from user.viewsets import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"group", GroupViewSet)


# fmt: off
urlpatterns = [
    path(route="", view=DashboardView.as_view(), name="dashboard_view"),
]
# fmt: on
