from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, LoginForm

# Create your views here.

# Home function
def home(request):
  return render(request, 'blog/home.html')

# About function
def about(request):
  return render(request, 'blog/about.html')

# Contact function
def contact(request):
  return render(request, 'blog/contact.html')

# Dashboard function
def dashboard(request):
  return render(request, 'blog/dashboard.html')

# Signup function
def User_Signup(request):
  form = SignupForm()
  return render(request, 'blog/signup.html', {'form': form})

# LogOut function
def User_Logout(request):
  return HttpResponseRedirect('/')

# Login function
def User_Login(request):
  form = LoginForm()
  return render(request, 'blog/login.html', {'form':form})



