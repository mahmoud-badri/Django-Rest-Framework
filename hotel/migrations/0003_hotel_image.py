# Generated by Django 5.0.3 on 2024-03-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_remove_hotel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
