# Generated by Django 5.0.3 on 2024-03-20 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('status', models.CharField(choices=[('Poor', 'Poor'), ('Okay', 'Okay'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')], default='good', max_length=20)),
                ('description', models.TextField(null=True)),
                ('governorate', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
    ]
