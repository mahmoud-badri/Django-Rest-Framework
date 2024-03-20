from django.db import models
# from hotel.models import Hotel
from users.models import User


class Review(models.Model):
    hotel = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name='reviews')
    rating = models.IntegerField(default=0)
    description = models.TextField(max_length=1000,default="",blank=False) 
    createAt = models.DateTimeField(auto_now_add=True) 
    # class Meta:
    #     ordering = ('review_date',)

    def __str__(self):
        return self.description