from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value

    def validate(self, data):
        if data['type'] not in ['income', 'expense']:
            raise serializers.ValidationError("Invalid type")
        return data

    class Meta:
        model = Record
        fields = '__all__'