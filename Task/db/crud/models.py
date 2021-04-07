from django.db import models

# Create your models here.
class Crud(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    number=models.CharField(max_length=12)
    address=models.CharField(max_length=50)