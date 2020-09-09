from django.contrib import admin
from django.urls import path, include

import user
from vote import views, models
from vote.views import VoteLV

urlpatterns = [
    path('', VoteLV.as_view(), name='vote_list'),
]
