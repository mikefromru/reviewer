# Generated by Django 4.2.4 on 2023-08-23 14:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_userfile_created_remove_userfile_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='userfiles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['py'])]),
        ),
    ]
