from django.urls import re_path
from rest_framework import routers

from games import views

urlpatterns = [
    re_path(r"^games/<uuid:pk>/download-<str:version>/$", views.download_game_view)
]

router = routers.DefaultRouter()
router.register(r"games", views.GameViewSet, basename="game")
urlpatterns += router.urls
