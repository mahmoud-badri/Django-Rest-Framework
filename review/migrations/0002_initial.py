<<<<<<< HEAD
# Generated by Django 5.0.2 on 2024-03-21 00:14
=======
# Generated by Django 5.0.3 on 2024-03-21 00:43
>>>>>>> main

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.user'),
        ),
    ]
