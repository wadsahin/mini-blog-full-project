from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, LoginForm, postForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserPost
from django.contrib.auth.models import Group


# Create your views here.

# Home function
def home(request):
  posts = UserPost.objects.all()
  return render(request, 'blog/home.html', {'posts':posts})

# About function
def about(request):
  return render(request, 'blog/about.html')

# Contact function
def contact(request):
  return render(request, 'blog/contact.html')

# Dashboard function
def dashboard(request):
  if request.user.is_authenticated:
   posts = UserPost.objects.all()
   user = request.user
   full_name = user.get_full_name()
   group = user.groups.all()
   return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':group})
  else:
   return HttpResponseRedirect('/login/')

# Signup function
def User_Signup(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      # permission feature add here
      savedUser = form.save()
      group = Group.objects.get(name='Author')
      savedUser.groups.add(group)
      # permission feature end here
      messages.success(request, 'Congratulations!! You have become an Author :)')
      form = SignupForm()
  else:
    form = SignupForm()
  return render(request, 'blog/signup.html', {'form': form})

# LogOut function
def User_Logout(request):
  logout(request)
  return HttpResponseRedirect('/')

# Login function
def User_Login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      form = LoginForm(request=request, data=request.POST)
      if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        login(request, user)
        messages.success(request, 'Welcome to your Dashboard !!')
        return HttpResponseRedirect('/dashboard/')
    else:
      form = LoginForm()
    return render(request, 'blog/login.html', {'form':form})
  else:
    return HttpResponseRedirect('/dashboard/')

# Add new post
def add_post(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = postForm(request.POST)
      if form.is_valid():
        form.save()
        form = postForm()
    else:
      form = postForm()
    return render(request, 'blog/addpost.html', {'form':form})
  else:
    return HttpResponseRedirect('/login/')
  

# Upadte post
def upate_post(request, id):
  if request.user.is_authenticated:
    if request.method == "POST":
      pi = UserPost.objects.get(pk = id)
      form = postForm(request.POST, instance=pi)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/dashboard/')
    else:
      pi = UserPost.objects.get(pk = id)
      form = postForm(instance=pi)
    return render(request, 'blog/updatepost.html', {'form':form})
  else:
    return HttpResponseRedirect('/login/')


# Delete post
def delete_post(request, id):
  if request.user.is_authenticated:
    if request.method == "POST":
      pi = UserPost.objects.get(pk = id)
      pi.delete()
      return HttpResponseRedirect('/dashboard/')
  else:
    return HttpResponseRedirect('/login/')
