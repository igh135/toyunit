import json
import bcrypt
import jwt
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from rest_framework.generics import DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from toy_project.settings import SECRET_KEY
from .serializers import UserSerializer
from rest_framework import status


class UserView(APIView):
    """
    POST /user
    """

    def post(self, request):
        data = json.loads(request.body)
        if User.objects.filter(UserID=data['UserID']).exists():
            return JsonResponse({"message": "existing UserID"}, status=400)
        else:
            User.objects.create(
                UserID=data['UserID'],
                password=bcrypt.hashpw(data['password'].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
                name=data['name']
            ).save()
            return HttpResponse(status=200)

    def get(self, request):
        user_data = User.objects.value()
        return JsonResponse({'user': list(user_data)}, status=200)


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignIn(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
