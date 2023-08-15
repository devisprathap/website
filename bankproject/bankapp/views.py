from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def  register(request):


    return render(request,"register.html")


def login(request):

    return render(request,"login.html")






def form(request):
    return render(request,"form.html")
def logout(request):
    return render(request,"logout.html")

def home(request):
    return render(request,"home.html")
def link(request):
    return render(request,"link.html")
    return redirect('/')