from django.urls import path
from .views import SignUpView


urlpatterns = [
    path("record/", SignUpView.as_view(), name="record"),
]