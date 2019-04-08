from rest_framework_simplejwt.views import TokenObtainPairView

from GameCenter.apps.authentication.serializers import TokenSerializer


class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer
