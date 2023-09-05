from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsModerator(BasePermission):
    """Add custom permission for User.role Moderator
    (Добавлено дополнительное право доступа User.role Moderator)"""
    message = "Вы не являетесь модератором!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False
