from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView

from user.forms import InstructorForm, StudentForm
from user.models import Instructor, Student
from utils.views import DeleteMixin, PartialTemplateMixin, SearchMixin


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy("user_login"))

class IndexView(View):
    template_name = "index.html"
    authorized_groups = ["admin"]

    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,self.template_name,context)

class StudentMixin(SearchMixin,PartialTemplateMixin):
    form_class = StudentForm
    model = Student
    success_url = reverse_lazy("student_list")
    queryset = Student.objects.all()
    paginate_by = 10
    template_dir="Student/"


class StudentListView(StudentMixin, ListView):
    template_name = "student/list.html"
    search_lookup_fields = ["full_name","email"]
    queryset = Student.objects.all()
    

class StudentDetailView(StudentMixin, DetailView):
    template_name = "student/student_detail.html"


class StudentCreateView(StudentMixin, CreateView):
    template_name = "create.html"

class StudentUpdateView(StudentMixin, UpdateView):
    template_name = "update.html"


class StudentDeleteView(StudentMixin,DeleteMixin, View):
    ...




class InstructorMixin(SearchMixin,PartialTemplateMixin):
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
    

class InstructorDetailView(InstructorMixin, DetailView):
    template_name = "instructor/instructor_detail.html"


class InstructorCreateView(InstructorMixin, CreateView):
    template_name = "create.html"

class InstructorUpdateView(InstructorMixin, UpdateView):
    template_name = "update.html"


class InstructorDeleteView(InstructorMixin,DeleteMixin, View):
    ...
