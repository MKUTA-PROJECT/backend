# Generated by Django 3.1.6 on 2021-04-08 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_auto_20210408_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.customuser')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'ACTIVE'), (2, 'DOMANT'), (3, 'DEAD')], default=2, null=True)),
                ('Tel', models.CharField(max_length=31, verbose_name='Phone Number')),
            ],
        ),
    ]
