from django.db import models

# Create your models here
class TestForms(models.Model):
    username = models.CharField(max_length=50)
    pass1=models.CharField(max_length=7)
    pass2=models.CharField(max_length=7)
    date=models.DateTimeField(auto_now=False,auto_now_add=False,null=True)
    email = models.EmailField(max_length=30)