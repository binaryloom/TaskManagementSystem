from django.contrib.auth.models import Group

from abstract.serializers import HyperlinkedModelSerializer
from user.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "first_name", "last_name", "mobile_no"]


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
