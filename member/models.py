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

    ACTIVE = 1
    DOMANT = 2
    DEAD = 3
    
    STATUS_CHOICES = (
        (ACTIVE, 'ACTIVE'),
        (DOMANT, 'DOMANT'),
        (DEAD, 'DEAD'),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=True, null=True, default=2)

    PAID = 1
    NOT_PAID = 2
    
    FEE_CHOICES = (
        (PAID, 'PAID'),
        (NOT_PAID, 'NOT PAID'),
    )
    fee_status = models.PositiveSmallIntegerField(choices=FEE_CHOICES, blank=True, null=True, default=2)
    tel = models.CharField(max_length=31, blank = False, verbose_name = "Phone Number")
    timestamp   = models.DateTimeField(null=True, blank=True, auto_now_add=False) # To control the fee status

