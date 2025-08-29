from django.forms import  ModelForm
from utils.forms import BaseForm

from course.models import Course

class CourseForm(BaseForm,ModelForm):
    class Meta:
        model = Course
        fields = ["title","code","description","meta_data"]