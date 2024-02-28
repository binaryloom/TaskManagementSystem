from rest_framework import routers

from user.viewsets import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"group", GroupViewSet)
