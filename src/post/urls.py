from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from post import views



urlpatterns = [
    path('create/', views.Create.as_view(), name='postcreate_view'),
    path('details/<pk>', views.Details.as_view(), name='details_view'),
    path('myposts/', views.myPost, name='myposts_view'),
    path('delete/<pk>', views.Delete.as_view(), name='delete_view'),
    path('update/<pk>', views.Update.as_view(), name='update_view')


]

