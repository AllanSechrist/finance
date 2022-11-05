from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# class ListUsers(APIView):

#     def get(self, request, format=None):
#         query = CustomUser.objects.all()
#         serializer_class = UserSerializer(query, many=True)
#         return Response(serializer_class.data)