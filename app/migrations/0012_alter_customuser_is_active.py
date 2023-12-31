# Generated by Django 4.2.4 on 2023-08-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_customuser_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active.Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
