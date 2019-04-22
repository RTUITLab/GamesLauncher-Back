from django.http import FileResponse, Http404
from rest_framework import viewsets
from rest_framework.decorators import api_view

from games_launcher.apps.authentication.permissions import IsUploader, IsAdmin
from .serializers import Game, GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdmin | IsUploader,)  # todo set IsAuth for get-list
    filterset_fields = ("id", "name", "version")


@api_view(["GET"])
def download_game_view(request, name: str, version: str, filename: str):
    try:
        games = Game.objects.filter(name=name)
        if version == "latest":
            game = games.latest()
        else:
            game = games.get(version=version)
    except:
        raise Http404()

    if filename == "logo" and game.logo:
        filepath = game.logo.path
    elif filename == "bin" and game.file:
        filepath = game.file.path
    else:
        raise Http404()
    return FileResponse(open(filepath, "rb"))
