from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from user.forms import InstructorForm, StudentForm
from user.models import Instructor, Student
from utils.permissions import AccessMixin
from utils.views import DeleteMixin, MetaDataFilterMixin, MetadataContextMixin, PartialTemplateMixin, PrefetchMixin, SearchMixin
from django.contrib.auth.mixins import LoginRequiredMixin

def logout_user(request):
    logout(request)
    return redirect(reverse_lazy("user_login"))

class IndexView(AccessMixin,View):
    template_name = "index.html"
    authorized_groups = ["admin"]

    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,self.template_name,context)

class StudentMixin(AccessMixin,SearchMixin,PartialTemplateMixin):
    form_class = StudentForm
    model = Student
    success_url = reverse_lazy("student_list")
    queryset = Student.objects.all()
    paginate_by = 10
    template_dir = "Student/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class StudentListView(StudentMixin,MetaDataFilterMixin, ListView):
    template_name = "student/list.html"
    search_lookup_fields = ["full_name","email"]
    queryset = Student.objects.all()
    

class StudentDetailView(StudentMixin,PrefetchMixin, DetailView):
    template_name = "student/detail.html"


class StudentCreateView(StudentMixin,MetadataContextMixin, CreateView):
    template_name = "dynamic_create.html"

class StudentUpdateView(StudentMixin,MetadataContextMixin, UpdateView):
    template_name = "dynamic_update.html"


class StudentDeleteView(StudentMixin,DeleteMixin, View):
    ...




class InstructorMixin(AccessMixin,SearchMixin,PartialTemplateMixin):
    form_class = InstructorForm
    model = Instructor
    success_url = reverse_lazy("instructor_list")
    queryset = Instructor.objects.all()
    paginate_by = 10
    template_dir="instructor/"


class InstructorListView(InstructorMixin, ListView):
    template_name = "instructor/list.html"
    search_lookup_fields = ["full_name","email"]
    queryset = Instructor.objects.all()
    

class InstructorDetailView(InstructorMixin,PrefetchMixin, DetailView):
    template_name = "instructor/detail.html"


class InstructorCreateView(InstructorMixin,MetadataContextMixin, CreateView):
    template_name = "dynamic_create.html"

class InstructorUpdateView(InstructorMixin,MetadataContextMixin, UpdateView):
    template_name = "dynamic_update.html"


class InstructorDeleteView(InstructorMixin,DeleteMixin, View):
    ...
