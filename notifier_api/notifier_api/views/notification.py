from rest_framework import viewsets, filters

from ..serializers.notification import NotificationsSerializer
from ..models.notification import Notifications


class NotificationViewSet(viewsets.ModelViewSet):
    """Handles creating, updating, and searching notifications"""
    serializer_class = NotificationsSerializer
    queryset = Notifications.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('ts_created', 'ts_expires', 'content', 'source')
