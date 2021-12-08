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

        cashbook = CashBook.objects.create(user=request.user, **serializer.validated_data)

        rtn = CashBookSerializer(cashbook).data
        return Response(rtn, status=status.HTTP_200_OK)

    def list(self, request):
        """
        가계부 리스트 조회
        - GET /cashbooks/
        """
        cashbooks = CashBook.objects.filter(user=request.user)

        rtn = CashBookSerializer(cashbooks, many=True).data
        return Response(rtn, status=status.HTTP_200_OK)

    def update(self, request, pk):
        """
        가계부 수정
        - PUT /cashbooks/{cashbook_id}/
        - data params
            - name(required)
        """
        try:
            cashbook = CashBook.objects.get(user=request.user, id=pk)
        except CashBook.DoesNotExist:
            return Response({'error': 'Not Authorized'}, status=status.HTTP_403_FORBIDDEN)

        name = request.data.get('name')
        if name is not None:
            cashbook.name = name
            cashbook.save()

        rtn = CashBookSerializer(cashbook).data
        return Response(rtn, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """
        가계부 삭제
        - DELETE /cashbooks/{cashbook_id}/
        """
        try:
            cashbook = CashBook.objects.get(user=request.user, id=pk)
        except CashBook.DoesNotExist:
            return Response({'error': 'Not Authorized'}, status=status.HTTP_403_FORBIDDEN)

        cashbook.delete()
        return Response(status=status.HTTP_200_OK)
