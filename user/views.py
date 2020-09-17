import json
import bcrypt
import jwt
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import View
from rest_framework.generics import DestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from toy_project.settings import SECRET_KEY
from .serializers import UserSerializer
from rest_framework import status


class UserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request, message=getattr(permission, 'message', None)
                )