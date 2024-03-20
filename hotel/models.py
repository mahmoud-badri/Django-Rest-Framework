from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Hotel(models.Model):
    RATING_CHOICES = (
        ('⭐️', '1 Star'),
        ('⭐️⭐️', '2 Stars'),
        ('⭐️⭐️⭐️', '3 Stars'),
        ('⭐️⭐️⭐️⭐️', '4 Stars'),
        ('⭐️⭐️⭐️⭐️⭐️', '5 Stars'),
    )
    STATUS_CHOICES = (
        ('Poor', 'Poor'),
        ('Okay', 'Okay'),
        ('Good', 'Good'),
        ('Very Good', 'Very Good'),
        ('Excellent', 'Excellent'),
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', null=True)
    address = models.CharField(max_length=255, null=True)
    rate = models.FloatField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    prices = models.FloatField(default=0.0)
    rating = models.CharField(max_length=10, choices=RATING_CHOICES, default='⭐️')
    review = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Good')
    description = models.TextField(null=True)
    governorate = models.CharField(max_length=100, default='Unknown')

    # Additional room types
    single_room = models.FloatField(default=0.0)
    suite = models.FloatField(default=0.0)
    family_room = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
