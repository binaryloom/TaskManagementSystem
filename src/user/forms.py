from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, PasswordInput

from user.models import User


class AuthForm(AuthenticationForm):
    """
    Custom authentication form.

    This form extends the default AuthenticationForm provided by Django.

    Attributes:
        username (CharField): Field for entering the username.
        password (PasswordInput): Field for entering the password securely (masked).

    Inherits:
        AuthenticationForm: Base authentication form provided by Django.

    Note:
        This class overrides the username field to allow customizations.
    """

    username = CharField()
    password = PasswordInput()


class RegistrationForm(UserCreationForm):
    """
    Form for user registration.

    This form extends the default UserCreationForm provided by Django for user registration.

    Meta:
        model (User): The user model for which the form is created.
        fields (list): List of fields to be included in the form, including "username", "password1", and "password2".

    Inherits:
        UserCreationForm: Base form provided by Django for user registration.
    """

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
