from django.db import models

# Create your models here.
class ActivityType(models.Model):
    name = models.CharField(max_length = 30, blank = False, null = False)
    def _str_(self):
        return self.name

class Activity(models.Model):
    name = models.ForeignKey(ActivityType, on_delete = models.CASCADE)
    date_conducted = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=30, blank = False)
    district = models.CharField(max_length=30, blank = False)
    ward = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=30, blank = True)
    def _str_(self):
        return self.name

