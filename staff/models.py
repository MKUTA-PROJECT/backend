from django.db import models
from account.models import CustomUser
# Create your models here.
class StaffProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    date_joined = models.DateTimeField(auto_now_add=True) 
    position = models.CharField(max_length=50, blank = False, verbose_name = "Position")

    ACTIVE = 1
    DOMANT = 2
    DEAD = 3
    STATUS_CHOICES = (
        (ACTIVE, 'ACTIVE'),
        (DOMANT, 'DOMANT'),
        (DEAD, 'DEAD'),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=True, null=True, default=2)

    tel = models.CharField(max_length=31, blank = False, verbose_name = "Phone Number")