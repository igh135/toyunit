from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.views.generic import ListView

import vote
from vote.models import Vote


class VoteLV(ListView):
    model = Vote