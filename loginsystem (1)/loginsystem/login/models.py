from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo_user(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)