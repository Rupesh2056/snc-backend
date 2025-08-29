import decimal
from django.db import models

from meta.models import MetaData
from utils.models import TimeStampModel

# Create your models here.

class Course(TimeStampModel):
    title = models.CharField(max_length=55)
    code = models.CharField(unique=True)
    description = models.TextField(blank=True,null=True)
    meta_data = models.ManyToManyField(MetaData,related_name="course_metas",blank=True)

    def __str__(self):
        return f"{self.title} ({self.code})"



class Enrollment(TimeStampModel):
    student = models.ForeignKey("user.Student",on_delete=models.CASCADE,related_name="enrollments")
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="enrollments")
    score = models.DecimalField(max_digits=5,decimal_places=2,default=decimal.Decimal(0.0))
    meta_data = models.ManyToManyField(MetaData,related_name="enrollment_metas",blank=True)


    class Meta:
        unique_together = [["student", "course"]]