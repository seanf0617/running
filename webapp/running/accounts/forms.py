from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(max_length=254)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "targetmiles", "location")
        labels = {
            'email': 'Email Address',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'location': 'Location',
            'targetmiles': 'Target Miles',
        }
        # DOB


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "targetmiles", "location", )
        # location
        # DOB
