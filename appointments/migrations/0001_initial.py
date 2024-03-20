# Generated by Django 5.0.3 on 2024-03-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('start_day', models.DateField(default='2024-01-01')),
                ('end_day', models.DateField(default='2024-01-05')),
                ('adults', models.IntegerField(default=1)),
                ('children', models.IntegerField(default=0)),
                ('infants', models.IntegerField(default=0)),
                ('pets', models.BooleanField(default=False)),
            ],
        ),
    ]
