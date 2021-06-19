from club.models import Club
from django.db import models
from account.models import CustomUser
# Create your models here.
class MemberProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name="memberProfile")
    date_joined = models.DateTimeField(auto_now_add=True) 
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank= False, related_name="club")

    CHAIRMAN = 1
    ASS_CHAIR = 2
    SECRETARY = 3
    ASS_SECRETARY = 4
    TREASURER = 5
    MEMBER = 6
    
    ROLE_CHOICES = (
        (CHAIRMAN, 'CHAIRMAN'),
        (ASS_CHAIR, 'ASS. CHAIR'),
        (SECRETARY, 'SECRETARY'),
        (ASS_SECRETARY, 'ASS_SECRETARY'),
        (TREASURER, 'TREASURER'),
        (MEMBER, 'MEMBER'),  
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=6)
    status = models.CharField(max_length=31, blank = False, verbose_name = "status", default = "Domant")
    fee_status = models.CharField(max_length=31, blank = False, verbose_name = "fee status", default = "Not Paid")
    tel = models.CharField(max_length=31, blank = False, verbose_name = "Phone Number")
    timestamp   = models.DateTimeField(null=True, blank=True, auto_now_add=False) # To control the fee status
    def _str_(self):
        return self.user

