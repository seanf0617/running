from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    targetmiles = models.IntegerField(blank=True, null=True)
    location = models.CharField(null=True, blank=True, max_length=100)
    # DOB

    def __str__(self):
        return f'{self.username}'