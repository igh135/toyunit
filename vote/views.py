from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


def post_list(request):
    return render(request, 'vote/post_list.html', {})
