from django.db import models
from account.models import CustomUser
# Create your models here.
class TbInfo(models.Model):
    female_below_15 = models.CharField(max_length=31, blank = False)
    female_above_15 = models.CharField(max_length=31, blank = False)
    male_below_15 = models.CharField(max_length=31, blank = False)
    male_above_15 = models.CharField(max_length=31, blank = False)
    date = models.DateTimeField(auto_now_add=True)
    zone = models.CharField(max_length=30, blank = False)
    region = models.CharField(max_length=30, blank = False)
    district = models.CharField(max_length=30, blank = False)
    sub_district = models.CharField(max_length=30, blank = True)
    ward = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=30, blank = True)
