from django.urls import path
from rest_framework import routers

from games import views

urlpatterns = [
    path("games/<uuid:pk>/<str:version>/logo/", views.download_logo_view),
    path("games/<uuid:pk>/<str:version>/bin/", views.download_game_view),
]

router = routers.DefaultRouter()
router.register(r"games", views.GameViewSet, basename="game")
urlpatterns += router.urls
