from django.urls import path
from rest_framework import routers

from games_launcher.apps.games import views

router = routers.DefaultRouter()
router.register(r"games", views.GameViewSet, basename="game")
urlpatterns = [
    path(
        "games/download/<str:name>/<str:version>/<str:filename>/",
        views.download_game_view,
    )
]

urlpatterns += router.urls
