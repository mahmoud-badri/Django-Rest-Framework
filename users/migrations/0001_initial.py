# Generated by Django 5.0.3 on 2024-03-25 07:05

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator(), users.models.validate_email_format])),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(blank=True, choices=[('user', 'User'), ('hotel', 'Hotel')], max_length=10, null=True)),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(8), users.models.validate_password_complexity])),
                ('confirm_password', models.CharField(default='0', max_length=255)),
                ('email_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
