from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path("record/", include("django.contrib.auth.urls")),
    path('record/', TemplateView.as_view(template_name='record.html'), name='record'),
]