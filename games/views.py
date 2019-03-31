from django.conf import settings
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from authentication.permissions import IsLoader
from .serializers import Game, GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('created')
    serializer_class = GameSerializer
    permission_classes = (IsAdminUser | IsLoader,)
    filterset_fields = ("id", "name", "version",)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def download_game_view(request, pk, version):

    print("downloading game...", version)
    if version == 'latest':
        version = queryset.latest()

    game = get_object_or_404(Game, pk=pk, version=version)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name, "rb") as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    filename = game.file.name.split("/")[-1]
    response = StreamingHttpResponse(file_iterator(game.file.path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def download_logo_view(request, pk, version):
    print("downloading logo...", version)
    game = get_object_or_404(Game, pk=pk, version=version)
    filename = game.logo.name.split("/")[-1]
    content_type = filename.split(".")[-1]
    response = HttpResponse(game.logo.open(), content_type="image/{}".format(content_type))
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response
