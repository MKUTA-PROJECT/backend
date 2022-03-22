from django.db import models



# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30, blank = False)
    description = models.CharField(max_length=500, blank = False)
    start_date = models.CharField(max_length=20, blank = False)
    end_date = models.CharField(max_length=20, blank = False)
    
    def _str_(self):
        return self.name
