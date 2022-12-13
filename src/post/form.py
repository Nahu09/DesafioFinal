from django import forms
from django.forms import ModelForm
from post.models import Post

class PostCreate(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title', 
            'subtitle' ,
            'description',
            'date',
            'image'
            ]