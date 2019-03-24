from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'name', 'date_joined', 'role')
        read_only_fields = ('date_joined',)
