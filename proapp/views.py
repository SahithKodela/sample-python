# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404
from login.forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from login.forms import EmployeeForm
from .models import Profile,Employee

class HomeView(LoginRequiredMixin,TemplateView):
    form_class = UserLoginForm
    login_url = '/login/'
    template_name = 'home.html'
    #success_url = "/home/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        s = str(instance.user)
        return super(HomeView, self).form_valid(form),s

def cal(request):
    s = str(request.user)
    if s == "sahithkodela":
        title = "Registration-1"
        form = EmployeeForm()
        if request.method== "POST":
            name = request.POST.get("name")
            Email= request.POST.get("Email")
            FatherName= request.POST.get("FatherName")
            DateofBirth= request.POST.get("DateofBirth")
            age= request.POST.get("age")
            address= request.POST.get("address")
            image = request.FILES.get("image")
            Profile.objects.create(name= name, Email= Email, FatherName= FatherName, DateofBirth= DateofBirth, age= age, address= address, image = image)

    else:
         return redirect('/')
    context = {
        "form":form,
        "title":title,
        "s":s
    }
    return render(request,'pform.html' , context)

def time(request):
    u = request.user
    q = Employee.objects.filter(name__exact= u)
    #l = LogOut.objects.filter(name__exact= u)
    context = {
        "object_list":q,


    }
    return render(request,'proapp/att.html' , context)

def post_view():
    pass

def profile_view(request):
    u = request.user
    q = Profile.objects.all()
    context = {
        "object_list":q,

    }
    return render(request,'proapp/profile_list.html' , context)


# Create your views here.
