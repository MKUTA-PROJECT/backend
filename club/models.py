from django.db import models
from lookup.models import HealthFacilityLookup, LocationLookup

from supervisor.models import Supervisor

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=30, blank=False,
                            verbose_name="Club Name")
    phone = models.CharField(max_length=30, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, null=True)
    health_facility = models.ForeignKey(
        HealthFacilityLookup, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(
        Supervisor, on_delete=models.SET_NULL, null=True, related_name="club")
    is_under_cso = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def get_name(self):
        return self.name


class CSO(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    location = models.ForeignKey(LocationLookup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CSOCLUB(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    cso = models.ForeignKey(CSO, on_delete=models.CASCADE)
