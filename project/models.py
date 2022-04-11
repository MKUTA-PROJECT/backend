from django.db import models

from lookup.models import ZoneLookup



# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30, blank = False)
    description = models.CharField(max_length=500, blank = False)
    funder = models.CharField(max_length=100, blank = True, null=True)
    start_date = models.CharField(max_length=20, blank = False)
    end_date = models.CharField(max_length=20, blank = False)
    
    def _str_(self):
        return self.name


class ZonalProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    zone = models.ForeignKey(ZoneLookup, on_delete=models.SET_NULL, null=True)

