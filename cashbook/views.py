from django.utils.decorators import method_decorator
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cashbook.models import CashBook
from cashbook.serializers import CashBookSerializer, UpdateCashBookSerializer
from cashbook.services import CashBookService
from schema.cashbook import CashBookSchema


class CashBookViewSet(viewsets.GenericViewSet):
    queryset = CashBook.objects.all()
    serializer_class = CashBookSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        가계부 생성
        - POST /cashbooks/
        - data params
            - name(default:'기본')
        """
        serializer = CashBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        cashbook = CashBookService().create(request.user, validated_data)

        rtn = CashBookSerializer(cashbook).data
        return Response(rtn, status=status.HTTP_200_OK)

    def list(self, request):
        """
        가계부 리스트 조회
        - GET /cashbooks/
        """
        cashbooks = CashBookService().list(request.user)

        rtn = CashBookSerializer(cashbooks, many=True).data
        return Response(rtn, status=status.HTTP_200_OK)

    def retrieve(self, request, pk:int):
        """
        가계부 정보 조회
        - GET /cashbooks/{cashbook_id}/
        """
        cashbook = CashBookService().retrieve(request.user, pk)

        rtn = CashBookSerializer(cashbook).data
        return Response(rtn, status=status.HTTP_200_OK)

    def update(self, request, pk:int):
        """
        가계부 수정
        - PUT /cashbooks/{cashbook_id}/
        - data params
            - name(required)
        """
        serializer = UpdateCashBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        cashbook = CashBookService().update(request.user, pk, validated_data)

        rtn = CashBookSerializer(cashbook).data
        return Response(rtn, status=status.HTTP_200_OK)

    def destroy(self, request, pk: int):
        """
        가계부 삭제
        - DELETE /cashbooks/{cashbook_id}/
        """
        cashbook = CashBookService().delete(request.user, pk)

        return Response(status=status.HTTP_200_OK)
