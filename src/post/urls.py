from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from post import views


urlpatterns = [
    #path('create/', views.Create.as_view(), name='postcreate_view')
    path('create/', views.PostView.create, name='postcreate_view')
]
