from rest_framework import permissions


class OwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Изменение публикаций достпуно только их автору."""

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
