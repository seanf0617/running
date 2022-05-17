from cProfile import label
import email
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(max_length=254)

    class Meta:
        model = CustomUser
        fields = ("username", "email")
        labels = {'email':'email address',}

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")
