
from django.urls import path
from django.contrib.auth.views import LoginView

from user.views import IndexView, InstructorCreateView, InstructorDeleteView, InstructorDetailView, InstructorListView, InstructorUpdateView, StudentCreateView, StudentDeleteView, StudentDetailView, StudentListView, StudentUpdateView, logout_user


urlpatterns = [
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="user_login"),
    path('logout/', logout_user,name="user_logout"),
]

# student
urlpatterns += [
    path("student/",StudentListView.as_view(),name="student_list"),   
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("student/create/", StudentCreateView.as_view(), name="student_create"),
    path("student/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("student/delete", StudentDeleteView.as_view(), name="student_delete"), 
]


# instructor
urlpatterns += [
    path("instructor/",InstructorListView.as_view(),name="instructor_list"),   
    path("instructor/<int:pk>/", InstructorDetailView.as_view(), name="instructor_detail"),
    path("instructor/create/", InstructorCreateView.as_view(), name="instructor_create"),
    path("instructor/<int:pk>/update/", InstructorUpdateView.as_view(), name="instructor_update"),
    path("instructor/delete", InstructorDeleteView.as_view(), name="instructor_delete"), 
]


