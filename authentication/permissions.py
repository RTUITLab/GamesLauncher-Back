from rest_framework.permissions import BasePermission


class IsLoader(BasePermission):
    """
    Allows only POST method
    """

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_staff and
            request.method == "POST"
        )
