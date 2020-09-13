from django.contrib import admin
from django.urls import path, include

import user
from vote import views, models
from vote.views import VoteView, VoteGetView, VoteImgView

urlpatterns = [
    path('list', VoteGetView.as_view()),
    path('enroll',VoteView.as_view()),
    path('list/img',VoteGetView.voteImg),
    path('enroll/img',VoteImgView.as_view()),
]
