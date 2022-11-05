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
    
    def create(self, validated_data):
        """
        Checks to make sure that there is a password
        """
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance