from django.contrib.auth import authenticate, login, logout

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# PROJECT
from user.serializers import UserSerializer
from user.services import UserService


class CashBookViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated()]

    def create(self, request):
        """
        가계부 생성
        - POST /cashbooks/
        - data params
            - name(default:'기본')
        """
        pass

    def update(self, request):
        """
        가계부 수정
        - PUT /cashbooks/{cashbook_id}/
        - data params
            - name(required)
        """
        pass

    def delete(self, request):
        """
        가계부 삭제
        - DELETE /cashbooks/{cashbook_id}/
        """
        pass


class CashBookLogViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated()]

    def create(self, request):
        """
        가계부 내역 생성
        - POST /cashbook-logs/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")

        """
        pass

    def list(self, request):
        """
        가계부 내역 리스트 조회
        - GET /cashbook-logs/
        - data params
            - cashbook_id (required)
        """
        pass

    def retrieve(self, request, pk):
        """
        가계부 내역 단건(상세내역) 조회
        - GET /cashbook-logs/{log_id}/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        pass

    def update(self, request, pk):
        """
        가계부 내역 수정
        - PUT /cashbook-logs/{log_id}/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        pass

    def delete(self, request, pk):
        """
        가계부 내역 삭제
        - DELETE /cashbook-logs/{log_id}/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        pass
