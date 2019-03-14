from rest_framework import routers
from launcher import views

router = routers.DefaultRouter()

router.register(r'games', views.GameViewSet, basename='game')
urlpatterns = []
urlpatterns = router.urls
