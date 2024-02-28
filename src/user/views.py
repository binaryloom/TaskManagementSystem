from rest_framework.permissions import AllowAny

from abstract.views import CreateAPIView
from user.models import User
from user.serializers import RegistrationSerializer

# Create your views here.


class RegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
