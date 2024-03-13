# Generated by Django 5.0.3 on 2024-03-13 09:13

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
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
