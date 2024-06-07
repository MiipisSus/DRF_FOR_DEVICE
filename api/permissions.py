from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.groups.filter(name='Editor').exists()

    
class IsViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or \
            request.user.groups.filter(name='Editor').exists() or \
            request.user.groups.filter(name='Viewer').exists()