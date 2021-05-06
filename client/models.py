from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30, blank = False, verbose_name = "Name")
    sex= models.CharField(max_length=30, blank = False)
    tel = models.CharField(max_length=30, blank = False, null = True)
    age = models.IntegerField(blank = False, null = False)
    region = models.CharField(max_length=30, blank = False)
    district = models.CharField(max_length=30, blank = False)
    ward = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=30, blank = True)
    agreed_screening = models.BooleanField(default=None)
    tb_suspect = models.BooleanField(default=None)
    sputum_collection = models.BooleanField(default=None)
    tb_status = models.BooleanField(default=None)
    referal = models.BooleanField(default=None)
    refered_hospital = models.CharField(max_length=30, blank = True, null = True)
    treatment_status = models.BooleanField(default=None)
    def _str_(self):
        return self.name