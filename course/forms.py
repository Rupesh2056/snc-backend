from django.forms import  ModelForm
from utils.forms import BaseForm

from course.models import Course, Enrollment

class CourseForm(BaseForm,ModelForm):
    class Meta:
        model = Course
        fields = ["title","code","description","meta_data"]


class EnrollmentForm(BaseForm,ModelForm):
    class Meta:
        model = Enrollment
        fields = ("student","course","score","meta_data")