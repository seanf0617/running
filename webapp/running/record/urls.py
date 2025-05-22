from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.RecordCreateView.as_view(), name='record_create'),
    path('list/', views.RecordListView.as_view(), name='record_list'),
    # The base path 'record/' will be prefixed at the project-level urls.py
]