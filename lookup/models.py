from django.db import models

# Create your models here.


class LocationLookup(models.Model):
    zone = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    subdistrict = models.CharField(max_length=100)
    street_or_village = models.CharField(max_length=100)

    def __str__(self):
        return self.zone + ' ' + self.region + ' ' + self.district + ' ' + self.street_or_village


class StaffRoleLookup(models.Model):
    name = models.CharField(
        max_length=50, blank=False, verbose_name="Position")

    def __str__(self):
        return self.name


class HealthFacilityLookup(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(LocationLookup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name