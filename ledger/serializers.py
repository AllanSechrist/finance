from rest_framework import serializers

from .models import Ledger

class LedgerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Ledger
        fields = (
            "id",
            "title",
            "total",
            "user",
        )