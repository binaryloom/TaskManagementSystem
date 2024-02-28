from abstract.views import CreateAPIView
from user.models import User
from user.serializers import RegistrationSerializer

# Create your views here.


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
