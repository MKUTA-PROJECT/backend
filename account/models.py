from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
# Create your models here.

from account.manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    MNE_MANAGER = 1
    STAFF_USER = 2
    ZONAL_CORDINATOR = 3
    CHAIRPERSON = 4
    CLUB_LEADER = 5
    MEMBER = 6
    ADMIN = 7
    
    ROLE_CHOICES = (
        (MNE_MANAGER, 'MNE MANAGER'),
        (STAFF_USER, 'STAFF USER'),
        (ZONAL_CORDINATOR, 'ZONAL CORDINATOR'),
        (CHAIRPERSON, 'CHAIRPERSON'),
        (CLUB_LEADER, 'CLUB LEADER'),
        (MEMBER, 'MEMBER'),
        (ADMIN, 'ADMIN'),    
    )

    roles = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=6)
    email = models.EmailField(max_length = 40, verbose_name = 'Email Address', unique = True)
    first_name =  models.CharField(max_length=30, blank=True, verbose_name = 'First Name')
    middle_name = models.CharField(max_length=30, blank=True, verbose_name = 'Middle Name')
    last_name =  models.CharField(max_length=30, blank=True, verbose_name = 'Last Name')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()
    
    REQUIRED_FIELDS = ['first_name','middle_name', 'last_name']
    
    USERNAME_FIELD = 'email'

    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
    class Meta:
        verbose_name_plural = "Users"

    