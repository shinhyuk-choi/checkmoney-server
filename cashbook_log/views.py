from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cashbook_log.serializers import CashBookLogSerializer


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
        serializer = CashBookLogSerializer(data=request.data)
        return Response()

    def list(self, request):
        """
        가계부 내역 리스트 조회
        - GET /cashbook-logs/
        - data params
            - cashbook_id (required)
        """
        return Response()

    def retrieve(self, request, pk):
        """
        가계부 내역 단건(상세내역) 조회
        - GET /cashbook-logs/{log_id}/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        return Response()

    def update(self, request, pk):
        """
        가계부 내역 수정
        - PUT /cashbook-logs/{log_id}/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        return Response()

    def destroy(self, request, pk):
        """
        가계부 내역 삭제
        - DELETE /cashbook-logs/{log_id}/
        - data params
            - cashbook_id (required)
            - log_type (required: "deposit" or "expense")
        """
        return Response()
