from django.urls import path
from rest_framework import routers

from GameCenter.apps.games import views

urlpatterns = [
    path("games/download/<str:name>/<str:version>/<str:filename>/", views.download_game_view),
]

router = routers.DefaultRouter()
router.register(r"games", views.GameViewSet, basename="game")
urlpatterns += router.urls
