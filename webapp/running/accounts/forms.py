from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
 
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    phone_no = forms.CharField(max_length = 20)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']