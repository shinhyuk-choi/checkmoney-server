from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException

from user.models import User


class UserService:
    class Meta:
        model = User

    def create(self, **validated_data):
        user = self.Meta.model.objects.create(**validated_data)
        Token.objects.create(user=user)
        return user
