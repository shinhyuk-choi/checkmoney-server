from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'token',
        )

    def validate_password(self, value):
        return make_password(value)

    def get_token(self, user) -> str:
        token= user.auth_token.key
        return token
