from django.shortcuts import render
from post.models import Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from post.form import PostCreate
from django.http import HttpRequest
# Create your views here.

def myPost(request):
    context = {'posts':Post.objects.filter(author=request.user)}
    return render(request, 'myposts.html', context)



class Create(CreateView):
    template_name = 'create.html'
    form_class = PostCreate
    success_url = reverse_lazy('home_view')
    model = Post
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Details(DetailView):
    template_name = 'details.html'
    model = Post
    fields = '__all__'
    

class Delete(DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('myposts_view')


class Update(UpdateView):
    template_name = 'update.html'
    model = Post
    success_url = reverse_lazy('myposts_view')
    fields = [            
            'title', 
            'subtitle' ,
            'description',
            'image'
            ]


