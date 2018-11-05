from rest_framework import serializers

from ..models import notification_user, notification
from ..serializers import notification


class NotificationUsersSerializer(serializers.ModelSerializer):
    # notifications = notification.NotificationsSerializer(many=True)

    class Meta:
        model = notification_user.NotificationUsers
        fields = ('user_id', 'notification_id')

    # def create(self, validated_data):
    #     notification_data = validated_data.pop('notifications')
    #     user_id = notification_user.NotificationUsers.objects.create(**validated_data)
    #     for notification_data in notification_data:
    #         notification.Notifications.objects.create(user_ids=user_id, **notification_data)
    #     return user_id


