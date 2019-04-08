from django.http import FileResponse, Http404
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
def download_game_view(request, name: str, version: str, filename: str):
    if filename != "bin" and filename != "logo":
        raise Http404()

    try:
        games = Game.objects.filter(name=name)
        if version == "latest":
            game = games.latest()
        else:
            game = games.get(version=version)
    except:
        raise Http404()

    filepath = (game.file.path, game.logo.path)[filename == "logo"]
    return FileResponse(open(filepath, "rb"))
