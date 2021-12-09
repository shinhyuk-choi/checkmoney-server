from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from log_category.serializers import LogCategorySerializer, CategoryTypeSerializer
from log_category.services import LogCategoryService


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

        category = LogCategoryService().create(request.user, validated_data)

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

        categories = LogCategoryService().list(request.user, validated_data)

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

        category = LogCategoryService().update(request.user, pk, validated_data)

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

        LogCategoryService().delete(request.user, pk, validated_data)

        return Response(status=status.HTTP_200_OK)
