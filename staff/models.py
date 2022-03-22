from django.db import models
from account.models import CustomUser
from lookup.models import StaffRoleLookup
# Create your models here.


class StaffManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roles=1)


# The proxy model for the Agency user
class Staff(CustomUser):
    objects = StaffManager()

    @property
    def more(self):
        return self.staffprofile

    class Meta:
        proxy = True
        verbose_name_plural = "Staff"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.roles = 1
        return super(Staff, self).save(*args, **kwargs)




class StaffProfile(models.Model):
    user = models.OneToOneField(
        Staff, on_delete=models.CASCADE)
    role = models.OneToOneField(
        StaffRoleLookup, on_delete=models.SET_DEFAULT, null=True, default=1)
