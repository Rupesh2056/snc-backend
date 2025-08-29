from django.shortcuts import render
from django.urls import reverse_lazy

from course.forms import CourseForm, EnrollmentForm
from course.models import Course, Enrollment
from utils.views import DeleteMixin, PartialTemplateMixin, SearchMixin
from django.views.generic import ListView,CreateView,UpdateView,DetailView,View


# Create your views here.

class CourseMixin(SearchMixin,PartialTemplateMixin):
    form_class = CourseForm
    model = Course
    success_url = reverse_lazy("course_list")
    queryset = Course.objects.all()
    paginate_by = 10
    template_dir="course/"


class CourseListView(CourseMixin, ListView):
    template_name = "course/list.html"
    search_lookup_fields = ["title"]
    queryset = Course.objects.all()
    

class CourseDetailView(CourseMixin, DetailView):
    template_name = "Course/Course_detail.html"


class CourseCreateView(CourseMixin, CreateView):
    template_name = "create.html"

class CourseUpdateView(CourseMixin, UpdateView):
    template_name = "update.html"


class CourseDeleteView(CourseMixin,DeleteMixin, View):
    ...




class EnrollmentMixin(SearchMixin,PartialTemplateMixin):
    form_class = EnrollmentForm
    model = Enrollment
    success_url = reverse_lazy("enrollment_list")
    queryset = Enrollment.objects.all()
    paginate_by = 10
    template_dir="enrollment/"


class EnrollmentListView(EnrollmentMixin, ListView):
    template_name = "enrollment/list.html"
    search_lookup_fields = ["student__full_name","student__email"]
    queryset = Enrollment.objects.all()
    

class EnrollmentDetailView(EnrollmentMixin, DetailView):
    template_name = "enrollment/enrollment_detail.html"


class EnrollmentCreateView(EnrollmentMixin, CreateView):
    template_name = "create.html"

class EnrollmentUpdateView(EnrollmentMixin, UpdateView):
    template_name = "update.html"


class EnrollmentDeleteView(EnrollmentMixin,DeleteMixin, View):
    ...
