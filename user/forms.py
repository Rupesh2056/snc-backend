from django.forms import  ModelForm
from course.models import Enrollment
from user.models import Instructor, Student
from utils.forms import BaseForm


class StudentForm(BaseForm,ModelForm):
    class Meta:
        model = Student
        fields = ["full_name","email","dob","meta_data"]
        

class InstructorForm(BaseForm,ModelForm):
    class Meta:
        model = Instructor
        fields = ("full_name","email","courses","meta_data")