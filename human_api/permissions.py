from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow human to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check human is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnCase(permissions.BasePermission):
    """Allow human to edit their own case"""

    def has_object_permission(self, request, view, obj):
        """Check human is trying to edit their own case"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.human_profile.id == request.user.id
