# Generated by Django 5.0.3 on 2024-03-22 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_remove_hotel_rate_remove_hotel_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_email',
        ),
    ]