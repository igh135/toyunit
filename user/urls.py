from django.contrib import admin
from django.http import request
from django.urls import path, include

import user
from user import views, models

urlpatterns = [
    path('', views.UserCreateView.as_view(), name='index'),
    path('signup', views.user_new, name='signup'),
]
