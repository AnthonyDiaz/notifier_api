from rest_framework import viewsets, filters

from ..serializers.notification_user import NotificationUsersSerializer
from ..models.notification_user import NotificationUsers


class NotificationUserViewSet(viewsets.ModelViewSet):
    """Handles creating, updating, and searching notifications"""
    serializer_class = NotificationUsersSerializer

    notifications_id = NotificationUsers.objects.filter()
    queryset = NotificationUsers.objects.all()

    filter_backends = (filters.SearchFilter,)
    search_fields = ('notification_id', 'user_id')
