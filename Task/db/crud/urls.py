from django.contrib import admin
from django.urls import path

from . import views 

urlpatterns = [
    path('',views.insert),
    path('datainsert',views.datainsert),
    path('display',views.display,name='display'),
    path('delete/<int:id>/',views.delete)
]