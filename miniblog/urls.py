
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.User_Logout, name='logout'),
    path('login/', views.User_Login, name='login'),
    path('signup/', views.User_Signup, name='signup'),
]
