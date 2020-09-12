from django.contrib import admin
from django.http import request
from django.urls import path, include

import user
from user import views, models

urlpatterns = [
    path('signup', views.UserView.as_view()),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('signin', views.SignIn.as_view()), # User pk id가 전달되는 경우
    path('delete',views.UserDeleteView.as_view()),
]
