from django.shortcuts import render
from post.models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from post.form import PostCreate
from django.http import HttpRequest
# Create your views here.

#class Create(CreateView):
    #template_name = 'create.html'
    #form_class = PostCreate
    #success_url = reverse_lazy('home')
    #model = Post
    #fields = '__all__'

class PostView(HttpRequest):
    def create(request):
        print(request.user)
        print('hola')
        form = PostCreate(initial={'author': request.user})
        context = {'form': form}
        return render(request, 'create.html', context=context)

