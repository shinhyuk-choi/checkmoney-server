from rest_framework import serializers

from cashbook_log.models import CashBookLog


class CashBookLogSerializer(serializers.ModelSerializer):
    cashbook_id = serializers.IntegerField(required=True)
    log_type = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CashBookLog
        fields = (
            'id',
            'amount',
            'memo',
            'date',
            'cashbook_id',
            'category_id',
            'log_type',
        )