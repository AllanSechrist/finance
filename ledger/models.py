from django.db import models
from django.conf import settings


class Ledger(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="ledger", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
