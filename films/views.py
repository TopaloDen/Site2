from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'registration/Login.html'


def about(request):
    return render(request, 'About.html')


def sign(request):
    return render(request, 'registration/Sign.html')


def login(request):
    return render(request, 'registration/Login.html')
