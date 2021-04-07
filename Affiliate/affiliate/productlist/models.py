from django.db import models
# Create your models here.
class productTable(models.Model):
    name = models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    category=models.CharField(max_length=50)
    desc=models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    url=models.ImageField(max_length=255)
   

    