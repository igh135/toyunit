import json
import bcrypt
import jwt

from toy_project.settings import SECRET_KEY
from .models import User

from django.views import View
from django.http import JsonResponse, HttpResponse


def post(self, request):
    if request == request.POST:
        data = json.loads(request.body)
        try:
            if User.objects.filter(UserID=data['UserID']).exists():
                return HttpResponse(status=400)

            # == 비밀번호 암호화==#

            password = data['password'].encode('utf-8')  # 입력된 패스워드를 바이트 형태로 인코딩
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())  # 암호화된 비밀번호 생성
            password_crypt = password_crypt.decode('utf-8')  # DB에 저장할 수 있는 유니코드 문자열 형태로 디코딩

            # ====================#

            User(
                UserID=data['UserID'],
                password=password_crypt,  # 암호화된 비밀번호를 DB에 저장
                name=data['name']
            ).save()

            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(UserID=data['UserID']).exists():
                user = User.objects.get(UserID=data['UserID'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):

                    # ----------토큰 발행----------#

                    token = jwt.encode({'UserID': data['UserID']}, SECRET_KEY, algorithm="HS256")
                    token = token.decode('utf-8')  # 유니코드 문자열로 디코딩

                    # -----------------------------#
                    return JsonResponse({"token": token}, status=200)

                else:
                    return HttpResponse(status=401)

            return HttpResponse(status=400)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)
