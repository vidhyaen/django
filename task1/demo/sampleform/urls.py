from django.urls import path
from .import views

urlpatterns = [
    path('show',views.show,name='show'),
    path('register',views.register,name='register')
]
