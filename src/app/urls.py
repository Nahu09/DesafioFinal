from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from app import views



urlpatterns = [
    path('', views.Login.as_view(), name="login_view"),
    path('home/', views.Home.as_view(), name='home_view'),
    path('logout/', views.Logout.as_view(), name="logout_view"),
    path('signup/', views.SignUp.as_view(), name="signup_view"),
    path('about/', views.About.as_view(), name='about_view'),
    #path('myprofile/', views.myProfile, name='myprofile_view'),
    path('createprofile/', views.CreateProfile.as_view(), name='myprofile_view')
    
]

