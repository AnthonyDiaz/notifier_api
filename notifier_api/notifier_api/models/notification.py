from django.db import models


class Notifications(models.Model):
    id = models.IntegerField(primary_key=True)
    ts_created = models.DateTimeField()
    ts_expires = models.DateTimeField(null=True)
    content = models.TextField()
    content_encoding = models.TextField()
    absolute_url = models.TextField()
    source = models.TextField()

    class Meta:
        db_table = 'notification'
