from datetime import timezone
from club.models import Club
from django.db import models
from account.models import CustomUser
from lookup.models import MemberRoleLookup
# Create your models here.


class MemberManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roles=3)


# The proxy model for the Agency user
class Member(CustomUser):
    objects = MemberManager()

    @property
    def more(self):
        return self.memberprofile

    class Meta:
        proxy = True
        verbose_name_plural = "Members"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.roles = 3
        return super(Member, self).save(*args, **kwargs)





class MemberProfile(models.Model):
    # STATUS choices
    ACTIVE = 1
    DEAD = 3
    DOMANT = 2
    STATUS_CHOICES = (
        (ACTIVE, 'ACTIVE'),
        (DEAD, 'DEAD'),
        (DOMANT, 'DOMANT'),
    )
    user = models.OneToOneField(
        Member, on_delete=models.CASCADE, related_name="memberProfile")
    status= models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, blank=True, null=True, default=1)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=False, blank=False, related_name="club")
    role = models.ForeignKey(
        MemberRoleLookup, on_delete=models.SET_DEFAULT, default=1)
    is_post_tb = models.BooleanField(null=True)
    # project = models.ManyToManyField(
    #     project, related_name='profiles', blank=True, null=True)

    def _str_(self):
        return self.user


class MemberContribution(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, null=False, blank=False, related_name="member")
    amount = models.FloatField()
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
