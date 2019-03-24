from rest_framework.permissions import BasePermission


class IsLoader(BasePermission):
    """
    Allows access only to loaders.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and (
                    request.method == "post" or
                    request.method == "put" or
                    request.method == "patch"
            )
        )
