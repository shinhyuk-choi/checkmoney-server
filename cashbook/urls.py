from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cashbook.views import CashBookViewSet, CashBookLogViewSet

app_name = 'cashbook'

router = SimpleRouter()

router.register('cashbooks', CashBookViewSet, basename='cashbooks')
router.register('cashbook-logs', CashBookLogViewSet, basename='cashbook-logs')

urlpatterns = [
    path('', include((router.urls)))
]
