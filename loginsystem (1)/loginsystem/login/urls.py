from django.urls import path
from .import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('todo',views.todo,name='todo'),
    path('home',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('update/<int:id>/dataupdate',views.dataupdate,name='update'),
    path('logout',views.logout,name='logout')

]
