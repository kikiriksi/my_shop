from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class Login(AuthenticationForm):
    '''Авторизация'''
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']