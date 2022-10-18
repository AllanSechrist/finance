from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import LedgerSerializer


class LedgerViewSet(viewsets.ModelViewSet):
    serializer_class = LedgerSerializer

    def get_queryset(self):
        return self.request.user.ledgers.all()