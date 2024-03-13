from django.db import models
from hotel.models import *
# Create your models here.
class Appointment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Appointment at {self.hotel} on {self.date}"