from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer

    def get_queryset(self):
        return self.request.user.entries.all()
