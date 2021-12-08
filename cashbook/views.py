from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cashbook.models import CashBook
from cashbook.serializers import CashBookSerializer


class CashBookViewSet(viewsets.GenericViewSet):
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
        CashBook.objects.create(user=request.user, **serializer.validated_data)
        return Response()

    def list(self, request):
        """
        가계부 리스트 조회
        - GET /cashbooks/
        """
        cashbooks = CashBook.objects.filter(user=request.user)
        return Response(CashBookSerializer(cashbooks, many=True).data)

    def update(self, request, pk):
        """
        가계부 수정
        - PUT /cashbooks/{cashbook_id}/
        - data params
            - name(required)
        """
        # 가계부가 유저의 소유인지 확인한다.
        try:
            cashbook = CashBook.objects.get(user=request.user, id=pk)
        except CashBook.DoesNotExist:
            pass
        name = request.data.get('name')
        if name is not None:
            cashbook.name = name
            cashbook.save()
        return Response()

    def destroy(self, request, pk):
        """
        가계부 삭제
        - DELETE /cashbooks/{cashbook_id}/
        """
        try:
            cashbook = CashBook.objects.get(user=request.user, id=pk)
        except CashBook.DoesNotExist:
            pass
        name = request.data.get('name')
        if name is not None:
            cashbook.name = name
            cashbook.save()
        return Response()
