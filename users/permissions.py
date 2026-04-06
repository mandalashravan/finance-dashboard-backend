from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    message = "You do not have permission or Role header is missing."

    def has_permission(self, request, view):
        role = request.headers.get('Role')

        if not role:
            return False

        if role == 'ADMIN':
            return True

        if role in ['ANALYST', 'VIEWER']:
            return request.method == 'GET'

        return False