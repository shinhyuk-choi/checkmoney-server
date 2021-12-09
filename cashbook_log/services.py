from django.db.models import Q

from rest_framework.exceptions import NotFound, APIException

from cashbook.models import CashBook
from cashbook_log.models import DepositLog, ExpenseLog
from log_category.models import DepositCategory, ExpenseCategory


class CashBookLogService:

    def create(self, user, validated_data):
        log_type = validated_data.get('log_type')
        del validated_data['log_type']

        cashbook = self._get_cashbook(user, validated_data.get('cashbook_id'))
        cashbook_log = self._create_log(user, cashbook, log_type, validated_data)
        self._update_balance(cashbook, log_type, validated_data.get('amount'))
        return cashbook_log

    def retrieve(self, log_id, user, validated_data):
        log_type = validated_data.get('log_type')
        if log_type == 'deposit':
            try:
                cashbook_log = DepositLog.objects.get(
                    cashbook__user=user,
                    cashbook_id=validated_data.get('cashbook_id'),
                    id=log_id,
                )
            except DepositLog.DoesNotExist:
                raise NotFound(detail=f"Could not retrieve DepositLog: (id:{log_id})")
        elif log_type == 'expense':
            try:
                cashbook_log = ExpenseLog.objects.get(
                    cashbook__user=user,
                    cashbook_id=validated_data.get('cashbook_id'),
                    id=log_id,
                )
            except ExpenseLog.DoesNotExist:
                raise NotFound(detail=f"Could not retrieve ExpenseLog: (id:{log_id})")
        else:
            raise APIException(detail="Invalid log_type")
        return cashbook_log

    def update(self, log_id, user, validated_data):
        log_type = validated_data.get('log_type')
        cashbook = self._get_cashbook(user, validated_data.get('cashbook_id'))
        cashbook_log = self._get_cashbook_log(cashbook, log_type, log_id)

        if validated_data.get('restore'):
            cashbook_log.is_deleted = False
            self._update_balance(cashbook, log_type, cashbook_log.amount)
        else:
            if validated_data.get('amount'):
                self._update_balance(cashbook, log_type, validated_data.get('amount') - cashbook_log.amount)
                cashbook_log.amount = validated_data.get('amount')
            if validated_data.get('memo'):
                cashbook_log.memo = validated_data.get('memo')

        cashbook_log.save()
        return cashbook_log

    def delete(self, log_id, user, validated_data):
        log_type = validated_data.get('log_type')
        cashbook = self._get_cashbook(user, validated_data.get('cashbook_id'))
        cashbook_log = self._get_cashbook_log(cashbook, log_type, log_id)
        if cashbook_log.is_deleted:
            raise APIException(detail="Already Deleted Log")
        self._update_balance(cashbook, log_type, cashbook_log.amount * -1)
        cashbook_log.is_deleted = True
        cashbook_log.save()
        return cashbook_log

    def _get_cashbook(self, user, cashbook_id):
        try:
            cashbook = CashBook.objects.get(user=user, id=cashbook_id)
        except CashBook.DoesNotExist:
            raise NotFound(detail=f"User does not have CashBook: (id:{cashbook_id})")
        return cashbook

    def _get_cashbook_log(self, cashbook, log_type, log_id):
        if log_type == 'deposit':
            try:
                cashbook_log = DepositLog.objects.get(
                    cashbook=cashbook,
                    id=log_id,
                )
            except DepositLog.DoesNotExist:
                raise NotFound(detail=f"CashBook does not have DepositLog: (id:{log_id})")
        elif log_type == 'expense':
            try:
                cashbook_log = ExpenseLog.objects.get(
                    cashbook=cashbook,
                    id=log_id,
                )
            except ExpenseLog.DoesNotExist:
                raise NotFound(detail=f"CashBook does not have ExpenseLog: (id:{log_id})")
        else:
            raise APIException(detail="Invalid log_type")
        return cashbook_log

    def _update_balance(self, cashbook, log_type, amount):
        if log_type == 'deposit':
            cashbook.balance += amount
        elif log_type == 'expense':
            cashbook.balance -= amount
        else:
            raise APIException(detail="Invalid log_type")
        cashbook.save()

    def _create_log(self, user, cashbook, log_type, validated_data):
        category_id = validated_data.get('category_id')
        if log_type == 'deposit':
            try:
                category = DepositCategory.objects.get(Q(user=user) | Q(user=None),
                                                       id=category_id)
            except DepositCategory.DoesNotExist:
                raise NotFound(detail=f"User does not have DepositCategory: (id:{category_id})")
            cashbook_log = DepositLog.objects.create(cashbook=cashbook, category=category, **validated_data)

        elif log_type == 'expense':
            try:
                category = ExpenseCategory.objects.get(Q(user=user) | Q(user=None),
                                                       id=category_id)
            except DepositCategory.DoesNotExist:
                raise NotFound(detail=f"User does not have ExpenseCategory: (id:{category_id})")

            cashbook_log = ExpenseLog.objects.create(cashbook=cashbook, category=category, **validated_data)
        else:
            raise APIException(detail="Invalid log_type")
        return cashbook_log
