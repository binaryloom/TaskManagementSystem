from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import CharField, EmailField, ValidationError
from rest_framework.validators import UniqueValidator

from abstract.serializers import HyperlinkedModelSerializer, ModelSerializer
from user.models import User


class UserSerializer(HyperlinkedModelSerializer):
    """
    Serializer for the User model.

    This serializer is used to serialize User objects into JSON representations
    and vice versa, particularly for use in RESTful APIs.

    Meta:
        model (User): The user model for which the serializer is created.
        fields (list): List of fields to be included in the serialized representation.

    Attributes:
        url (HyperlinkedIdentityField): Hyperlinked field representing the URL of the user object.
        first_name (CharField): Field for the user's first name.
        last_name (CharField): Field for the user's last name.
        mobile_no (CharField): Field for the user's mobile number.

    Note:
        This serializer is tailored for the User model.
    """

    class Meta:
        model = User
        fields = ["url", "first_name", "last_name", "mobile_no"]


class GroupSerializer(HyperlinkedModelSerializer):
    """
    Serializer for the Group model.

    This serializer is used to serialize Group objects into JSON representations
    and vice versa, particularly for use in RESTful APIs.

    Meta:
        model (Group): The group model for which the serializer is created.
        fields (list): List of fields to be included in the serialized representation.

    Attributes:
        url (HyperlinkedIdentityField): Hyperlinked field representing the URL of the group object.
        name (CharField): Field for the group's name.

    Note:
        This serializer is tailored for the Group model.
    """

    class Meta:
        model = Group
        fields = ["url", "name"]


class RegistrationSerializer(ModelSerializer):
    """
    Serializer for user registration.

    This serializer is used to handle user registration requests, including
    validation of user input and creation of user accounts.

    Attributes:
        email (EmailField): Field for the user's email address.
        password (CharField): Field for the user's password.
        password2 (CharField): Field for confirming the user's password.
        username (CharField): Field for the user's username.
        first_name (CharField): Field for the user's first name.
        last_name (CharField): Field for the user's last name.

    Methods:
        validate(): Method to validate the serializer's data, ensuring password fields match.
        create(): Method to create a new user account based on validated data.

    Meta:
        model (User): The user model for which the serializer is created.
        fields (list): List of fields to be included in the serialized representation.
        extra_kwargs (dict): Additional keyword arguments for serializer fields.

    Note:
        This serializer is designed specifically for user registration.
    """

    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    def validate(self, attrs):
        """
        Validate password fields.

        This method ensures that the password and password2 fields match.

        Args:
            attrs (dict): The dictionary containing the serializer's data.

        Returns:
            dict: The validated data dictionary.

        Raises:
            ValidationError: If the password fields do not match.
        """
        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        """
        Create a new user account.

        This method creates a new user account based on the provided validated data.

        Args:
            validated_data (dict): The dictionary containing the validated serializer data.

        Returns:
            User: The newly created user object.
        """
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

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
