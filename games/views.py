from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import Game, GameSerializer
from .storage import compare_dirs


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def download_file(file, content_type):
    response = HttpResponse(file, content_type="application/{}".format(content_type))
    response["Content-Disposition"] = 'attachment; filename="{}"'.format(file.name)
    return response


@api_view(["GET"])
def download_game_view(request, pk, version):
    game = get_object_or_404(Game, pk=pk)
    if game.version == version and compare_dirs(game.file.path, version):
        file = game.file.open()
        return download_file(file, "zip")
    return HttpResponse(status=404)
