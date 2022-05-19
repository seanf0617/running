from django.db import models
from django.db.models import Model


# Create your models here.
class RecordActivity(Model):
    pass
    # add additional fields in here
#    username = models.CharField(null=True, blank=False, max_length=150)
    username = models.CharField(max_length=150)
    recorddistance = models.IntegerField(blank=True, null=True)
    recorddate = models.DateField()
