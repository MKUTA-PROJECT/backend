from django.db import models
from member.models import MemberProfile

class Activity(models.Model):
    name = models.CharField(max_length=30, blank = False)
    member = models.ForeignKey(MemberProfile, on_delete = models.CASCADE, null = True) 
    date_conducted = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=30, blank = False)
    district = models.CharField(max_length=30, blank = False)
    ward = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=30, blank = True)
    def _str_(self):
        return self.name

