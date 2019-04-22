from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from games_launcher.apps.authentication.views import (
    RoleViewSet,
    TokenView,
    UserViewSet,
    get_profile_view,
)

router = routers.DefaultRouter()
router.register("roles", RoleViewSet)
router.register("users", UserViewSet)

urlpatterns = [
    path("login/", TokenView.as_view(), name="token_access"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/me/", get_profile_view, name="profile"),
]

urlpatterns += router.urls
