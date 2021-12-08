from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cashbook_log.views import CashBookLogViewSet

app_name = 'cashbook_log'

router = SimpleRouter()

router.register('cashbook-logs', CashBookLogViewSet, basename='cashbook-logs')

urlpatterns = [
    path('', include((router.urls)))
]
