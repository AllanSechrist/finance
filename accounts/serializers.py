from rest_framework import serializers

from .models import CustomUser
from ledger.serializers import LedgerSerializer
from entry.serializers import EntrySerializer


class UserSerializer(serializers.ModelSerializer):
    ledgers = LedgerSerializer(many=True)
    entries = EntrySerializer(many=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "ledgers",
            "entries",
        )
