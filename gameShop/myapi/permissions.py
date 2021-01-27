from rest_framework.permissions import IsAdminUser, SAFE_METHODS

#these classes were implemented to grant access

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class AdminReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS and is_admin

class ReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
