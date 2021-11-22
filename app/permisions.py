from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.user.role == 1 or request.user.is_superuser) and request.user.is_active:
            return True


class IsSimplesUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 2 and request.user.is_active:
            return True
