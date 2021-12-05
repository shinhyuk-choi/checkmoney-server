from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
# PROJECT
from user.models import User


class UserService:
    class Meta:
        model = User

    def create(self, **validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        if not password:
            raise ValidationError('password empty')
        user = self.Meta.model.objects.create(email=email, password=password)
        Token.objects.create(user=user)
        return user
