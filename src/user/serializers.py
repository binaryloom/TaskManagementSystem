from django.contrib.auth.models import Group

from abstract.serializers import HyperlinkedModelSerializer
from user.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
