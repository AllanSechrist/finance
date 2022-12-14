from django.db import models
from django.conf import settings


class Ledger(models.Model):
    title = models.CharField(max_length=250)
    total = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="ledgers", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
