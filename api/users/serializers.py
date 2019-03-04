from rest_framework import serializers

from api.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', 'email', 'name')
        read_only_fields = ('is_staff',)