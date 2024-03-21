
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


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
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', null=True)
    address = models.CharField(max_length=255, null=True)
    rate = models.FloatField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    prices = models.FloatField(default=0.0)
    rating = models.CharField(max_length=10, choices=RATING_CHOICES, default='⭐️')
    review = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Good')
    description = models.TextField(null=True)
    governorate = models.CharField(max_length=101, default='Unknown')
    # Additional room types
    single_room = models.IntegerField(default=0)
    suite = models.IntegerField(default=0)
    family_room = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Booking(models.Model):
    ROOM_CHOICES = (
        ('Single', 'Single Room'),
        ('Suite', 'Suite'),
        ('Family', 'Family Room'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.EmailField(_('User Email'), max_length=255)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50, choices=ROOM_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.FloatField()
    guest = models.IntegerField(default=0)

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError(_('End date should be greater than start date.'))

    def __str__(self):
        return f"{self.user}'s booking at {self.hotel.name}"