from django.db.models import Q

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
            cashbook_log = DepositLog.objects.get(
                cashbook__user=user,
                cashbook_id=validated_data.get('cashbook_id'),
                id=log_id,
            )
        else:
            cashbook_log = ExpenseLog.objects.get(
                cashbook__user=user,
                cashbook_id=validated_data.get('cashbook_id'),
                id=log_id,
            )
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
            # todo: 에러 처리
            pass
        self._update_balance(cashbook, log_type, -cashbook_log.amount)
        cashbook_log.is_deleted = True
        cashbook_log.save()
        return cashbook_log

    def _get_cashbook(self, user, cashbook_id):
        cashbook = CashBook.objects.get(user=user, id=cashbook_id)
        return cashbook

    def _get_cashbook_log(self, cashbook, log_type, log_id):
        if log_type == 'deposit':
            cashbook_log = DepositLog.objects.get(
                cashbook=cashbook,
                id=log_id,
            )
        else:
            cashbook_log = ExpenseLog.objects.get(
                cashbook=cashbook,
                id=log_id,
            )
        return cashbook_log

    def _update_balance(self, cashbook, log_type, amount):
        if log_type == 'deposit':
            cashbook.balance += amount
        else:
            cashbook.balance -= amount
        cashbook.save()

    def _create_log(self, user, cashbook, log_type, validated_data):
        if log_type == 'deposit':
            category = DepositCategory.objects.get(Q(user=user) | Q(user=None),
                                                   id=validated_data.get('category_id'))
            cashbook_log = DepositLog.objects.create(cashbook=cashbook, category=category, **validated_data)
        else:
            category = ExpenseCategory.objects.get(Q(user=user) | Q(user=None),
                                                   id=validated_data.get('category_id'))
            cashbook_log = ExpenseLog.objects.create(cashbook=cashbook, category=category, **validated_data)
        return cashbook_log
