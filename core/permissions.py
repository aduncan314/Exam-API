from rest_framework import permissions


class IsOwnerOrParentOfOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # TODO: check request.user children; create list
        # ~pseudo~ children = [child for child in request.user.children]
        return request.user == obj.owner
