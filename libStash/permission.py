from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class AbstractBasePermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user and request.user.is_authenticated


class IsOwner(AbstractBasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        return request.user == obj.account


class IsOwnProfile(AbstractBasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.unique_id == obj.unique_id