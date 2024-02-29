from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField


class AuthForm(AuthenticationForm):
    username = CharField()
    password = CharField()
