from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

from utils.views import PartialTemplateMixin


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy("user_login"))

class IndexView(View):
    template_name = "index.html"
    authorized_groups = ["admin"]

    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,self.template_name,context)

class StudentListView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"user/student_list.html")