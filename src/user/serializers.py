from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import CharField, EmailField, ValidationError
from rest_framework.validators import UniqueValidator

from abstract.serializers import HyperlinkedModelSerializer, ModelSerializer
from user.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "first_name", "last_name", "mobile_no"]


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class RegistrationSerializer(ModelSerializer):
    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
