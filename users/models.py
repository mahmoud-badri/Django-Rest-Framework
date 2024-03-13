from django.db import models

# Create your models here.
class User(models.Model):
    fullname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    
