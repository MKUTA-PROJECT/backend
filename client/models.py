from django.db import models
from activity.models import Activity

# Create your models here.
class Client(models.Model):
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length=30, blank = False, verbose_name = "Name")
    sex= models.CharField(max_length=30, blank = False)
    tel = models.CharField(max_length=30, blank = False, null = True)
    age = models.IntegerField(blank = False, null = False)
    region = models.CharField(max_length=30, blank = False)
    district = models.CharField(max_length=30, blank = False)
    ward = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=30, blank = True)
    tb_suspect = models.BooleanField(default=None)
    tb_status = models.BooleanField(default=None)
    def _str_(self):
        return self.name