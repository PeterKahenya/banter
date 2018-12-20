from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponse
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2' )


class SignUp(generic.CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy("login")
    template_name="registration/signup.html"

