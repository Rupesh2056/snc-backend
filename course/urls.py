from django.urls import path

from course.views import CourseCreateView, CourseDeleteView, CourseDetailView, CourseListView, CourseUpdateView

urlpatterns = [
    path("course/",CourseListView.as_view(),name="course_list"),   
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("course/create/", CourseCreateView.as_view(), name="course_create"),
    path("course/<int:pk>/update/", CourseUpdateView.as_view(), name="course_update"),
    path("course/delete", CourseDeleteView.as_view(), name="course_delete"), 
]
