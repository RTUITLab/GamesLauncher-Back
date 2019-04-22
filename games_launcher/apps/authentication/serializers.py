from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Role, User


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token["username"] = user.username
        token["roles"] = [str(role).lower() for role in user.roles.all()]
        return token


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("name",)


class UserInResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "second_name", "last_name", "roles")
        read_only_fields = ("id",)


class UserInCreateSerializer(UserInResponseSerializer):
    class Meta(UserInResponseSerializer.Meta):
        fields = UserInResponseSerializer.Meta.fields + ("password",)
        extra_kwargs = {"password": {"write_only": True}}
