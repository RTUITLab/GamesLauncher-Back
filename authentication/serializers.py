from rest_framework import serializers
from .models import User
from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'name', 'date_joined', 'role')
