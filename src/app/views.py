from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView
from app.form import SignUpForm
from post.models import Post
from app.models import UserProfile

# Create your views here.


class Login(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home_view')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_view')
        return super().dispatch(request, *args, **kwargs)

class Logout(LogoutView):
    template_name = 'login.html'
    next_page = 'login_view'


class Home(TemplateView):
    template_name = 'index.html'
    extra_context = {'posts': Post.objects.all()}



class SignUp(CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login_view')



class About(TemplateView):
    template_name = 'about.html'

def notFound(request, exeption):

    return render(request, 'not_found.html')


#def myProfile(request):
    #context = {'user': UserProfile.objects.first}
    #return render(request, 'myprofile.html', context = context)

class CreateProfile(CreateView):
    template_name = 'myprofile.html'
    model = UserProfile
    fields = [
        'email',
        'description',
        'website',
        'image'
    ]
    success_url = reverse_lazy('home_view')
    
    def post(self, request):
        data = request.POST
        user = request.user
        email = data['email']
        image = data['image']
        description = data['description']
        website = data['website']

        user_data = UserProfile.objects.filter(user=user)
        if user_data:
            user_data.email = email
            user_data.image = image
            user_data.description = description
            user_data.website = website
            user_data.update()
            return redirect(reverse_lazy('home_view'))


        profile = UserProfile.objects.create(user=user, email=email, image=image, description=description, website=website)
        return redirect(reverse_lazy('home_view'))


        



