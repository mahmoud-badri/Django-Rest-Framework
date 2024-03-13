from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='',null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name


