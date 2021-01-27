from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Additional details needed for dev registration
class DevRegisterForm(UserRegisterForm):
    seller_id = forms.CharField(max_length=255)
    secret_key = forms.CharField(max_length=255)


