from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic import CreateView
from app.form import SignUpForm

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


class SignUp(CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home_view')


