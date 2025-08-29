from django.db import models

from course.models import Course
from meta.models import MetaData
from utils.models import TimeStampModel

# Create your models here.
class Student(TimeStampModel):
    full_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True,null=True)
    meta_data = models.ManyToManyField(MetaData,related_name="student_metas",blank=True)

    def __str__(self):
        return self.email


class Instructor(TimeStampModel):
    full_name = models.CharField()
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course,related_name="instructors")
    meta_data = models.ManyToManyField(MetaData,related_name="instructor_metas",blank=True)

    def __str__(self):
        return self.email
