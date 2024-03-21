# Generated by Django 5.0.3 on 2024-03-21 00:43

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('address', models.CharField(max_length=255, null=True)),
                ('rate', models.FloatField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('prices', models.FloatField(default=0.0)),
                ('rating', models.CharField(choices=[('⭐️', '1 Star'), ('⭐️⭐️', '2 Stars'), ('⭐️⭐️⭐️', '3 Stars'), ('⭐️⭐️⭐️⭐️', '4 Stars'), ('⭐️⭐️⭐️⭐️⭐️', '5 Stars')], default='⭐️', max_length=10)),
                ('review', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Poor', 'Poor'), ('Okay', 'Okay'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')], default='Good', max_length=20)),
                ('description', models.TextField(null=True)),
                ('governorate', models.CharField(default='Unknown', max_length=100)),
                ('single_room', models.FloatField(default=0.0)),
                ('suite', models.FloatField(default=0.0)),
                ('family_room', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=255, verbose_name='User Email')),
                ('room_type', models.CharField(choices=[('Single', 'Single Room'), ('Suite', 'Suite'), ('Family', 'Family Room')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_price', models.FloatField()),
                ('guest', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
        ),
    ]
