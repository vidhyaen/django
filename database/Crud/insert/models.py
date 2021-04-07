from django.db import models

# Create your models here.
class TestSamples(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)