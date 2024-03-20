# Generated by Django 5.0.3 on 2024-03-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('description', models.TextField(default='', max_length=1000)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
