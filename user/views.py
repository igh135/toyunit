import json

from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import include
from django.views.generic.base import View

from django.views.generic import CreateView
from .forms import UserForm
from .models import User


class UserCreateView(CreateView):  # 2
    form_class = UserForm

    template_name = 'user/index.html'

    def after(self):
        return render(self, 'user/signup.html')


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid() and form != User:
            user = form.save(commit=True)
            user.save()
            return redirect('/user', {'form': form})
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})
