from rest_framework.permissions import BasePermission


class IsUploader(BasePermission):
    """
    Allows only upload game
    """

    def has_permission(self, request, view):
        return bool(
            request.user.is_uploader
            and (
                    request.method == "POST"
                    or request.method == "PUT"
                    or request.method == "PATCH"
            )
        )


class IsAdmin(BasePermission):
    """
    Simply admin permission
    """

    def has_permission(self, request, view):
        return request.user.is_admin
