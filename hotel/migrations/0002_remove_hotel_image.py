# Generated by Django 5.0.2 on 2024-03-18 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='image',
        ),
    ]