# Generated by Django 3.2.4 on 2021-06-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='tel',
            field=models.IntegerField(max_length=10),
        ),
    ]
