from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cashbook.views import CashBookViewSet

app_name = 'cashbook'

router = SimpleRouter()

router.register('cashbooks', CashBookViewSet, basename='cashbooks')


urlpatterns = [
    path('', include((router.urls)))
]
