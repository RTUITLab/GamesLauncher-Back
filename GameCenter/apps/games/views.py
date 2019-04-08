from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser

from GameCenter.apps.authentication.permissions import IsLoader
from .serializers import Game, GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminUser | IsLoader,)
    filterset_fields = ("id", "name", "version",)


@api_view(["GET"])
def download_game_view(request, name, version):
    game = get_object_or_404(Game, name=name, version=version)
    return FileResponse(open(game.file.path, "rb"))


@api_view(["GET"])
def download_logo_view(request, name, version):
    game = get_object_or_404(Game, name=name, version=version)
    return FileResponse(open(game.logo.path, "rb"))
