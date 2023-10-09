from django.contrib.auth.forms import AuthenticationForm
from .models import User

class Login(AuthenticationForm):
    '''Авторизация'''
    class Meta:
        model = User
        fields = ['username', 'password']