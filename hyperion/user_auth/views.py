from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import generic
from django.core.validators import RegexValidator
from django import forms


# Create your views here.
class CustomSignUpForm(UserCreationForm):
    #creating a regex for the username feild for email 
    email_validator = RegexValidator(
        regex=r'^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$',
        message='Enter a valid email address.',
        code='invalid_email'
        )
    username = forms.CharField(
        max_length = 30,
        required =True,
        help_text = 'Enter a valid email adress',
        validators = [email_validator]
        )
    class Meta:
        model = User
        fields = ('first_name','username', 'password1', 'password2')

class SignUpView(generic.CreateView):
    form_class = CustomSignUpForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "registration/signup.html"


def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))

def show_user(request):
    print(request.user.username)
    context ={
        "username": request.user.username,
        "password": request.user.password,
        "firstname": request.user.first_name
    }
    return render(request, 'authentication/user.html',context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('webhome:home'))
