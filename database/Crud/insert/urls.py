from django.urls import path
from .import views

urlpatterns = [
 
    path('',views.insert),
    path('datainsert',views.datainsert),
    path('display',views.display,name='display'),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('update/dataupdate/<int:id>',views.dataupdate)
]