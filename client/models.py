from django.db import models
from activity.models import Activity

# Create your models here.
class Client(models.Model):
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, null = True)
    first_name = models.CharField(max_length=30, blank = False)
    middle_name = models.CharField(max_length=30, blank = False)
    last_name = models.CharField(max_length=30, blank = False)
    sex= models.IntegerField(blank=False)
    tel = models.CharField(max_length=10, blank = False, null = True)
    age = models.IntegerField(blank = False, null = False)
    region = models.CharField(max_length=30, blank = False)
    district = models.CharField(max_length=30, blank = False)
    ward = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=30, blank = True)
    tb_suspect = models.BooleanField(default=None)
    tb_status = models.BooleanField(default=None)
    date = models.DateField(blank = False, editable=True)
    def _str_(self):
        return self.name