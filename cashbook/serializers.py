from rest_framework import serializers

from cashbook.models import CashBook


class CashBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashBook
        fields = (
            'id',
            'name',
            'balance',
        )
