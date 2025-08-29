from django.contrib import admin

from user.models import Instructor, Student

# Register your models here.
admin.site.register([
    Student,
    Instructor
])
