from rest_framework import serializers

from log_category.models import DepositCategory


class CashBookLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.IntegerField(required=True)
    memo = serializers.CharField(required=False)
    date = serializers.DateField(required=True)
    cashbook_id = serializers.IntegerField(required=True, write_only=True)
    category_id = serializers.IntegerField(required=True, write_only=True)
    category = serializers.SerializerMethodField(read_only=True)
    log_type = serializers.CharField(required=True, write_only=True)
    is_deleted = serializers.BooleanField(read_only=True)

    class Meta:
        fields = (
            'id',
            'category',
            'amount',
            'memo',
            'date',
            'cashbook_id',
            'category_id',
            'log_type',
            'is_deleted',
        )

    def validate_log_type(self, log_type):
        if log_type not in ['deposit', 'expense']:
            raise serializers.ValidationError("This field should be \'deposit\' or \'expense\' ")
        return log_type

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("This field should be positive integer")
        return amount

    def get_category(self, log):
        category = log.category
        if type(category) == DepositCategory:
            return f'[deposit]{log.category.name}'
        else:
            return f'[expense]{log.category.name}'


class LogTypeSerializer(serializers.Serializer):
    cashbook_id = serializers.IntegerField(required=True, write_only=True)
    log_type = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = (
            'cashbook_id',
            'log_type',
        )

    def validate_log_type(self, log_type):
        if log_type not in ['deposit', 'expense']:
            raise serializers.ValidationError("This field should be \'deposit\' or \'expense\' ")
        return log_type


class UpdateLogSerializer(serializers.Serializer):
    cashbook_id = serializers.IntegerField(required=True, write_only=True)
    log_type = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=False)
    memo = serializers.CharField(required=False)
    restore = serializers.BooleanField()

    class Meta:
        fields = (
            'cashbook_id',
            'log_type',
            'amount',
            'memo',
        )

    def validate_log_type(self, log_type):
        if log_type not in ['deposit', 'expense']:
            raise serializers.ValidationError("This field should be \'deposit\' or \'expense\' ")
        return log_type

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("This field should be positive integer")
        return amount

    def validate(self, data):
        restore = data.get('restore')
        amount = data.get('amount')
        memo = data.get('memo')

        if restore and (amount is not None or memo is not None):
            raise serializers.ValidationError("Could not restore and update together")
        return super(UpdateLogSerializer, self).validate(data)


class ListLogSerializer(serializers.Serializer):
    cashbook_id = serializers.IntegerField(required=True, write_only=True)
    log_type = serializers.CharField(required=False, write_only=True)
    date_from = serializers.DateField(required=False)
    date_to = serializers.DateField(required=False)
    is_deleted = serializers.BooleanField(default=False)

    def validate_log_type(self, log_type):
        if log_type not in ['deposit', 'expense']:
            raise serializers.ValidationError("This field should be \'deposit\' or \'expense\' ")
        return log_type

    def validate(self, data):
        date_from = data.get('date_from')
        date_to = data.get('date_to')

        if (date_from or date_to) and not (date_from and date_to):
            raise serializers.ValidationError("Enter date_from, date_to both ")
        return super(ListLogSerializer, self).validate(data)