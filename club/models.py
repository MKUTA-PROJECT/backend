from django.db import models

# Create your models here.
class Supervisor(models.Model):
    name = models.CharField(max_length=30, blank = False, verbose_name = "Name")
    position = models.CharField(max_length=30, blank = False)
    email = models.CharField(max_length=30, blank = False)
    tel = models.CharField(max_length=30, blank = False)


class Club(models.Model):
    name = models.CharField(max_length=30, blank = False, verbose_name = "Club Name")
    health_facility = models.CharField(max_length=30, blank = False)
    zone = models.CharField(max_length=30, blank = False)
    region = models.CharField(max_length=30, blank = False)
    district = models.CharField(max_length=30, blank = False)
    sub_district = models.CharField(max_length=30, blank = True)
    ward = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=30, blank = True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True)