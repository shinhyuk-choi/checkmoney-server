from django.db import transaction

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cashbook_log.models import DepositLog
from cashbook_log.serializers import CashBookLogSerializer, LogTypeSerializer, UpdateLogSerializer, ListLogSerializer
from cashbook_log.services import CashBookLogService


class CashBookLogViewSet(viewsets.GenericViewSet):
    queryset = DepositLog.objects.all()
    serializer_class = CashBookLogSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def create(self, request):
        """
        가계부 내역 생성
        - POST /cashbook-logs/
        - data params
            - cashbook_id (required)
            - category_id (required)
            - log_type (required: "deposit" or "expense")
            - amount (required)
            - date (required)
            - memo

        """
        serializer = CashBookLogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        cashbook_log = CashBookLogService().create(request.user, validated_data)
        rtn = CashBookLogSerializer(cashbook_log).data
        return Response(rtn, status=status.HTTP_201_CREATED)

    def list(self, request):
        """
        가계부 내역 리스트 조회
        - GET /cashbook-logs/
        - query params
            - cashbook_id (required)
        """
        serializer = ListLogSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        cashbook_logs = CashBookLogService().list(request.user, validated_data)
        rtn = CashBookLogSerializer(cashbook_logs, many=True).data
        return Response(rtn, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """
        가계부 내역 단건(상세내역) 조회
        - GET /cashbook-logs/{log_id}/
        - query params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        serializer = LogTypeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        cashbook_log = CashBookLogService().retrieve(pk, request.user, validated_data)
        rtn = CashBookLogSerializer(cashbook_log).data
        return Response(rtn, status=status.HTTP_200_OK)

    @transaction.atomic
    def update(self, request, pk):
        """
        가계부 내역 수정
        - PUT /cashbook-logs/{log_id}/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        serializer = UpdateLogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        cashbook_log = CashBookLogService().update(pk, request.user, validated_data)
        rtn = CashBookLogSerializer(cashbook_log).data
        return Response(rtn, status=status.HTTP_200_OK)

    @transaction.atomic
    def destroy(self, request, pk):
        """
        가계부 내역 삭제
        - DELETE /cashbook-logs/{log_id}/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        serializer = LogTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        cashbook_log = CashBookLogService().delete(pk, request.user, validated_data)
        return Response(status=status.HTTP_200_OK)
