from django.contrib import admin
from django.urls import path, include

import user
from vote import views, models

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
