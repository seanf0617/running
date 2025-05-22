from django import forms
#from django.contrib.auth.models import User

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

#from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"