# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import(
authenticate,
login,
logout,
)
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, TextForm
from proapp.models import Profile,EmployeeProfile,Log, Employee,Text

def inview(request):
        return redirect('/')
        context = {}
        return render(request,'in.html' , context)


def login_view(request):
    title ="Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if user.is_authenticated:
            EmployeeProfile.objects.create(name = user)
        return redirect('/')

    return render(request, "form.html",{"form":form, "title": title})

def register_view(request):
    print(request.user.is_authenticated())
    title = "Registration"
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        co_password = form.cleaned_data.get('Conform_Password')
        if password==co_password:
            pw = password
            user.set_password(pw)
            user.save()

        return redirect('/')
    context = {
        "form":form,
        "title":title
    }
    return render(request, "form.html",context)


def logout_view(request):
    u = request.user
    Log.objects.create(name= u)
    s = EmployeeProfile.objects.filter(name=u).last()
    a = Log.objects.filter(name= u).last()
    Employee.objects.create(name=u,date= s.date, login = s.login, logout = a.logout)
    logout(request)
    return redirect('/')

def pro(request):
    u = request.user
    q = Profile.objects.filter(name__exact= u)
    context = {
        "object_list":q,

    }
    return render(request,'proapp/profile_list.html' , context)

def textview(request):
    title = "Text"
    form = TextForm()
    if request.method == "POST":
        n = request.POST.get("to")
        name = Profile.objects.get(name = n)
        text = request.POST.get("text")

        Text.objects.create(to=name,text=text)
        return redirect('/')
    context = {
        "form":form,
        "title":title
    }
    return render(request, "pform.html",context)
   # return render(request, "form.html",{})
# Create your views here.
