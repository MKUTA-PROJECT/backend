# Generated by Django 3.1.6 on 2021-05-09 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffprofile',
            old_name='Tel',
            new_name='tel',
        ),
    ]