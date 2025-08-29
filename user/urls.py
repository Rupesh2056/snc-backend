
from django.urls import path
from django.contrib.auth.views import LoginView

from user.views import IndexView, StudentListView, logout_user


urlpatterns = [
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="user_login"),
    path('logout/', logout_user,name="user_logout"),


]
