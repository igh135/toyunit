import self
from django.contrib import admin
from django.http import request
from django.urls import path, include

import user
from user import views, models
from user.models import User

urlpatterns = [
    path('signup', views.UserView.as_view()),
    path('login', views.LoginView.post),
    path('delete',views.UserDeleteView.as_view()),
]
