from django.db import models

from utils.models import TimeStampModel
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class MetaData(TimeStampModel):
    key = models.CharField(max_length=25, db_index=True)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = [["key", "value"]]

    def __str__(self):
        return f"{self.key} : {self.value}"


class StudentMetaData(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey("user.student", on_delete=models.CASCADE)
    metadata = models.ForeignKey(MetaData, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "user_student_meta_data"
        unique_together = [["student", "metadata"]]
