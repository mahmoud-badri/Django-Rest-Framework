# Generated by Django 5.0.3 on 2024-03-25 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='hotel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel'),
        ),
    ]
