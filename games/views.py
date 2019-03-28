from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser

from authentication.permissions import IsLoader
from .serializers import Game, GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminUser | IsLoader,)
    filterset_fields = ("id", "name", "version",)


@api_view(["GET"])
def download_game_view(request, pk, version):
    game = get_object_or_404(Game, pk=pk, version=version)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(game.file.path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(game.file.path)
    return response
