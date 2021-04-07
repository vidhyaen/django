from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views 

urlpatterns = [
    path('',views.display),
       path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='commons/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
]