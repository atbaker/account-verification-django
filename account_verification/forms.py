from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    """Form class for signing up new users"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number']
