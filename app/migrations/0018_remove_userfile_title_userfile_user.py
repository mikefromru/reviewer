# Generated by Django 4.2.4 on 2023-08-23 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_userfile_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='title',
        ),
        migrations.AddField(
            model_name='userfile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
