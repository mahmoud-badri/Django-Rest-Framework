from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='',null=True)
    def __str__(self):
        return self.name


