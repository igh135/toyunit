import body as body
from django.contrib import admin
from django.http import request
from django.urls import path, include

import user
from user import views, models
from user.models import User

from django.urls import path, include
from .views import HelloAPI, RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
]
