from django.db import models
from users.models import User
from hotel.models import Hotel
# Create your models here.
class Appointment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,default = None )
    user = models.ForeignKey(User, on_delete=models.CASCADE , default = None)
    date = models.DateTimeField(auto_now_add=True)
    start_day = models.DateField(default='2024-01-01')
    end_day = models.DateField(default='2024-01-05')
    adults = models.IntegerField(default = 1)
    children = models.IntegerField(default=0)
    infants = models.IntegerField(default=0)
    pets = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment from {self.user} at {self.hotel} on {self.date}"