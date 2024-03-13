# ratings/models.py
from django.db import models

class Rating(models.Model):
    hotel_name = models.CharField(max_length=100)  # Name of the item being rated
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 ratings
