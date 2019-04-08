from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from GameCenter.apps.authentication.views import TokenView

urlpatterns = [
    path("login/", TokenView.as_view(), name="token_access"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
