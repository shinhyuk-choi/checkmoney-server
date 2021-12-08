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
