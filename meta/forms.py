from django.forms import  ModelForm
from meta.models import MetaData
from utils.forms import BaseForm

from course.models import Course

class MetaDataForm(BaseForm,ModelForm):
    class Meta:
        model = MetaData
        fields = ("key","value")