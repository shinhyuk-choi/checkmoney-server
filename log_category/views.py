from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from log_category.models import DepositCategory, ExpenseCategory
from log_category.serializers import LogCategorySerializer, CategoryTypeSerializer


class LogCategoryViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        POST /log-categories/
        data params
            - log_type(required: 'deposit' or 'expense')
        """
        serializer = LogCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        if validated_data.get('log_type') == 'deposit':
            category = DepositCategory.objects.create(user=request.user, name=validated_data.get('name'))
        else:
            category = ExpenseCategory.objects.create(user=request.user, name=validated_data.get('name'))

        rtn = LogCategorySerializer(category).data
        return Response(rtn, status=status.HTTP_201_CREATED)

    def list(self, request):
        """
        GET /log-categories/
        query_params
            - log_type(required: 'deposit' or 'expense')
        """
        serializer = CategoryTypeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        if validated_data.get('log_type') == 'deposit':
            categories = DepositCategory.objects.filter(Q(user=request.user) | Q(user=None))
        else:
            categories = ExpenseCategory.objects.filter(Q(user=request.user) | Q(user=None))

        rtn = LogCategorySerializer(categories, many=True).data
        return Response(rtn, status=status.HTTP_200_OK)

    def update(self, request, pk):
        """
        PUT /log-categories/{log_category_id}
        data params
            - log_type(required: 'deposit' or 'expense')
            - name(required)
        """
        serializer = LogCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        if validated_data.get('log_type') == 'deposit':
            category = DepositCategory.objects.get(user=request.user, id=pk)
        else:
            category = ExpenseCategory.objects.get(user=request.user, id=pk)
        category.name = validated_data.get('name')
        category.save()

        rtn = LogCategorySerializer(category).data
        return Response(rtn, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """
        DELETE /log-categories/{log_category_id}
        data params
            - log_type(required: 'deposit' or 'expense')
        """

        serializer = CategoryTypeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        if validated_data.get('log_type') == 'deposit':
            category = DepositCategory.objects.get(user=request.user, id=pk)
        else:
            category = ExpenseCategory.objects.get(user=request.user, id=pk)

        category.delete()
        return Response(status=status.HTTP_200_OK)
