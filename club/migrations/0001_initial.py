# Generated by Django 3.2.4 on 2022-02-28 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name='Last Name')),
                ('position', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Club Name')),
                ('phone', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('health_facility', models.CharField(max_length=30)),
                ('office', models.CharField(blank=True, max_length=30)),
                ('zone', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('sub_district', models.CharField(blank=True, max_length=30)),
                ('ward', models.CharField(blank=True, max_length=30)),
                ('street', models.CharField(blank=True, max_length=30)),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='club', to='club.supervisor')),
            ],
        ),
    ]
