from django.db import models

from account.models import CustomUser

# Create your models here.
class SupervisorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roles=3)


# The proxy model for the Agency user
class Supervisor(CustomUser):
    objects = SupervisorManager()

    @property
    def more(self):
        return self.supervisorprofile

    class Meta:
        proxy = True
        verbose_name_plural = "Supervisors"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.roles = 3
        return super(Supervisor, self).save(*args, **kwargs)


class SupervisorProfile(models.Model):
    user = models.OneToOneField(
        Supervisor, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(
        max_length=50, blank=False, verbose_name="Position")
