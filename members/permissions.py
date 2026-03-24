from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Admin can do anything
        if request.user.is_staff:
            return True

        # Owner can edit/delete
        return obj.owner == request.user