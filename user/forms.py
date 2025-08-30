from django.forms import ModelForm
from course.models import Enrollment
from meta.models import StudentMetaData
from user.models import Instructor, Student
from utils.forms import BaseForm


class StudentForm(BaseForm, ModelForm):
    class Meta:
        model = Student
        fields = ["full_name", "email", "dob", "meta_data"]

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        if request:
            self.user = request.user
            print("self.user")
            print(self.user)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()

        # save meta_data
        if "meta_data" in self.cleaned_data:
            print("metaaaa")
            for meta in self.cleaned_data["meta_data"]:
                StudentMetaData.objects.get_or_create(
                    student=student, metadata=meta, defaults={"added_by": self.user}
                )
        return student


class InstructorForm(BaseForm, ModelForm):
    class Meta:
        model = Instructor
        fields = ("full_name","email","courses","meta_data")