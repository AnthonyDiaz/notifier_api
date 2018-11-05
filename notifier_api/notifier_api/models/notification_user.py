from django.db import models

from ..models.notification import Notifications


class NotificationUsers(models.Model):
    user_id = models.IntegerField(primary_key=True)
    notification_id = models.ForeignKey(Notifications, related_name='notifications', on_delete=models.CASCADE)

    class Meta:
        db_table = 'notification_user'
