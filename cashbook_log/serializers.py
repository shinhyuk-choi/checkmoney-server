from rest_framework import serializers


class CashBookLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.IntegerField(required=True)
    memo = serializers.CharField(required=False)
    date = serializers.DateField(required=True)
    cashbook_id = serializers.IntegerField(required=True, write_only=True)
    category_id = serializers.IntegerField(required=True, write_only=True)
    category = serializers.SerializerMethodField(read_only=True)
    log_type = serializers.CharField(required=True, write_only=True)

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
        return log.category.name


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
    amount = serializers.IntegerField()
    memo = serializers.CharField()
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
