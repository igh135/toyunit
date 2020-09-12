import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from lunar.models import Lunar
from lunar.serializers import LunarSerializer


class LunarImageView(ListAPIView):
    queryset = Lunar.objects.all()
    serializer_class = LunarSerializer
