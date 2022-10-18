from rest_framework import serializers

from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Entry
        fields = (
            "id",
            "description",
            "is_debit",
            "amount",
            "created_at",
            "updated_at",
            "ledger",
            "user",
        )
