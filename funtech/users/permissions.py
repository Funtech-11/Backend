from rest_framework import permissions


class SelfUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user)