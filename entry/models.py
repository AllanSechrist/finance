from django.db import models
from django.conf import settings

from ledger.models import Ledger

class Entry(models.Model):
    description = models.CharField(max_length=500)
    is_debit = models.BooleanField()
    amount = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    ledger = models.ForeignKey(Ledger, related_name="entries", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="entries", on_delete=models.CASCADE)

    def __str__(self):
        return self.description
