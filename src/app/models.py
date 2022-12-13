from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=255)
    website = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank = False, null=False)