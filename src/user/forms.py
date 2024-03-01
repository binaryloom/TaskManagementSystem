from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, PasswordInput

from user.models import User


class AuthForm(AuthenticationForm):
    username = CharField()
    password = PasswordInput()


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
