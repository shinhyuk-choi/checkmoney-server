from django.db import models


class CashBook(models.Model):
    class Meta:
        db_table = 'cashbook'

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='cashbooks'
    )
    name = models.CharField(max_length=20, default='기본')
    balance = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
        'cashbook.DepositCategory',
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
        'cashbook.ExpenseCategory',
        on_delete=models.SET_NULL,
        related_name='logs',
        null=True
    )


class LogCategory(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DepositCategory(LogCategory):
    class Meta:
        db_table = 'deposit_category'
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_deposit_category')
        ]

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='deposit_categories',
        null=True
    )


class ExpenseCategory(LogCategory):
    class Meta:
        db_table = 'expense_category'
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_expense_category')
        ]

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='expense_categories',
        null=True
    )
