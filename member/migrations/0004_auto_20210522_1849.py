# Generated by Django 3.1.6 on 2021-05-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20210506_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='fee_status',
            field=models.CharField(default='Not Paid', max_length=31, verbose_name='fee status'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='status',
            field=models.CharField(default='Domant', max_length=31, verbose_name='status'),
        ),
    ]
