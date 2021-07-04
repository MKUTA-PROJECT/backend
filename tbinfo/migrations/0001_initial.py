# Generated by Django 3.2.4 on 2021-07-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('female_below_15', models.IntegerField()),
                ('female_above_15', models.IntegerField()),
                ('male_below_15', models.IntegerField()),
                ('male_above_15', models.IntegerField()),
                ('date', models.DateField()),
                ('zone', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('sub_district', models.CharField(blank=True, max_length=30)),
                ('ward', models.CharField(blank=True, max_length=30)),
                ('street', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
