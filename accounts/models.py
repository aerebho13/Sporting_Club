from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

