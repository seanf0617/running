from django.urls import path, include
from .views import SignUpView
from accounts import views as accounts_view
from django.contrib.auth import views as auth



urlpatterns = [
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
]