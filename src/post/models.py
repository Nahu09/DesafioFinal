from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default = datetime.now())
    image = models.ImageField(upload_to = 'images/')
    ble = models.CharField(max_length=40)

    def __str__(self):
        return self.title