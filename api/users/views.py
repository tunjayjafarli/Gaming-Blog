from rest_framework import viewsets

from api.users.models import User
from api.users.serializers import UserSerializer

# Users API endpoints

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_fields = ('name')
