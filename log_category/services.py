from django.db.models import Q

from rest_framework.exceptions import NotFound, APIException

from log_category.models import DepositCategory, ExpenseCategory


class LogCategoryService:
    def create(self, user, validated_data):
        log_type = validated_data.get('log_type')
        if log_type == 'deposit':
            category = DepositCategory.objects.create(user=user, name=validated_data.get('name'))
        elif log_type == 'expense':
            category = ExpenseCategory.objects.create(user=user, name=validated_data.get('name'))
        else:
            raise APIException(detail='Invalid log_type')
        return category

    def list(self, user, validated_data):
        log_type = validated_data.get('log_type')
        if log_type == 'deposit':
            categories = DepositCategory.objects.filter(Q(user=user) | Q(user=None))
        elif log_type == 'expense':
            categories = ExpenseCategory.objects.filter(Q(user=user) | Q(user=None))
        else:
            raise APIException(detail='Invalid log_type')
        return categories

    def update(self, user, category_id, validated_data):
        log_type = validated_data.get('log_type')
        category = self._get_log_category(user, category_id, log_type)
        category.name = validated_data.get('name')
        category.save()
        return category

    def delete(self, user, category_id, validated_data):
        log_type = validated_data.get('log_type')
        category = self._get_log_category(user, category_id, log_type)
        category.delete()

    def _get_log_category(self, user, category_id, log_type):
        if log_type == 'deposit':
            try:
                category = DepositCategory.objects.get(user=user, id=category_id)
            except DepositCategory.DoesNotExist:
                raise NotFound(detail=f"User does not have DepositCategory: (id:{category_id})")
        elif log_type == 'expense':
            try:
                category = ExpenseCategory.objects.get(user=user, id=category_id)
            except ExpenseCategory.DoesNotExist:
                raise NotFound(detail=f"User does not have DepositCategory: (id:{category_id})")
        else:
            raise APIException(detail="Invalid log_type")
        return category
