from django.contrib.auth import authenticate, login, logout

from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
# PROJECT
from user.models import User


class UserService:
    class Meta:
        model = User

    def create(self, **validated_data):
        user = self.Meta.model.objects.create(**validated_data)
        Token.objects.create(user=user)
        return user

    def login(self, request):
        try:
            user = authenticate(request, email=request.data.get('email'), password=request.data.get('password'))
            login(request, user)
        except:
            raise APIException("Wrong email or wrong password")
        return user

    def logout(self, request):
        logout(request)
