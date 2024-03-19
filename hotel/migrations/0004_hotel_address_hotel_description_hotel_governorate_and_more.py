# Generated by Django 5.0.3 on 2024-03-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_hotel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='governorate',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='prices',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.CharField(choices=[('⭐️', '1 Star'), ('⭐️⭐️', '2 Stars'), ('⭐️⭐️⭐️', '3 Stars'), ('⭐️⭐️⭐️⭐️', '4 Stars'), ('⭐️⭐️⭐️⭐️⭐️', '5 Stars')], default='⭐️', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='review',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotel',
            name='status',
            field=models.CharField(choices=[('poor', 'Poor'), ('okay', 'Okay'), ('good', 'Good'), ('very_good', 'Very Good'), ('excellent', 'Excellent')], default='good', max_length=20),
        ),
    ]