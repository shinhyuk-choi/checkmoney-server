from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# PROJECT
from user.serializers import UserSerializer
from user.services import UserService


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated()]

    def get_permissions(self):
        if self.action in ('create', 'login'):
            return [AllowAny()]
        return self.permission_classes

    def create(self, request):
        """
        - 회원 가입
        - POST users/
        - data params
            - email(required)
            - password(required)
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService().create(**serializer.validated_data)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        """
        - 로그인
        - POST users/login/
        - data params
            - email(required)
            - password(required)
        """
        user = UserService().login(request)
        data = UserSerializer(user).data
        return Response(data)

    @action(detail=False, methods=['POST'])
    def logout(self, request):
        """
        - 로그아웃
        - POST users/logout/
        """
        UserService().logout(request)
        return Response()
