from django.urls import path, include
from rest_framework.routers import SimpleRouter

from log_category.views import LogCategoryViewSet

app_name = 'log_category'

router = SimpleRouter()

router.register('log-categories', LogCategoryViewSet, basename='log-categories')


urlpatterns = [
    path('', include((router.urls)))
]
