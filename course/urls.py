from django.urls import path

from course.views import CourseCreateView, CourseDeleteView, CourseDetailView, CourseListView, CourseUpdateView, EnrollmentCreateView, EnrollmentDeleteView, EnrollmentDetailView, EnrollmentListView, EnrollmentUpdateView

urlpatterns = [
    path("course/",CourseListView.as_view(),name="course_list"),   
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("course/create/", CourseCreateView.as_view(), name="course_create"),
    path("course/<int:pk>/update/", CourseUpdateView.as_view(), name="course_update"),
    path("course/delete", CourseDeleteView.as_view(), name="course_delete"), 
]


# enrollment
urlpatterns += [
    path("enrollment/",EnrollmentListView.as_view(),name="enrollment_list"),   
    path("enrollment/<int:pk>/", EnrollmentDetailView.as_view(), name="enrollment_detail"),
    path("enrollment/create/", EnrollmentCreateView.as_view(), name="enrollment_create"),
    path("enrollment/<int:pk>/update/", EnrollmentUpdateView.as_view(), name="enrollment_update"),
    path("enrollment/delete", EnrollmentDeleteView.as_view(), name="enrollment_delete"), 
]