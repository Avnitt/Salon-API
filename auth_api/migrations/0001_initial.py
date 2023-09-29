# Generated by Django 4.2.5 on 2023-09-27 12:33

import auth_api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. Please Enter a valid Phone Number.', max_length=150, unique=True, validators=[auth_api.validators.PhoneValidator()], verbose_name='phone')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
            ],
            options={
                'ordering': ['-date_joined'],
            },
        ),
    ]
