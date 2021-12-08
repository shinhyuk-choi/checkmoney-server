from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class LogCategoryViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        POST /log-categories/
        """
        return Response()

    def list(self, request):
        """
        GET /log-categories/
        """
        return Response()

    def update(self, request, pk):
        """
        PUT /log-categories/{log_category_id}
        """
        return Response()

    def destroy(self, request, pk):
        """
        DELETE /log-categories/{log_category_id}
        """
        return Response()
