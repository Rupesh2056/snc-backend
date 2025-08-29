from django.db import models

from utils.models import TimeStampModel

# Create your models here.
class MetaData(TimeStampModel):
    key = models.CharField(max_length=25,db_index=True)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = [["key","value"]]
    

    def __str__(self):
        return f"{self.key} : {self.value}"
    
