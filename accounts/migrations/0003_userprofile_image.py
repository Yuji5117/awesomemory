# Generated by Django 2.2.6 on 2020-01-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/%y/%m/%d', verbose_name='Profile Image'),
        ),
    ]