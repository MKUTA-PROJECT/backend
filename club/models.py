from django.db import models

# Create your models here.
class Supervisor(models.Model):
    first_name = models.CharField(max_length=30, blank = False, verbose_name = "First Name")
    last_name = models.CharField(max_length=30, blank = False, null = True, verbose_name = "Last Name")
    position = models.CharField(max_length=30, blank = False)
    email = models.CharField(max_length=30, blank = False)
    tel = models.CharField(max_length=30, blank = False)

    def _str_(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=30, blank = False, verbose_name = "Club Name")
    phone = models.CharField(max_length=30, blank = False, null = True)
    email = models.EmailField(max_length=30, blank = False, null = True)
    health_facility = models.CharField(max_length=30, blank = False)
    office = models.CharField(max_length=30, blank = True)
    zone = models.CharField(max_length=30, blank = False)
    region = models.CharField(max_length=30, blank = False)
    district = models.CharField(max_length=30, blank = False)
    sub_district = models.CharField(max_length=30, blank = True)
    ward = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=30, blank = True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, related_name="club")

    def _str_(self):
        return self.name