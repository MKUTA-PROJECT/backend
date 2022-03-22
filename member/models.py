from datetime import timezone
from club.models import Club
from django.db import models
from account.models import CustomUser
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


class MemberRoleLookup(models.Model):
    name = models.CharField(
        max_length=50, blank=False, verbose_name="Position")

    def __str__(self):
        return self.name


class MemberProfile(models.Model):
    user = models.OneToOneField(
        Member, on_delete=models.CASCADE, related_name="memberProfile")
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=False, blank=False, related_name="club")
    role = models.ForeignKey(
        MemberRoleLookup, on_delete=models.SET_DEFAULT, default=1)
    is_post_tb = models.BooleanField()
    # project = models.ManyToManyField(
    #     project, related_name='profiles', blank=True, null=True)

    def _str_(self):
        return self.user


class MemberContribution(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, null=False, blank=False, related_name="member")
    amouunt = models.FloatField()
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
