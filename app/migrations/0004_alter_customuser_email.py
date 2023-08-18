# Generated by Django 4.2.4 on 2023-08-17 19:14

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='email adress'),
        ),
    ]
