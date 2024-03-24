from django.db import models
from hotel.models import Hotel
from users.models import User


class Rate(models.Model):
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.CASCADE,related_name='reviews')
    name = models.TextField(max_length=100,default="",blank=False) 
    rating = models.IntegerField(default=0)
    description = models.TextField(max_length=1000,default="",blank=False) 
    createAt = models.DateTimeField(auto_now_add=True) 
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.description