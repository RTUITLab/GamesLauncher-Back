from rest_framework.permissions import BasePermission


class IsLoader(BasePermission):
    """
    Allows only upload game
    """
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and
            "loader" in request.user.roles and
            (request.method == "POST" or request.method == "PUT" or request.method == "PATCH")
        )
