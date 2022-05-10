from django.db import models

# Create your models here.
class ZoneLookup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, name='this will include the names of the regions in this zone')

    def __str__(self):
        return self.name

class LocationLookup(models.Model):
    zone = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    subdistrict = models.CharField(max_length=100)
    ward = models.CharField(max_length=100,null=True)
    street_or_village = models.CharField(max_length=100)

    def __str__(self):
        return self.zone + ' ' + self.region + ' ' + self.district + ' ' + self.street_or_village


class StaffRoleLookup(models.Model):
    name = models.CharField(
        max_length=50, blank=False, verbose_name="Position")

    def __str__(self):
        return self.name
    def get_name(self):
        return self.name
 
class MemberRoleLookup(models.Model):
    # STATUS choices
    CHAIRMAN = 1
    ASS_CHAIRMAN = 2
    SECRETARY = 3
    ASS_SECRETARY = 4
    TREASURER = 5
    MEMBER = 6

    STATUS_CHOICES = (
        (CHAIRMAN, 'CHAIRMAN'),
        (ASS_CHAIRMAN, 'ASSISTANT CHAIRMAN'),
        (SECRETARY, 'SECRETARY'),
        (ASS_SECRETARY, 'ASSISTANT SECRETARY'),
        (TREASURER, 'TREASURER'),
        (MEMBER, 'MEMBER'),
    )
    value= models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, blank=True, null=True, default=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_name(self):
        return self.name


class HealthFacilityLookup(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(LocationLookup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_name(self):
        return self.name


class ProjectLevelLookup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



