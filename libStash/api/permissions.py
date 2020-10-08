from rest_framework import permissions


class CanViewAccountDetails(permissions.BasePermission):
    """
    Custom permission to prevent users from views other users account information.
    """

    def has_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the account.
        return obj.email == request.user