from django.db import models
from users.models import User
# Create your models here.
class Room(models.Model):
    hotel = models.ForeignKey(User,on_delete=models.CASCADE)
    bed = models.IntegerField()
    type= models.CharField(max_length = 10)

class Facility(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    description=models.CharField(max_length = 200)
