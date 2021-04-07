from django.db import models

# Create your models here.
class File_Tabel(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    url = models.ImageField(max_length=20)
   
