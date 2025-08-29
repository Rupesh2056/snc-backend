from django.db import models

from utils.models import TimeStampModel

# Create your models here.
class MetaData(TimeStampModel):
    key = models.CharField(max_length=25)
    value = models.CharField(max_length=255)