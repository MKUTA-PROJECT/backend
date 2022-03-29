from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.

from account.manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    STAFF = 1
    SUPERVISOR = 2
    MEMBER = 3
    ADMIN = 4

    # Sex choices
    MALE = 1
    FEMALE = 2

    ROLE_CHOICES = (
        (STAFF, 'STAFF USER'),
        (SUPERVISOR, 'SUPERVISOR'),
        (MEMBER, 'MEMBER'),
        (ADMIN, 'ADMIN'),    
    )
    SEX_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )
    email = models.EmailField(max_length = 40, verbose_name = 'Email Address', unique = True)
    first_name =  models.CharField(max_length=30, blank=True, verbose_name = 'First Name')
    middle_name = models.CharField(max_length=30, blank=True, verbose_name = 'Middle Name')
    last_name =  models.CharField(max_length=30, blank=True, verbose_name = 'Last Name')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex], max_length=17, unique=True, blank=True, null=True)
    roles = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True, default=1)
    sex = models.PositiveSmallIntegerField(
        choices=SEX_CHOICES, blank=True, null=True, default=1)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True) 

    objects = CustomUserManager()
    
    REQUIRED_FIELDS = ['first_name','middle_name', 'last_name','sex','phone','roles']
    
    USERNAME_FIELD = 'email'

    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
    class Meta:
        verbose_name_plural = "Users"

    