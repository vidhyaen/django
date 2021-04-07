from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Sellerregister(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    bank=models.CharField(max_length=50)
    site=models.CharField(max_length=50)
    
    
class Affiliateregister(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=255)
    bank=models.CharField(max_length=100)

   



    