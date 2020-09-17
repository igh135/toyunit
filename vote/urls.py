from urllib import request

from django.contrib import admin
from django.urls import path, include
from rest_framework import request

import user
from vote import views, models
from vote.models import Vote
from vote.views import VoteView, VoteGetView, VoteImgView, VoteDeleteView

urlpatterns = [
    path('', VoteGetView.as_view()),
    path('enroll', VoteView.as_view()),
    path('img', VoteGetView.voteImg),
    path('enroll/img', VoteImgView.as_view()),
    path('delete',VoteDeleteView.as_view())
]
