from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse



# Create your views here.
def home(request):
    return render(request,"home.html")
def login(request):
    return render(request, "registration/login.html")

def signup(request):
    return render(request, "registration/signup.html")





