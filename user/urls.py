
from django.contrib import admin
from django.http import request
from django.urls import path, include

import user
from user import views, models
from user.models import User
from user.views import SignInView

urlpatterns = [
    path('up',views.post),
    path('in',SignInView.post),
]
