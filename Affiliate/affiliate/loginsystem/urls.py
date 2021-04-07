from django.urls import path
from .import views

 
urlpatterns = [
    path('', views.index,name='index'),
    path('Affiliate', views.Affiliate,name='Affiliate'),
    path('Seller',views.Seller,name='Seller'),
    path('register', views.register,name='register'),
    path('logout',views.logout,name='logout')
    
]
