import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.views.generic import ListView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView

import lunar
import vote
from lunar.models import Lunar
from lunar.serializers import LunarSerializer
from lunar.views import LunarImageView
from vote.models import Vote
from vote.serializers import VoteSerializer


class VoteView(CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteImgView(CreateAPIView):
    queryset = Lunar.objects.all()
    serializer_class = LunarSerializer


class VoteGetView(ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def voteImg(self):
        return HttpResponse(Lunar.prof_img)

class VoteCountView(UpdateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

