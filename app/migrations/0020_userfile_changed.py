# Generated by Django 4.2.4 on 2023-08-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_userfile_created_userfile_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='changed',
            field=models.BooleanField(default=False),
        ),
    ]