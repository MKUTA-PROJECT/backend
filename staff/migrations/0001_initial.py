# Generated by Django 3.2.4 on 2021-06-19 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.customuser')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
                ('status', models.CharField(default='Active', max_length=31, verbose_name='Status')),
                ('tel', models.CharField(max_length=31, verbose_name='Phone Number')),
            ],
        ),
    ]
