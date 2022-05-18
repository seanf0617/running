"""running URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

#from users import views as users_views
from accounts import views as accounts_view
from django.contrib.auth import views as auth


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', accounts_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='accounts/index.html'), name ='logout'),
    ##### the next entry is to cover logout from the record miles page, not sure why the line above does not do it...
    path('record/accounts/logout/', auth.LogoutView.as_view(template_name ='accounts/index.html'), name ='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path('miles/', TemplateView.as_view(template_name='miles.html'), name='miles'),
    path('record/', TemplateView.as_view(template_name='record.html'), name='record'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
