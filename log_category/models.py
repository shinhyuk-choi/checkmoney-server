from django.db import models


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
