from datetime import date
from rest_framework import serializers

from ..models.notification import Notifications


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('id', 'ts_created', 'ts_expires', 'content', 'content_encoding', 'absolute_url', 'source')


