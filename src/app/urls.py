from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from app import views



urlpatterns = [
    path('', views.Login.as_view(), name="login_view"),
    path('home/', views.Home.as_view(), name='home_view'),
    path('logout/', views.Logout.as_view(), name="logout_view"),
    path('signup/', views.SignUp.as_view(), name="signup_view")
    
]