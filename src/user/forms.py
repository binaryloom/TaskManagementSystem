from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, PasswordInput


class AuthForm(AuthenticationForm):
    username = CharField()
    password = PasswordInput()


class RegistrationForm(UserCreationForm):
    username = CharField()
    password1 = CharField()
    password2 = CharField()
