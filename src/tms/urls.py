"""
URL configuration for tms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_registration.api.views import (
    change_password,
    login,
    logout,
    profile,
    register,
)

from task_management.urls import router as task_management_router
from user.urls import router as user_router
from user.views import RedirectView, RegistrationView

urlpatterns = [
    path("auth/login/", login, name="login"),
    path("auth/logout/", logout, name="logout"),
    path("auth/profile/", profile, name="profile"),
    path("auth/register/", register, name="register"),
    path("auth/password/change/", change_password, name="change_password"),
    path("auth/jwt/", TokenObtainPairView.as_view(), name="jwt_auth"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/registration/", RegistrationView.as_view(), name="registration"),
]


router = DefaultRouter()
router.registry.extend(task_management_router.registry)
router.registry.extend(user_router.registry)

urlpatterns = urlpatterns + [
    path("api/", include(router.urls)),
    path(
        route="board/",
        view=include(
            arg=("task_management.urls", "task_management"),
            namespace="task_management",
        ),
    ),
    path(
        route="",
        view=include(
            arg=("user.urls", "user"),
            namespace="user",
        ),
    ),
    path("accounts/login/", RedirectView.as_view(), name="redirect_view"),
]

# URL SECTION
urlpatterns = urlpatterns + [
    path("admin/", admin.site.urls),
    # browser reload
    path("__reload__/", include("django_browser_reload.urls")),
]
