from rest_framework import permissions


class AdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.role == 'admin'
        )


class IsAuth(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
        )