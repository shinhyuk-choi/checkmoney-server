from django.db import models


class CashBookLog(models.Model):
    class Meta:
        abstract = True

    amount = models.IntegerField()
    memo = models.TextField()
    date = models.DateField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DepositLog(CashBookLog):
    class Meta:
        db_table = 'deposit_log'

    cashbook = models.ForeignKey(
        'cashbook.CashBook',
        on_delete=models.CASCADE,
        related_name='deposit_logs'
    )
    category = models.ForeignKey(
        'log_category.DepositCategory',
        on_delete=models.SET_NULL,
        related_name='logs',
        null=True,
    )


class ExpenseLog(CashBookLog):
    class Meta:
        db_table = 'expense_log'

    cashbook = models.ForeignKey(
        'cashbook.CashBook',
        on_delete=models.CASCADE,
        related_name='expense_logs'
    )
    category = models.ForeignKey(
        'log_category.ExpenseCategory',
        on_delete=models.SET_NULL,
        related_name='logs',
        null=True
    )
