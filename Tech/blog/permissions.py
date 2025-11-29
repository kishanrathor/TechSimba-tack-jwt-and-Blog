from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Allow:
    - Admin users can edit/delete any post.
    - Normal users can edit/delete only their own posts.
    - Everyone can view.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE methods = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Admin can edit or delete any post
        if request.user.is_staff:
            return True

        # Regular user can edit/delete only their posts
        return obj.author == request.user
