# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..notifier_api import models

# Register your models here.
admin.site.register(models.notificaton)
admin.site.register(models.notification_user)
