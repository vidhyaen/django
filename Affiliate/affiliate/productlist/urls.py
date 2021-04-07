from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('', views.display, name='home'),
    path('detail/<int:id>',views.detail,name='detail')
 
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

