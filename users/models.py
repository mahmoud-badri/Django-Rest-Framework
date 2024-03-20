import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

def validate_email_format(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    if not re.match(email_regex, value):
        raise ValidationError('Invalid email format.')

def validate_password_complexity(value):
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters long.')
    # Add custom complexity validation logic here, e.g., check for uppercase, lowercase, digits, special characters, etc.
    if not any(c.isupper() for c in value):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not any(c.islower() for c in value):
        raise ValidationError('Password must contain at least one lowercase letter.')
    if not any(c.isdigit() for c in value):
        raise ValidationError('Password must contain at least one digit.')
    # Add more checks as needed

def validate_egyptian_phone(value):
    phone_regex = r'^01[0125]{1}[0-9]{8}$'  # Matches the format 01X followed by 8 digits
    if not re.match(phone_regex, value):
        raise ValidationError('Invalid Egyptian phone number.')

class User(AbstractUser):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator(), validate_email_format])
    phone_number = models.CharField(max_length=11, validators=[validate_egyptian_phone], blank=True, null=True)
    user_type = [
        ('user', 'User'),
        ('hotel', 'Hotel'),
    ]
    type = models.CharField(max_length=10, choices=user_type, blank=True, null=True)
    password = models.CharField(max_length=255, validators=[MinLengthValidator(8), validate_password_complexity])
    confirm_password = models.CharField(max_length=255, blank=True, null=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)

    def clean(self):
        super().clean()
        if not self.name:
            raise ValidationError({'name': _('Name field cannot be empty.')})
        if self.password != self.confirm_password:
            raise ValidationError({'confirm_password': _('Passwords do not match.')})

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)  # Hash the password before saving
        super().save(*args, **kwargs)

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="hotel", null=False, blank=True)
