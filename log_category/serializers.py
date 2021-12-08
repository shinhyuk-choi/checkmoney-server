from rest_framework import serializers


class LogCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=20)
    log_type = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'log_type',
        )

    def validate_log_type(self, log_type):
        if log_type not in ['deposit', 'expense']:
            raise serializers.ValidationError("This field should be \'deposit\' or \'expense\' ")
        return log_type


class LogTypeSerializer(serializers.Serializer):
    log_type = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = (
            'log_type',
        )

    def validate_log_type(self, log_type):
        if log_type not in ['deposit', 'expense']:
            raise serializers.ValidationError("This field should be \'deposit\' or \'expense\' ")
        return log_type
