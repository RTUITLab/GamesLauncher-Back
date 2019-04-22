from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from games_launcher.apps.authentication.models import Role, User
from games_launcher.apps.authentication.permissions import IsAdmin
from games_launcher.apps.authentication.serializers import (
    RoleSerializer,
    TokenSerializer,
    UserInCreateSerializer,
    UserInResponseSerializer,
)


class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAdmin,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInResponseSerializer
    permission_classes = (IsAdmin,)

    def create(self, request, **kwargs):
        serializer = UserInCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        user = User.objects.create_user(**data)

        return Response(
            data=UserInResponseSerializer(user).data, status=status.HTTP_201_CREATED
        )


@swagger_auto_schema(
    method="get",
    operation_summary="Get Current User Profile",
    operation_description="Retrieve profile for user that makes request",
    responses={200: UserInResponseSerializer},
)
@api_view(("GET",))
def get_profile_view(request: Request):
    serializer = UserInResponseSerializer(request.user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
