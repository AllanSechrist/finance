from django.db import models
from django.db import settings

from ledger.models import Ledger

class Entry(models.Model):
    description = models.CharField(max_length=500)
    is_debit = models.BooleanField(required=False)
    amount = models.IntegerField()
    date = models.DateField()
    ledger = models.ForeignKey(Ledger, related_name="entry", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="entry", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
